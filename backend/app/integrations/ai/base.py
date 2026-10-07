from dataclasses import dataclass, field
from typing import Protocol

from app.services.document_text_extraction_service import ExtractedDocument


@dataclass
class EvidenceItem:
    field_name: str
    field_value: str | None
    page_number: int | None
    confidence: float | None
    evidence_text: str | None
    source: str = "AI"


@dataclass
class AIAnalysisResult:
    detected_document_type: str | None
    summary: str | None
    structured_data: dict = field(default_factory=dict)
    overall_confidence: float | None = None
    evidence: list[EvidenceItem] = field(default_factory=list)


class DocumentAIProvider(Protocol):
    def analyze(
        self,
        extracted_document: ExtractedDocument,
    ) -> AIAnalysisResult:
        ...