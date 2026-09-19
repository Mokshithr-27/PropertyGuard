from datetime import datetime
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document import Document, DocumentVersion


def get_document(
    db: Session,
    document_id: UUID,
) -> Document | None:
    return db.scalar(
        select(Document).where(
            Document.id == document_id,
            Document.deleted_at.is_(None),
        )
    )


def get_project_documents(
    db: Session,
    project_id: UUID,
) -> list[Document]:
    return list(
        db.scalars(
            select(Document)
            .where(
                Document.project_id == project_id,
                Document.deleted_at.is_(None),
            )
            .order_by(Document.created_at.desc())
        ).all()
    )


def get_document_versions(
    db: Session,
    document_id: UUID,
) -> list[DocumentVersion]:
    return list(
        db.scalars(
            select(DocumentVersion)
            .where(
                DocumentVersion.document_id == document_id,
                DocumentVersion.deleted_at.is_(None),
            )
            .order_by(DocumentVersion.version_number.desc())
        ).all()
    )


def get_latest_version(
    db: Session,
    document_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        select(DocumentVersion)
        .where(
            DocumentVersion.document_id == document_id,
            DocumentVersion.deleted_at.is_(None),
        )
        .order_by(DocumentVersion.version_number.desc())
        .limit(1)
    )


def create_document(
    db: Session,
    document: Document,
) -> Document:
    db.add(document)
    db.flush()
    return document


def create_document_version(
    db: Session,
    version: DocumentVersion,
) -> DocumentVersion:
    db.add(version)
    db.flush()
    return version


def soft_delete_document(
    db: Session,
    document: Document,
) -> Document:
    document.deleted_at = datetime.utcnow()
    document.status = "INACTIVE"

    db.commit()
    db.refresh(document)

    return document