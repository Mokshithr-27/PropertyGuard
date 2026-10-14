"""
PropertyGuard Document Processing Lifecycle Service
---------------------------------------------------
Manages processing job states (QUEUED, PROCESSING, COMPLETED, FAILED), updating
DocumentVersion processing statuses and recording job run details.
"""

from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy.orm import Session

from app.models import DocumentVersion
from app.models.document_processing_job import DocumentProcessingJob
from app.repositories.document_processing_job_repository import (
    create_processing_job,
    get_active_processing_job,
    get_processing_job,
    update_processing_job,
)
from app.repositories.document_repository import (
    update_document_version,
)


def queue_document_processing(
    db: Session,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """
    Queue document processing for a document version.

    Prevents multiple active jobs for the same version.
    """

    if version.deleted_at is not None:
        raise ValueError("Cannot process a deleted document version")

    active_job = get_active_processing_job(
        db,
        version.id,
    )

    if active_job is not None:
        raise ValueError(
            "An active processing job already exists"
        )

    job = DocumentProcessingJob(
        document_version_id=version.id,
        status="QUEUED",
        attempt_count=0,
        queued_at=datetime.now(timezone.utc),
    )

    version.processing_status = "QUEUED"

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def start_document_processing(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    """Mark a queued job as processing."""

    if job.status != "QUEUED":
        raise ValueError(
            "Only queued jobs can be started"
        )

    job.status = "PROCESSING"
    job.attempt_count += 1
    job.started_at = datetime.now(timezone.utc)

    return update_processing_job(db, job)


def complete_document_processing(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """Mark processing as completed."""

    if job.status != "PROCESSING":
        raise ValueError(
            "Only processing jobs can be completed"
        )

    job.status = "COMPLETED"
    job.completed_at = datetime.now(timezone.utc)
    version.processing_status = "COMPLETED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def fail_document_processing(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
    error_message: str,
) -> DocumentProcessingJob:
    """Mark processing as failed."""

    if job.status != "PROCESSING":
        raise ValueError(
            "Only processing jobs can fail"
        )

    job.status = "FAILED"
    job.completed_at = datetime.now(timezone.utc)
    job.error_message = error_message
    version.processing_status = "FAILED"

    update_document_version(db, version)

    return update_processing_job(db, job)