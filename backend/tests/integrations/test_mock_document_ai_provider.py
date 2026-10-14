"""
PropertyGuard Mock Document AI Provider Test Suite
--------------------------------------------------
Validates that MockDocumentAIProvider properly extracts regex patterns, creates
evidence items, and generates standardized AIAnalysisResult objects.
"""

from app.integrations.ai.base import AIAnalysisResult
from app.integrations.ai.mock_provider import MockDocumentAIProvider
from app.services.document_text_extraction_service import (
    ExtractedDocument,
    ExtractedPage,
)


def test_mock_provider_returns_analysis_result():
    extracted = ExtractedDocument(
        page_count=2,
        pages=[
            ExtractedPage(
                page_number=1,
                text="RERA Registration No: P02400001234",
            ),
            ExtractedPage(
                page_number=2,
                text="Project Name: ABC Residency",
            ),
        ],
    )

    provider = MockDocumentAIProvider()

    result = provider.analyze(extracted)

    assert isinstance(result, AIAnalysisResult)
    assert result.detected_document_type == "RERA"
    assert result.overall_confidence == 0.85
    assert result.structured_data["page_count"] == 2
    assert result.structured_data["has_text"] is True

    registration = next(
        item for item in result.evidence
        if item.field_name == "registration_number"
    )
    project = next(
        item for item in result.evidence
        if item.field_name == "project_name"
    )

    assert registration.field_value == "P02400001234"
    assert project.field_value == "ABC Residency"
    assert len(result.evidence) == 4


def test_mock_provider_preserves_page_evidence():
    extracted = ExtractedDocument(
        page_count=2,
        pages=[
            ExtractedPage(
                page_number=1,
                text="RERA Registration No: P02400001234",
                source="PDF_TEXT",
            ),
            ExtractedPage(
                page_number=2,
                text="Project Name: ABC Residency",
                source="OCR",
            ),
        ],
    )

    provider = MockDocumentAIProvider()

    result = provider.analyze(extracted)

    page_evidence = [
        item for item in result.evidence
        if item.field_name == "page_text"
    ]

    assert len(page_evidence) == 2

    first, second = page_evidence

    assert first.field_value == "RERA Registration No: P02400001234"
    assert first.page_number == 1
    assert first.source == "PDF_TEXT"

    assert second.field_value == "Project Name: ABC Residency"
    assert second.page_number == 2
    assert second.source == "OCR"


def test_mock_provider_skips_blank_pages():
    extracted = ExtractedDocument(
        page_count=3,
        pages=[
            ExtractedPage(page_number=1, text=""),
            ExtractedPage(page_number=2, text="Important document text"),
            ExtractedPage(page_number=3, text="   "),
        ],
    )

    provider = MockDocumentAIProvider()

    result = provider.analyze(extracted)

    assert len(result.evidence) == 1
    assert result.evidence[0].page_number == 2
    assert result.evidence[0].field_value == "Important document text"