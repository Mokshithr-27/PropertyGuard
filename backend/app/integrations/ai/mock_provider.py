from app.integrations.ai.base import (
    AIAnalysisResult,
    DocumentAIProvider,
    EvidenceItem,
)
from app.services.document_text_extraction_service import ExtractedDocument


class MockDocumentAIProvider:
    def analyze(
        self,
        extracted_document: ExtractedDocument,
    ) -> AIAnalysisResult:
        evidence: list[EvidenceItem] = []

        for page in extracted_document.pages:
            text = page.text.strip()

            if not text:
                continue

            evidence.append(
                EvidenceItem(
                    field_name="page_text",
                    field_value=text,
                    page_number=page.page_number,
                    confidence=1.0,
                    evidence_text=text,
                    source=page.source,
                )
            )

        return AIAnalysisResult(
            detected_document_type="UNKNOWN",
            summary=(
                f"Mock AI analysis of "
                f"{extracted_document.page_count} page(s)."
            ),
            structured_data={
                "page_count": extracted_document.page_count,
                "has_text": extracted_document.has_text,
                "text_length": len(extracted_document.full_text),
            },
            overall_confidence=1.0 if extracted_document.has_text else 0.0,
            evidence=evidence,
        )