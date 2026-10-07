import pytest

from app.integrations.ai.factory import get_ai_provider
from app.integrations.ai.mock_provider import MockDocumentAIProvider

from app.integrations.ai.gemini_provider import (
    GeminiDocumentAIProvider,
)


def test_get_ai_provider_returns_mock_provider(monkeypatch):
    monkeypatch.setattr(
        "app.integrations.ai.factory.AI_PROVIDER",
        "mock",
    )

    provider = get_ai_provider()

    assert isinstance(provider, MockDocumentAIProvider)


def test_get_ai_provider_rejects_unsupported_provider(monkeypatch):
    import app.integrations.ai.factory as factory

    monkeypatch.setattr(
        factory,
        "AI_PROVIDER",
        "unsupported",
    )

    with pytest.raises(ValueError, match="Unsupported AI provider"):
        factory.get_ai_provider()


def test_get_ai_provider_returns_gemini_provider(monkeypatch):
    monkeypatch.setattr(
        "app.integrations.ai.factory.AI_PROVIDER",
        "gemini",
    )

    provider = get_ai_provider()

    assert isinstance(
        provider,
        GeminiDocumentAIProvider,
    )

