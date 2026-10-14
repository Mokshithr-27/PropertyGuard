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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_queue_document_processing__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_queue_document_processing__mutmut)
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


def x_queue_document_processing__mutmut_orig(
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


def x_queue_document_processing__mutmut_1(
    db: Session,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """
    Queue document processing for a document version.

    Prevents multiple active jobs for the same version.
    """

    if version.deleted_at is None:
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


def x_queue_document_processing__mutmut_2(
    db: Session,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """
    Queue document processing for a document version.

    Prevents multiple active jobs for the same version.
    """

    if version.deleted_at is not None:
        raise ValueError(None)

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


def x_queue_document_processing__mutmut_3(
    db: Session,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """
    Queue document processing for a document version.

    Prevents multiple active jobs for the same version.
    """

    if version.deleted_at is not None:
        raise ValueError("XXCannot process a deleted document versionXX")

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


def x_queue_document_processing__mutmut_4(
    db: Session,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """
    Queue document processing for a document version.

    Prevents multiple active jobs for the same version.
    """

    if version.deleted_at is not None:
        raise ValueError("cannot process a deleted document version")

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


def x_queue_document_processing__mutmut_5(
    db: Session,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """
    Queue document processing for a document version.

    Prevents multiple active jobs for the same version.
    """

    if version.deleted_at is not None:
        raise ValueError("CANNOT PROCESS A DELETED DOCUMENT VERSION")

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


def x_queue_document_processing__mutmut_6(
    db: Session,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """
    Queue document processing for a document version.

    Prevents multiple active jobs for the same version.
    """

    if version.deleted_at is not None:
        raise ValueError("Cannot process a deleted document version")

    active_job = None

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


def x_queue_document_processing__mutmut_7(
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
        None,
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


def x_queue_document_processing__mutmut_8(
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
        None,
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


def x_queue_document_processing__mutmut_9(
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


def x_queue_document_processing__mutmut_10(
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


def x_queue_document_processing__mutmut_11(
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

    if active_job is None:
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


def x_queue_document_processing__mutmut_12(
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
            None
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


def x_queue_document_processing__mutmut_13(
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
            "XXAn active processing job already existsXX"
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


def x_queue_document_processing__mutmut_14(
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
            "an active processing job already exists"
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


def x_queue_document_processing__mutmut_15(
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
            "AN ACTIVE PROCESSING JOB ALREADY EXISTS"
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


def x_queue_document_processing__mutmut_16(
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

    job = None

    version.processing_status = "QUEUED"

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_17(
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
        document_version_id=None,
        status="QUEUED",
        attempt_count=0,
        queued_at=datetime.now(timezone.utc),
    )

    version.processing_status = "QUEUED"

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_18(
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
        status=None,
        attempt_count=0,
        queued_at=datetime.now(timezone.utc),
    )

    version.processing_status = "QUEUED"

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_19(
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
        attempt_count=None,
        queued_at=datetime.now(timezone.utc),
    )

    version.processing_status = "QUEUED"

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_20(
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
        queued_at=None,
    )

    version.processing_status = "QUEUED"

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_21(
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
        status="QUEUED",
        attempt_count=0,
        queued_at=datetime.now(timezone.utc),
    )

    version.processing_status = "QUEUED"

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_22(
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
        attempt_count=0,
        queued_at=datetime.now(timezone.utc),
    )

    version.processing_status = "QUEUED"

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_23(
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
        queued_at=datetime.now(timezone.utc),
    )

    version.processing_status = "QUEUED"

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_24(
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
        )

    version.processing_status = "QUEUED"

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_25(
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
        status="XXQUEUEDXX",
        attempt_count=0,
        queued_at=datetime.now(timezone.utc),
    )

    version.processing_status = "QUEUED"

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_26(
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
        status="queued",
        attempt_count=0,
        queued_at=datetime.now(timezone.utc),
    )

    version.processing_status = "QUEUED"

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_27(
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
        attempt_count=1,
        queued_at=datetime.now(timezone.utc),
    )

    version.processing_status = "QUEUED"

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_28(
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
        queued_at=datetime.now(None),
    )

    version.processing_status = "QUEUED"

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_29(
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

    version.processing_status = None

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_30(
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

    version.processing_status = "XXQUEUEDXX"

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_31(
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

    version.processing_status = "queued"

    create_processing_job(db, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_32(
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

    create_processing_job(None, job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_33(
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

    create_processing_job(db, None)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_34(
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

    create_processing_job(job)
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_35(
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

    create_processing_job(db, )
    update_document_version(db, version)

    return job


def x_queue_document_processing__mutmut_36(
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
    update_document_version(None, version)

    return job


def x_queue_document_processing__mutmut_37(
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
    update_document_version(db, None)

    return job


def x_queue_document_processing__mutmut_38(
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
    update_document_version(version)

    return job


def x_queue_document_processing__mutmut_39(
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
    update_document_version(db, )

    return job

mutants_x_queue_document_processing__mutmut['_mutmut_orig'] = x_queue_document_processing__mutmut_orig # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_1'] = x_queue_document_processing__mutmut_1 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_2'] = x_queue_document_processing__mutmut_2 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_3'] = x_queue_document_processing__mutmut_3 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_4'] = x_queue_document_processing__mutmut_4 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_5'] = x_queue_document_processing__mutmut_5 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_6'] = x_queue_document_processing__mutmut_6 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_7'] = x_queue_document_processing__mutmut_7 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_8'] = x_queue_document_processing__mutmut_8 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_9'] = x_queue_document_processing__mutmut_9 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_10'] = x_queue_document_processing__mutmut_10 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_11'] = x_queue_document_processing__mutmut_11 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_12'] = x_queue_document_processing__mutmut_12 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_13'] = x_queue_document_processing__mutmut_13 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_14'] = x_queue_document_processing__mutmut_14 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_15'] = x_queue_document_processing__mutmut_15 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_16'] = x_queue_document_processing__mutmut_16 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_17'] = x_queue_document_processing__mutmut_17 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_18'] = x_queue_document_processing__mutmut_18 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_19'] = x_queue_document_processing__mutmut_19 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_20'] = x_queue_document_processing__mutmut_20 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_21'] = x_queue_document_processing__mutmut_21 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_22'] = x_queue_document_processing__mutmut_22 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_23'] = x_queue_document_processing__mutmut_23 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_24'] = x_queue_document_processing__mutmut_24 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_25'] = x_queue_document_processing__mutmut_25 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_26'] = x_queue_document_processing__mutmut_26 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_27'] = x_queue_document_processing__mutmut_27 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_28'] = x_queue_document_processing__mutmut_28 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_29'] = x_queue_document_processing__mutmut_29 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_30'] = x_queue_document_processing__mutmut_30 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_31'] = x_queue_document_processing__mutmut_31 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_32'] = x_queue_document_processing__mutmut_32 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_33'] = x_queue_document_processing__mutmut_33 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_34'] = x_queue_document_processing__mutmut_34 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_35'] = x_queue_document_processing__mutmut_35 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_36'] = x_queue_document_processing__mutmut_36 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_37'] = x_queue_document_processing__mutmut_37 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_38'] = x_queue_document_processing__mutmut_38 # type: ignore # mutmut generated
mutants_x_queue_document_processing__mutmut['x_queue_document_processing__mutmut_39'] = x_queue_document_processing__mutmut_39 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_start_document_processing__mutmut)
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


def x_start_document_processing__mutmut_orig(
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


def x_start_document_processing__mutmut_1(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    """Mark a queued job as processing."""

    if job.status == "QUEUED":
        raise ValueError(
            "Only queued jobs can be started"
        )

    job.status = "PROCESSING"
    job.attempt_count += 1
    job.started_at = datetime.now(timezone.utc)

    return update_processing_job(db, job)


def x_start_document_processing__mutmut_2(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    """Mark a queued job as processing."""

    if job.status != "XXQUEUEDXX":
        raise ValueError(
            "Only queued jobs can be started"
        )

    job.status = "PROCESSING"
    job.attempt_count += 1
    job.started_at = datetime.now(timezone.utc)

    return update_processing_job(db, job)


def x_start_document_processing__mutmut_3(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    """Mark a queued job as processing."""

    if job.status != "queued":
        raise ValueError(
            "Only queued jobs can be started"
        )

    job.status = "PROCESSING"
    job.attempt_count += 1
    job.started_at = datetime.now(timezone.utc)

    return update_processing_job(db, job)


def x_start_document_processing__mutmut_4(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    """Mark a queued job as processing."""

    if job.status != "QUEUED":
        raise ValueError(
            None
        )

    job.status = "PROCESSING"
    job.attempt_count += 1
    job.started_at = datetime.now(timezone.utc)

    return update_processing_job(db, job)


def x_start_document_processing__mutmut_5(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    """Mark a queued job as processing."""

    if job.status != "QUEUED":
        raise ValueError(
            "XXOnly queued jobs can be startedXX"
        )

    job.status = "PROCESSING"
    job.attempt_count += 1
    job.started_at = datetime.now(timezone.utc)

    return update_processing_job(db, job)


def x_start_document_processing__mutmut_6(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    """Mark a queued job as processing."""

    if job.status != "QUEUED":
        raise ValueError(
            "only queued jobs can be started"
        )

    job.status = "PROCESSING"
    job.attempt_count += 1
    job.started_at = datetime.now(timezone.utc)

    return update_processing_job(db, job)


def x_start_document_processing__mutmut_7(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    """Mark a queued job as processing."""

    if job.status != "QUEUED":
        raise ValueError(
            "ONLY QUEUED JOBS CAN BE STARTED"
        )

    job.status = "PROCESSING"
    job.attempt_count += 1
    job.started_at = datetime.now(timezone.utc)

    return update_processing_job(db, job)


def x_start_document_processing__mutmut_8(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    """Mark a queued job as processing."""

    if job.status != "QUEUED":
        raise ValueError(
            "Only queued jobs can be started"
        )

    job.status = None
    job.attempt_count += 1
    job.started_at = datetime.now(timezone.utc)

    return update_processing_job(db, job)


def x_start_document_processing__mutmut_9(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    """Mark a queued job as processing."""

    if job.status != "QUEUED":
        raise ValueError(
            "Only queued jobs can be started"
        )

    job.status = "XXPROCESSINGXX"
    job.attempt_count += 1
    job.started_at = datetime.now(timezone.utc)

    return update_processing_job(db, job)


def x_start_document_processing__mutmut_10(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    """Mark a queued job as processing."""

    if job.status != "QUEUED":
        raise ValueError(
            "Only queued jobs can be started"
        )

    job.status = "processing"
    job.attempt_count += 1
    job.started_at = datetime.now(timezone.utc)

    return update_processing_job(db, job)


def x_start_document_processing__mutmut_11(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    """Mark a queued job as processing."""

    if job.status != "QUEUED":
        raise ValueError(
            "Only queued jobs can be started"
        )

    job.status = "PROCESSING"
    job.attempt_count = 1
    job.started_at = datetime.now(timezone.utc)

    return update_processing_job(db, job)


def x_start_document_processing__mutmut_12(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    """Mark a queued job as processing."""

    if job.status != "QUEUED":
        raise ValueError(
            "Only queued jobs can be started"
        )

    job.status = "PROCESSING"
    job.attempt_count -= 1
    job.started_at = datetime.now(timezone.utc)

    return update_processing_job(db, job)


def x_start_document_processing__mutmut_13(
    db: Session,
    job: DocumentProcessingJob,
) -> DocumentProcessingJob:
    """Mark a queued job as processing."""

    if job.status != "QUEUED":
        raise ValueError(
            "Only queued jobs can be started"
        )

    job.status = "PROCESSING"
    job.attempt_count += 2
    job.started_at = datetime.now(timezone.utc)

    return update_processing_job(db, job)


def x_start_document_processing__mutmut_14(
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
    job.started_at = None

    return update_processing_job(db, job)


def x_start_document_processing__mutmut_15(
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
    job.started_at = datetime.now(None)

    return update_processing_job(db, job)


def x_start_document_processing__mutmut_16(
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

    return update_processing_job(None, job)


def x_start_document_processing__mutmut_17(
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

    return update_processing_job(db, None)


def x_start_document_processing__mutmut_18(
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

    return update_processing_job(job)


def x_start_document_processing__mutmut_19(
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

    return update_processing_job(db, )

mutants_x_start_document_processing__mutmut['_mutmut_orig'] = x_start_document_processing__mutmut_orig # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_1'] = x_start_document_processing__mutmut_1 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_2'] = x_start_document_processing__mutmut_2 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_3'] = x_start_document_processing__mutmut_3 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_4'] = x_start_document_processing__mutmut_4 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_5'] = x_start_document_processing__mutmut_5 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_6'] = x_start_document_processing__mutmut_6 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_7'] = x_start_document_processing__mutmut_7 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_8'] = x_start_document_processing__mutmut_8 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_9'] = x_start_document_processing__mutmut_9 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_10'] = x_start_document_processing__mutmut_10 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_11'] = x_start_document_processing__mutmut_11 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_12'] = x_start_document_processing__mutmut_12 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_13'] = x_start_document_processing__mutmut_13 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_14'] = x_start_document_processing__mutmut_14 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_15'] = x_start_document_processing__mutmut_15 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_16'] = x_start_document_processing__mutmut_16 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_17'] = x_start_document_processing__mutmut_17 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_18'] = x_start_document_processing__mutmut_18 # type: ignore # mutmut generated
mutants_x_start_document_processing__mutmut['x_start_document_processing__mutmut_19'] = x_start_document_processing__mutmut_19 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_complete_document_processing__mutmut)
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


def x_complete_document_processing__mutmut_orig(
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


def x_complete_document_processing__mutmut_1(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """Mark processing as completed."""

    if job.status == "PROCESSING":
        raise ValueError(
            "Only processing jobs can be completed"
        )

    job.status = "COMPLETED"
    job.completed_at = datetime.now(timezone.utc)
    version.processing_status = "COMPLETED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_2(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """Mark processing as completed."""

    if job.status != "XXPROCESSINGXX":
        raise ValueError(
            "Only processing jobs can be completed"
        )

    job.status = "COMPLETED"
    job.completed_at = datetime.now(timezone.utc)
    version.processing_status = "COMPLETED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_3(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """Mark processing as completed."""

    if job.status != "processing":
        raise ValueError(
            "Only processing jobs can be completed"
        )

    job.status = "COMPLETED"
    job.completed_at = datetime.now(timezone.utc)
    version.processing_status = "COMPLETED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_4(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """Mark processing as completed."""

    if job.status != "PROCESSING":
        raise ValueError(
            None
        )

    job.status = "COMPLETED"
    job.completed_at = datetime.now(timezone.utc)
    version.processing_status = "COMPLETED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_5(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """Mark processing as completed."""

    if job.status != "PROCESSING":
        raise ValueError(
            "XXOnly processing jobs can be completedXX"
        )

    job.status = "COMPLETED"
    job.completed_at = datetime.now(timezone.utc)
    version.processing_status = "COMPLETED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_6(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """Mark processing as completed."""

    if job.status != "PROCESSING":
        raise ValueError(
            "only processing jobs can be completed"
        )

    job.status = "COMPLETED"
    job.completed_at = datetime.now(timezone.utc)
    version.processing_status = "COMPLETED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_7(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """Mark processing as completed."""

    if job.status != "PROCESSING":
        raise ValueError(
            "ONLY PROCESSING JOBS CAN BE COMPLETED"
        )

    job.status = "COMPLETED"
    job.completed_at = datetime.now(timezone.utc)
    version.processing_status = "COMPLETED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_8(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """Mark processing as completed."""

    if job.status != "PROCESSING":
        raise ValueError(
            "Only processing jobs can be completed"
        )

    job.status = None
    job.completed_at = datetime.now(timezone.utc)
    version.processing_status = "COMPLETED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_9(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """Mark processing as completed."""

    if job.status != "PROCESSING":
        raise ValueError(
            "Only processing jobs can be completed"
        )

    job.status = "XXCOMPLETEDXX"
    job.completed_at = datetime.now(timezone.utc)
    version.processing_status = "COMPLETED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_10(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
) -> DocumentProcessingJob:
    """Mark processing as completed."""

    if job.status != "PROCESSING":
        raise ValueError(
            "Only processing jobs can be completed"
        )

    job.status = "completed"
    job.completed_at = datetime.now(timezone.utc)
    version.processing_status = "COMPLETED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_11(
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
    job.completed_at = None
    version.processing_status = "COMPLETED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_12(
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
    job.completed_at = datetime.now(None)
    version.processing_status = "COMPLETED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_13(
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
    version.processing_status = None

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_14(
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
    version.processing_status = "XXCOMPLETEDXX"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_15(
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
    version.processing_status = "completed"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_16(
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

    update_document_version(None, version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_17(
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

    update_document_version(db, None)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_18(
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

    update_document_version(version)

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_19(
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

    update_document_version(db, )

    return update_processing_job(db, job)


def x_complete_document_processing__mutmut_20(
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

    return update_processing_job(None, job)


def x_complete_document_processing__mutmut_21(
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

    return update_processing_job(db, None)


def x_complete_document_processing__mutmut_22(
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

    return update_processing_job(job)


def x_complete_document_processing__mutmut_23(
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

    return update_processing_job(db, )

mutants_x_complete_document_processing__mutmut['_mutmut_orig'] = x_complete_document_processing__mutmut_orig # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_1'] = x_complete_document_processing__mutmut_1 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_2'] = x_complete_document_processing__mutmut_2 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_3'] = x_complete_document_processing__mutmut_3 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_4'] = x_complete_document_processing__mutmut_4 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_5'] = x_complete_document_processing__mutmut_5 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_6'] = x_complete_document_processing__mutmut_6 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_7'] = x_complete_document_processing__mutmut_7 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_8'] = x_complete_document_processing__mutmut_8 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_9'] = x_complete_document_processing__mutmut_9 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_10'] = x_complete_document_processing__mutmut_10 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_11'] = x_complete_document_processing__mutmut_11 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_12'] = x_complete_document_processing__mutmut_12 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_13'] = x_complete_document_processing__mutmut_13 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_14'] = x_complete_document_processing__mutmut_14 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_15'] = x_complete_document_processing__mutmut_15 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_16'] = x_complete_document_processing__mutmut_16 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_17'] = x_complete_document_processing__mutmut_17 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_18'] = x_complete_document_processing__mutmut_18 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_19'] = x_complete_document_processing__mutmut_19 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_20'] = x_complete_document_processing__mutmut_20 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_21'] = x_complete_document_processing__mutmut_21 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_22'] = x_complete_document_processing__mutmut_22 # type: ignore # mutmut generated
mutants_x_complete_document_processing__mutmut['x_complete_document_processing__mutmut_23'] = x_complete_document_processing__mutmut_23 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_fail_document_processing__mutmut)
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


def x_fail_document_processing__mutmut_orig(
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


def x_fail_document_processing__mutmut_1(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
    error_message: str,
) -> DocumentProcessingJob:
    """Mark processing as failed."""

    if job.status == "PROCESSING":
        raise ValueError(
            "Only processing jobs can fail"
        )

    job.status = "FAILED"
    job.completed_at = datetime.now(timezone.utc)
    job.error_message = error_message
    version.processing_status = "FAILED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_2(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
    error_message: str,
) -> DocumentProcessingJob:
    """Mark processing as failed."""

    if job.status != "XXPROCESSINGXX":
        raise ValueError(
            "Only processing jobs can fail"
        )

    job.status = "FAILED"
    job.completed_at = datetime.now(timezone.utc)
    job.error_message = error_message
    version.processing_status = "FAILED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_3(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
    error_message: str,
) -> DocumentProcessingJob:
    """Mark processing as failed."""

    if job.status != "processing":
        raise ValueError(
            "Only processing jobs can fail"
        )

    job.status = "FAILED"
    job.completed_at = datetime.now(timezone.utc)
    job.error_message = error_message
    version.processing_status = "FAILED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_4(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
    error_message: str,
) -> DocumentProcessingJob:
    """Mark processing as failed."""

    if job.status != "PROCESSING":
        raise ValueError(
            None
        )

    job.status = "FAILED"
    job.completed_at = datetime.now(timezone.utc)
    job.error_message = error_message
    version.processing_status = "FAILED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_5(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
    error_message: str,
) -> DocumentProcessingJob:
    """Mark processing as failed."""

    if job.status != "PROCESSING":
        raise ValueError(
            "XXOnly processing jobs can failXX"
        )

    job.status = "FAILED"
    job.completed_at = datetime.now(timezone.utc)
    job.error_message = error_message
    version.processing_status = "FAILED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_6(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
    error_message: str,
) -> DocumentProcessingJob:
    """Mark processing as failed."""

    if job.status != "PROCESSING":
        raise ValueError(
            "only processing jobs can fail"
        )

    job.status = "FAILED"
    job.completed_at = datetime.now(timezone.utc)
    job.error_message = error_message
    version.processing_status = "FAILED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_7(
    db: Session,
    job: DocumentProcessingJob,
    version: DocumentVersion,
    error_message: str,
) -> DocumentProcessingJob:
    """Mark processing as failed."""

    if job.status != "PROCESSING":
        raise ValueError(
            "ONLY PROCESSING JOBS CAN FAIL"
        )

    job.status = "FAILED"
    job.completed_at = datetime.now(timezone.utc)
    job.error_message = error_message
    version.processing_status = "FAILED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_8(
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

    job.status = None
    job.completed_at = datetime.now(timezone.utc)
    job.error_message = error_message
    version.processing_status = "FAILED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_9(
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

    job.status = "XXFAILEDXX"
    job.completed_at = datetime.now(timezone.utc)
    job.error_message = error_message
    version.processing_status = "FAILED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_10(
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

    job.status = "failed"
    job.completed_at = datetime.now(timezone.utc)
    job.error_message = error_message
    version.processing_status = "FAILED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_11(
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
    job.completed_at = None
    job.error_message = error_message
    version.processing_status = "FAILED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_12(
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
    job.completed_at = datetime.now(None)
    job.error_message = error_message
    version.processing_status = "FAILED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_13(
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
    job.error_message = None
    version.processing_status = "FAILED"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_14(
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
    version.processing_status = None

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_15(
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
    version.processing_status = "XXFAILEDXX"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_16(
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
    version.processing_status = "failed"

    update_document_version(db, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_17(
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

    update_document_version(None, version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_18(
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

    update_document_version(db, None)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_19(
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

    update_document_version(version)

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_20(
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

    update_document_version(db, )

    return update_processing_job(db, job)


def x_fail_document_processing__mutmut_21(
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

    return update_processing_job(None, job)


def x_fail_document_processing__mutmut_22(
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

    return update_processing_job(db, None)


def x_fail_document_processing__mutmut_23(
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

    return update_processing_job(job)


def x_fail_document_processing__mutmut_24(
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

    return update_processing_job(db, )

mutants_x_fail_document_processing__mutmut['_mutmut_orig'] = x_fail_document_processing__mutmut_orig # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_1'] = x_fail_document_processing__mutmut_1 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_2'] = x_fail_document_processing__mutmut_2 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_3'] = x_fail_document_processing__mutmut_3 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_4'] = x_fail_document_processing__mutmut_4 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_5'] = x_fail_document_processing__mutmut_5 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_6'] = x_fail_document_processing__mutmut_6 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_7'] = x_fail_document_processing__mutmut_7 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_8'] = x_fail_document_processing__mutmut_8 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_9'] = x_fail_document_processing__mutmut_9 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_10'] = x_fail_document_processing__mutmut_10 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_11'] = x_fail_document_processing__mutmut_11 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_12'] = x_fail_document_processing__mutmut_12 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_13'] = x_fail_document_processing__mutmut_13 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_14'] = x_fail_document_processing__mutmut_14 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_15'] = x_fail_document_processing__mutmut_15 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_16'] = x_fail_document_processing__mutmut_16 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_17'] = x_fail_document_processing__mutmut_17 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_18'] = x_fail_document_processing__mutmut_18 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_19'] = x_fail_document_processing__mutmut_19 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_20'] = x_fail_document_processing__mutmut_20 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_21'] = x_fail_document_processing__mutmut_21 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_22'] = x_fail_document_processing__mutmut_22 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_23'] = x_fail_document_processing__mutmut_23 # type: ignore # mutmut generated
mutants_x_fail_document_processing__mutmut['x_fail_document_processing__mutmut_24'] = x_fail_document_processing__mutmut_24 # type: ignore # mutmut generated