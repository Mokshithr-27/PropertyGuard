"""
PropertyGuard AI Provider Factory
----------------------------------
Instantiates the configured DocumentAIProvider implementation ('mock' or 'gemini')
based on environment configuration settings.
"""

from app.core.config import AI_PROVIDER
from app.integrations.ai.gemini_provider import GeminiDocumentAIProvider
from app.integrations.ai.mock_provider import MockDocumentAIProvider


def get_ai_provider():
    if AI_PROVIDER == "mock":
        return MockDocumentAIProvider()

    if AI_PROVIDER == "gemini":
        return GeminiDocumentAIProvider()

    raise ValueError(
        f"Unsupported AI provider: {AI_PROVIDER}"
    )