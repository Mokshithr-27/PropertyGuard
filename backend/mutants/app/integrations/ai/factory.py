"""
PropertyGuard AI Provider Factory
----------------------------------
Instantiates the configured DocumentAIProvider implementation ('mock' or 'gemini')
based on environment configuration settings.
"""

from app.core.config import AI_PROVIDER
from app.integrations.ai.gemini_provider import GeminiDocumentAIProvider
from app.integrations.ai.mock_provider import MockDocumentAIProvider


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_ai_provider__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_ai_provider__mutmut)
def get_ai_provider():
    if AI_PROVIDER == "mock":
        return MockDocumentAIProvider()

    if AI_PROVIDER == "gemini":
        return GeminiDocumentAIProvider()

    raise ValueError(
        f"Unsupported AI provider: {AI_PROVIDER}"
    )


def x_get_ai_provider__mutmut_orig():
    if AI_PROVIDER == "mock":
        return MockDocumentAIProvider()

    if AI_PROVIDER == "gemini":
        return GeminiDocumentAIProvider()

    raise ValueError(
        f"Unsupported AI provider: {AI_PROVIDER}"
    )


def x_get_ai_provider__mutmut_1():
    if AI_PROVIDER != "mock":
        return MockDocumentAIProvider()

    if AI_PROVIDER == "gemini":
        return GeminiDocumentAIProvider()

    raise ValueError(
        f"Unsupported AI provider: {AI_PROVIDER}"
    )


def x_get_ai_provider__mutmut_2():
    if AI_PROVIDER == "XXmockXX":
        return MockDocumentAIProvider()

    if AI_PROVIDER == "gemini":
        return GeminiDocumentAIProvider()

    raise ValueError(
        f"Unsupported AI provider: {AI_PROVIDER}"
    )


def x_get_ai_provider__mutmut_3():
    if AI_PROVIDER == "MOCK":
        return MockDocumentAIProvider()

    if AI_PROVIDER == "gemini":
        return GeminiDocumentAIProvider()

    raise ValueError(
        f"Unsupported AI provider: {AI_PROVIDER}"
    )


def x_get_ai_provider__mutmut_4():
    if AI_PROVIDER == "mock":
        return MockDocumentAIProvider()

    if AI_PROVIDER != "gemini":
        return GeminiDocumentAIProvider()

    raise ValueError(
        f"Unsupported AI provider: {AI_PROVIDER}"
    )


def x_get_ai_provider__mutmut_5():
    if AI_PROVIDER == "mock":
        return MockDocumentAIProvider()

    if AI_PROVIDER == "XXgeminiXX":
        return GeminiDocumentAIProvider()

    raise ValueError(
        f"Unsupported AI provider: {AI_PROVIDER}"
    )


def x_get_ai_provider__mutmut_6():
    if AI_PROVIDER == "mock":
        return MockDocumentAIProvider()

    if AI_PROVIDER == "GEMINI":
        return GeminiDocumentAIProvider()

    raise ValueError(
        f"Unsupported AI provider: {AI_PROVIDER}"
    )


def x_get_ai_provider__mutmut_7():
    if AI_PROVIDER == "mock":
        return MockDocumentAIProvider()

    if AI_PROVIDER == "gemini":
        return GeminiDocumentAIProvider()

    raise ValueError(
        None
    )

mutants_x_get_ai_provider__mutmut['_mutmut_orig'] = x_get_ai_provider__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_ai_provider__mutmut['x_get_ai_provider__mutmut_1'] = x_get_ai_provider__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_ai_provider__mutmut['x_get_ai_provider__mutmut_2'] = x_get_ai_provider__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_ai_provider__mutmut['x_get_ai_provider__mutmut_3'] = x_get_ai_provider__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_ai_provider__mutmut['x_get_ai_provider__mutmut_4'] = x_get_ai_provider__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_ai_provider__mutmut['x_get_ai_provider__mutmut_5'] = x_get_ai_provider__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_ai_provider__mutmut['x_get_ai_provider__mutmut_6'] = x_get_ai_provider__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_ai_provider__mutmut['x_get_ai_provider__mutmut_7'] = x_get_ai_provider__mutmut_7 # type: ignore # mutmut generated