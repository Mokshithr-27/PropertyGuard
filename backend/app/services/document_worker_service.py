"""
PropertyGuard Document Processing Job Worker Service
----------------------------------------------------
Executes document text extraction jobs for a specified job ID, downloading file bytes
from storage, extracting text, updating job status, and capturing error logs.
"""

from sqlalchemy.orm import Session

from app.integrations.storage import download_bytes
from app.models import DocumentVersion
from app.repositories.document_processing_job_repository import (
    get_processing_job,
)
from app.services.document_extraction_service import extract_document_text
from app.services.document_processing_service import (
    complete_document_processing,
    fail_document_processing,
    start_document_processing,
)


def process_document_job(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, job_id)

    if job is None:
        raise ValueError("Processing job not found")

    if job.status != "QUEUED":
        raise ValueError("Only queued jobs can be processed")

    version = db.get(
        DocumentVersion,
        job.document_version_id,
    )

    if version is None or version.deleted_at is not None:
        raise ValueError("Document version not found")

    try:
        start_document_processing(
            db=db,
            job=job,
        )

        db.commit()

        file_bytes = download_bytes(
            version.storage_key,
        )

        extracted_text = extract_document_text(
            file_bytes=file_bytes,
            file_name=version.file_name,
            mime_type=version.mime_type,
        )

        # Temporary verification point.
        # Persistent extracted-text storage will be implemented next.
        if not extracted_text:
            raise ValueError("No text could be extracted from the document")

        complete_document_processing(
            db=db,
            job=job,
            version=version,
        )

        db.commit()

        return extracted_text

    except Exception as exc:
        db.rollback()

        job = get_processing_job(
            db,
            job_id,
        )

        version = db.get(
            DocumentVersion,
            job.document_version_id,
        )

        if job is not None and version is not None:
            try:
                fail_document_processing(
                    db=db,
                    job=job,
                    version=version,
                    error_message=str(exc),
                )

                db.commit()

            except Exception:
                db.rollback()

        raise