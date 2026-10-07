from typing import Literal

from google import genai
from pydantic import BaseModel, Field

from app.core.config import GEMINI_API_KEY, AI_MODEL_NAME
from app.integrations.ai.base import (
    AIAnalysisResult,
    EvidenceItem,
)
from app.services.document_text_extraction_service import ExtractedDocument


class GeminiEvidence(BaseModel):
    field_name: str = Field(
        description="Semantic evidence field name."
    )
    field_value: str | None = Field(
        default=None,
        description="Extracted value as text. Null when not confidently available."
    )
    page_number: int | None = Field(
        default=None,
        description="1-based page number where the evidence appears."
    )
    confidence: float | None = Field(
        default=None,
        description="Confidence from 0.0 to 1.0."
    )
    evidence_text: str | None = Field(
        default=None,
        description="Short verbatim supporting text from the document."
    )


class GeminiAnalysisResponse(BaseModel):
    detected_document_type: Literal[
        "RERA",
        "SANCTIONED_PLAN",
        "FIRE_NOC",
        "UNKNOWN",
    ]

    summary: str | None = None

    overall_confidence: float | None = Field(
        default=None,
        description="Overall extraction confidence from 0.0 to 1.0."
    )

    evidence: list[GeminiEvidence] = Field(
        default_factory=list
    )


class GeminiDocumentAIProvider:
    def __init__(
        self,
        api_key: str | None = None,
        model_name: str | None = None,
        client=None,
    ) -> None:
        resolved_api_key = api_key or GEMINI_API_KEY

        if not resolved_api_key:
            raise ValueError(
                "GEMINI_API_KEY is not configured"
            )

        self.model_name = model_name or AI_MODEL_NAME
        self.client = client or genai.Client(
            api_key=resolved_api_key
        )

    def analyze(
        self,
        extracted_document: ExtractedDocument,
    ) -> AIAnalysisResult:
        if not extracted_document.has_text:
            raise ValueError(
                "Cannot analyze a document without extracted text"
            )

        document_text = self._build_document_text(
            extracted_document
        )

        prompt = self._build_prompt(document_text)

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": GeminiAnalysisResponse,
            },
        )

        parsed = response.parsed

        if parsed is None:
            raise ValueError(
                "Gemini returned no structured response"
            )

        if not isinstance(parsed, GeminiAnalysisResponse):
            parsed = GeminiAnalysisResponse.model_validate(parsed)

        evidence = [
            EvidenceItem(
                field_name=item.field_name,
                field_value=item.field_value,
                page_number=item.page_number,
                confidence=item.confidence,
                evidence_text=item.evidence_text,
                source="AI",
            )
            for item in parsed.evidence
            if item.field_name
        ]

        structured_data = {
            "detected_document_type": parsed.detected_document_type,
            "evidence_count": len(evidence),
        }

        return AIAnalysisResult(
            detected_document_type=parsed.detected_document_type,
            summary=parsed.summary,
            structured_data=structured_data,
            overall_confidence=parsed.overall_confidence,
            evidence=evidence,
        )

    @staticmethod
    def _build_document_text(
        extracted_document: ExtractedDocument,
    ) -> str:
        pages = []

        for page in extracted_document.pages:
            if not page.text.strip():
                continue

            pages.append(
                f"--- PAGE {page.page_number} ---\n"
                f"{page.text.strip()}"
            )

        return "\n\n".join(pages)

    @staticmethod
    def _build_prompt(document_text: str) -> str:
        return f"""
You are the document-understanding component of PropertyGuard,
an AI-assisted property compliance and risk assessment platform.

Analyze the supplied property document.

Your task is ONLY:
1. Classify the document.
2. Extract factual evidence explicitly present in the document.
3. Provide the page number for every extracted field.
4. Provide a short supporting evidence quote.
5. Assign confidence between 0.0 and 1.0.

You MUST NOT:
- decide legal compliance;
- decide PASS, FAIL, or NEEDS_REVIEW;
- invent missing information;
- infer facts that are not supported by the document;
- treat the absence of a field as proof that it does not exist.

Allowed document types:
- RERA
- SANCTIONED_PLAN
- FIRE_NOC
- UNKNOWN

Useful semantic fields include:

RERA:
- registration_number
- project_name
- promoter_name
- registration_date
- validity_date

SANCTIONED_PLAN:
- approval_number
- project_name
- building_name
- number_of_floors
- sanctioned_area

FIRE_NOC:
- certificate_number
- project_name
- issuing_authority
- issue_date
- validity_date

Only return evidence that is actually supported by the document.

The evidence_text must be a short excerpt from the supplied document.
Page numbers are 1-based.

DOCUMENT:

{document_text}
""".strip()