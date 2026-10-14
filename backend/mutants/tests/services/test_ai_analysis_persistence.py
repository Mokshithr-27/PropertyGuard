"""
PropertyGuard AI Analysis Persistence Test Suite
------------------------------------------------
Tests database persistence of DocumentAnalysis records and linked DocumentEvidence
items using simulated database sessions.
"""

from app.integrations.ai.base import (
    AIAnalysisResult,
    EvidenceItem,
)
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


def test_persist_document_analysis():
    db = FakeDB()

    result = AIAnalysisResult(
        detected_document_type="RERA",
        summary="RERA registration certificate.",
        structured_data={
            "registration_number": "P02400001234",
            "project_name": "ABC Residency",
        },
        overall_confidence=0.94,
        evidence=[
            EvidenceItem(
                field_name="registration_number",
                field_value="P02400001234",
                page_number=1,
                confidence=0.98,
                evidence_text="Registration No: P02400001234",
                source="AI",
            ),
            EvidenceItem(
                field_name="project_name",
                field_value="ABC Residency",
                page_number=1,
                confidence=0.96,
                evidence_text="Project Name: ABC Residency",
                source="AI",
            ),
        ],
    )

    analysis = document_analysis_service.persist_document_analysis(
        db=db,
        document_version_id="test-version-id",
        result=result,
    )

    assert analysis.status == "COMPLETED"
    assert analysis.provider == "AI"
    assert analysis.detected_document_type == "RERA"
    assert analysis.summary == "RERA registration certificate."
    assert analysis.overall_confidence == 0.94

    assert analysis.structured_data["registration_number"] == (
        "P02400001234"
    )

    evidence = [
        obj
        for obj in db.added
        if obj.__class__.__name__ == "DocumentEvidence"
    ]

    assert len(evidence) == 2

    assert evidence[0].field_name == "registration_number"
    assert evidence[0].field_value == "P02400001234"
    assert evidence[0].page_number == 1
    assert evidence[0].confidence == 0.98
    assert evidence[0].source == "AI"

    assert evidence[1].field_name == "project_name"
    assert evidence[1].field_value == "ABC Residency"
    assert evidence[1].page_number == 1

    assert db.flush_count == 2