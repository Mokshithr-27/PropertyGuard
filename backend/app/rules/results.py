from dataclasses import dataclass
from typing import Any

from app.rules.types import EvaluationOutcome


@dataclass(frozen=True)
class EvaluationResult:
    outcome: EvaluationOutcome
    explanation: str
    evidence: dict[str, Any] | None = None
    dependency_affected: bool = False