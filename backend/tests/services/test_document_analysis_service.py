"""
PropertyGuard Document Analysis Service Test Suite
--------------------------------------------------
Validates creation of DocumentAnalysis models and extraction of evidence facts
(dates, registration numbers, approvals) from extracted documents.
"""

from types import SimpleNamespace

from app.services import document_analysis_service


class FakeDB:
    def __init__(self):
        self.added = []
        self.flush_count = 0

    def add(self, obj):
        self.added.append(obj)

    def flush(self):
        self.flush_count += 1

    def refresh(self, obj):
        pass


def make_extracted_document():
    page_1 = SimpleNamespace(
        page_number=1,
        text="RERA Registration Number: RERA123456",
    )

    page_2 = SimpleNamespace(
        page_number=2,
        text="Project Name: Hyderabad Residential Apartment",
    )

    return SimpleNamespace(
        page_count=2,
        pages=[page_1, page_2],
        full_text=(
            "RERA Registration Number: RERA123456\n\n"
            "Project Name: Hyderabad Residential Apartment"
        ),
        has_text=True,
    )


def test_create_document_analysis_success():
    db = FakeDB()
    extracted = make_extracted_document()

    result = document_analysis_service.create_document_analysis(
        db=db,
        document_version_id="test-version-id",
        extracted=extracted,
    )

    assert result.status == "COMPLETED"
    assert result.provider == "deterministic"
    assert result.model_name == "pymupdf-text-extraction"
    assert result.detected_document_type is None
    assert result.overall_confidence == 1.0

    assert result.structured_data["page_count"] == 2
    assert result.structured_data["has_text"] is True
    assert result.structured_data["text_length"] == len(extracted.full_text)

    evidence = [
        obj
        for obj in db.added
        if obj.__class__.__name__ == "DocumentEvidence"
    ]

    assert len(evidence) == 2

    assert evidence[0].field_name == "page_text"
    assert evidence[0].page_number == 1
    assert evidence[0].confidence == 1.0
    assert evidence[0].source == "PDF_TEXT"
    assert evidence[0].evidence_text == "RERA Registration Number: RERA123456"

    assert evidence[1].field_name == "page_text"
    assert evidence[1].page_number == 2
    assert evidence[1].confidence == 1.0
    assert evidence[1].source == "PDF_TEXT"
    assert evidence[1].evidence_text == (
        "Project Name: Hyderabad Residential Apartment"
    )

    assert db.flush_count == 2


def test_create_document_analysis_skips_blank_pages():
    db = FakeDB()

    page_1 = SimpleNamespace(
        page_number=1,
        text="Valid document text",
    )

    page_2 = SimpleNamespace(
        page_number=2,
        text="   ",
    )

    extracted = SimpleNamespace(
        page_count=2,
        pages=[page_1, page_2],
        full_text="Valid document text",
        has_text=True,
    )

    result = document_analysis_service.create_document_analysis(
        db=db,
        document_version_id="test-version-id",
        extracted=extracted,
    )

    evidence = [
        obj
        for obj in db.added
        if obj.__class__.__name__ == "DocumentEvidence"
    ]

    assert len(evidence) == 1
    assert evidence[0].page_number == 1
    assert evidence[0].evidence_text == "Valid document text"


def test_create_document_analysis_for_blank_document():
    db = FakeDB()

    extracted = SimpleNamespace(
        page_count=2,
        pages=[
            SimpleNamespace(page_number=1, text=""),
            SimpleNamespace(page_number=2, text="   "),
        ],
        full_text="",
        has_text=False,
    )

    result = document_analysis_service.create_document_analysis(
        db=db,
        document_version_id="test-version-id",
        extracted=extracted,
    )

    assert result.status == "COMPLETED"
    assert result.overall_confidence == 0.0
    assert result.structured_data["page_count"] == 2
    assert result.structured_data["has_text"] is False
    assert result.structured_data["text_length"] == 0

    evidence = [
        obj
        for obj in db.added
        if obj.__class__.__name__ == "DocumentEvidence"
    ]

    assert len(evidence) == 0