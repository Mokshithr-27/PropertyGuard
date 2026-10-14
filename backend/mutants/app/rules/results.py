"""
PropertyGuard Rule Evaluation Result Dataclass
----------------------------------------------
Defines the EvaluationResult dataclass capturing evaluation outcomes (PASS, FAIL,
NEEDS_REVIEW, NOT_APPLICABLE), human-readable explanations, and evidence maps.
"""

from dataclasses import dataclass
from typing import Any

from app.rules.types import EvaluationOutcome


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class EvaluationResult:
    outcome: EvaluationOutcome
    explanation: str
    evidence: dict[str, Any] | None = None
    dependency_affected: bool = False