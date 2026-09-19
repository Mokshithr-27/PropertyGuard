from typing import Any

from app.rules.context import EvidenceContext
from app.rules.exceptions import InvalidRuleError, UnsupportedOperatorError
from app.rules.results import EvaluationResult
from app.rules.types import EvaluationOperator, EvaluationOutcome


class RuleEvaluator:
    """Deterministic evaluator for controlled rule definitions."""

    def evaluate(
        self,
        evaluation_logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        if not evaluation_logic:
            raise InvalidRuleError("evaluation_logic is required")

        operator_value = evaluation_logic.get("type")

        if not operator_value:
            raise InvalidRuleError(
                "evaluation_logic.type is required"
            )

        try:
            operator = EvaluationOperator(operator_value)
        except ValueError as exc:
            raise UnsupportedOperatorError(
                f"Unsupported evaluation operator: {operator_value}"
            ) from exc

        if operator == EvaluationOperator.DOCUMENT_EXISTS:
            return self._document_exists(
                evaluation_logic,
                context,
            )

        if operator == EvaluationOperator.FIELD_EXISTS:
            return self._field_exists(
                evaluation_logic,
                context,
            )

        if operator == EvaluationOperator.FIELD_EQUALS:
            return self._field_equals(
                evaluation_logic,
                context,
            )

        if operator == EvaluationOperator.FIELD_NOT_EQUALS:
            return self._field_not_equals(
                evaluation_logic,
                context,
            )

        if operator == EvaluationOperator.FIELD_MIN:
            return self._field_min(
                evaluation_logic,
                context,
            )

        if operator == EvaluationOperator.FIELD_MAX:
            return self._field_max(
                evaluation_logic,
                context,
            )

        if operator == EvaluationOperator.FIELD_RANGE:
            return self._field_range(
                evaluation_logic,
                context,
            )

        raise UnsupportedOperatorError(
            f"Unsupported evaluation operator: {operator}"
        )

    @staticmethod
    def _document_exists(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        document_type = logic.get("document_type")

        if not document_type:
            raise InvalidRuleError(
                "DOCUMENT_EXISTS requires document_type"
            )

        matching = [
            document
            for document in context.documents
            if document.document_type == document_type
        ]

        if not matching:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=(
                    f"Required document '{document_type}' "
                    "was not found."
                ),
            )

        required_status = logic.get("required_status")

        if required_status is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.PASS,
                explanation=(
                    f"Document '{document_type}' exists."
                ),
                evidence={
                    "document_count": len(matching),
                },
            )

        valid_documents = [
            document
            for document in matching
            if document.status == required_status
        ]

        if valid_documents:
            return EvaluationResult(
                outcome=EvaluationOutcome.PASS,
                explanation=(
                    f"Document '{document_type}' exists "
                    f"with status '{required_status}'."
                ),
                evidence={
                    "document_count": len(valid_documents),
                    "required_status": required_status,
                },
            )

        return EvaluationResult(
            outcome=EvaluationOutcome.FAIL,
            explanation=(
                f"Document '{document_type}' exists, but none "
                f"has required status '{required_status}'."
            ),
            evidence={
                "document_count": len(matching),
                "required_status": required_status,
            },
        )

    @staticmethod
    def _field_exists(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field_name = logic.get("field")

        if not field_name:
            raise InvalidRuleError(
                "FIELD_EXISTS requires field"
            )

        if field_name not in context.fields:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=(
                    f"Required field '{field_name}' "
                    "is missing."
                ),
            )

        if context.fields[field_name] is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=(
                    f"Required field '{field_name}' "
                    "has no value."
                ),
            )

        return EvaluationResult(
            outcome=EvaluationOutcome.PASS,
            explanation=f"Field '{field_name}' exists.",
            evidence={
                "field": field_name,
                "value": context.fields[field_name],
            },
        )

    @staticmethod
    def _get_field(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> tuple[str, Any] | None:
        field_name = logic.get("field")

        if not field_name:
            raise InvalidRuleError(
                "Field operator requires field"
            )

        if field_name not in context.fields:
            return None

        value = context.fields[field_name]

        if value is None:
            return None

        return field_name, value

    @classmethod
    def _field_equals(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_EQUALS requires value"
            )

        expected = logic["value"]

        if actual == expected:
            outcome = EvaluationOutcome.PASS
            explanation = (
                f"Field '{field_name}' equals expected value."
            )
        else:
            outcome = EvaluationOutcome.FAIL
            explanation = (
                f"Field '{field_name}' does not equal "
                "expected value."
            )

        return EvaluationResult(
            outcome=outcome,
            explanation=explanation,
            evidence={
                "field": field_name,
                "actual": actual,
                "expected": expected,
            },
        )

    @classmethod
    def _field_not_equals(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_NOT_EQUALS requires value"
            )

        expected = logic["value"]

        if actual != expected:
            outcome = EvaluationOutcome.PASS
            explanation = (
                f"Field '{field_name}' differs from "
                "forbidden value."
            )
        else:
            outcome = EvaluationOutcome.FAIL
            explanation = (
                f"Field '{field_name}' equals the "
                "forbidden value."
            )

        return EvaluationResult(
            outcome=outcome,
            explanation=explanation,
            evidence={
                "field": field_name,
                "actual": actual,
                "expected": expected,
            },
        )

    @classmethod
    def _field_min(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_MIN requires value"
            )

        minimum = logic["value"]

        if actual >= minimum:
            outcome = EvaluationOutcome.PASS
            explanation = (
                f"Field '{field_name}' satisfies minimum "
                f"value {minimum}."
            )
        else:
            outcome = EvaluationOutcome.FAIL
            explanation = (
                f"Field '{field_name}' is below minimum "
                f"value {minimum}."
            )

        return EvaluationResult(
            outcome=outcome,
            explanation=explanation,
            evidence={
                "field": field_name,
                "actual": actual,
                "minimum": minimum,
            },
        )

    @classmethod
    def _field_max(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_MAX requires value"
            )

        maximum = logic["value"]

        if actual <= maximum:
            outcome = EvaluationOutcome.PASS
            explanation = (
                f"Field '{field_name}' satisfies maximum "
                f"value {maximum}."
            )
        else:
            outcome = EvaluationOutcome.FAIL
            explanation = (
                f"Field '{field_name}' exceeds maximum "
                f"value {maximum}."
            )

        return EvaluationResult(
            outcome=outcome,
            explanation=explanation,
            evidence={
                "field": field_name,
                "actual": actual,
                "maximum": maximum,
            },
        )

    @classmethod
    def _field_range(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field

        if "minimum" not in logic or "maximum" not in logic:
            raise InvalidRuleError(
                "FIELD_RANGE requires minimum and maximum"
            )

        minimum = logic["minimum"]
        maximum = logic["maximum"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )

        if minimum <= actual <= maximum:
            outcome = EvaluationOutcome.PASS
            explanation = (
                f"Field '{field_name}' is within the "
                f"allowed range {minimum}–{maximum}."
            )
        else:
            outcome = EvaluationOutcome.FAIL
            explanation = (
                f"Field '{field_name}' is outside the "
                f"allowed range {minimum}–{maximum}."
            )

        return EvaluationResult(
            outcome=outcome,
            explanation=explanation,
            evidence={
                "field": field_name,
                "actual": actual,
                "minimum": minimum,
                "maximum": maximum,
            },
        )