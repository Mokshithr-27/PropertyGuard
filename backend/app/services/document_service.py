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
)


def calculate_file_hash(data: bytes) -> str:
    """Calculate SHA-256 hash of a file."""
    return hashlib.sha256(data).hexdigest()


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