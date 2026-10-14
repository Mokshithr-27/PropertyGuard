"""
PropertyGuard Document Management Service
-----------------------------------------
Coordinates document upload, SHA-256 integrity hashing, incremental version numbering,
MinIO object storage persistence, version metadata updates, and soft deletion.
"""

import hashlib
import uuid

from sqlalchemy.orm import Session

from app.integrations.storage import (
    delete_object,
    object_exists,
    upload_bytes,
)
from app.models import Document, DocumentVersion
from app.repositories.document_repository import (
    create_document as create_document_record,
    create_document_version as create_document_version_record,
    get_latest_version,
    soft_delete_document as soft_delete_document_record,
    update_document_version,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_calculate_file_hash__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_calculate_file_hash__mutmut)
def calculate_file_hash(data: bytes) -> str:
    """Calculate SHA-256 hash of a file."""
    return hashlib.sha256(data).hexdigest()


def x_calculate_file_hash__mutmut_orig(data: bytes) -> str:
    """Calculate SHA-256 hash of a file."""
    return hashlib.sha256(data).hexdigest()


def x_calculate_file_hash__mutmut_1(data: bytes) -> str:
    """Calculate SHA-256 hash of a file."""
    return hashlib.sha256(None).hexdigest()

mutants_x_calculate_file_hash__mutmut['_mutmut_orig'] = x_calculate_file_hash__mutmut_orig # type: ignore # mutmut generated
mutants_x_calculate_file_hash__mutmut['x_calculate_file_hash__mutmut_1'] = x_calculate_file_hash__mutmut_1 # type: ignore # mutmut generated


def generate_storage_key(
    project_id: uuid.UUID,
    document_id: uuid.UUID,
    version_number: int,
    file_name: str,
) -> str:
    """Generate a unique MinIO object key."""

    return (
        f"projects/{project_id}/"
        f"documents/{document_id}/"
        f"v{version_number}/"
        f"{file_name}"
    )
mutants_x_get_next_version_number__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_next_version_number__mutmut)
def get_next_version_number(
    db: Session,
    document_id: uuid.UUID,
) -> int:
    """Return the next version number for a document."""

    latest_version = get_latest_version(
        db,
        document_id,
    )

    if latest_version is None:
        return 1

    return latest_version.version_number + 1


def x_get_next_version_number__mutmut_orig(
    db: Session,
    document_id: uuid.UUID,
) -> int:
    """Return the next version number for a document."""

    latest_version = get_latest_version(
        db,
        document_id,
    )

    if latest_version is None:
        return 1

    return latest_version.version_number + 1


def x_get_next_version_number__mutmut_1(
    db: Session,
    document_id: uuid.UUID,
) -> int:
    """Return the next version number for a document."""

    latest_version = None

    if latest_version is None:
        return 1

    return latest_version.version_number + 1


def x_get_next_version_number__mutmut_2(
    db: Session,
    document_id: uuid.UUID,
) -> int:
    """Return the next version number for a document."""

    latest_version = get_latest_version(
        None,
        document_id,
    )

    if latest_version is None:
        return 1

    return latest_version.version_number + 1


def x_get_next_version_number__mutmut_3(
    db: Session,
    document_id: uuid.UUID,
) -> int:
    """Return the next version number for a document."""

    latest_version = get_latest_version(
        db,
        None,
    )

    if latest_version is None:
        return 1

    return latest_version.version_number + 1


def x_get_next_version_number__mutmut_4(
    db: Session,
    document_id: uuid.UUID,
) -> int:
    """Return the next version number for a document."""

    latest_version = get_latest_version(
        document_id,
    )

    if latest_version is None:
        return 1

    return latest_version.version_number + 1


def x_get_next_version_number__mutmut_5(
    db: Session,
    document_id: uuid.UUID,
) -> int:
    """Return the next version number for a document."""

    latest_version = get_latest_version(
        db,
        )

    if latest_version is None:
        return 1

    return latest_version.version_number + 1


def x_get_next_version_number__mutmut_6(
    db: Session,
    document_id: uuid.UUID,
) -> int:
    """Return the next version number for a document."""

    latest_version = get_latest_version(
        db,
        document_id,
    )

    if latest_version is not None:
        return 1

    return latest_version.version_number + 1


def x_get_next_version_number__mutmut_7(
    db: Session,
    document_id: uuid.UUID,
) -> int:
    """Return the next version number for a document."""

    latest_version = get_latest_version(
        db,
        document_id,
    )

    if latest_version is None:
        return 2

    return latest_version.version_number + 1


def x_get_next_version_number__mutmut_8(
    db: Session,
    document_id: uuid.UUID,
) -> int:
    """Return the next version number for a document."""

    latest_version = get_latest_version(
        db,
        document_id,
    )

    if latest_version is None:
        return 1

    return latest_version.version_number - 1


def x_get_next_version_number__mutmut_9(
    db: Session,
    document_id: uuid.UUID,
) -> int:
    """Return the next version number for a document."""

    latest_version = get_latest_version(
        db,
        document_id,
    )

    if latest_version is None:
        return 1

    return latest_version.version_number + 2

mutants_x_get_next_version_number__mutmut['_mutmut_orig'] = x_get_next_version_number__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_next_version_number__mutmut['x_get_next_version_number__mutmut_1'] = x_get_next_version_number__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_next_version_number__mutmut['x_get_next_version_number__mutmut_2'] = x_get_next_version_number__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_next_version_number__mutmut['x_get_next_version_number__mutmut_3'] = x_get_next_version_number__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_next_version_number__mutmut['x_get_next_version_number__mutmut_4'] = x_get_next_version_number__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_next_version_number__mutmut['x_get_next_version_number__mutmut_5'] = x_get_next_version_number__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_next_version_number__mutmut['x_get_next_version_number__mutmut_6'] = x_get_next_version_number__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_next_version_number__mutmut['x_get_next_version_number__mutmut_7'] = x_get_next_version_number__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_next_version_number__mutmut['x_get_next_version_number__mutmut_8'] = x_get_next_version_number__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_next_version_number__mutmut['x_get_next_version_number__mutmut_9'] = x_get_next_version_number__mutmut_9 # type: ignore # mutmut generated
mutants_x_delete_document__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_delete_document__mutmut)
def delete_document(
    db: Session,
    document: Document,
) -> Document:
    """
    Soft-delete an existing document.

    The database record is preserved for audit/history.
    The document is marked INACTIVE and receives a deleted_at timestamp.
    """

    if document.deleted_at is not None:
        raise ValueError("Document is already deleted")

    document.status = "INACTIVE"

    return soft_delete_document_record(
        db,
        document,
    )

def x_delete_document__mutmut_orig(
    db: Session,
    document: Document,
) -> Document:
    """
    Soft-delete an existing document.

    The database record is preserved for audit/history.
    The document is marked INACTIVE and receives a deleted_at timestamp.
    """

    if document.deleted_at is not None:
        raise ValueError("Document is already deleted")

    document.status = "INACTIVE"

    return soft_delete_document_record(
        db,
        document,
    )

def x_delete_document__mutmut_1(
    db: Session,
    document: Document,
) -> Document:
    """
    Soft-delete an existing document.

    The database record is preserved for audit/history.
    The document is marked INACTIVE and receives a deleted_at timestamp.
    """

    if document.deleted_at is None:
        raise ValueError("Document is already deleted")

    document.status = "INACTIVE"

    return soft_delete_document_record(
        db,
        document,
    )

def x_delete_document__mutmut_2(
    db: Session,
    document: Document,
) -> Document:
    """
    Soft-delete an existing document.

    The database record is preserved for audit/history.
    The document is marked INACTIVE and receives a deleted_at timestamp.
    """

    if document.deleted_at is not None:
        raise ValueError(None)

    document.status = "INACTIVE"

    return soft_delete_document_record(
        db,
        document,
    )

def x_delete_document__mutmut_3(
    db: Session,
    document: Document,
) -> Document:
    """
    Soft-delete an existing document.

    The database record is preserved for audit/history.
    The document is marked INACTIVE and receives a deleted_at timestamp.
    """

    if document.deleted_at is not None:
        raise ValueError("XXDocument is already deletedXX")

    document.status = "INACTIVE"

    return soft_delete_document_record(
        db,
        document,
    )

def x_delete_document__mutmut_4(
    db: Session,
    document: Document,
) -> Document:
    """
    Soft-delete an existing document.

    The database record is preserved for audit/history.
    The document is marked INACTIVE and receives a deleted_at timestamp.
    """

    if document.deleted_at is not None:
        raise ValueError("document is already deleted")

    document.status = "INACTIVE"

    return soft_delete_document_record(
        db,
        document,
    )

def x_delete_document__mutmut_5(
    db: Session,
    document: Document,
) -> Document:
    """
    Soft-delete an existing document.

    The database record is preserved for audit/history.
    The document is marked INACTIVE and receives a deleted_at timestamp.
    """

    if document.deleted_at is not None:
        raise ValueError("DOCUMENT IS ALREADY DELETED")

    document.status = "INACTIVE"

    return soft_delete_document_record(
        db,
        document,
    )

def x_delete_document__mutmut_6(
    db: Session,
    document: Document,
) -> Document:
    """
    Soft-delete an existing document.

    The database record is preserved for audit/history.
    The document is marked INACTIVE and receives a deleted_at timestamp.
    """

    if document.deleted_at is not None:
        raise ValueError("Document is already deleted")

    document.status = None

    return soft_delete_document_record(
        db,
        document,
    )

def x_delete_document__mutmut_7(
    db: Session,
    document: Document,
) -> Document:
    """
    Soft-delete an existing document.

    The database record is preserved for audit/history.
    The document is marked INACTIVE and receives a deleted_at timestamp.
    """

    if document.deleted_at is not None:
        raise ValueError("Document is already deleted")

    document.status = "XXINACTIVEXX"

    return soft_delete_document_record(
        db,
        document,
    )

def x_delete_document__mutmut_8(
    db: Session,
    document: Document,
) -> Document:
    """
    Soft-delete an existing document.

    The database record is preserved for audit/history.
    The document is marked INACTIVE and receives a deleted_at timestamp.
    """

    if document.deleted_at is not None:
        raise ValueError("Document is already deleted")

    document.status = "inactive"

    return soft_delete_document_record(
        db,
        document,
    )

def x_delete_document__mutmut_9(
    db: Session,
    document: Document,
) -> Document:
    """
    Soft-delete an existing document.

    The database record is preserved for audit/history.
    The document is marked INACTIVE and receives a deleted_at timestamp.
    """

    if document.deleted_at is not None:
        raise ValueError("Document is already deleted")

    document.status = "INACTIVE"

    return soft_delete_document_record(
        None,
        document,
    )

def x_delete_document__mutmut_10(
    db: Session,
    document: Document,
) -> Document:
    """
    Soft-delete an existing document.

    The database record is preserved for audit/history.
    The document is marked INACTIVE and receives a deleted_at timestamp.
    """

    if document.deleted_at is not None:
        raise ValueError("Document is already deleted")

    document.status = "INACTIVE"

    return soft_delete_document_record(
        db,
        None,
    )

def x_delete_document__mutmut_11(
    db: Session,
    document: Document,
) -> Document:
    """
    Soft-delete an existing document.

    The database record is preserved for audit/history.
    The document is marked INACTIVE and receives a deleted_at timestamp.
    """

    if document.deleted_at is not None:
        raise ValueError("Document is already deleted")

    document.status = "INACTIVE"

    return soft_delete_document_record(
        document,
    )

def x_delete_document__mutmut_12(
    db: Session,
    document: Document,
) -> Document:
    """
    Soft-delete an existing document.

    The database record is preserved for audit/history.
    The document is marked INACTIVE and receives a deleted_at timestamp.
    """

    if document.deleted_at is not None:
        raise ValueError("Document is already deleted")

    document.status = "INACTIVE"

    return soft_delete_document_record(
        db,
        )

mutants_x_delete_document__mutmut['_mutmut_orig'] = x_delete_document__mutmut_orig # type: ignore # mutmut generated
mutants_x_delete_document__mutmut['x_delete_document__mutmut_1'] = x_delete_document__mutmut_1 # type: ignore # mutmut generated
mutants_x_delete_document__mutmut['x_delete_document__mutmut_2'] = x_delete_document__mutmut_2 # type: ignore # mutmut generated
mutants_x_delete_document__mutmut['x_delete_document__mutmut_3'] = x_delete_document__mutmut_3 # type: ignore # mutmut generated
mutants_x_delete_document__mutmut['x_delete_document__mutmut_4'] = x_delete_document__mutmut_4 # type: ignore # mutmut generated
mutants_x_delete_document__mutmut['x_delete_document__mutmut_5'] = x_delete_document__mutmut_5 # type: ignore # mutmut generated
mutants_x_delete_document__mutmut['x_delete_document__mutmut_6'] = x_delete_document__mutmut_6 # type: ignore # mutmut generated
mutants_x_delete_document__mutmut['x_delete_document__mutmut_7'] = x_delete_document__mutmut_7 # type: ignore # mutmut generated
mutants_x_delete_document__mutmut['x_delete_document__mutmut_8'] = x_delete_document__mutmut_8 # type: ignore # mutmut generated
mutants_x_delete_document__mutmut['x_delete_document__mutmut_9'] = x_delete_document__mutmut_9 # type: ignore # mutmut generated
mutants_x_delete_document__mutmut['x_delete_document__mutmut_10'] = x_delete_document__mutmut_10 # type: ignore # mutmut generated
mutants_x_delete_document__mutmut['x_delete_document__mutmut_11'] = x_delete_document__mutmut_11 # type: ignore # mutmut generated
mutants_x_delete_document__mutmut['x_delete_document__mutmut_12'] = x_delete_document__mutmut_12 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_create_document_version__mutmut)
def create_document_version(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_orig(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_1(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = None

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_2(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        None,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_3(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        None,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_4(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_5(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_6(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = None
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_7(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = None

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_8(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(None)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_9(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = None

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_10(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=None,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_11(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=None,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_12(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=None,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_13(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=None,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_14(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_15(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_16(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_17(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_18(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(None):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_19(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            None
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_20(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=None,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_21(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=None,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_22(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=None,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_23(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_24(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_25(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_26(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = None

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_27(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=None,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_28(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=None,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_29(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=None,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_30(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=None,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_31(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=None,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_32(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=None,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_33(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=None,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_34(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=None,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_35(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status=None,
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_36(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_37(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_38(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_39(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_40(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_41(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_42(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_43(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_44(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_45(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="XXUPLOADEDXX",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_46(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="uploaded",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_47(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            None,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_48(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            None,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_49(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_50(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_51(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(None)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document_version__mutmut_52(
    db: Session,
    document: Document,
    uploaded_by: uuid.UUID,
    file_name: str,
    mime_type: str,
    data: bytes,
) -> DocumentVersion:
    """
    Create a new version for an existing document.

    The file is stored in MinIO and the version metadata
    is stored in PostgreSQL.
    """

    version_number = get_next_version_number(
        db,
        document.id,
    )

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    storage_key = generate_storage_key(
        project_id=document.project_id,
        document_id=document.id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document_version = DocumentVersion(
            document_id=document.id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document_version)

        return document_version

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(None)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

mutants_x_create_document_version__mutmut['_mutmut_orig'] = x_create_document_version__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_1'] = x_create_document_version__mutmut_1 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_2'] = x_create_document_version__mutmut_2 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_3'] = x_create_document_version__mutmut_3 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_4'] = x_create_document_version__mutmut_4 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_5'] = x_create_document_version__mutmut_5 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_6'] = x_create_document_version__mutmut_6 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_7'] = x_create_document_version__mutmut_7 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_8'] = x_create_document_version__mutmut_8 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_9'] = x_create_document_version__mutmut_9 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_10'] = x_create_document_version__mutmut_10 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_11'] = x_create_document_version__mutmut_11 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_12'] = x_create_document_version__mutmut_12 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_13'] = x_create_document_version__mutmut_13 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_14'] = x_create_document_version__mutmut_14 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_15'] = x_create_document_version__mutmut_15 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_16'] = x_create_document_version__mutmut_16 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_17'] = x_create_document_version__mutmut_17 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_18'] = x_create_document_version__mutmut_18 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_19'] = x_create_document_version__mutmut_19 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_20'] = x_create_document_version__mutmut_20 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_21'] = x_create_document_version__mutmut_21 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_22'] = x_create_document_version__mutmut_22 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_23'] = x_create_document_version__mutmut_23 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_24'] = x_create_document_version__mutmut_24 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_25'] = x_create_document_version__mutmut_25 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_26'] = x_create_document_version__mutmut_26 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_27'] = x_create_document_version__mutmut_27 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_28'] = x_create_document_version__mutmut_28 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_29'] = x_create_document_version__mutmut_29 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_30'] = x_create_document_version__mutmut_30 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_31'] = x_create_document_version__mutmut_31 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_32'] = x_create_document_version__mutmut_32 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_33'] = x_create_document_version__mutmut_33 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_34'] = x_create_document_version__mutmut_34 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_35'] = x_create_document_version__mutmut_35 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_36'] = x_create_document_version__mutmut_36 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_37'] = x_create_document_version__mutmut_37 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_38'] = x_create_document_version__mutmut_38 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_39'] = x_create_document_version__mutmut_39 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_40'] = x_create_document_version__mutmut_40 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_41'] = x_create_document_version__mutmut_41 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_42'] = x_create_document_version__mutmut_42 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_43'] = x_create_document_version__mutmut_43 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_44'] = x_create_document_version__mutmut_44 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_45'] = x_create_document_version__mutmut_45 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_46'] = x_create_document_version__mutmut_46 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_47'] = x_create_document_version__mutmut_47 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_48'] = x_create_document_version__mutmut_48 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_49'] = x_create_document_version__mutmut_49 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_50'] = x_create_document_version__mutmut_50 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_51'] = x_create_document_version__mutmut_51 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_52'] = x_create_document_version__mutmut_52 # type: ignore # mutmut generated
mutants_x_create_document__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_create_document__mutmut)
def create_document(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_orig(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_1(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "XXPRIVATEXX",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_2(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "private",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_3(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = None

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_4(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = None
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_5(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = None

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_6(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(None)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_7(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = None

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_8(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 2

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_9(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = None

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_10(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=None,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_11(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=None,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_12(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=None,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_13(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=None,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_14(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_15(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_16(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_17(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_18(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(None):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_19(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            None
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_20(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=None,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_21(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=None,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_22(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=None,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_23(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_24(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_25(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_26(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = None

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_27(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=None,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_28(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=None,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_29(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=None,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_30(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=None,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_31(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=None,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_32(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=None,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_33(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=None,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_34(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=None,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_35(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status=None,
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_36(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_37(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_38(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_39(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_40(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_41(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_42(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_43(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_44(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_45(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="XXACTIVEXX",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_46(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="active",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_47(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            None,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_48(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            None,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_49(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_50(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_51(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = None

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_52(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=None,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_53(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=None,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_54(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=None,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_55(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=None,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_56(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=None,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_57(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=None,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_58(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=None,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_59(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=None,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_60(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status=None,
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_61(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_62(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_63(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_64(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_65(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_66(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_67(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_68(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_69(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_70(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="XXUPLOADEDXX",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_71(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="uploaded",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_72(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            None,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_73(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            None,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_74(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_75(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_76(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(None)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(storage_key)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

def x_create_document__mutmut_77(
    db: Session,
    project_id: uuid.UUID,
    uploaded_by: uuid.UUID,
    document_type: str,
    title: str,
    file_name: str,
    mime_type: str,
    data: bytes,
    description: str | None = None,
    visibility: str = "PRIVATE",
    authority_level: int | None = None,
    expiry_date=None,
) -> Document:
    """
    Create a document and its first version.

    The file is stored in MinIO and the metadata is stored in PostgreSQL.
    """

    document_id = uuid.uuid4()

    file_size = len(data)
    file_hash = calculate_file_hash(data)

    version_number = 1

    storage_key = generate_storage_key(
        project_id=project_id,
        document_id=document_id,
        version_number=version_number,
        file_name=file_name,
    )

    if object_exists(storage_key):
        raise ValueError(
            f"Storage object already exists: {storage_key}"
        )

    # Upload to MinIO first.
    upload_bytes(
        data=data,
        object_name=storage_key,
        content_type=mime_type,
    )

    try:
        document = Document(
            id=document_id,
            project_id=project_id,
            document_type=document_type,
            title=title,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=expiry_date,
            status="ACTIVE",
        )

        create_document_record(
            db,
            document,
        )

        document_version = DocumentVersion(
            document_id=document_id,
            version_number=version_number,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            file_hash=file_hash,
            storage_key=storage_key,
            uploaded_by=uploaded_by,
            processing_status="UPLOADED",
        )

        create_document_version_record(
            db,
            document_version,
        )

        db.commit()
        db.refresh(document)

        return document

    except Exception:
        db.rollback()

        # PostgreSQL failed after MinIO upload.
        # Remove the object so storage does not contain an orphan.
        try:
            delete_object(None)
        except Exception:
            # Preserve the original database exception.
            pass

        raise

mutants_x_create_document__mutmut['_mutmut_orig'] = x_create_document__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_1'] = x_create_document__mutmut_1 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_2'] = x_create_document__mutmut_2 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_3'] = x_create_document__mutmut_3 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_4'] = x_create_document__mutmut_4 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_5'] = x_create_document__mutmut_5 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_6'] = x_create_document__mutmut_6 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_7'] = x_create_document__mutmut_7 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_8'] = x_create_document__mutmut_8 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_9'] = x_create_document__mutmut_9 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_10'] = x_create_document__mutmut_10 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_11'] = x_create_document__mutmut_11 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_12'] = x_create_document__mutmut_12 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_13'] = x_create_document__mutmut_13 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_14'] = x_create_document__mutmut_14 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_15'] = x_create_document__mutmut_15 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_16'] = x_create_document__mutmut_16 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_17'] = x_create_document__mutmut_17 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_18'] = x_create_document__mutmut_18 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_19'] = x_create_document__mutmut_19 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_20'] = x_create_document__mutmut_20 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_21'] = x_create_document__mutmut_21 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_22'] = x_create_document__mutmut_22 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_23'] = x_create_document__mutmut_23 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_24'] = x_create_document__mutmut_24 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_25'] = x_create_document__mutmut_25 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_26'] = x_create_document__mutmut_26 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_27'] = x_create_document__mutmut_27 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_28'] = x_create_document__mutmut_28 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_29'] = x_create_document__mutmut_29 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_30'] = x_create_document__mutmut_30 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_31'] = x_create_document__mutmut_31 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_32'] = x_create_document__mutmut_32 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_33'] = x_create_document__mutmut_33 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_34'] = x_create_document__mutmut_34 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_35'] = x_create_document__mutmut_35 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_36'] = x_create_document__mutmut_36 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_37'] = x_create_document__mutmut_37 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_38'] = x_create_document__mutmut_38 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_39'] = x_create_document__mutmut_39 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_40'] = x_create_document__mutmut_40 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_41'] = x_create_document__mutmut_41 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_42'] = x_create_document__mutmut_42 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_43'] = x_create_document__mutmut_43 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_44'] = x_create_document__mutmut_44 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_45'] = x_create_document__mutmut_45 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_46'] = x_create_document__mutmut_46 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_47'] = x_create_document__mutmut_47 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_48'] = x_create_document__mutmut_48 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_49'] = x_create_document__mutmut_49 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_50'] = x_create_document__mutmut_50 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_51'] = x_create_document__mutmut_51 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_52'] = x_create_document__mutmut_52 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_53'] = x_create_document__mutmut_53 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_54'] = x_create_document__mutmut_54 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_55'] = x_create_document__mutmut_55 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_56'] = x_create_document__mutmut_56 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_57'] = x_create_document__mutmut_57 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_58'] = x_create_document__mutmut_58 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_59'] = x_create_document__mutmut_59 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_60'] = x_create_document__mutmut_60 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_61'] = x_create_document__mutmut_61 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_62'] = x_create_document__mutmut_62 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_63'] = x_create_document__mutmut_63 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_64'] = x_create_document__mutmut_64 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_65'] = x_create_document__mutmut_65 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_66'] = x_create_document__mutmut_66 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_67'] = x_create_document__mutmut_67 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_68'] = x_create_document__mutmut_68 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_69'] = x_create_document__mutmut_69 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_70'] = x_create_document__mutmut_70 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_71'] = x_create_document__mutmut_71 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_72'] = x_create_document__mutmut_72 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_73'] = x_create_document__mutmut_73 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_74'] = x_create_document__mutmut_74 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_75'] = x_create_document__mutmut_75 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_76'] = x_create_document__mutmut_76 # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_77'] = x_create_document__mutmut_77 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_update_document_processing_status__mutmut)
def update_document_processing_status(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "QUEUED",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        version,
    )

def x_update_document_processing_status__mutmut_orig(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "QUEUED",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        version,
    )

def x_update_document_processing_status__mutmut_1(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = None

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        version,
    )

def x_update_document_processing_status__mutmut_2(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "XXUPLOADEDXX",
        "QUEUED",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        version,
    )

def x_update_document_processing_status__mutmut_3(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "uploaded",
        "QUEUED",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        version,
    )

def x_update_document_processing_status__mutmut_4(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "XXQUEUEDXX",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        version,
    )

def x_update_document_processing_status__mutmut_5(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "queued",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        version,
    )

def x_update_document_processing_status__mutmut_6(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "QUEUED",
        "XXPROCESSINGXX",
        "COMPLETED",
        "FAILED",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        version,
    )

def x_update_document_processing_status__mutmut_7(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "QUEUED",
        "processing",
        "COMPLETED",
        "FAILED",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        version,
    )

def x_update_document_processing_status__mutmut_8(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "QUEUED",
        "PROCESSING",
        "XXCOMPLETEDXX",
        "FAILED",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        version,
    )

def x_update_document_processing_status__mutmut_9(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "QUEUED",
        "PROCESSING",
        "completed",
        "FAILED",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        version,
    )

def x_update_document_processing_status__mutmut_10(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "QUEUED",
        "PROCESSING",
        "COMPLETED",
        "XXFAILEDXX",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        version,
    )

def x_update_document_processing_status__mutmut_11(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "QUEUED",
        "PROCESSING",
        "COMPLETED",
        "failed",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        version,
    )

def x_update_document_processing_status__mutmut_12(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "QUEUED",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
    }

    if new_status in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        version,
    )

def x_update_document_processing_status__mutmut_13(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "QUEUED",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            None
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        version,
    )

def x_update_document_processing_status__mutmut_14(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "QUEUED",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = None

    return update_document_version(
        db,
        version,
    )

def x_update_document_processing_status__mutmut_15(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "QUEUED",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        None,
        version,
    )

def x_update_document_processing_status__mutmut_16(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "QUEUED",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        None,
    )

def x_update_document_processing_status__mutmut_17(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "QUEUED",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        version,
    )

def x_update_document_processing_status__mutmut_18(
    db: Session,
    version: DocumentVersion,
    new_status: str,
) -> DocumentVersion:
    """
    Update the processing status of a document version.
    """

    allowed_statuses = {
        "UPLOADED",
        "QUEUED",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
    }

    if new_status not in allowed_statuses:
        raise ValueError(
            f"Invalid processing status: {new_status}"
        )

    version.processing_status = new_status

    return update_document_version(
        db,
        )

mutants_x_update_document_processing_status__mutmut['_mutmut_orig'] = x_update_document_processing_status__mutmut_orig # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_1'] = x_update_document_processing_status__mutmut_1 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_2'] = x_update_document_processing_status__mutmut_2 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_3'] = x_update_document_processing_status__mutmut_3 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_4'] = x_update_document_processing_status__mutmut_4 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_5'] = x_update_document_processing_status__mutmut_5 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_6'] = x_update_document_processing_status__mutmut_6 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_7'] = x_update_document_processing_status__mutmut_7 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_8'] = x_update_document_processing_status__mutmut_8 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_9'] = x_update_document_processing_status__mutmut_9 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_10'] = x_update_document_processing_status__mutmut_10 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_11'] = x_update_document_processing_status__mutmut_11 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_12'] = x_update_document_processing_status__mutmut_12 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_13'] = x_update_document_processing_status__mutmut_13 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_14'] = x_update_document_processing_status__mutmut_14 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_15'] = x_update_document_processing_status__mutmut_15 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_16'] = x_update_document_processing_status__mutmut_16 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_17'] = x_update_document_processing_status__mutmut_17 # type: ignore # mutmut generated
mutants_x_update_document_processing_status__mutmut['x_update_document_processing_status__mutmut_18'] = x_update_document_processing_status__mutmut_18 # type: ignore # mutmut generated