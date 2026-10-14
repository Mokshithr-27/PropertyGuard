"""
PropertyGuard Document Processing Job Repository
------------------------------------------------
Provides database CRUD operations for DocumentProcessingJob entities,
tracking execution states and worker tasks.
"""

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document_processing_job import DocumentProcessingJob


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_create_processing_job__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_create_processing_job__mutmut)
def create_processing_job(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    db.add(job)
    db.flush()
    db.refresh(job)
    return job


def x_create_processing_job__mutmut_orig(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    db.add(job)
    db.flush()
    db.refresh(job)
    return job


def x_create_processing_job__mutmut_1(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    db.add(None)
    db.flush()
    db.refresh(job)
    return job


def x_create_processing_job__mutmut_2(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    db.add(job)
    db.flush()
    db.refresh(None)
    return job

mutants_x_create_processing_job__mutmut['_mutmut_orig'] = x_create_processing_job__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_processing_job__mutmut['x_create_processing_job__mutmut_1'] = x_create_processing_job__mutmut_1 # type: ignore # mutmut generated
mutants_x_create_processing_job__mutmut['x_create_processing_job__mutmut_2'] = x_create_processing_job__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_processing_job__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_processing_job__mutmut)
def get_processing_job(
    db: Session,
    job_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(DocumentProcessingJob).where(
            DocumentProcessingJob.id == job_id,
        )
    )


def x_get_processing_job__mutmut_orig(
    db: Session,
    job_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(DocumentProcessingJob).where(
            DocumentProcessingJob.id == job_id,
        )
    )


def x_get_processing_job__mutmut_1(
    db: Session,
    job_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        None
    )


def x_get_processing_job__mutmut_2(
    db: Session,
    job_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(DocumentProcessingJob).where(
            None,
        )
    )


def x_get_processing_job__mutmut_3(
    db: Session,
    job_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(None).where(
            DocumentProcessingJob.id == job_id,
        )
    )


def x_get_processing_job__mutmut_4(
    db: Session,
    job_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(DocumentProcessingJob).where(
            DocumentProcessingJob.id != job_id,
        )
    )

mutants_x_get_processing_job__mutmut['_mutmut_orig'] = x_get_processing_job__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_processing_job__mutmut['x_get_processing_job__mutmut_1'] = x_get_processing_job__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_processing_job__mutmut['x_get_processing_job__mutmut_2'] = x_get_processing_job__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_processing_job__mutmut['x_get_processing_job__mutmut_3'] = x_get_processing_job__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_processing_job__mutmut['x_get_processing_job__mutmut_4'] = x_get_processing_job__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_processing_jobs_for_version__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_processing_jobs_for_version__mutmut)
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


def x_get_processing_jobs_for_version__mutmut_orig(
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


def x_get_processing_jobs_for_version__mutmut_1(
    db: Session,
    document_version_id: UUID,
) -> list[DocumentProcessingJob]:
    return list(
        None
    )


def x_get_processing_jobs_for_version__mutmut_2(
    db: Session,
    document_version_id: UUID,
) -> list[DocumentProcessingJob]:
    return list(
        db.scalars(
            None
        ).all()
    )


def x_get_processing_jobs_for_version__mutmut_3(
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
                None
            )
        ).all()
    )


def x_get_processing_jobs_for_version__mutmut_4(
    db: Session,
    document_version_id: UUID,
) -> list[DocumentProcessingJob]:
    return list(
        db.scalars(
            select(DocumentProcessingJob)
            .where(
                None,
            )
            .order_by(
                DocumentProcessingJob.created_at.desc()
            )
        ).all()
    )


def x_get_processing_jobs_for_version__mutmut_5(
    db: Session,
    document_version_id: UUID,
) -> list[DocumentProcessingJob]:
    return list(
        db.scalars(
            select(None)
            .where(
                DocumentProcessingJob.document_version_id
                == document_version_id,
            )
            .order_by(
                DocumentProcessingJob.created_at.desc()
            )
        ).all()
    )


def x_get_processing_jobs_for_version__mutmut_6(
    db: Session,
    document_version_id: UUID,
) -> list[DocumentProcessingJob]:
    return list(
        db.scalars(
            select(DocumentProcessingJob)
            .where(
                DocumentProcessingJob.document_version_id != document_version_id,
            )
            .order_by(
                DocumentProcessingJob.created_at.desc()
            )
        ).all()
    )

mutants_x_get_processing_jobs_for_version__mutmut['_mutmut_orig'] = x_get_processing_jobs_for_version__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_processing_jobs_for_version__mutmut['x_get_processing_jobs_for_version__mutmut_1'] = x_get_processing_jobs_for_version__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_processing_jobs_for_version__mutmut['x_get_processing_jobs_for_version__mutmut_2'] = x_get_processing_jobs_for_version__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_processing_jobs_for_version__mutmut['x_get_processing_jobs_for_version__mutmut_3'] = x_get_processing_jobs_for_version__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_processing_jobs_for_version__mutmut['x_get_processing_jobs_for_version__mutmut_4'] = x_get_processing_jobs_for_version__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_processing_jobs_for_version__mutmut['x_get_processing_jobs_for_version__mutmut_5'] = x_get_processing_jobs_for_version__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_processing_jobs_for_version__mutmut['x_get_processing_jobs_for_version__mutmut_6'] = x_get_processing_jobs_for_version__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_active_processing_job__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_active_processing_job__mutmut)
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


def x_get_active_processing_job__mutmut_orig(
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


def x_get_active_processing_job__mutmut_1(
    db: Session,
    document_version_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        None
    )


def x_get_active_processing_job__mutmut_2(
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
        .limit(None)
    )


def x_get_active_processing_job__mutmut_3(
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
            None
        )
        .limit(1)
    )


def x_get_active_processing_job__mutmut_4(
    db: Session,
    document_version_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(DocumentProcessingJob)
        .where(
            None,
            DocumentProcessingJob.status.in_(
                ["QUEUED", "PROCESSING"]
            ),
        )
        .order_by(
            DocumentProcessingJob.created_at.desc()
        )
        .limit(1)
    )


def x_get_active_processing_job__mutmut_5(
    db: Session,
    document_version_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(DocumentProcessingJob)
        .where(
            DocumentProcessingJob.document_version_id
            == document_version_id,
            None,
        )
        .order_by(
            DocumentProcessingJob.created_at.desc()
        )
        .limit(1)
    )


def x_get_active_processing_job__mutmut_6(
    db: Session,
    document_version_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(DocumentProcessingJob)
        .where(
            DocumentProcessingJob.status.in_(
                ["QUEUED", "PROCESSING"]
            ),
        )
        .order_by(
            DocumentProcessingJob.created_at.desc()
        )
        .limit(1)
    )


def x_get_active_processing_job__mutmut_7(
    db: Session,
    document_version_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(DocumentProcessingJob)
        .where(
            DocumentProcessingJob.document_version_id
            == document_version_id,
            )
        .order_by(
            DocumentProcessingJob.created_at.desc()
        )
        .limit(1)
    )


def x_get_active_processing_job__mutmut_8(
    db: Session,
    document_version_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(None)
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


def x_get_active_processing_job__mutmut_9(
    db: Session,
    document_version_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(DocumentProcessingJob)
        .where(
            DocumentProcessingJob.document_version_id != document_version_id,
            DocumentProcessingJob.status.in_(
                ["QUEUED", "PROCESSING"]
            ),
        )
        .order_by(
            DocumentProcessingJob.created_at.desc()
        )
        .limit(1)
    )


def x_get_active_processing_job__mutmut_10(
    db: Session,
    document_version_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(DocumentProcessingJob)
        .where(
            DocumentProcessingJob.document_version_id
            == document_version_id,
            DocumentProcessingJob.status.in_(
                None
            ),
        )
        .order_by(
            DocumentProcessingJob.created_at.desc()
        )
        .limit(1)
    )


def x_get_active_processing_job__mutmut_11(
    db: Session,
    document_version_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(DocumentProcessingJob)
        .where(
            DocumentProcessingJob.document_version_id
            == document_version_id,
            DocumentProcessingJob.status.in_(
                ["XXQUEUEDXX", "PROCESSING"]
            ),
        )
        .order_by(
            DocumentProcessingJob.created_at.desc()
        )
        .limit(1)
    )


def x_get_active_processing_job__mutmut_12(
    db: Session,
    document_version_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(DocumentProcessingJob)
        .where(
            DocumentProcessingJob.document_version_id
            == document_version_id,
            DocumentProcessingJob.status.in_(
                ["queued", "PROCESSING"]
            ),
        )
        .order_by(
            DocumentProcessingJob.created_at.desc()
        )
        .limit(1)
    )


def x_get_active_processing_job__mutmut_13(
    db: Session,
    document_version_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(DocumentProcessingJob)
        .where(
            DocumentProcessingJob.document_version_id
            == document_version_id,
            DocumentProcessingJob.status.in_(
                ["QUEUED", "XXPROCESSINGXX"]
            ),
        )
        .order_by(
            DocumentProcessingJob.created_at.desc()
        )
        .limit(1)
    )


def x_get_active_processing_job__mutmut_14(
    db: Session,
    document_version_id: UUID,
) -> DocumentProcessingJob | None:
    return db.scalar(
        select(DocumentProcessingJob)
        .where(
            DocumentProcessingJob.document_version_id
            == document_version_id,
            DocumentProcessingJob.status.in_(
                ["QUEUED", "processing"]
            ),
        )
        .order_by(
            DocumentProcessingJob.created_at.desc()
        )
        .limit(1)
    )


def x_get_active_processing_job__mutmut_15(
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
        .limit(2)
    )

mutants_x_get_active_processing_job__mutmut['_mutmut_orig'] = x_get_active_processing_job__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_active_processing_job__mutmut['x_get_active_processing_job__mutmut_1'] = x_get_active_processing_job__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_active_processing_job__mutmut['x_get_active_processing_job__mutmut_2'] = x_get_active_processing_job__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_active_processing_job__mutmut['x_get_active_processing_job__mutmut_3'] = x_get_active_processing_job__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_active_processing_job__mutmut['x_get_active_processing_job__mutmut_4'] = x_get_active_processing_job__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_active_processing_job__mutmut['x_get_active_processing_job__mutmut_5'] = x_get_active_processing_job__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_active_processing_job__mutmut['x_get_active_processing_job__mutmut_6'] = x_get_active_processing_job__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_active_processing_job__mutmut['x_get_active_processing_job__mutmut_7'] = x_get_active_processing_job__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_active_processing_job__mutmut['x_get_active_processing_job__mutmut_8'] = x_get_active_processing_job__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_active_processing_job__mutmut['x_get_active_processing_job__mutmut_9'] = x_get_active_processing_job__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_active_processing_job__mutmut['x_get_active_processing_job__mutmut_10'] = x_get_active_processing_job__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_active_processing_job__mutmut['x_get_active_processing_job__mutmut_11'] = x_get_active_processing_job__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_active_processing_job__mutmut['x_get_active_processing_job__mutmut_12'] = x_get_active_processing_job__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_active_processing_job__mutmut['x_get_active_processing_job__mutmut_13'] = x_get_active_processing_job__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_active_processing_job__mutmut['x_get_active_processing_job__mutmut_14'] = x_get_active_processing_job__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_active_processing_job__mutmut['x_get_active_processing_job__mutmut_15'] = x_get_active_processing_job__mutmut_15 # type: ignore # mutmut generated
mutants_x_update_processing_job__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_update_processing_job__mutmut)
def update_processing_job(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    db.add(job)
    db.flush()
    db.refresh(job)
    return job


def x_update_processing_job__mutmut_orig(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    db.add(job)
    db.flush()
    db.refresh(job)
    return job


def x_update_processing_job__mutmut_1(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    db.add(None)
    db.flush()
    db.refresh(job)
    return job


def x_update_processing_job__mutmut_2(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    db.add(job)
    db.flush()
    db.refresh(None)
    return job

mutants_x_update_processing_job__mutmut['_mutmut_orig'] = x_update_processing_job__mutmut_orig # type: ignore # mutmut generated
mutants_x_update_processing_job__mutmut['x_update_processing_job__mutmut_1'] = x_update_processing_job__mutmut_1 # type: ignore # mutmut generated
mutants_x_update_processing_job__mutmut['x_update_processing_job__mutmut_2'] = x_update_processing_job__mutmut_2 # type: ignore # mutmut generated