"""
PropertyGuard Document Analysis Repository
------------------------------------------
Handles database retrieval of the latest completed DocumentAnalysis records
and associated DocumentEvidence collections for specific document versions.
"""

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document_analysis import DocumentAnalysis, DocumentEvidence


def get_latest_document_analysis(
    db: Session,
    document_version_id: UUID,
) -> DocumentAnalysis | None:
    return db.scalar(
        select(DocumentAnalysis)
        .where(
            DocumentAnalysis.document_version_id == document_version_id,
            DocumentAnalysis.status == "COMPLETED",
        )
        .order_by(
            DocumentAnalysis.created_at.desc(),
            DocumentAnalysis.id.desc(),
        )
        .limit(1)
    )


def get_document_analysis_evidence(
    db: Session,
    analysis_id: UUID,
) -> list[DocumentEvidence]:
    return list(
        db.scalars(
            select(DocumentEvidence)
            .where(
                DocumentEvidence.analysis_id == analysis_id,
            )
            .order_by(
                DocumentEvidence.page_number.asc(),
                DocumentEvidence.created_at.asc(),
            )
        ).all()
    )