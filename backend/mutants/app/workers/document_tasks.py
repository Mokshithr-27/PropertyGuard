"""
PropertyGuard Asynchronous Document Processing Pipeline Tasks
-------------------------------------------------------------
Orchestrates background document processing: downloads files from MinIO, selects
either fast text extraction (PyMuPDF) or OCR worker routing (PaddleOCR), passes
extracted content to the configured AI Provider for entity/evidence extraction,
and persists analysis records and evidence items in PostgreSQL.
"""

from uuid import UUID

from app.core.database import SessionLocal
from app.integrations.storage import download_bytes
from app.repositories.document_processing_job_repository import (
    get_processing_job,
)
from app.repositories.document_repository import (
    get_document_version,
)
from app.services.document_processing_service import (
    complete_document_processing,
    fail_document_processing,
    start_document_processing,
)
from app.services.document_text_extraction_service import (
    extract_pdf_text,
)
from app.workers.celery_app import celery_app

from app.integrations.ai.factory import get_ai_provider
from app.services.document_analysis_service import persist_document_analysis

from app.services.ocr_result_adapter import (
    ocr_result_to_extracted_document,
)


from celery import Celery

from app.core.config import REDIS_URL


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict



@celery_app.task
def process_document_task(
    version_id: str,
    job_id: str,
) -> dict:
    db = SessionLocal()

    try:
        version = get_document_version(
            db,
            UUID(version_id),
        )

        if version is None:
            raise ValueError(
                "Document version not found"
            )

        job = get_processing_job(
            db,
            UUID(job_id),
        )

        if job is None:
            raise ValueError(
                "Document processing job not found"
            )

        start_document_processing(
            db,
            job,
        )
        db.commit()
        db.refresh(job)

        file_bytes = download_bytes(
            version.storage_key
        )

        # Extract once. Do not print raw document contents to logs: property
        # documents may contain confidential personal and financial information.
        extracted = extract_pdf_text(file_bytes)

        if not extracted.has_text:

            ocr_app = Celery(
                "propertyguard_ocr_dispatch",
                broker=REDIS_URL,
                backend=REDIS_URL,
            )

            ocr_app.send_task(
                "app.ocr_worker.tasks.ocr_process_document",
                args=[
                    version.storage_key,
                    version_id,
                    job_id,
                ],
                queue="ocr",
            )

            db.commit()

            return {
                "version_id": version_id,
                "job_id": job_id,
                "page_count": extracted.page_count,
                "has_text": False,
                "text_length": 0,
                "extraction_source": "OCR",
                "status": "OCR_QUEUED",
            }

        provider = get_ai_provider()

        result = provider.analyze(extracted)

        persist_document_analysis(
            db=db,
            document_version_id=version.id,
            result=result,
        )

        complete_document_processing(
            db,
            job,
            version,
        )

        db.commit()

        return {
            "version_id": version_id,
            "job_id": job_id,
            "page_count": extracted.page_count,
            "has_text": extracted.has_text,
            "text_length": len(extracted.full_text),
            "status": "COMPLETED",
        }

    except Exception as exc:
        db.rollback()

        version = get_document_version(
            db,
            UUID(version_id),
        )

        job = get_processing_job(
            db,
            UUID(job_id),
        )

        if (
            version is not None
            and job is not None
            and job.status == "PROCESSING"
        ):
            fail_document_processing(
                db,
                job,
                version,
                str(exc),
            )
            db.commit()

        raise

    finally:
        db.close()


@celery_app.task
def continue_document_processing_after_ocr(
    version_id: str,
    job_id: str,
    ocr_result: dict,
) -> dict:
    db = SessionLocal()

    try:
        version = get_document_version(
            db,
            UUID(version_id),
        )

        if version is None:
            raise ValueError(
                "Document version not found"
            )

        job = get_processing_job(
            db,
            UUID(job_id),
        )

        if job is None:
            raise ValueError(
                "Document processing job not found"
            )

        extracted = ocr_result_to_extracted_document(
            ocr_result
        )

        provider = get_ai_provider()

        result = provider.analyze(
            extracted
        )

        persist_document_analysis(
            db=db,
            document_version_id=version.id,
            result=result,
        )

        complete_document_processing(
            db,
            job,
            version,
        )

        db.commit()

        return {
            "version_id": version_id,
            "job_id": job_id,
            "page_count": extracted.page_count,
            "has_text": extracted.has_text,
            "text_length": len(extracted.full_text),
            "extraction_source": "OCR",
            "status": "COMPLETED",
        }

    except Exception as exc:
        db.rollback()

        version = get_document_version(
            db,
            UUID(version_id),
        )

        job = get_processing_job(
            db,
            UUID(job_id),
        )

        if (
            version is not None
            and job is not None
            and job.status == "PROCESSING"
        ):
            fail_document_processing(
                db,
                job,
                version,
                str(exc),
            )
            db.commit()

        raise

    finally:
        db.close()