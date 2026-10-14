"""
PropertyGuard Document Repository
---------------------------------
Provides database query and persistence methods for Document and DocumentVersion
entities, handling soft deletes, version lookups, and project document listings.
"""

from datetime import datetime
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document import Document, DocumentVersion


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_document__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_document__mutmut)
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


def x_get_document__mutmut_orig(
    db: Session,
    document_id: UUID,
) -> Document | None:
    return db.scalar(
        select(Document).where(
            Document.id == document_id,
            Document.deleted_at.is_(None),
        )
    )


def x_get_document__mutmut_1(
    db: Session,
    document_id: UUID,
) -> Document | None:
    return db.scalar(
        None
    )


def x_get_document__mutmut_2(
    db: Session,
    document_id: UUID,
) -> Document | None:
    return db.scalar(
        select(Document).where(
            None,
            Document.deleted_at.is_(None),
        )
    )


def x_get_document__mutmut_3(
    db: Session,
    document_id: UUID,
) -> Document | None:
    return db.scalar(
        select(Document).where(
            Document.id == document_id,
            None,
        )
    )


def x_get_document__mutmut_4(
    db: Session,
    document_id: UUID,
) -> Document | None:
    return db.scalar(
        select(Document).where(
            Document.deleted_at.is_(None),
        )
    )


def x_get_document__mutmut_5(
    db: Session,
    document_id: UUID,
) -> Document | None:
    return db.scalar(
        select(Document).where(
            Document.id == document_id,
            )
    )


def x_get_document__mutmut_6(
    db: Session,
    document_id: UUID,
) -> Document | None:
    return db.scalar(
        select(None).where(
            Document.id == document_id,
            Document.deleted_at.is_(None),
        )
    )


def x_get_document__mutmut_7(
    db: Session,
    document_id: UUID,
) -> Document | None:
    return db.scalar(
        select(Document).where(
            Document.id != document_id,
            Document.deleted_at.is_(None),
        )
    )

mutants_x_get_document__mutmut['_mutmut_orig'] = x_get_document__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_document__mutmut['x_get_document__mutmut_1'] = x_get_document__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_document__mutmut['x_get_document__mutmut_2'] = x_get_document__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_document__mutmut['x_get_document__mutmut_3'] = x_get_document__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_document__mutmut['x_get_document__mutmut_4'] = x_get_document__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_document__mutmut['x_get_document__mutmut_5'] = x_get_document__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_document__mutmut['x_get_document__mutmut_6'] = x_get_document__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_document__mutmut['x_get_document__mutmut_7'] = x_get_document__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_project_documents__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_project_documents__mutmut)
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


def x_get_project_documents__mutmut_orig(
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


def x_get_project_documents__mutmut_1(
    db: Session,
    project_id: UUID,
) -> list[Document]:
    return list(
        None
    )


def x_get_project_documents__mutmut_2(
    db: Session,
    project_id: UUID,
) -> list[Document]:
    return list(
        db.scalars(
            None
        ).all()
    )


def x_get_project_documents__mutmut_3(
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
            .order_by(None)
        ).all()
    )


def x_get_project_documents__mutmut_4(
    db: Session,
    project_id: UUID,
) -> list[Document]:
    return list(
        db.scalars(
            select(Document)
            .where(
                None,
                Document.deleted_at.is_(None),
            )
            .order_by(Document.created_at.desc())
        ).all()
    )


def x_get_project_documents__mutmut_5(
    db: Session,
    project_id: UUID,
) -> list[Document]:
    return list(
        db.scalars(
            select(Document)
            .where(
                Document.project_id == project_id,
                None,
            )
            .order_by(Document.created_at.desc())
        ).all()
    )


def x_get_project_documents__mutmut_6(
    db: Session,
    project_id: UUID,
) -> list[Document]:
    return list(
        db.scalars(
            select(Document)
            .where(
                Document.deleted_at.is_(None),
            )
            .order_by(Document.created_at.desc())
        ).all()
    )


def x_get_project_documents__mutmut_7(
    db: Session,
    project_id: UUID,
) -> list[Document]:
    return list(
        db.scalars(
            select(Document)
            .where(
                Document.project_id == project_id,
                )
            .order_by(Document.created_at.desc())
        ).all()
    )


def x_get_project_documents__mutmut_8(
    db: Session,
    project_id: UUID,
) -> list[Document]:
    return list(
        db.scalars(
            select(None)
            .where(
                Document.project_id == project_id,
                Document.deleted_at.is_(None),
            )
            .order_by(Document.created_at.desc())
        ).all()
    )


def x_get_project_documents__mutmut_9(
    db: Session,
    project_id: UUID,
) -> list[Document]:
    return list(
        db.scalars(
            select(Document)
            .where(
                Document.project_id != project_id,
                Document.deleted_at.is_(None),
            )
            .order_by(Document.created_at.desc())
        ).all()
    )

mutants_x_get_project_documents__mutmut['_mutmut_orig'] = x_get_project_documents__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_project_documents__mutmut['x_get_project_documents__mutmut_1'] = x_get_project_documents__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_project_documents__mutmut['x_get_project_documents__mutmut_2'] = x_get_project_documents__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_project_documents__mutmut['x_get_project_documents__mutmut_3'] = x_get_project_documents__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_project_documents__mutmut['x_get_project_documents__mutmut_4'] = x_get_project_documents__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_project_documents__mutmut['x_get_project_documents__mutmut_5'] = x_get_project_documents__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_project_documents__mutmut['x_get_project_documents__mutmut_6'] = x_get_project_documents__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_project_documents__mutmut['x_get_project_documents__mutmut_7'] = x_get_project_documents__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_project_documents__mutmut['x_get_project_documents__mutmut_8'] = x_get_project_documents__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_project_documents__mutmut['x_get_project_documents__mutmut_9'] = x_get_project_documents__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_document_versions__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_document_versions__mutmut)
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


def x_get_document_versions__mutmut_orig(
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


def x_get_document_versions__mutmut_1(
    db: Session,
    document_id: UUID,
) -> list[DocumentVersion]:
    return list(
        None
    )


def x_get_document_versions__mutmut_2(
    db: Session,
    document_id: UUID,
) -> list[DocumentVersion]:
    return list(
        db.scalars(
            None
        ).all()
    )


def x_get_document_versions__mutmut_3(
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
            .order_by(None)
        ).all()
    )


def x_get_document_versions__mutmut_4(
    db: Session,
    document_id: UUID,
) -> list[DocumentVersion]:
    return list(
        db.scalars(
            select(DocumentVersion)
            .where(
                None,
                DocumentVersion.deleted_at.is_(None),
            )
            .order_by(DocumentVersion.version_number.desc())
        ).all()
    )


def x_get_document_versions__mutmut_5(
    db: Session,
    document_id: UUID,
) -> list[DocumentVersion]:
    return list(
        db.scalars(
            select(DocumentVersion)
            .where(
                DocumentVersion.document_id == document_id,
                None,
            )
            .order_by(DocumentVersion.version_number.desc())
        ).all()
    )


def x_get_document_versions__mutmut_6(
    db: Session,
    document_id: UUID,
) -> list[DocumentVersion]:
    return list(
        db.scalars(
            select(DocumentVersion)
            .where(
                DocumentVersion.deleted_at.is_(None),
            )
            .order_by(DocumentVersion.version_number.desc())
        ).all()
    )


def x_get_document_versions__mutmut_7(
    db: Session,
    document_id: UUID,
) -> list[DocumentVersion]:
    return list(
        db.scalars(
            select(DocumentVersion)
            .where(
                DocumentVersion.document_id == document_id,
                )
            .order_by(DocumentVersion.version_number.desc())
        ).all()
    )


def x_get_document_versions__mutmut_8(
    db: Session,
    document_id: UUID,
) -> list[DocumentVersion]:
    return list(
        db.scalars(
            select(None)
            .where(
                DocumentVersion.document_id == document_id,
                DocumentVersion.deleted_at.is_(None),
            )
            .order_by(DocumentVersion.version_number.desc())
        ).all()
    )


def x_get_document_versions__mutmut_9(
    db: Session,
    document_id: UUID,
) -> list[DocumentVersion]:
    return list(
        db.scalars(
            select(DocumentVersion)
            .where(
                DocumentVersion.document_id != document_id,
                DocumentVersion.deleted_at.is_(None),
            )
            .order_by(DocumentVersion.version_number.desc())
        ).all()
    )

mutants_x_get_document_versions__mutmut['_mutmut_orig'] = x_get_document_versions__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_document_versions__mutmut['x_get_document_versions__mutmut_1'] = x_get_document_versions__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_document_versions__mutmut['x_get_document_versions__mutmut_2'] = x_get_document_versions__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_document_versions__mutmut['x_get_document_versions__mutmut_3'] = x_get_document_versions__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_document_versions__mutmut['x_get_document_versions__mutmut_4'] = x_get_document_versions__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_document_versions__mutmut['x_get_document_versions__mutmut_5'] = x_get_document_versions__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_document_versions__mutmut['x_get_document_versions__mutmut_6'] = x_get_document_versions__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_document_versions__mutmut['x_get_document_versions__mutmut_7'] = x_get_document_versions__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_document_versions__mutmut['x_get_document_versions__mutmut_8'] = x_get_document_versions__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_document_versions__mutmut['x_get_document_versions__mutmut_9'] = x_get_document_versions__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_latest_version__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_latest_version__mutmut)
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


def x_get_latest_version__mutmut_orig(
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


def x_get_latest_version__mutmut_1(
    db: Session,
    document_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        None
    )


def x_get_latest_version__mutmut_2(
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
        .limit(None)
    )


def x_get_latest_version__mutmut_3(
    db: Session,
    document_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        select(DocumentVersion)
        .where(
            DocumentVersion.document_id == document_id,
            DocumentVersion.deleted_at.is_(None),
        )
        .order_by(None)
        .limit(1)
    )


def x_get_latest_version__mutmut_4(
    db: Session,
    document_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        select(DocumentVersion)
        .where(
            None,
            DocumentVersion.deleted_at.is_(None),
        )
        .order_by(DocumentVersion.version_number.desc())
        .limit(1)
    )


def x_get_latest_version__mutmut_5(
    db: Session,
    document_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        select(DocumentVersion)
        .where(
            DocumentVersion.document_id == document_id,
            None,
        )
        .order_by(DocumentVersion.version_number.desc())
        .limit(1)
    )


def x_get_latest_version__mutmut_6(
    db: Session,
    document_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        select(DocumentVersion)
        .where(
            DocumentVersion.deleted_at.is_(None),
        )
        .order_by(DocumentVersion.version_number.desc())
        .limit(1)
    )


def x_get_latest_version__mutmut_7(
    db: Session,
    document_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        select(DocumentVersion)
        .where(
            DocumentVersion.document_id == document_id,
            )
        .order_by(DocumentVersion.version_number.desc())
        .limit(1)
    )


def x_get_latest_version__mutmut_8(
    db: Session,
    document_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        select(None)
        .where(
            DocumentVersion.document_id == document_id,
            DocumentVersion.deleted_at.is_(None),
        )
        .order_by(DocumentVersion.version_number.desc())
        .limit(1)
    )


def x_get_latest_version__mutmut_9(
    db: Session,
    document_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        select(DocumentVersion)
        .where(
            DocumentVersion.document_id != document_id,
            DocumentVersion.deleted_at.is_(None),
        )
        .order_by(DocumentVersion.version_number.desc())
        .limit(1)
    )


def x_get_latest_version__mutmut_10(
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
        .limit(2)
    )

mutants_x_get_latest_version__mutmut['_mutmut_orig'] = x_get_latest_version__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_latest_version__mutmut['x_get_latest_version__mutmut_1'] = x_get_latest_version__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_latest_version__mutmut['x_get_latest_version__mutmut_2'] = x_get_latest_version__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_latest_version__mutmut['x_get_latest_version__mutmut_3'] = x_get_latest_version__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_latest_version__mutmut['x_get_latest_version__mutmut_4'] = x_get_latest_version__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_latest_version__mutmut['x_get_latest_version__mutmut_5'] = x_get_latest_version__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_latest_version__mutmut['x_get_latest_version__mutmut_6'] = x_get_latest_version__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_latest_version__mutmut['x_get_latest_version__mutmut_7'] = x_get_latest_version__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_latest_version__mutmut['x_get_latest_version__mutmut_8'] = x_get_latest_version__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_latest_version__mutmut['x_get_latest_version__mutmut_9'] = x_get_latest_version__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_latest_version__mutmut['x_get_latest_version__mutmut_10'] = x_get_latest_version__mutmut_10 # type: ignore # mutmut generated
mutants_x_create_document__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_create_document__mutmut)
def create_document(
    db: Session,
    document: Document,
) -> Document:
    db.add(document)
    db.flush()
    return document


def x_create_document__mutmut_orig(
    db: Session,
    document: Document,
) -> Document:
    db.add(document)
    db.flush()
    return document


def x_create_document__mutmut_1(
    db: Session,
    document: Document,
) -> Document:
    db.add(None)
    db.flush()
    return document

mutants_x_create_document__mutmut['_mutmut_orig'] = x_create_document__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_document__mutmut['x_create_document__mutmut_1'] = x_create_document__mutmut_1 # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_create_document_version__mutmut)
def create_document_version(
    db: Session,
    version: DocumentVersion,
) -> DocumentVersion:
    db.add(version)
    db.flush()
    return version


def x_create_document_version__mutmut_orig(
    db: Session,
    version: DocumentVersion,
) -> DocumentVersion:
    db.add(version)
    db.flush()
    return version


def x_create_document_version__mutmut_1(
    db: Session,
    version: DocumentVersion,
) -> DocumentVersion:
    db.add(None)
    db.flush()
    return version

mutants_x_create_document_version__mutmut['_mutmut_orig'] = x_create_document_version__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_document_version__mutmut['x_create_document_version__mutmut_1'] = x_create_document_version__mutmut_1 # type: ignore # mutmut generated
mutants_x_soft_delete_document__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_soft_delete_document__mutmut)
def soft_delete_document(
    db: Session,
    document: Document,
) -> Document:
    document.deleted_at = datetime.utcnow()
    document.status = "INACTIVE"

    db.commit()
    db.refresh(document)

    return document


def x_soft_delete_document__mutmut_orig(
    db: Session,
    document: Document,
) -> Document:
    document.deleted_at = datetime.utcnow()
    document.status = "INACTIVE"

    db.commit()
    db.refresh(document)

    return document


def x_soft_delete_document__mutmut_1(
    db: Session,
    document: Document,
) -> Document:
    document.deleted_at = None
    document.status = "INACTIVE"

    db.commit()
    db.refresh(document)

    return document


def x_soft_delete_document__mutmut_2(
    db: Session,
    document: Document,
) -> Document:
    document.deleted_at = datetime.utcnow()
    document.status = None

    db.commit()
    db.refresh(document)

    return document


def x_soft_delete_document__mutmut_3(
    db: Session,
    document: Document,
) -> Document:
    document.deleted_at = datetime.utcnow()
    document.status = "XXINACTIVEXX"

    db.commit()
    db.refresh(document)

    return document


def x_soft_delete_document__mutmut_4(
    db: Session,
    document: Document,
) -> Document:
    document.deleted_at = datetime.utcnow()
    document.status = "inactive"

    db.commit()
    db.refresh(document)

    return document


def x_soft_delete_document__mutmut_5(
    db: Session,
    document: Document,
) -> Document:
    document.deleted_at = datetime.utcnow()
    document.status = "INACTIVE"

    db.commit()
    db.refresh(None)

    return document

mutants_x_soft_delete_document__mutmut['_mutmut_orig'] = x_soft_delete_document__mutmut_orig # type: ignore # mutmut generated
mutants_x_soft_delete_document__mutmut['x_soft_delete_document__mutmut_1'] = x_soft_delete_document__mutmut_1 # type: ignore # mutmut generated
mutants_x_soft_delete_document__mutmut['x_soft_delete_document__mutmut_2'] = x_soft_delete_document__mutmut_2 # type: ignore # mutmut generated
mutants_x_soft_delete_document__mutmut['x_soft_delete_document__mutmut_3'] = x_soft_delete_document__mutmut_3 # type: ignore # mutmut generated
mutants_x_soft_delete_document__mutmut['x_soft_delete_document__mutmut_4'] = x_soft_delete_document__mutmut_4 # type: ignore # mutmut generated
mutants_x_soft_delete_document__mutmut['x_soft_delete_document__mutmut_5'] = x_soft_delete_document__mutmut_5 # type: ignore # mutmut generated
mutants_x_update_document_version__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_update_document_version__mutmut)
def update_document_version(
    db: Session,
    version: DocumentVersion,
) -> DocumentVersion:
    db.add(version)
    db.flush()
    db.refresh(version)
    return version

def x_update_document_version__mutmut_orig(
    db: Session,
    version: DocumentVersion,
) -> DocumentVersion:
    db.add(version)
    db.flush()
    db.refresh(version)
    return version

def x_update_document_version__mutmut_1(
    db: Session,
    version: DocumentVersion,
) -> DocumentVersion:
    db.add(None)
    db.flush()
    db.refresh(version)
    return version

def x_update_document_version__mutmut_2(
    db: Session,
    version: DocumentVersion,
) -> DocumentVersion:
    db.add(version)
    db.flush()
    db.refresh(None)
    return version

mutants_x_update_document_version__mutmut['_mutmut_orig'] = x_update_document_version__mutmut_orig # type: ignore # mutmut generated
mutants_x_update_document_version__mutmut['x_update_document_version__mutmut_1'] = x_update_document_version__mutmut_1 # type: ignore # mutmut generated
mutants_x_update_document_version__mutmut['x_update_document_version__mutmut_2'] = x_update_document_version__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_document_version__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_get_document_version__mutmut)
def get_document_version(
    db: Session,
    version_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        select(DocumentVersion).where(
            DocumentVersion.id == version_id,
            DocumentVersion.deleted_at.is_(None),
        )
    )

def x_get_document_version__mutmut_orig(
    db: Session,
    version_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        select(DocumentVersion).where(
            DocumentVersion.id == version_id,
            DocumentVersion.deleted_at.is_(None),
        )
    )

def x_get_document_version__mutmut_1(
    db: Session,
    version_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        None
    )

def x_get_document_version__mutmut_2(
    db: Session,
    version_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        select(DocumentVersion).where(
            None,
            DocumentVersion.deleted_at.is_(None),
        )
    )

def x_get_document_version__mutmut_3(
    db: Session,
    version_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        select(DocumentVersion).where(
            DocumentVersion.id == version_id,
            None,
        )
    )

def x_get_document_version__mutmut_4(
    db: Session,
    version_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        select(DocumentVersion).where(
            DocumentVersion.deleted_at.is_(None),
        )
    )

def x_get_document_version__mutmut_5(
    db: Session,
    version_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        select(DocumentVersion).where(
            DocumentVersion.id == version_id,
            )
    )

def x_get_document_version__mutmut_6(
    db: Session,
    version_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        select(None).where(
            DocumentVersion.id == version_id,
            DocumentVersion.deleted_at.is_(None),
        )
    )

def x_get_document_version__mutmut_7(
    db: Session,
    version_id: UUID,
) -> DocumentVersion | None:
    return db.scalar(
        select(DocumentVersion).where(
            DocumentVersion.id != version_id,
            DocumentVersion.deleted_at.is_(None),
        )
    )

mutants_x_get_document_version__mutmut['_mutmut_orig'] = x_get_document_version__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_document_version__mutmut['x_get_document_version__mutmut_1'] = x_get_document_version__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_document_version__mutmut['x_get_document_version__mutmut_2'] = x_get_document_version__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_document_version__mutmut['x_get_document_version__mutmut_3'] = x_get_document_version__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_document_version__mutmut['x_get_document_version__mutmut_4'] = x_get_document_version__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_document_version__mutmut['x_get_document_version__mutmut_5'] = x_get_document_version__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_document_version__mutmut['x_get_document_version__mutmut_6'] = x_get_document_version__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_document_version__mutmut['x_get_document_version__mutmut_7'] = x_get_document_version__mutmut_7 # type: ignore # mutmut generated