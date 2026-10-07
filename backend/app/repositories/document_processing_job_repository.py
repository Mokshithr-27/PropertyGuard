from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document_processing_job import DocumentProcessingJob


def create_processing_job(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    db.add(job)
    db.flush()
    db.refresh(job)
    return job


def get_processing_job(
    db: Session,
    job_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(DocumentProcessingJob).where(
            DocumentProcessingJob.id == job_id,
        )
    )


def get_processing_jobs_for_version(
    db: Session,
    document_version_id: UUID,
) -> list[DocumentProcessingJob]:
    return list(
        db.scalars(
            select(DocumentProcessingJob)
            .where(
                DocumentProcessingJob.document_version_id
                == document_version_id,
            )
            .order_by(
                DocumentProcessingJob.created_at.desc()
            )
        ).all()
    )


def get_active_processing_job(
    db: Session,
    document_version_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(DocumentProcessingJob)
        .where(
            DocumentProcessingJob.document_version_id
            == document_version_id,
            DocumentProcessingJob.status.in_(
                ["QUEUED", "PROCESSING"]
            ),
        )
        .order_by(
            DocumentProcessingJob.created_at.desc()
        )
        .limit(1)
    )


def update_processing_job(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    db.add(job)
    db.flush()
    db.refresh(job)
    return job