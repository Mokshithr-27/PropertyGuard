from types import SimpleNamespace
from uuid import uuid4

from app.integrations.ai.gemini_provider import (
    GeminiAnalysisResponse,
    GeminiDocumentAIProvider,
)
from app.services.document_text_extraction_service import (
    ExtractedDocument,
    ExtractedPage,
)


class FakeGeminiModels:
    def __init__(self, parsed_response):
        self.parsed_response = parsed_response
        self.last_model = None
        self.last_contents = None
        self.last_config = None

    def generate_content(
        self,
        model,
        contents,
        config,
    ):
        self.last_model = model
        self.last_contents = contents
        self.last_config = config

        return SimpleNamespace(
            parsed=self.parsed_response
        )


class FakeGeminiClient:
    def __init__(self, parsed_response):
        self.models = FakeGeminiModels(parsed_response)


def make_document():
    return ExtractedDocument(
        page_count=1,
        pages=[
            ExtractedPage(
                page_number=1,
                text=(
                    "RERA Registration Number: P123456789\n"
                    "Project Name: Green Valley Apartments\n"
                    "Promoter: ABC Developers"
                ),
            )
        ],
    )


def test_gemini_provider_converts_structured_response():
    parsed = GeminiAnalysisResponse(
        detected_document_type="RERA",
        summary="RERA registration certificate.",
        overall_confidence=0.96,
        evidence=[
            {
                "field_name": "registration_number",
                "field_value": "P123456789",
                "page_number": 1,
                "confidence": 0.98,
                "evidence_text": "RERA Registration Number: P123456789",
            },
            {
                "field_name": "project_name",
                "field_value": "Green Valley Apartments",
                "page_number": 1,
                "confidence": 0.96,
                "evidence_text": "Project Name: Green Valley Apartments",
            },
        ],
    )

    client = FakeGeminiClient(parsed)

    provider = GeminiDocumentAIProvider(
        api_key="test-key",
        model_name="gemini-2.5-flash",
        client=client,
    )

    result = provider.analyze(make_document())

    assert result.detected_document_type == "RERA"
    assert result.summary == "RERA registration certificate."
    assert result.overall_confidence == 0.96

    assert len(result.evidence) == 2

    assert result.evidence[0].field_name == "registration_number"
    assert result.evidence[0].field_value == "P123456789"
    assert result.evidence[0].page_number == 1
    assert result.evidence[0].source == "AI"

    assert result.evidence[1].field_name == "project_name"
    assert result.evidence[1].field_value == "Green Valley Apartments"


def test_gemini_provider_sends_structured_output_request():
    parsed = GeminiAnalysisResponse(
        detected_document_type="RERA",
        summary="Test",
        overall_confidence=1.0,
        evidence=[],
    )

    client = FakeGeminiClient(parsed)

    provider = GeminiDocumentAIProvider(
        api_key="test-key",
        model_name="gemini-2.5-flash",
        client=client,
    )

    provider.analyze(make_document())

    assert client.models.last_model == "gemini-2.5-flash"

    assert (
        client.models.last_config["response_mime_type"]
        == "application/json"
    )

    assert (
        client.models.last_config["response_schema"]
        == GeminiAnalysisResponse
    )

    assert "PAGE 1" in client.models.last_contents
    assert "P123456789" in client.models.last_contents


def test_gemini_provider_rejects_empty_document():
    client = FakeGeminiClient(None)

    provider = GeminiDocumentAIProvider(
        api_key="test-key",
        model_name="gemini-2.5-flash",
        client=client,
    )

    empty_document = ExtractedDocument(
        page_count=1,
        pages=[
            ExtractedPage(
                page_number=1,
                text="",
            )
        ],
    )

    try:
        provider.analyze(empty_document)
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert str(exc) == (
            "Cannot analyze a document without extracted text"
        )

def test_gemini_provider_requires_api_key(monkeypatch):
    monkeypatch.setattr(
        "app.integrations.ai.gemini_provider.GEMINI_API_KEY",
        "",
    )

    try:
        GeminiDocumentAIProvider(
            api_key=None,
            model_name="gemini-2.5-flash",
        )
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert str(exc) == "GEMINI_API_KEY is not configured"

        