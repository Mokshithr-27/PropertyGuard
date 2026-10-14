"""
PropertyGuard Document Analysis Persistence Service
---------------------------------------------------
Persists structured document analyses and AI-generated evidence records
(page numbers, citations, confidence scores, extracted properties) into PostgreSQL.
"""

from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.document_analysis import (
    DocumentAnalysis,
    DocumentEvidence,
)
from app.services.document_text_extraction_service import (
    ExtractedDocument,
)

from app.integrations.ai.base import AIAnalysisResult

def create_document_analysis(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
        provider="deterministic",
        model_name="pymupdf-text-extraction",
        detected_document_type=None,
        summary=(
            f"Extracted text from {extracted.page_count} "
            f"page(s)."
        ),
        structured_data={
            "page_count": extracted.page_count,
            "has_text": extracted.has_text,
            "text_length": len(extracted.full_text),
        },
        overall_confidence=1.0 if extracted.has_text else 0.0,
        completed_at=datetime.now(timezone.utc),
    )

    db.add(analysis)
    db.flush()

    for page in extracted.pages:
        if not page.text.strip():
            continue

        evidence = DocumentEvidence(
            analysis_id=analysis.id,
            field_name="page_text",
            field_value=page.text,
            page_number=page.page_number,
            confidence=1.0,
            source="PDF_TEXT",
            evidence_text=page.text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis


def persist_document_analysis(
    db: Session,
    document_version_id: UUID,
    result: AIAnalysisResult,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
        provider="AI",
        model_name=None,
        detected_document_type=result.detected_document_type,
        summary=result.summary,
        structured_data=result.structured_data,
        overall_confidence=result.overall_confidence,
        completed_at=datetime.now(timezone.utc),
    )

    db.add(analysis)
    db.flush()

    for item in result.evidence:
        evidence = DocumentEvidence(
            analysis_id=analysis.id,
            field_name=item.field_name,
            field_value=item.field_value,
            page_number=item.page_number,
            confidence=item.confidence,
            source=item.source,
            evidence_text=item.evidence_text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis

