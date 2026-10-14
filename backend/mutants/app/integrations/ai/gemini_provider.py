"""
PropertyGuard Google Gemini Document AI Provider
-------------------------------------------------
Implements DocumentAIProvider using Google GenAI SDK (Gemini models).
Leverages structured outputs via Pydantic schemas to extract semantic evidence,
field metadata, confidence scores, and summaries from extracted document texts.
"""

from typing import Literal

from google import genai
from pydantic import BaseModel, Field

from app.core.config import GEMINI_API_KEY, AI_MODEL_NAME
from app.integrations.ai.base import (
    AIAnalysisResult,
    EvidenceItem,
)
from app.services.document_text_extraction_service import ExtractedDocument


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_xǁGeminiDocumentAIProviderǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut: MutantDict = {}  # type: ignore


class GeminiDocumentAIProvider:
    @_mutmut_mutated(mutants_xǁGeminiDocumentAIProviderǁ__init____mutmut)
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
    def xǁGeminiDocumentAIProviderǁ__init____mutmut_orig(
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
    def xǁGeminiDocumentAIProviderǁ__init____mutmut_1(
        self,
        api_key: str | None = None,
        model_name: str | None = None,
        client=None,
    ) -> None:
        resolved_api_key = None

        if not resolved_api_key:
            raise ValueError(
                "GEMINI_API_KEY is not configured"
            )

        self.model_name = model_name or AI_MODEL_NAME
        self.client = client or genai.Client(
            api_key=resolved_api_key
        )
    def xǁGeminiDocumentAIProviderǁ__init____mutmut_2(
        self,
        api_key: str | None = None,
        model_name: str | None = None,
        client=None,
    ) -> None:
        resolved_api_key = api_key and GEMINI_API_KEY

        if not resolved_api_key:
            raise ValueError(
                "GEMINI_API_KEY is not configured"
            )

        self.model_name = model_name or AI_MODEL_NAME
        self.client = client or genai.Client(
            api_key=resolved_api_key
        )
    def xǁGeminiDocumentAIProviderǁ__init____mutmut_3(
        self,
        api_key: str | None = None,
        model_name: str | None = None,
        client=None,
    ) -> None:
        resolved_api_key = api_key or GEMINI_API_KEY

        if resolved_api_key:
            raise ValueError(
                "GEMINI_API_KEY is not configured"
            )

        self.model_name = model_name or AI_MODEL_NAME
        self.client = client or genai.Client(
            api_key=resolved_api_key
        )
    def xǁGeminiDocumentAIProviderǁ__init____mutmut_4(
        self,
        api_key: str | None = None,
        model_name: str | None = None,
        client=None,
    ) -> None:
        resolved_api_key = api_key or GEMINI_API_KEY

        if not resolved_api_key:
            raise ValueError(
                None
            )

        self.model_name = model_name or AI_MODEL_NAME
        self.client = client or genai.Client(
            api_key=resolved_api_key
        )
    def xǁGeminiDocumentAIProviderǁ__init____mutmut_5(
        self,
        api_key: str | None = None,
        model_name: str | None = None,
        client=None,
    ) -> None:
        resolved_api_key = api_key or GEMINI_API_KEY

        if not resolved_api_key:
            raise ValueError(
                "XXGEMINI_API_KEY is not configuredXX"
            )

        self.model_name = model_name or AI_MODEL_NAME
        self.client = client or genai.Client(
            api_key=resolved_api_key
        )
    def xǁGeminiDocumentAIProviderǁ__init____mutmut_6(
        self,
        api_key: str | None = None,
        model_name: str | None = None,
        client=None,
    ) -> None:
        resolved_api_key = api_key or GEMINI_API_KEY

        if not resolved_api_key:
            raise ValueError(
                "gemini_api_key is not configured"
            )

        self.model_name = model_name or AI_MODEL_NAME
        self.client = client or genai.Client(
            api_key=resolved_api_key
        )
    def xǁGeminiDocumentAIProviderǁ__init____mutmut_7(
        self,
        api_key: str | None = None,
        model_name: str | None = None,
        client=None,
    ) -> None:
        resolved_api_key = api_key or GEMINI_API_KEY

        if not resolved_api_key:
            raise ValueError(
                "GEMINI_API_KEY IS NOT CONFIGURED"
            )

        self.model_name = model_name or AI_MODEL_NAME
        self.client = client or genai.Client(
            api_key=resolved_api_key
        )
    def xǁGeminiDocumentAIProviderǁ__init____mutmut_8(
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

        self.model_name = None
        self.client = client or genai.Client(
            api_key=resolved_api_key
        )
    def xǁGeminiDocumentAIProviderǁ__init____mutmut_9(
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

        self.model_name = model_name and AI_MODEL_NAME
        self.client = client or genai.Client(
            api_key=resolved_api_key
        )
    def xǁGeminiDocumentAIProviderǁ__init____mutmut_10(
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
        self.client = None
    def xǁGeminiDocumentAIProviderǁ__init____mutmut_11(
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
        self.client = client and genai.Client(
            api_key=resolved_api_key
        )
    def xǁGeminiDocumentAIProviderǁ__init____mutmut_12(
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
            api_key=None
        )

    @_mutmut_mutated(mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut)
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_orig(
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_1(
        self,
        extracted_document: ExtractedDocument,
    ) -> AIAnalysisResult:
        if extracted_document.has_text:
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_2(
        self,
        extracted_document: ExtractedDocument,
    ) -> AIAnalysisResult:
        if not extracted_document.has_text:
            raise ValueError(
                None
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_3(
        self,
        extracted_document: ExtractedDocument,
    ) -> AIAnalysisResult:
        if not extracted_document.has_text:
            raise ValueError(
                "XXCannot analyze a document without extracted textXX"
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_4(
        self,
        extracted_document: ExtractedDocument,
    ) -> AIAnalysisResult:
        if not extracted_document.has_text:
            raise ValueError(
                "cannot analyze a document without extracted text"
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_5(
        self,
        extracted_document: ExtractedDocument,
    ) -> AIAnalysisResult:
        if not extracted_document.has_text:
            raise ValueError(
                "CANNOT ANALYZE A DOCUMENT WITHOUT EXTRACTED TEXT"
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_6(
        self,
        extracted_document: ExtractedDocument,
    ) -> AIAnalysisResult:
        if not extracted_document.has_text:
            raise ValueError(
                "Cannot analyze a document without extracted text"
            )

        document_text = None

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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_7(
        self,
        extracted_document: ExtractedDocument,
    ) -> AIAnalysisResult:
        if not extracted_document.has_text:
            raise ValueError(
                "Cannot analyze a document without extracted text"
            )

        document_text = self._build_document_text(
            None
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_8(
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

        prompt = None

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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_9(
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

        prompt = self._build_prompt(None)

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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_10(
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

        response = None

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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_11(
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
            model=None,
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_12(
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
            contents=None,
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_13(
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
            config=None,
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_14(
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_15(
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_16(
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_17(
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
                "XXresponse_mime_typeXX": "application/json",
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_18(
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
                "RESPONSE_MIME_TYPE": "application/json",
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_19(
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
                "response_mime_type": "XXapplication/jsonXX",
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_20(
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
                "response_mime_type": "APPLICATION/JSON",
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_21(
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
                "XXresponse_schemaXX": GeminiAnalysisResponse,
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_22(
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
                "RESPONSE_SCHEMA": GeminiAnalysisResponse,
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_23(
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

        parsed = None

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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_24(
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

        if parsed is not None:
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_25(
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
                None
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_26(
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
                "XXGemini returned no structured responseXX"
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_27(
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
                "gemini returned no structured response"
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_28(
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
                "GEMINI RETURNED NO STRUCTURED RESPONSE"
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_29(
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

        if isinstance(parsed, GeminiAnalysisResponse):
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_30(
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
            parsed = None

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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_31(
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
            parsed = GeminiAnalysisResponse.model_validate(None)

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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_32(
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

        evidence = None

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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_33(
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
                field_name=None,
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_34(
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
                field_value=None,
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_35(
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
                page_number=None,
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_36(
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
                confidence=None,
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_37(
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
                evidence_text=None,
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_38(
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
                source=None,
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_39(
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_40(
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_41(
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_42(
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_43(
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_44(
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_45(
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
                source="XXAIXX",
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_46(
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
                source="ai",
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

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_47(
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

        structured_data = None

        return AIAnalysisResult(
            detected_document_type=parsed.detected_document_type,
            summary=parsed.summary,
            structured_data=structured_data,
            overall_confidence=parsed.overall_confidence,
            evidence=evidence,
        )

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_48(
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
            "XXdetected_document_typeXX": parsed.detected_document_type,
            "evidence_count": len(evidence),
        }

        return AIAnalysisResult(
            detected_document_type=parsed.detected_document_type,
            summary=parsed.summary,
            structured_data=structured_data,
            overall_confidence=parsed.overall_confidence,
            evidence=evidence,
        )

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_49(
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
            "DETECTED_DOCUMENT_TYPE": parsed.detected_document_type,
            "evidence_count": len(evidence),
        }

        return AIAnalysisResult(
            detected_document_type=parsed.detected_document_type,
            summary=parsed.summary,
            structured_data=structured_data,
            overall_confidence=parsed.overall_confidence,
            evidence=evidence,
        )

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_50(
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
            "XXevidence_countXX": len(evidence),
        }

        return AIAnalysisResult(
            detected_document_type=parsed.detected_document_type,
            summary=parsed.summary,
            structured_data=structured_data,
            overall_confidence=parsed.overall_confidence,
            evidence=evidence,
        )

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_51(
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
            "EVIDENCE_COUNT": len(evidence),
        }

        return AIAnalysisResult(
            detected_document_type=parsed.detected_document_type,
            summary=parsed.summary,
            structured_data=structured_data,
            overall_confidence=parsed.overall_confidence,
            evidence=evidence,
        )

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_52(
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
            detected_document_type=None,
            summary=parsed.summary,
            structured_data=structured_data,
            overall_confidence=parsed.overall_confidence,
            evidence=evidence,
        )

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_53(
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
            summary=None,
            structured_data=structured_data,
            overall_confidence=parsed.overall_confidence,
            evidence=evidence,
        )

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_54(
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
            structured_data=None,
            overall_confidence=parsed.overall_confidence,
            evidence=evidence,
        )

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_55(
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
            overall_confidence=None,
            evidence=evidence,
        )

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_56(
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
            evidence=None,
        )

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_57(
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
            summary=parsed.summary,
            structured_data=structured_data,
            overall_confidence=parsed.overall_confidence,
            evidence=evidence,
        )

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_58(
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
            structured_data=structured_data,
            overall_confidence=parsed.overall_confidence,
            evidence=evidence,
        )

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_59(
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
            overall_confidence=parsed.overall_confidence,
            evidence=evidence,
        )

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_60(
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
            evidence=evidence,
        )

    def xǁGeminiDocumentAIProviderǁanalyze__mutmut_61(
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
            )

    @staticmethod
    @_mutmut_mutated(mutants_xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut)
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
    def xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_orig(
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
    def xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_1(
        extracted_document: ExtractedDocument,
    ) -> str:
        pages = None

        for page in extracted_document.pages:
            if not page.text.strip():
                continue

            pages.append(
                f"--- PAGE {page.page_number} ---\n"
                f"{page.text.strip()}"
            )

        return "\n\n".join(pages)

    @staticmethod
    def xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_2(
        extracted_document: ExtractedDocument,
    ) -> str:
        pages = []

        for page in extracted_document.pages:
            if page.text.strip():
                continue

            pages.append(
                f"--- PAGE {page.page_number} ---\n"
                f"{page.text.strip()}"
            )

        return "\n\n".join(pages)

    @staticmethod
    def xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_3(
        extracted_document: ExtractedDocument,
    ) -> str:
        pages = []

        for page in extracted_document.pages:
            if not page.text.strip():
                break

            pages.append(
                f"--- PAGE {page.page_number} ---\n"
                f"{page.text.strip()}"
            )

        return "\n\n".join(pages)

    @staticmethod
    def xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_4(
        extracted_document: ExtractedDocument,
    ) -> str:
        pages = []

        for page in extracted_document.pages:
            if not page.text.strip():
                continue

            pages.append(
                None
            )

        return "\n\n".join(pages)

    @staticmethod
    def xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_5(
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

        return "\n\n".join(None)

    @staticmethod
    def xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_6(
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

        return "XX\n\nXX".join(pages)

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

mutants_xǁGeminiDocumentAIProviderǁ__init____mutmut['_mutmut_orig'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ__init____mutmut['xǁGeminiDocumentAIProviderǁ__init____mutmut_1'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ__init____mutmut['xǁGeminiDocumentAIProviderǁ__init____mutmut_2'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ__init____mutmut['xǁGeminiDocumentAIProviderǁ__init____mutmut_3'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ__init____mutmut['xǁGeminiDocumentAIProviderǁ__init____mutmut_4'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ__init____mutmut['xǁGeminiDocumentAIProviderǁ__init____mutmut_5'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ__init____mutmut['xǁGeminiDocumentAIProviderǁ__init____mutmut_6'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ__init____mutmut['xǁGeminiDocumentAIProviderǁ__init____mutmut_7'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ__init____mutmut['xǁGeminiDocumentAIProviderǁ__init____mutmut_8'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ__init____mutmut['xǁGeminiDocumentAIProviderǁ__init____mutmut_9'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ__init____mutmut['xǁGeminiDocumentAIProviderǁ__init____mutmut_10'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ__init____mutmut['xǁGeminiDocumentAIProviderǁ__init____mutmut_11'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ__init____mutmut['xǁGeminiDocumentAIProviderǁ__init____mutmut_12'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ__init____mutmut_12 # type: ignore # mutmut generated

mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['_mutmut_orig'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_1'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_2'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_3'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_4'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_5'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_6'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_7'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_8'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_9'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_10'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_11'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_12'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_13'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_14'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_15'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_16'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_17'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_18'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_19'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_20'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_21'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_22'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_23'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_24'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_25'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_26'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_27'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_28'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_29'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_30'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_31'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_32'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_33'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_34'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_35'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_36'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_37'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_38'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_39'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_40'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_41'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_42'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_43'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_44'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_44 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_45'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_45 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_46'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_46 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_47'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_47 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_48'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_48 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_49'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_49 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_50'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_50 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_51'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_51 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_52'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_52 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_53'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_53 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_54'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_54 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_55'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_55 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_56'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_56 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_57'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_57 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_58'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_58 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_59'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_59 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_60'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_60 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁanalyze__mutmut['xǁGeminiDocumentAIProviderǁanalyze__mutmut_61'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁanalyze__mutmut_61 # type: ignore # mutmut generated

mutants_xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut['_mutmut_orig'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut['xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_1'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut['xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_2'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut['xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_3'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut['xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_4'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut['xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_5'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut['xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_6'] = GeminiDocumentAIProvider.xǁGeminiDocumentAIProviderǁ_build_document_text__mutmut_6 # type: ignore # mutmut generated