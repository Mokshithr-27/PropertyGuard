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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_create_document_analysis__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_create_document_analysis__mutmut)
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

def x_create_document_analysis__mutmut_orig(
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

def x_create_document_analysis__mutmut_1(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = None

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

def x_create_document_analysis__mutmut_2(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=None,
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

def x_create_document_analysis__mutmut_3(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status=None,
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

def x_create_document_analysis__mutmut_4(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
        provider=None,
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

def x_create_document_analysis__mutmut_5(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
        provider="deterministic",
        model_name=None,
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

def x_create_document_analysis__mutmut_6(
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
        summary=None,
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

def x_create_document_analysis__mutmut_7(
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
        structured_data=None,
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

def x_create_document_analysis__mutmut_8(
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
        overall_confidence=None,
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

def x_create_document_analysis__mutmut_9(
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
        completed_at=None,
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

def x_create_document_analysis__mutmut_10(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
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

def x_create_document_analysis__mutmut_11(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
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

def x_create_document_analysis__mutmut_12(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
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

def x_create_document_analysis__mutmut_13(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
        provider="deterministic",
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

def x_create_document_analysis__mutmut_14(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
        provider="deterministic",
        model_name="pymupdf-text-extraction",
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

def x_create_document_analysis__mutmut_15(
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

def x_create_document_analysis__mutmut_16(
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

def x_create_document_analysis__mutmut_17(
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

def x_create_document_analysis__mutmut_18(
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

def x_create_document_analysis__mutmut_19(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="XXCOMPLETEDXX",
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

def x_create_document_analysis__mutmut_20(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="completed",
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

def x_create_document_analysis__mutmut_21(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
        provider="XXdeterministicXX",
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

def x_create_document_analysis__mutmut_22(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
        provider="DETERMINISTIC",
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

def x_create_document_analysis__mutmut_23(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
        provider="deterministic",
        model_name="XXpymupdf-text-extractionXX",
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

def x_create_document_analysis__mutmut_24(
    db: Session,
    document_version_id: UUID,
    extracted: ExtractedDocument,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
        provider="deterministic",
        model_name="PYMUPDF-TEXT-EXTRACTION",
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

def x_create_document_analysis__mutmut_25(
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
            "XXpage_countXX": extracted.page_count,
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

def x_create_document_analysis__mutmut_26(
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
            "PAGE_COUNT": extracted.page_count,
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

def x_create_document_analysis__mutmut_27(
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
            "XXhas_textXX": extracted.has_text,
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

def x_create_document_analysis__mutmut_28(
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
            "HAS_TEXT": extracted.has_text,
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

def x_create_document_analysis__mutmut_29(
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
            "XXtext_lengthXX": len(extracted.full_text),
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

def x_create_document_analysis__mutmut_30(
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
            "TEXT_LENGTH": len(extracted.full_text),
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

def x_create_document_analysis__mutmut_31(
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
        overall_confidence=1.0 if (extracted.has_text) and False else 0.0,
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

def x_create_document_analysis__mutmut_32(
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
        overall_confidence=1.0 if (extracted.has_text) or True else 0.0,
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

def x_create_document_analysis__mutmut_33(
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
        overall_confidence=2.0 if extracted.has_text else 0.0,
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

def x_create_document_analysis__mutmut_34(
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
        overall_confidence=1.0 if extracted.has_text else 1.0,
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

def x_create_document_analysis__mutmut_35(
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
        completed_at=datetime.now(None),
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

def x_create_document_analysis__mutmut_36(
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

    db.add(None)
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

def x_create_document_analysis__mutmut_37(
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
        if page.text.strip():
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

def x_create_document_analysis__mutmut_38(
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
            break

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

def x_create_document_analysis__mutmut_39(
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

        evidence = None

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis

def x_create_document_analysis__mutmut_40(
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
            analysis_id=None,
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

def x_create_document_analysis__mutmut_41(
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
            field_name=None,
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

def x_create_document_analysis__mutmut_42(
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
            field_value=None,
            page_number=page.page_number,
            confidence=1.0,
            source="PDF_TEXT",
            evidence_text=page.text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis

def x_create_document_analysis__mutmut_43(
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
            page_number=None,
            confidence=1.0,
            source="PDF_TEXT",
            evidence_text=page.text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis

def x_create_document_analysis__mutmut_44(
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
            confidence=None,
            source="PDF_TEXT",
            evidence_text=page.text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis

def x_create_document_analysis__mutmut_45(
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
            source=None,
            evidence_text=page.text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis

def x_create_document_analysis__mutmut_46(
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
            evidence_text=None,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis

def x_create_document_analysis__mutmut_47(
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

def x_create_document_analysis__mutmut_48(
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

def x_create_document_analysis__mutmut_49(
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
            page_number=page.page_number,
            confidence=1.0,
            source="PDF_TEXT",
            evidence_text=page.text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis

def x_create_document_analysis__mutmut_50(
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
            confidence=1.0,
            source="PDF_TEXT",
            evidence_text=page.text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis

def x_create_document_analysis__mutmut_51(
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
            source="PDF_TEXT",
            evidence_text=page.text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis

def x_create_document_analysis__mutmut_52(
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
            evidence_text=page.text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis

def x_create_document_analysis__mutmut_53(
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
            )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis

def x_create_document_analysis__mutmut_54(
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
            field_name="XXpage_textXX",
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

def x_create_document_analysis__mutmut_55(
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
            field_name="PAGE_TEXT",
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

def x_create_document_analysis__mutmut_56(
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
            confidence=2.0,
            source="PDF_TEXT",
            evidence_text=page.text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis

def x_create_document_analysis__mutmut_57(
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
            source="XXPDF_TEXTXX",
            evidence_text=page.text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis

def x_create_document_analysis__mutmut_58(
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
            source="pdf_text",
            evidence_text=page.text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis

def x_create_document_analysis__mutmut_59(
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

        db.add(None)

    db.flush()
    db.refresh(analysis)

    return analysis

def x_create_document_analysis__mutmut_60(
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
    db.refresh(None)

    return analysis

mutants_x_create_document_analysis__mutmut['_mutmut_orig'] = x_create_document_analysis__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_1'] = x_create_document_analysis__mutmut_1 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_2'] = x_create_document_analysis__mutmut_2 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_3'] = x_create_document_analysis__mutmut_3 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_4'] = x_create_document_analysis__mutmut_4 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_5'] = x_create_document_analysis__mutmut_5 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_6'] = x_create_document_analysis__mutmut_6 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_7'] = x_create_document_analysis__mutmut_7 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_8'] = x_create_document_analysis__mutmut_8 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_9'] = x_create_document_analysis__mutmut_9 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_10'] = x_create_document_analysis__mutmut_10 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_11'] = x_create_document_analysis__mutmut_11 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_12'] = x_create_document_analysis__mutmut_12 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_13'] = x_create_document_analysis__mutmut_13 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_14'] = x_create_document_analysis__mutmut_14 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_15'] = x_create_document_analysis__mutmut_15 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_16'] = x_create_document_analysis__mutmut_16 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_17'] = x_create_document_analysis__mutmut_17 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_18'] = x_create_document_analysis__mutmut_18 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_19'] = x_create_document_analysis__mutmut_19 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_20'] = x_create_document_analysis__mutmut_20 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_21'] = x_create_document_analysis__mutmut_21 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_22'] = x_create_document_analysis__mutmut_22 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_23'] = x_create_document_analysis__mutmut_23 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_24'] = x_create_document_analysis__mutmut_24 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_25'] = x_create_document_analysis__mutmut_25 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_26'] = x_create_document_analysis__mutmut_26 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_27'] = x_create_document_analysis__mutmut_27 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_28'] = x_create_document_analysis__mutmut_28 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_29'] = x_create_document_analysis__mutmut_29 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_30'] = x_create_document_analysis__mutmut_30 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_31'] = x_create_document_analysis__mutmut_31 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_32'] = x_create_document_analysis__mutmut_32 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_33'] = x_create_document_analysis__mutmut_33 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_34'] = x_create_document_analysis__mutmut_34 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_35'] = x_create_document_analysis__mutmut_35 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_36'] = x_create_document_analysis__mutmut_36 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_37'] = x_create_document_analysis__mutmut_37 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_38'] = x_create_document_analysis__mutmut_38 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_39'] = x_create_document_analysis__mutmut_39 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_40'] = x_create_document_analysis__mutmut_40 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_41'] = x_create_document_analysis__mutmut_41 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_42'] = x_create_document_analysis__mutmut_42 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_43'] = x_create_document_analysis__mutmut_43 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_44'] = x_create_document_analysis__mutmut_44 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_45'] = x_create_document_analysis__mutmut_45 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_46'] = x_create_document_analysis__mutmut_46 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_47'] = x_create_document_analysis__mutmut_47 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_48'] = x_create_document_analysis__mutmut_48 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_49'] = x_create_document_analysis__mutmut_49 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_50'] = x_create_document_analysis__mutmut_50 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_51'] = x_create_document_analysis__mutmut_51 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_52'] = x_create_document_analysis__mutmut_52 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_53'] = x_create_document_analysis__mutmut_53 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_54'] = x_create_document_analysis__mutmut_54 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_55'] = x_create_document_analysis__mutmut_55 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_56'] = x_create_document_analysis__mutmut_56 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_57'] = x_create_document_analysis__mutmut_57 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_58'] = x_create_document_analysis__mutmut_58 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_59'] = x_create_document_analysis__mutmut_59 # type: ignore # mutmut generated
mutants_x_create_document_analysis__mutmut['x_create_document_analysis__mutmut_60'] = x_create_document_analysis__mutmut_60 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_persist_document_analysis__mutmut)
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


def x_persist_document_analysis__mutmut_orig(
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


def x_persist_document_analysis__mutmut_1(
    db: Session,
    document_version_id: UUID,
    result: AIAnalysisResult,
) -> DocumentAnalysis:
    analysis = None

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


def x_persist_document_analysis__mutmut_2(
    db: Session,
    document_version_id: UUID,
    result: AIAnalysisResult,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=None,
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


def x_persist_document_analysis__mutmut_3(
    db: Session,
    document_version_id: UUID,
    result: AIAnalysisResult,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status=None,
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


def x_persist_document_analysis__mutmut_4(
    db: Session,
    document_version_id: UUID,
    result: AIAnalysisResult,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
        provider=None,
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


def x_persist_document_analysis__mutmut_5(
    db: Session,
    document_version_id: UUID,
    result: AIAnalysisResult,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
        provider="AI",
        model_name=None,
        detected_document_type=None,
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


def x_persist_document_analysis__mutmut_6(
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
        summary=None,
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


def x_persist_document_analysis__mutmut_7(
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
        structured_data=None,
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


def x_persist_document_analysis__mutmut_8(
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
        overall_confidence=None,
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


def x_persist_document_analysis__mutmut_9(
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
        completed_at=None,
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


def x_persist_document_analysis__mutmut_10(
    db: Session,
    document_version_id: UUID,
    result: AIAnalysisResult,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
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


def x_persist_document_analysis__mutmut_11(
    db: Session,
    document_version_id: UUID,
    result: AIAnalysisResult,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
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


def x_persist_document_analysis__mutmut_12(
    db: Session,
    document_version_id: UUID,
    result: AIAnalysisResult,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
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


def x_persist_document_analysis__mutmut_13(
    db: Session,
    document_version_id: UUID,
    result: AIAnalysisResult,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
        provider="AI",
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


def x_persist_document_analysis__mutmut_14(
    db: Session,
    document_version_id: UUID,
    result: AIAnalysisResult,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
        provider="AI",
        model_name=None,
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


def x_persist_document_analysis__mutmut_15(
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


def x_persist_document_analysis__mutmut_16(
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


def x_persist_document_analysis__mutmut_17(
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


def x_persist_document_analysis__mutmut_18(
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


def x_persist_document_analysis__mutmut_19(
    db: Session,
    document_version_id: UUID,
    result: AIAnalysisResult,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="XXCOMPLETEDXX",
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


def x_persist_document_analysis__mutmut_20(
    db: Session,
    document_version_id: UUID,
    result: AIAnalysisResult,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="completed",
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


def x_persist_document_analysis__mutmut_21(
    db: Session,
    document_version_id: UUID,
    result: AIAnalysisResult,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
        provider="XXAIXX",
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


def x_persist_document_analysis__mutmut_22(
    db: Session,
    document_version_id: UUID,
    result: AIAnalysisResult,
) -> DocumentAnalysis:
    analysis = DocumentAnalysis(
        document_version_id=document_version_id,
        status="COMPLETED",
        provider="ai",
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


def x_persist_document_analysis__mutmut_23(
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
        completed_at=datetime.now(None),
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


def x_persist_document_analysis__mutmut_24(
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

    db.add(None)
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


def x_persist_document_analysis__mutmut_25(
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
        evidence = None

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis


def x_persist_document_analysis__mutmut_26(
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
            analysis_id=None,
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


def x_persist_document_analysis__mutmut_27(
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
            field_name=None,
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


def x_persist_document_analysis__mutmut_28(
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
            field_value=None,
            page_number=item.page_number,
            confidence=item.confidence,
            source=item.source,
            evidence_text=item.evidence_text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis


def x_persist_document_analysis__mutmut_29(
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
            page_number=None,
            confidence=item.confidence,
            source=item.source,
            evidence_text=item.evidence_text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis


def x_persist_document_analysis__mutmut_30(
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
            confidence=None,
            source=item.source,
            evidence_text=item.evidence_text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis


def x_persist_document_analysis__mutmut_31(
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
            source=None,
            evidence_text=item.evidence_text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis


def x_persist_document_analysis__mutmut_32(
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
            evidence_text=None,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis


def x_persist_document_analysis__mutmut_33(
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


def x_persist_document_analysis__mutmut_34(
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


def x_persist_document_analysis__mutmut_35(
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
            page_number=item.page_number,
            confidence=item.confidence,
            source=item.source,
            evidence_text=item.evidence_text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis


def x_persist_document_analysis__mutmut_36(
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
            confidence=item.confidence,
            source=item.source,
            evidence_text=item.evidence_text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis


def x_persist_document_analysis__mutmut_37(
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
            source=item.source,
            evidence_text=item.evidence_text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis


def x_persist_document_analysis__mutmut_38(
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
            evidence_text=item.evidence_text,
        )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis


def x_persist_document_analysis__mutmut_39(
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
            )

        db.add(evidence)

    db.flush()
    db.refresh(analysis)

    return analysis


def x_persist_document_analysis__mutmut_40(
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

        db.add(None)

    db.flush()
    db.refresh(analysis)

    return analysis


def x_persist_document_analysis__mutmut_41(
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
    db.refresh(None)

    return analysis

mutants_x_persist_document_analysis__mutmut['_mutmut_orig'] = x_persist_document_analysis__mutmut_orig # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_1'] = x_persist_document_analysis__mutmut_1 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_2'] = x_persist_document_analysis__mutmut_2 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_3'] = x_persist_document_analysis__mutmut_3 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_4'] = x_persist_document_analysis__mutmut_4 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_5'] = x_persist_document_analysis__mutmut_5 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_6'] = x_persist_document_analysis__mutmut_6 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_7'] = x_persist_document_analysis__mutmut_7 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_8'] = x_persist_document_analysis__mutmut_8 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_9'] = x_persist_document_analysis__mutmut_9 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_10'] = x_persist_document_analysis__mutmut_10 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_11'] = x_persist_document_analysis__mutmut_11 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_12'] = x_persist_document_analysis__mutmut_12 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_13'] = x_persist_document_analysis__mutmut_13 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_14'] = x_persist_document_analysis__mutmut_14 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_15'] = x_persist_document_analysis__mutmut_15 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_16'] = x_persist_document_analysis__mutmut_16 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_17'] = x_persist_document_analysis__mutmut_17 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_18'] = x_persist_document_analysis__mutmut_18 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_19'] = x_persist_document_analysis__mutmut_19 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_20'] = x_persist_document_analysis__mutmut_20 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_21'] = x_persist_document_analysis__mutmut_21 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_22'] = x_persist_document_analysis__mutmut_22 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_23'] = x_persist_document_analysis__mutmut_23 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_24'] = x_persist_document_analysis__mutmut_24 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_25'] = x_persist_document_analysis__mutmut_25 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_26'] = x_persist_document_analysis__mutmut_26 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_27'] = x_persist_document_analysis__mutmut_27 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_28'] = x_persist_document_analysis__mutmut_28 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_29'] = x_persist_document_analysis__mutmut_29 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_30'] = x_persist_document_analysis__mutmut_30 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_31'] = x_persist_document_analysis__mutmut_31 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_32'] = x_persist_document_analysis__mutmut_32 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_33'] = x_persist_document_analysis__mutmut_33 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_34'] = x_persist_document_analysis__mutmut_34 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_35'] = x_persist_document_analysis__mutmut_35 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_36'] = x_persist_document_analysis__mutmut_36 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_37'] = x_persist_document_analysis__mutmut_37 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_38'] = x_persist_document_analysis__mutmut_38 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_39'] = x_persist_document_analysis__mutmut_39 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_40'] = x_persist_document_analysis__mutmut_40 # type: ignore # mutmut generated
mutants_x_persist_document_analysis__mutmut['x_persist_document_analysis__mutmut_41'] = x_persist_document_analysis__mutmut_41 # type: ignore # mutmut generated

