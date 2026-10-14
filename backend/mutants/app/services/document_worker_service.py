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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_process_document_job__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_process_document_job__mutmut)
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


def x_process_document_job__mutmut_orig(
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


def x_process_document_job__mutmut_1(
    db: Session,
    job_id,
) -> str:
    job = None

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


def x_process_document_job__mutmut_2(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(None, job_id)

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


def x_process_document_job__mutmut_3(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, None)

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


def x_process_document_job__mutmut_4(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(job_id)

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


def x_process_document_job__mutmut_5(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, )

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


def x_process_document_job__mutmut_6(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, job_id)

    if job is not None:
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


def x_process_document_job__mutmut_7(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, job_id)

    if job is None:
        raise ValueError(None)

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


def x_process_document_job__mutmut_8(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, job_id)

    if job is None:
        raise ValueError("XXProcessing job not foundXX")

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


def x_process_document_job__mutmut_9(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, job_id)

    if job is None:
        raise ValueError("processing job not found")

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


def x_process_document_job__mutmut_10(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, job_id)

    if job is None:
        raise ValueError("PROCESSING JOB NOT FOUND")

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


def x_process_document_job__mutmut_11(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, job_id)

    if job is None:
        raise ValueError("Processing job not found")

    if job.status == "QUEUED":
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


def x_process_document_job__mutmut_12(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, job_id)

    if job is None:
        raise ValueError("Processing job not found")

    if job.status != "XXQUEUEDXX":
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


def x_process_document_job__mutmut_13(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, job_id)

    if job is None:
        raise ValueError("Processing job not found")

    if job.status != "queued":
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


def x_process_document_job__mutmut_14(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, job_id)

    if job is None:
        raise ValueError("Processing job not found")

    if job.status != "QUEUED":
        raise ValueError(None)

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


def x_process_document_job__mutmut_15(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, job_id)

    if job is None:
        raise ValueError("Processing job not found")

    if job.status != "QUEUED":
        raise ValueError("XXOnly queued jobs can be processedXX")

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


def x_process_document_job__mutmut_16(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, job_id)

    if job is None:
        raise ValueError("Processing job not found")

    if job.status != "QUEUED":
        raise ValueError("only queued jobs can be processed")

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


def x_process_document_job__mutmut_17(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, job_id)

    if job is None:
        raise ValueError("Processing job not found")

    if job.status != "QUEUED":
        raise ValueError("ONLY QUEUED JOBS CAN BE PROCESSED")

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


def x_process_document_job__mutmut_18(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, job_id)

    if job is None:
        raise ValueError("Processing job not found")

    if job.status != "QUEUED":
        raise ValueError("Only queued jobs can be processed")

    version = None

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


def x_process_document_job__mutmut_19(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, job_id)

    if job is None:
        raise ValueError("Processing job not found")

    if job.status != "QUEUED":
        raise ValueError("Only queued jobs can be processed")

    version = db.get(
        None,
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


def x_process_document_job__mutmut_20(
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
        None,
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


def x_process_document_job__mutmut_21(
    db: Session,
    job_id,
) -> str:
    job = get_processing_job(db, job_id)

    if job is None:
        raise ValueError("Processing job not found")

    if job.status != "QUEUED":
        raise ValueError("Only queued jobs can be processed")

    version = db.get(
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


def x_process_document_job__mutmut_22(
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


def x_process_document_job__mutmut_23(
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

    if version is None and version.deleted_at is not None:
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


def x_process_document_job__mutmut_24(
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

    if version is not None or version.deleted_at is not None:
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


def x_process_document_job__mutmut_25(
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

    if version is None or version.deleted_at is None:
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


def x_process_document_job__mutmut_26(
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
        raise ValueError(None)

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


def x_process_document_job__mutmut_27(
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
        raise ValueError("XXDocument version not foundXX")

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


def x_process_document_job__mutmut_28(
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
        raise ValueError("document version not found")

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


def x_process_document_job__mutmut_29(
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
        raise ValueError("DOCUMENT VERSION NOT FOUND")

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


def x_process_document_job__mutmut_30(
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
            db=None,
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


def x_process_document_job__mutmut_31(
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
            job=None,
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


def x_process_document_job__mutmut_32(
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


def x_process_document_job__mutmut_33(
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


def x_process_document_job__mutmut_34(
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

        file_bytes = None

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


def x_process_document_job__mutmut_35(
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
            None,
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


def x_process_document_job__mutmut_36(
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

        extracted_text = None

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


def x_process_document_job__mutmut_37(
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
            file_bytes=None,
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


def x_process_document_job__mutmut_38(
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
            file_name=None,
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


def x_process_document_job__mutmut_39(
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
            mime_type=None,
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


def x_process_document_job__mutmut_40(
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


def x_process_document_job__mutmut_41(
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


def x_process_document_job__mutmut_42(
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


def x_process_document_job__mutmut_43(
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
        if extracted_text:
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


def x_process_document_job__mutmut_44(
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
            raise ValueError(None)

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


def x_process_document_job__mutmut_45(
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
            raise ValueError("XXNo text could be extracted from the documentXX")

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


def x_process_document_job__mutmut_46(
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
            raise ValueError("no text could be extracted from the document")

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


def x_process_document_job__mutmut_47(
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
            raise ValueError("NO TEXT COULD BE EXTRACTED FROM THE DOCUMENT")

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


def x_process_document_job__mutmut_48(
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
            db=None,
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


def x_process_document_job__mutmut_49(
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
            job=None,
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


def x_process_document_job__mutmut_50(
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
            version=None,
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


def x_process_document_job__mutmut_51(
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


def x_process_document_job__mutmut_52(
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


def x_process_document_job__mutmut_53(
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


def x_process_document_job__mutmut_54(
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

        job = None

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


def x_process_document_job__mutmut_55(
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
            None,
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


def x_process_document_job__mutmut_56(
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
            None,
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


def x_process_document_job__mutmut_57(
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


def x_process_document_job__mutmut_58(
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


def x_process_document_job__mutmut_59(
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

        version = None

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


def x_process_document_job__mutmut_60(
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
            None,
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


def x_process_document_job__mutmut_61(
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
            None,
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


def x_process_document_job__mutmut_62(
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


def x_process_document_job__mutmut_63(
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


def x_process_document_job__mutmut_64(
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

        if job is not None or version is not None:
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


def x_process_document_job__mutmut_65(
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

        if job is None and version is not None:
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


def x_process_document_job__mutmut_66(
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

        if job is not None and version is None:
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


def x_process_document_job__mutmut_67(
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
                    db=None,
                    job=job,
                    version=version,
                    error_message=str(exc),
                )

                db.commit()

            except Exception:
                db.rollback()

        raise


def x_process_document_job__mutmut_68(
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
                    job=None,
                    version=version,
                    error_message=str(exc),
                )

                db.commit()

            except Exception:
                db.rollback()

        raise


def x_process_document_job__mutmut_69(
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
                    version=None,
                    error_message=str(exc),
                )

                db.commit()

            except Exception:
                db.rollback()

        raise


def x_process_document_job__mutmut_70(
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
                    error_message=None,
                )

                db.commit()

            except Exception:
                db.rollback()

        raise


def x_process_document_job__mutmut_71(
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
                    job=job,
                    version=version,
                    error_message=str(exc),
                )

                db.commit()

            except Exception:
                db.rollback()

        raise


def x_process_document_job__mutmut_72(
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
                    version=version,
                    error_message=str(exc),
                )

                db.commit()

            except Exception:
                db.rollback()

        raise


def x_process_document_job__mutmut_73(
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
                    error_message=str(exc),
                )

                db.commit()

            except Exception:
                db.rollback()

        raise


def x_process_document_job__mutmut_74(
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
                    )

                db.commit()

            except Exception:
                db.rollback()

        raise


def x_process_document_job__mutmut_75(
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
                    error_message=str(None),
                )

                db.commit()

            except Exception:
                db.rollback()

        raise

mutants_x_process_document_job__mutmut['_mutmut_orig'] = x_process_document_job__mutmut_orig # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_1'] = x_process_document_job__mutmut_1 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_2'] = x_process_document_job__mutmut_2 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_3'] = x_process_document_job__mutmut_3 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_4'] = x_process_document_job__mutmut_4 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_5'] = x_process_document_job__mutmut_5 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_6'] = x_process_document_job__mutmut_6 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_7'] = x_process_document_job__mutmut_7 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_8'] = x_process_document_job__mutmut_8 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_9'] = x_process_document_job__mutmut_9 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_10'] = x_process_document_job__mutmut_10 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_11'] = x_process_document_job__mutmut_11 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_12'] = x_process_document_job__mutmut_12 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_13'] = x_process_document_job__mutmut_13 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_14'] = x_process_document_job__mutmut_14 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_15'] = x_process_document_job__mutmut_15 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_16'] = x_process_document_job__mutmut_16 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_17'] = x_process_document_job__mutmut_17 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_18'] = x_process_document_job__mutmut_18 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_19'] = x_process_document_job__mutmut_19 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_20'] = x_process_document_job__mutmut_20 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_21'] = x_process_document_job__mutmut_21 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_22'] = x_process_document_job__mutmut_22 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_23'] = x_process_document_job__mutmut_23 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_24'] = x_process_document_job__mutmut_24 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_25'] = x_process_document_job__mutmut_25 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_26'] = x_process_document_job__mutmut_26 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_27'] = x_process_document_job__mutmut_27 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_28'] = x_process_document_job__mutmut_28 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_29'] = x_process_document_job__mutmut_29 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_30'] = x_process_document_job__mutmut_30 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_31'] = x_process_document_job__mutmut_31 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_32'] = x_process_document_job__mutmut_32 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_33'] = x_process_document_job__mutmut_33 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_34'] = x_process_document_job__mutmut_34 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_35'] = x_process_document_job__mutmut_35 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_36'] = x_process_document_job__mutmut_36 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_37'] = x_process_document_job__mutmut_37 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_38'] = x_process_document_job__mutmut_38 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_39'] = x_process_document_job__mutmut_39 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_40'] = x_process_document_job__mutmut_40 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_41'] = x_process_document_job__mutmut_41 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_42'] = x_process_document_job__mutmut_42 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_43'] = x_process_document_job__mutmut_43 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_44'] = x_process_document_job__mutmut_44 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_45'] = x_process_document_job__mutmut_45 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_46'] = x_process_document_job__mutmut_46 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_47'] = x_process_document_job__mutmut_47 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_48'] = x_process_document_job__mutmut_48 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_49'] = x_process_document_job__mutmut_49 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_50'] = x_process_document_job__mutmut_50 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_51'] = x_process_document_job__mutmut_51 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_52'] = x_process_document_job__mutmut_52 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_53'] = x_process_document_job__mutmut_53 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_54'] = x_process_document_job__mutmut_54 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_55'] = x_process_document_job__mutmut_55 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_56'] = x_process_document_job__mutmut_56 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_57'] = x_process_document_job__mutmut_57 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_58'] = x_process_document_job__mutmut_58 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_59'] = x_process_document_job__mutmut_59 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_60'] = x_process_document_job__mutmut_60 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_61'] = x_process_document_job__mutmut_61 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_62'] = x_process_document_job__mutmut_62 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_63'] = x_process_document_job__mutmut_63 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_64'] = x_process_document_job__mutmut_64 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_65'] = x_process_document_job__mutmut_65 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_66'] = x_process_document_job__mutmut_66 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_67'] = x_process_document_job__mutmut_67 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_68'] = x_process_document_job__mutmut_68 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_69'] = x_process_document_job__mutmut_69 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_70'] = x_process_document_job__mutmut_70 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_71'] = x_process_document_job__mutmut_71 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_72'] = x_process_document_job__mutmut_72 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_73'] = x_process_document_job__mutmut_73 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_74'] = x_process_document_job__mutmut_74 # type: ignore # mutmut generated
mutants_x_process_document_job__mutmut['x_process_document_job__mutmut_75'] = x_process_document_job__mutmut_75 # type: ignore # mutmut generated