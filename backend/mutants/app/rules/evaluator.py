"""
PropertyGuard Deterministic Rule Evaluator Engine
-------------------------------------------------
Executes deterministic compliance evaluation against property evidence contexts.
Supports operators: DOCUMENT_EXISTS, DOCUMENT_NOT_EXPIRED, FIELD_EQUALS, FIELD_EXISTS,
FIELD_IN, NUMERIC_COMPARISON, LOGICAL_AND, LOGICAL_OR, and LOGICAL_NOT.
"""

from typing import Any

from app.rules.context import EvidenceContext
from app.rules.exceptions import InvalidRuleError, UnsupportedOperatorError
from app.rules.results import EvaluationResult
from app.rules.types import EvaluationOperator, EvaluationOutcome


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁRuleEvaluatorǁevaluate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuleEvaluatorǁ_get_field__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuleEvaluatorǁ_field_min__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuleEvaluatorǁ_field_max__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuleEvaluatorǁ_field_range__mutmut: MutantDict = {}  # type: ignore


class RuleEvaluator:
    """Deterministic evaluator for controlled rule definitions."""

    @_mutmut_mutated(mutants_xǁRuleEvaluatorǁevaluate__mutmut)
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

    def xǁRuleEvaluatorǁevaluate__mutmut_orig(
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

    def xǁRuleEvaluatorǁevaluate__mutmut_1(
        self,
        evaluation_logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        if evaluation_logic:
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

    def xǁRuleEvaluatorǁevaluate__mutmut_2(
        self,
        evaluation_logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        if not evaluation_logic:
            raise InvalidRuleError(None)

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

    def xǁRuleEvaluatorǁevaluate__mutmut_3(
        self,
        evaluation_logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        if not evaluation_logic:
            raise InvalidRuleError("XXevaluation_logic is requiredXX")

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

    def xǁRuleEvaluatorǁevaluate__mutmut_4(
        self,
        evaluation_logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        if not evaluation_logic:
            raise InvalidRuleError("EVALUATION_LOGIC IS REQUIRED")

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

    def xǁRuleEvaluatorǁevaluate__mutmut_5(
        self,
        evaluation_logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        if not evaluation_logic:
            raise InvalidRuleError("evaluation_logic is required")

        operator_value = None

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

    def xǁRuleEvaluatorǁevaluate__mutmut_6(
        self,
        evaluation_logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        if not evaluation_logic:
            raise InvalidRuleError("evaluation_logic is required")

        operator_value = evaluation_logic.get(None)

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

    def xǁRuleEvaluatorǁevaluate__mutmut_7(
        self,
        evaluation_logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        if not evaluation_logic:
            raise InvalidRuleError("evaluation_logic is required")

        operator_value = evaluation_logic.get("XXtypeXX")

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

    def xǁRuleEvaluatorǁevaluate__mutmut_8(
        self,
        evaluation_logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        if not evaluation_logic:
            raise InvalidRuleError("evaluation_logic is required")

        operator_value = evaluation_logic.get("TYPE")

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

    def xǁRuleEvaluatorǁevaluate__mutmut_9(
        self,
        evaluation_logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        if not evaluation_logic:
            raise InvalidRuleError("evaluation_logic is required")

        operator_value = evaluation_logic.get("type")

        if operator_value:
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

    def xǁRuleEvaluatorǁevaluate__mutmut_10(
        self,
        evaluation_logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        if not evaluation_logic:
            raise InvalidRuleError("evaluation_logic is required")

        operator_value = evaluation_logic.get("type")

        if not operator_value:
            raise InvalidRuleError(
                None
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

    def xǁRuleEvaluatorǁevaluate__mutmut_11(
        self,
        evaluation_logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        if not evaluation_logic:
            raise InvalidRuleError("evaluation_logic is required")

        operator_value = evaluation_logic.get("type")

        if not operator_value:
            raise InvalidRuleError(
                "XXevaluation_logic.type is requiredXX"
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

    def xǁRuleEvaluatorǁevaluate__mutmut_12(
        self,
        evaluation_logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        if not evaluation_logic:
            raise InvalidRuleError("evaluation_logic is required")

        operator_value = evaluation_logic.get("type")

        if not operator_value:
            raise InvalidRuleError(
                "EVALUATION_LOGIC.TYPE IS REQUIRED"
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

    def xǁRuleEvaluatorǁevaluate__mutmut_13(
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
            operator = None
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

    def xǁRuleEvaluatorǁevaluate__mutmut_14(
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
            operator = EvaluationOperator(None)
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

    def xǁRuleEvaluatorǁevaluate__mutmut_15(
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
                None
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

    def xǁRuleEvaluatorǁevaluate__mutmut_16(
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

        if operator != EvaluationOperator.DOCUMENT_EXISTS:
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

    def xǁRuleEvaluatorǁevaluate__mutmut_17(
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
                None,
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

    def xǁRuleEvaluatorǁevaluate__mutmut_18(
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
                None,
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

    def xǁRuleEvaluatorǁevaluate__mutmut_19(
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

    def xǁRuleEvaluatorǁevaluate__mutmut_20(
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

    def xǁRuleEvaluatorǁevaluate__mutmut_21(
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

        if operator != EvaluationOperator.FIELD_EXISTS:
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

    def xǁRuleEvaluatorǁevaluate__mutmut_22(
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
                None,
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

    def xǁRuleEvaluatorǁevaluate__mutmut_23(
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
                None,
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

    def xǁRuleEvaluatorǁevaluate__mutmut_24(
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

    def xǁRuleEvaluatorǁevaluate__mutmut_25(
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

    def xǁRuleEvaluatorǁevaluate__mutmut_26(
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

        if operator != EvaluationOperator.FIELD_EQUALS:
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

    def xǁRuleEvaluatorǁevaluate__mutmut_27(
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
                None,
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

    def xǁRuleEvaluatorǁevaluate__mutmut_28(
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
                None,
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

    def xǁRuleEvaluatorǁevaluate__mutmut_29(
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

    def xǁRuleEvaluatorǁevaluate__mutmut_30(
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

    def xǁRuleEvaluatorǁevaluate__mutmut_31(
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

        if operator != EvaluationOperator.FIELD_NOT_EQUALS:
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

    def xǁRuleEvaluatorǁevaluate__mutmut_32(
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
                None,
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

    def xǁRuleEvaluatorǁevaluate__mutmut_33(
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
                None,
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

    def xǁRuleEvaluatorǁevaluate__mutmut_34(
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

    def xǁRuleEvaluatorǁevaluate__mutmut_35(
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

    def xǁRuleEvaluatorǁevaluate__mutmut_36(
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

        if operator != EvaluationOperator.FIELD_MIN:
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

    def xǁRuleEvaluatorǁevaluate__mutmut_37(
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
                None,
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

    def xǁRuleEvaluatorǁevaluate__mutmut_38(
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
                None,
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

    def xǁRuleEvaluatorǁevaluate__mutmut_39(
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

    def xǁRuleEvaluatorǁevaluate__mutmut_40(
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

    def xǁRuleEvaluatorǁevaluate__mutmut_41(
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

        if operator != EvaluationOperator.FIELD_MAX:
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

    def xǁRuleEvaluatorǁevaluate__mutmut_42(
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
                None,
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

    def xǁRuleEvaluatorǁevaluate__mutmut_43(
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
                None,
            )

        if operator == EvaluationOperator.FIELD_RANGE:
            return self._field_range(
                evaluation_logic,
                context,
            )

        raise UnsupportedOperatorError(
            f"Unsupported evaluation operator: {operator}"
        )

    def xǁRuleEvaluatorǁevaluate__mutmut_44(
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

    def xǁRuleEvaluatorǁevaluate__mutmut_45(
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
                )

        if operator == EvaluationOperator.FIELD_RANGE:
            return self._field_range(
                evaluation_logic,
                context,
            )

        raise UnsupportedOperatorError(
            f"Unsupported evaluation operator: {operator}"
        )

    def xǁRuleEvaluatorǁevaluate__mutmut_46(
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

        if operator != EvaluationOperator.FIELD_RANGE:
            return self._field_range(
                evaluation_logic,
                context,
            )

        raise UnsupportedOperatorError(
            f"Unsupported evaluation operator: {operator}"
        )

    def xǁRuleEvaluatorǁevaluate__mutmut_47(
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
                None,
                context,
            )

        raise UnsupportedOperatorError(
            f"Unsupported evaluation operator: {operator}"
        )

    def xǁRuleEvaluatorǁevaluate__mutmut_48(
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
                None,
            )

        raise UnsupportedOperatorError(
            f"Unsupported evaluation operator: {operator}"
        )

    def xǁRuleEvaluatorǁevaluate__mutmut_49(
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
                context,
            )

        raise UnsupportedOperatorError(
            f"Unsupported evaluation operator: {operator}"
        )

    def xǁRuleEvaluatorǁevaluate__mutmut_50(
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
                )

        raise UnsupportedOperatorError(
            f"Unsupported evaluation operator: {operator}"
        )

    def xǁRuleEvaluatorǁevaluate__mutmut_51(
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
            None
        )

    @staticmethod
    @_mutmut_mutated(mutants_xǁRuleEvaluatorǁ_document_exists__mutmut)
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_orig(
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_1(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        document_type = None

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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_2(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        document_type = logic.get(None)

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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_3(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        document_type = logic.get("XXdocument_typeXX")

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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_4(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        document_type = logic.get("DOCUMENT_TYPE")

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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_5(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        document_type = logic.get("document_type")

        if document_type:
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_6(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        document_type = logic.get("document_type")

        if not document_type:
            raise InvalidRuleError(
                None
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_7(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        document_type = logic.get("document_type")

        if not document_type:
            raise InvalidRuleError(
                "XXDOCUMENT_EXISTS requires document_typeXX"
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_8(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        document_type = logic.get("document_type")

        if not document_type:
            raise InvalidRuleError(
                "document_exists requires document_type"
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_9(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        document_type = logic.get("document_type")

        if not document_type:
            raise InvalidRuleError(
                "DOCUMENT_EXISTS REQUIRES DOCUMENT_TYPE"
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_10(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        document_type = logic.get("document_type")

        if not document_type:
            raise InvalidRuleError(
                "DOCUMENT_EXISTS requires document_type"
            )

        matching = None

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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_11(
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
            if document.document_type != document_type
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_12(
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

        if matching:
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_13(
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
                outcome=None,
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_14(
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
                explanation=None,
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_15(
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_16(
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_17(
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
                    "XXwas not found.XX"
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_18(
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
                    "WAS NOT FOUND."
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_19(
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

        required_status = None

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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_20(
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

        required_status = logic.get(None)

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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_21(
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

        required_status = logic.get("XXrequired_statusXX")

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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_22(
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

        required_status = logic.get("REQUIRED_STATUS")

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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_23(
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

        if required_status is not None:
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_24(
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
                outcome=None,
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_25(
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
                explanation=None,
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_26(
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
                evidence=None,
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_27(
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_28(
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_29(
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_30(
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
                    "XXdocument_countXX": len(matching),
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_31(
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
                    "DOCUMENT_COUNT": len(matching),
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_32(
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

        valid_documents = None

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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_33(
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
            if document.status != required_status
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_34(
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
                outcome=None,
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_35(
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
                explanation=None,
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_36(
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
                evidence=None,
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_37(
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_38(
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_39(
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_40(
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
                    "XXdocument_countXX": len(valid_documents),
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_41(
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
                    "DOCUMENT_COUNT": len(valid_documents),
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_42(
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
                    "XXrequired_statusXX": required_status,
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_43(
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
                    "REQUIRED_STATUS": required_status,
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_44(
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
            outcome=None,
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_45(
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
            explanation=None,
            evidence={
                "document_count": len(matching),
                "required_status": required_status,
            },
        )

    @staticmethod
    def xǁRuleEvaluatorǁ_document_exists__mutmut_46(
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
            evidence=None,
        )

    @staticmethod
    def xǁRuleEvaluatorǁ_document_exists__mutmut_47(
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
    def xǁRuleEvaluatorǁ_document_exists__mutmut_48(
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
            evidence={
                "document_count": len(matching),
                "required_status": required_status,
            },
        )

    @staticmethod
    def xǁRuleEvaluatorǁ_document_exists__mutmut_49(
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
            )

    @staticmethod
    def xǁRuleEvaluatorǁ_document_exists__mutmut_50(
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
                "XXdocument_countXX": len(matching),
                "required_status": required_status,
            },
        )

    @staticmethod
    def xǁRuleEvaluatorǁ_document_exists__mutmut_51(
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
                "DOCUMENT_COUNT": len(matching),
                "required_status": required_status,
            },
        )

    @staticmethod
    def xǁRuleEvaluatorǁ_document_exists__mutmut_52(
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
                "XXrequired_statusXX": required_status,
            },
        )

    @staticmethod
    def xǁRuleEvaluatorǁ_document_exists__mutmut_53(
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
                "REQUIRED_STATUS": required_status,
            },
        )

    @staticmethod
    @_mutmut_mutated(mutants_xǁRuleEvaluatorǁ_field_exists__mutmut)
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_orig(
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_1(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field_name = None

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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_2(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field_name = logic.get(None)

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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_3(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field_name = logic.get("XXfieldXX")

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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_4(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field_name = logic.get("FIELD")

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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_5(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field_name = logic.get("field")

        if field_name:
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_6(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field_name = logic.get("field")

        if not field_name:
            raise InvalidRuleError(
                None
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_7(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field_name = logic.get("field")

        if not field_name:
            raise InvalidRuleError(
                "XXFIELD_EXISTS requires fieldXX"
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_8(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field_name = logic.get("field")

        if not field_name:
            raise InvalidRuleError(
                "field_exists requires field"
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_9(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field_name = logic.get("field")

        if not field_name:
            raise InvalidRuleError(
                "FIELD_EXISTS REQUIRES FIELD"
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_10(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field_name = logic.get("field")

        if not field_name:
            raise InvalidRuleError(
                "FIELD_EXISTS requires field"
            )

        if field_name in context.fields:
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_11(
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
                outcome=None,
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_12(
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
                explanation=None,
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_13(
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_14(
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_15(
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
                    "XXis missing.XX"
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_16(
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
                    "IS MISSING."
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_17(
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

        if context.fields[field_name] is not None:
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_18(
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
                outcome=None,
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_19(
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
                explanation=None,
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_20(
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_21(
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_22(
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
                    "XXhas no value.XX"
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_23(
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
                    "HAS NO VALUE."
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
    def xǁRuleEvaluatorǁ_field_exists__mutmut_24(
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
            outcome=None,
            explanation=f"Field '{field_name}' exists.",
            evidence={
                "field": field_name,
                "value": context.fields[field_name],
            },
        )

    @staticmethod
    def xǁRuleEvaluatorǁ_field_exists__mutmut_25(
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
            explanation=None,
            evidence={
                "field": field_name,
                "value": context.fields[field_name],
            },
        )

    @staticmethod
    def xǁRuleEvaluatorǁ_field_exists__mutmut_26(
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
            evidence=None,
        )

    @staticmethod
    def xǁRuleEvaluatorǁ_field_exists__mutmut_27(
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
            explanation=f"Field '{field_name}' exists.",
            evidence={
                "field": field_name,
                "value": context.fields[field_name],
            },
        )

    @staticmethod
    def xǁRuleEvaluatorǁ_field_exists__mutmut_28(
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
            evidence={
                "field": field_name,
                "value": context.fields[field_name],
            },
        )

    @staticmethod
    def xǁRuleEvaluatorǁ_field_exists__mutmut_29(
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
            )

    @staticmethod
    def xǁRuleEvaluatorǁ_field_exists__mutmut_30(
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
                "XXfieldXX": field_name,
                "value": context.fields[field_name],
            },
        )

    @staticmethod
    def xǁRuleEvaluatorǁ_field_exists__mutmut_31(
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
                "FIELD": field_name,
                "value": context.fields[field_name],
            },
        )

    @staticmethod
    def xǁRuleEvaluatorǁ_field_exists__mutmut_32(
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
                "XXvalueXX": context.fields[field_name],
            },
        )

    @staticmethod
    def xǁRuleEvaluatorǁ_field_exists__mutmut_33(
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
                "VALUE": context.fields[field_name],
            },
        )

    @staticmethod
    @_mutmut_mutated(mutants_xǁRuleEvaluatorǁ_get_field__mutmut)
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

    @staticmethod
    def xǁRuleEvaluatorǁ_get_field__mutmut_orig(
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

    @staticmethod
    def xǁRuleEvaluatorǁ_get_field__mutmut_1(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> tuple[str, Any] | None:
        field_name = None

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

    @staticmethod
    def xǁRuleEvaluatorǁ_get_field__mutmut_2(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> tuple[str, Any] | None:
        field_name = logic.get(None)

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

    @staticmethod
    def xǁRuleEvaluatorǁ_get_field__mutmut_3(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> tuple[str, Any] | None:
        field_name = logic.get("XXfieldXX")

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

    @staticmethod
    def xǁRuleEvaluatorǁ_get_field__mutmut_4(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> tuple[str, Any] | None:
        field_name = logic.get("FIELD")

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

    @staticmethod
    def xǁRuleEvaluatorǁ_get_field__mutmut_5(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> tuple[str, Any] | None:
        field_name = logic.get("field")

        if field_name:
            raise InvalidRuleError(
                "Field operator requires field"
            )

        if field_name not in context.fields:
            return None

        value = context.fields[field_name]

        if value is None:
            return None

        return field_name, value

    @staticmethod
    def xǁRuleEvaluatorǁ_get_field__mutmut_6(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> tuple[str, Any] | None:
        field_name = logic.get("field")

        if not field_name:
            raise InvalidRuleError(
                None
            )

        if field_name not in context.fields:
            return None

        value = context.fields[field_name]

        if value is None:
            return None

        return field_name, value

    @staticmethod
    def xǁRuleEvaluatorǁ_get_field__mutmut_7(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> tuple[str, Any] | None:
        field_name = logic.get("field")

        if not field_name:
            raise InvalidRuleError(
                "XXField operator requires fieldXX"
            )

        if field_name not in context.fields:
            return None

        value = context.fields[field_name]

        if value is None:
            return None

        return field_name, value

    @staticmethod
    def xǁRuleEvaluatorǁ_get_field__mutmut_8(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> tuple[str, Any] | None:
        field_name = logic.get("field")

        if not field_name:
            raise InvalidRuleError(
                "field operator requires field"
            )

        if field_name not in context.fields:
            return None

        value = context.fields[field_name]

        if value is None:
            return None

        return field_name, value

    @staticmethod
    def xǁRuleEvaluatorǁ_get_field__mutmut_9(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> tuple[str, Any] | None:
        field_name = logic.get("field")

        if not field_name:
            raise InvalidRuleError(
                "FIELD OPERATOR REQUIRES FIELD"
            )

        if field_name not in context.fields:
            return None

        value = context.fields[field_name]

        if value is None:
            return None

        return field_name, value

    @staticmethod
    def xǁRuleEvaluatorǁ_get_field__mutmut_10(
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> tuple[str, Any] | None:
        field_name = logic.get("field")

        if not field_name:
            raise InvalidRuleError(
                "Field operator requires field"
            )

        if field_name in context.fields:
            return None

        value = context.fields[field_name]

        if value is None:
            return None

        return field_name, value

    @staticmethod
    def xǁRuleEvaluatorǁ_get_field__mutmut_11(
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

        value = None

        if value is None:
            return None

        return field_name, value

    @staticmethod
    def xǁRuleEvaluatorǁ_get_field__mutmut_12(
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

        if value is not None:
            return None

        return field_name, value

    @classmethod
    @_mutmut_mutated(mutants_xǁRuleEvaluatorǁ_field_equals__mutmut, is_classmethod = True)
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_orig(
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_1(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = None

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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_2(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(None, context)

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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_3(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, None)

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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_4(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(context)

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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_5(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, )

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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_6(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is not None:
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_7(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=None,
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_8(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=None,
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_9(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_10(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_11(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="XXRequired field value is missing.XX",
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_12(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="required field value is missing.",
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_13(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="REQUIRED FIELD VALUE IS MISSING.",
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_14(
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

        field_name, actual = None

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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_15(
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

        if "XXvalueXX" not in logic:
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_16(
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

        if "VALUE" not in logic:
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_17(
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

        if "value" in logic:
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_18(
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
                None
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_19(
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
                "XXFIELD_EQUALS requires valueXX"
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_20(
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
                "field_equals requires value"
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_21(
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
                "FIELD_EQUALS REQUIRES VALUE"
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_22(
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

        expected = None

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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_23(
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

        expected = logic["XXvalueXX"]

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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_24(
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

        expected = logic["VALUE"]

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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_25(
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

        if actual != expected:
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_26(
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
            outcome = None
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_27(
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
            explanation = None
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_28(
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
            outcome = None
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_29(
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
            explanation = None

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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_30(
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
                "XXexpected value.XX"
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_31(
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
                "EXPECTED VALUE."
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
    def xǁRuleEvaluatorǁ_field_equals__mutmut_32(
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
            outcome=None,
            explanation=explanation,
            evidence={
                "field": field_name,
                "actual": actual,
                "expected": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_equals__mutmut_33(
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
            explanation=None,
            evidence={
                "field": field_name,
                "actual": actual,
                "expected": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_equals__mutmut_34(
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
            evidence=None,
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_equals__mutmut_35(
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
            explanation=explanation,
            evidence={
                "field": field_name,
                "actual": actual,
                "expected": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_equals__mutmut_36(
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
            evidence={
                "field": field_name,
                "actual": actual,
                "expected": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_equals__mutmut_37(
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
            )

    @classmethod
    def xǁRuleEvaluatorǁ_field_equals__mutmut_38(
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
                "XXfieldXX": field_name,
                "actual": actual,
                "expected": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_equals__mutmut_39(
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
                "FIELD": field_name,
                "actual": actual,
                "expected": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_equals__mutmut_40(
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
                "XXactualXX": actual,
                "expected": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_equals__mutmut_41(
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
                "ACTUAL": actual,
                "expected": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_equals__mutmut_42(
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
                "XXexpectedXX": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_equals__mutmut_43(
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
                "EXPECTED": expected,
            },
        )

    @classmethod
    @_mutmut_mutated(mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut, is_classmethod = True)
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_orig(
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_1(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = None

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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_2(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(None, context)

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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_3(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, None)

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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_4(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(context)

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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_5(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, )

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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_6(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is not None:
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_7(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=None,
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_8(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=None,
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_9(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_10(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_11(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="XXRequired field value is missing.XX",
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_12(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="required field value is missing.",
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_13(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="REQUIRED FIELD VALUE IS MISSING.",
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_14(
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

        field_name, actual = None

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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_15(
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

        if "XXvalueXX" not in logic:
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_16(
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

        if "VALUE" not in logic:
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_17(
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

        if "value" in logic:
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_18(
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
                None
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_19(
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
                "XXFIELD_NOT_EQUALS requires valueXX"
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_20(
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
                "field_not_equals requires value"
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_21(
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
                "FIELD_NOT_EQUALS REQUIRES VALUE"
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_22(
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

        expected = None

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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_23(
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

        expected = logic["XXvalueXX"]

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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_24(
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

        expected = logic["VALUE"]

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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_25(
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

        if actual == expected:
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_26(
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
            outcome = None
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_27(
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
            explanation = None
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_28(
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
                "XXforbidden value.XX"
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_29(
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
                "FORBIDDEN VALUE."
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_30(
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
            outcome = None
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_31(
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
            explanation = None

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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_32(
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
                "XXforbidden value.XX"
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_33(
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
                "FORBIDDEN VALUE."
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
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_34(
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
            outcome=None,
            explanation=explanation,
            evidence={
                "field": field_name,
                "actual": actual,
                "expected": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_35(
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
            explanation=None,
            evidence={
                "field": field_name,
                "actual": actual,
                "expected": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_36(
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
            evidence=None,
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_37(
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
            explanation=explanation,
            evidence={
                "field": field_name,
                "actual": actual,
                "expected": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_38(
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
            evidence={
                "field": field_name,
                "actual": actual,
                "expected": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_39(
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
            )

    @classmethod
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_40(
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
                "XXfieldXX": field_name,
                "actual": actual,
                "expected": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_41(
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
                "FIELD": field_name,
                "actual": actual,
                "expected": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_42(
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
                "XXactualXX": actual,
                "expected": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_43(
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
                "ACTUAL": actual,
                "expected": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_44(
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
                "XXexpectedXX": expected,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_not_equals__mutmut_45(
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
                "EXPECTED": expected,
            },
        )

    @staticmethod
    @_mutmut_mutated(mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut)
    def _numeric_value_or_review(
        field_name: str,
        actual: Any,
    ) -> EvaluationResult | None:
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=(
                    f"Field '{field_name}' contains an invalid "
                    "numeric value."
                ),
                evidence={
                    "field": field_name,
                    "actual": actual,
                },
            )
        return None

    @staticmethod
    def xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_orig(
        field_name: str,
        actual: Any,
    ) -> EvaluationResult | None:
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=(
                    f"Field '{field_name}' contains an invalid "
                    "numeric value."
                ),
                evidence={
                    "field": field_name,
                    "actual": actual,
                },
            )
        return None

    @staticmethod
    def xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_1(
        field_name: str,
        actual: Any,
    ) -> EvaluationResult | None:
        if not isinstance(actual, (int, float)) and isinstance(actual, bool):
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=(
                    f"Field '{field_name}' contains an invalid "
                    "numeric value."
                ),
                evidence={
                    "field": field_name,
                    "actual": actual,
                },
            )
        return None

    @staticmethod
    def xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_2(
        field_name: str,
        actual: Any,
    ) -> EvaluationResult | None:
        if isinstance(actual, (int, float)) or isinstance(actual, bool):
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=(
                    f"Field '{field_name}' contains an invalid "
                    "numeric value."
                ),
                evidence={
                    "field": field_name,
                    "actual": actual,
                },
            )
        return None

    @staticmethod
    def xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_3(
        field_name: str,
        actual: Any,
    ) -> EvaluationResult | None:
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            return EvaluationResult(
                outcome=None,
                explanation=(
                    f"Field '{field_name}' contains an invalid "
                    "numeric value."
                ),
                evidence={
                    "field": field_name,
                    "actual": actual,
                },
            )
        return None

    @staticmethod
    def xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_4(
        field_name: str,
        actual: Any,
    ) -> EvaluationResult | None:
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=None,
                evidence={
                    "field": field_name,
                    "actual": actual,
                },
            )
        return None

    @staticmethod
    def xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_5(
        field_name: str,
        actual: Any,
    ) -> EvaluationResult | None:
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=(
                    f"Field '{field_name}' contains an invalid "
                    "numeric value."
                ),
                evidence=None,
            )
        return None

    @staticmethod
    def xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_6(
        field_name: str,
        actual: Any,
    ) -> EvaluationResult | None:
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            return EvaluationResult(
                explanation=(
                    f"Field '{field_name}' contains an invalid "
                    "numeric value."
                ),
                evidence={
                    "field": field_name,
                    "actual": actual,
                },
            )
        return None

    @staticmethod
    def xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_7(
        field_name: str,
        actual: Any,
    ) -> EvaluationResult | None:
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                evidence={
                    "field": field_name,
                    "actual": actual,
                },
            )
        return None

    @staticmethod
    def xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_8(
        field_name: str,
        actual: Any,
    ) -> EvaluationResult | None:
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=(
                    f"Field '{field_name}' contains an invalid "
                    "numeric value."
                ),
                )
        return None

    @staticmethod
    def xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_9(
        field_name: str,
        actual: Any,
    ) -> EvaluationResult | None:
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=(
                    f"Field '{field_name}' contains an invalid "
                    "XXnumeric value.XX"
                ),
                evidence={
                    "field": field_name,
                    "actual": actual,
                },
            )
        return None

    @staticmethod
    def xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_10(
        field_name: str,
        actual: Any,
    ) -> EvaluationResult | None:
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=(
                    f"Field '{field_name}' contains an invalid "
                    "NUMERIC VALUE."
                ),
                evidence={
                    "field": field_name,
                    "actual": actual,
                },
            )
        return None

    @staticmethod
    def xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_11(
        field_name: str,
        actual: Any,
    ) -> EvaluationResult | None:
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=(
                    f"Field '{field_name}' contains an invalid "
                    "numeric value."
                ),
                evidence={
                    "XXfieldXX": field_name,
                    "actual": actual,
                },
            )
        return None

    @staticmethod
    def xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_12(
        field_name: str,
        actual: Any,
    ) -> EvaluationResult | None:
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=(
                    f"Field '{field_name}' contains an invalid "
                    "numeric value."
                ),
                evidence={
                    "FIELD": field_name,
                    "actual": actual,
                },
            )
        return None

    @staticmethod
    def xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_13(
        field_name: str,
        actual: Any,
    ) -> EvaluationResult | None:
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=(
                    f"Field '{field_name}' contains an invalid "
                    "numeric value."
                ),
                evidence={
                    "field": field_name,
                    "XXactualXX": actual,
                },
            )
        return None

    @staticmethod
    def xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_14(
        field_name: str,
        actual: Any,
    ) -> EvaluationResult | None:
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=(
                    f"Field '{field_name}' contains an invalid "
                    "numeric value."
                ),
                evidence={
                    "field": field_name,
                    "ACTUAL": actual,
                },
            )
        return None


    @classmethod
    @_mutmut_mutated(mutants_xǁRuleEvaluatorǁ_field_min__mutmut, is_classmethod = True)
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_orig(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_1(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = None

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_2(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(None, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_3(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, None)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_4(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_5(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, )

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_6(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is not None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_7(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=None,
                explanation="Required field value is missing.",
            )

        field_name, actual = field


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_8(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=None,
            )

        field_name, actual = field


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_9(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                explanation="Required field value is missing.",
            )

        field_name, actual = field


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_10(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                )

        field_name, actual = field


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_11(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="XXRequired field value is missing.XX",
            )

        field_name, actual = field


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_12(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="required field value is missing.",
            )

        field_name, actual = field


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_13(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="REQUIRED FIELD VALUE IS MISSING.",
            )

        field_name, actual = field


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_14(
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

        field_name, actual = None


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_15(
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


        numeric_review = None

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_16(
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


        numeric_review = cls._numeric_value_or_review(
            None,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_17(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            None,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_18(
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


        numeric_review = cls._numeric_value_or_review(
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_19(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_20(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_21(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "XXvalueXX" not in logic:
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
    def xǁRuleEvaluatorǁ_field_min__mutmut_22(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "VALUE" not in logic:
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
    def xǁRuleEvaluatorǁ_field_min__mutmut_23(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" in logic:
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
    def xǁRuleEvaluatorǁ_field_min__mutmut_24(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                None
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
    def xǁRuleEvaluatorǁ_field_min__mutmut_25(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "XXFIELD_MIN requires valueXX"
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
    def xǁRuleEvaluatorǁ_field_min__mutmut_26(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "field_min requires value"
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
    def xǁRuleEvaluatorǁ_field_min__mutmut_27(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_MIN REQUIRES VALUE"
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
    def xǁRuleEvaluatorǁ_field_min__mutmut_28(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_MIN requires value"
            )

        minimum = None

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_29(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_MIN requires value"
            )

        minimum = logic["XXvalueXX"]

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_30(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_MIN requires value"
            )

        minimum = logic["VALUE"]

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_31(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_MIN requires value"
            )

        minimum = logic["value"]

        if actual > minimum:
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
    def xǁRuleEvaluatorǁ_field_min__mutmut_32(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_MIN requires value"
            )

        minimum = logic["value"]

        if actual >= minimum:
            outcome = None
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
    def xǁRuleEvaluatorǁ_field_min__mutmut_33(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_MIN requires value"
            )

        minimum = logic["value"]

        if actual >= minimum:
            outcome = EvaluationOutcome.PASS
            explanation = None
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
    def xǁRuleEvaluatorǁ_field_min__mutmut_34(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
            outcome = None
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
    def xǁRuleEvaluatorǁ_field_min__mutmut_35(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
            explanation = None

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
    def xǁRuleEvaluatorǁ_field_min__mutmut_36(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
            outcome=None,
            explanation=explanation,
            evidence={
                "field": field_name,
                "actual": actual,
                "minimum": minimum,
            },
        )


    @classmethod
    def xǁRuleEvaluatorǁ_field_min__mutmut_37(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
            explanation=None,
            evidence={
                "field": field_name,
                "actual": actual,
                "minimum": minimum,
            },
        )


    @classmethod
    def xǁRuleEvaluatorǁ_field_min__mutmut_38(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
            evidence=None,
        )


    @classmethod
    def xǁRuleEvaluatorǁ_field_min__mutmut_39(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
            explanation=explanation,
            evidence={
                "field": field_name,
                "actual": actual,
                "minimum": minimum,
            },
        )


    @classmethod
    def xǁRuleEvaluatorǁ_field_min__mutmut_40(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
            evidence={
                "field": field_name,
                "actual": actual,
                "minimum": minimum,
            },
        )


    @classmethod
    def xǁRuleEvaluatorǁ_field_min__mutmut_41(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
            )


    @classmethod
    def xǁRuleEvaluatorǁ_field_min__mutmut_42(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
                "XXfieldXX": field_name,
                "actual": actual,
                "minimum": minimum,
            },
        )


    @classmethod
    def xǁRuleEvaluatorǁ_field_min__mutmut_43(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
                "FIELD": field_name,
                "actual": actual,
                "minimum": minimum,
            },
        )


    @classmethod
    def xǁRuleEvaluatorǁ_field_min__mutmut_44(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
                "XXactualXX": actual,
                "minimum": minimum,
            },
        )


    @classmethod
    def xǁRuleEvaluatorǁ_field_min__mutmut_45(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
                "ACTUAL": actual,
                "minimum": minimum,
            },
        )


    @classmethod
    def xǁRuleEvaluatorǁ_field_min__mutmut_46(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
                "XXminimumXX": minimum,
            },
        )


    @classmethod
    def xǁRuleEvaluatorǁ_field_min__mutmut_47(
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


        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
                "MINIMUM": minimum,
            },
        )

    @classmethod
    @_mutmut_mutated(mutants_xǁRuleEvaluatorǁ_field_max__mutmut, is_classmethod = True)
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_orig(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_1(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = None

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_2(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(None, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_3(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, None)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_4(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_5(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, )

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_6(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is not None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="Required field value is missing.",
            )

        field_name, actual = field

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_7(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=None,
                explanation="Required field value is missing.",
            )

        field_name, actual = field

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_8(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=None,
            )

        field_name, actual = field

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_9(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                explanation="Required field value is missing.",
            )

        field_name, actual = field

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_10(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                )

        field_name, actual = field

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_11(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="XXRequired field value is missing.XX",
            )

        field_name, actual = field

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_12(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="required field value is missing.",
            )

        field_name, actual = field

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_13(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="REQUIRED FIELD VALUE IS MISSING.",
            )

        field_name, actual = field

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_14(
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

        field_name, actual = None

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_15(
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

        numeric_review = None

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_16(
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

        numeric_review = cls._numeric_value_or_review(
            None,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_17(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            None,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_18(
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

        numeric_review = cls._numeric_value_or_review(
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_19(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            )

        if numeric_review is not None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_20(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is None:
            return numeric_review

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_21(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "XXvalueXX" not in logic:
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
    def xǁRuleEvaluatorǁ_field_max__mutmut_22(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "VALUE" not in logic:
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
    def xǁRuleEvaluatorǁ_field_max__mutmut_23(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" in logic:
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
    def xǁRuleEvaluatorǁ_field_max__mutmut_24(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                None
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
    def xǁRuleEvaluatorǁ_field_max__mutmut_25(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "XXFIELD_MAX requires valueXX"
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
    def xǁRuleEvaluatorǁ_field_max__mutmut_26(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "field_max requires value"
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
    def xǁRuleEvaluatorǁ_field_max__mutmut_27(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_MAX REQUIRES VALUE"
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
    def xǁRuleEvaluatorǁ_field_max__mutmut_28(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_MAX requires value"
            )

        maximum = None

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_29(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_MAX requires value"
            )

        maximum = logic["XXvalueXX"]

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_30(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_MAX requires value"
            )

        maximum = logic["VALUE"]

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_31(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_MAX requires value"
            )

        maximum = logic["value"]

        if actual < maximum:
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
    def xǁRuleEvaluatorǁ_field_max__mutmut_32(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_MAX requires value"
            )

        maximum = logic["value"]

        if actual <= maximum:
            outcome = None
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
    def xǁRuleEvaluatorǁ_field_max__mutmut_33(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

        if "value" not in logic:
            raise InvalidRuleError(
                "FIELD_MAX requires value"
            )

        maximum = logic["value"]

        if actual <= maximum:
            outcome = EvaluationOutcome.PASS
            explanation = None
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
    def xǁRuleEvaluatorǁ_field_max__mutmut_34(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
            outcome = None
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
    def xǁRuleEvaluatorǁ_field_max__mutmut_35(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
            explanation = None

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
    def xǁRuleEvaluatorǁ_field_max__mutmut_36(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
            outcome=None,
            explanation=explanation,
            evidence={
                "field": field_name,
                "actual": actual,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_max__mutmut_37(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
            explanation=None,
            evidence={
                "field": field_name,
                "actual": actual,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_max__mutmut_38(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
            evidence=None,
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_max__mutmut_39(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
            explanation=explanation,
            evidence={
                "field": field_name,
                "actual": actual,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_max__mutmut_40(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
            evidence={
                "field": field_name,
                "actual": actual,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_max__mutmut_41(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
            )

    @classmethod
    def xǁRuleEvaluatorǁ_field_max__mutmut_42(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
                "XXfieldXX": field_name,
                "actual": actual,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_max__mutmut_43(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
                "FIELD": field_name,
                "actual": actual,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_max__mutmut_44(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
                "XXactualXX": actual,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_max__mutmut_45(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
                "ACTUAL": actual,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_max__mutmut_46(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
                "XXmaximumXX": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_max__mutmut_47(
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

        numeric_review = cls._numeric_value_or_review(
            field_name,
            actual,
        )

        if numeric_review is not None:
            return numeric_review

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
                "MAXIMUM": maximum,
            },
        )

    @classmethod
    @_mutmut_mutated(mutants_xǁRuleEvaluatorǁ_field_range__mutmut, is_classmethod = True)
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_orig(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_1(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = None

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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_2(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(None, context)

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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_3(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, None)

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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_4(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(context)

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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_5(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, )

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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_6(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is not None:
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_7(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=None,
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_8(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation=None,
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_9(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_10(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_11(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="XXRequired field value is missing.XX",
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_12(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="required field value is missing.",
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_13(
        cls,
        logic: dict[str, Any],
        context: EvidenceContext,
    ) -> EvaluationResult:
        field = cls._get_field(logic, context)

        if field is None:
            return EvaluationResult(
                outcome=EvaluationOutcome.NEEDS_REVIEW,
                explanation="REQUIRED FIELD VALUE IS MISSING.",
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_14(
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

        field_name, actual = None
        

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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_15(
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
        

        if "minimum" not in logic and "maximum" not in logic:
            raise InvalidRuleError(
                "FIELD_RANGE requires minimum and maximum"
            )

        minimum = logic["minimum"]
        maximum = logic["maximum"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_16(
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
        

        if "XXminimumXX" not in logic or "maximum" not in logic:
            raise InvalidRuleError(
                "FIELD_RANGE requires minimum and maximum"
            )

        minimum = logic["minimum"]
        maximum = logic["maximum"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_17(
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
        

        if "MINIMUM" not in logic or "maximum" not in logic:
            raise InvalidRuleError(
                "FIELD_RANGE requires minimum and maximum"
            )

        minimum = logic["minimum"]
        maximum = logic["maximum"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_18(
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
        

        if "minimum" in logic or "maximum" not in logic:
            raise InvalidRuleError(
                "FIELD_RANGE requires minimum and maximum"
            )

        minimum = logic["minimum"]
        maximum = logic["maximum"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_19(
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
        

        if "minimum" not in logic or "XXmaximumXX" not in logic:
            raise InvalidRuleError(
                "FIELD_RANGE requires minimum and maximum"
            )

        minimum = logic["minimum"]
        maximum = logic["maximum"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_20(
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
        

        if "minimum" not in logic or "MAXIMUM" not in logic:
            raise InvalidRuleError(
                "FIELD_RANGE requires minimum and maximum"
            )

        minimum = logic["minimum"]
        maximum = logic["maximum"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_21(
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
        

        if "minimum" not in logic or "maximum" in logic:
            raise InvalidRuleError(
                "FIELD_RANGE requires minimum and maximum"
            )

        minimum = logic["minimum"]
        maximum = logic["maximum"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_22(
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
                None
            )

        minimum = logic["minimum"]
        maximum = logic["maximum"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_23(
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
                "XXFIELD_RANGE requires minimum and maximumXX"
            )

        minimum = logic["minimum"]
        maximum = logic["maximum"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_24(
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
                "field_range requires minimum and maximum"
            )

        minimum = logic["minimum"]
        maximum = logic["maximum"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_25(
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
                "FIELD_RANGE REQUIRES MINIMUM AND MAXIMUM"
            )

        minimum = logic["minimum"]
        maximum = logic["maximum"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_26(
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

        minimum = None
        maximum = logic["maximum"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_27(
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

        minimum = logic["XXminimumXX"]
        maximum = logic["maximum"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_28(
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

        minimum = logic["MINIMUM"]
        maximum = logic["maximum"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_29(
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
        maximum = None

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_30(
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
        maximum = logic["XXmaximumXX"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_31(
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
        maximum = logic["MAXIMUM"]

        if minimum > maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_32(
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

        if minimum >= maximum:
            raise InvalidRuleError(
                "FIELD_RANGE minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_33(
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
                None
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_34(
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
                "XXFIELD_RANGE minimum cannot exceed maximumXX"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_35(
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
                "field_range minimum cannot exceed maximum"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_36(
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
                "FIELD_RANGE MINIMUM CANNOT EXCEED MAXIMUM"
            )
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_37(
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
        numeric_review = None
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_38(
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
        numeric_review = cls._numeric_value_or_review(
                    None,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_39(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    None,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_40(
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
        numeric_review = cls._numeric_value_or_review(
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_41(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    )
        if numeric_review is not None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_42(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is None:
            return numeric_review

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_43(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

        if minimum < actual <= maximum:
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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_44(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

        if minimum <= actual < maximum:
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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_45(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

        if minimum <= actual <= maximum:
            outcome = None
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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_46(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

        if minimum <= actual <= maximum:
            outcome = EvaluationOutcome.PASS
            explanation = None
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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_47(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

        if minimum <= actual <= maximum:
            outcome = EvaluationOutcome.PASS
            explanation = (
                f"Field '{field_name}' is within the "
                f"allowed range {minimum}–{maximum}."
            )
        else:
            outcome = None
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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_48(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

        if minimum <= actual <= maximum:
            outcome = EvaluationOutcome.PASS
            explanation = (
                f"Field '{field_name}' is within the "
                f"allowed range {minimum}–{maximum}."
            )
        else:
            outcome = EvaluationOutcome.FAIL
            explanation = None

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

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_49(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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
            outcome=None,
            explanation=explanation,
            evidence={
                "field": field_name,
                "actual": actual,
                "minimum": minimum,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_50(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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
            explanation=None,
            evidence={
                "field": field_name,
                "actual": actual,
                "minimum": minimum,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_51(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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
            evidence=None,
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_52(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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
            explanation=explanation,
            evidence={
                "field": field_name,
                "actual": actual,
                "minimum": minimum,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_53(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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
            evidence={
                "field": field_name,
                "actual": actual,
                "minimum": minimum,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_54(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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
            )

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_55(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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
                "XXfieldXX": field_name,
                "actual": actual,
                "minimum": minimum,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_56(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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
                "FIELD": field_name,
                "actual": actual,
                "minimum": minimum,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_57(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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
                "XXactualXX": actual,
                "minimum": minimum,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_58(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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
                "ACTUAL": actual,
                "minimum": minimum,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_59(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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
                "XXminimumXX": minimum,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_60(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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
                "MINIMUM": minimum,
                "maximum": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_61(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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
                "XXmaximumXX": maximum,
            },
        )

    @classmethod
    def xǁRuleEvaluatorǁ_field_range__mutmut_62(
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
        numeric_review = cls._numeric_value_or_review(
                    field_name,
                    actual,
                )
        if numeric_review is not None:
            return numeric_review

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
                "MAXIMUM": maximum,
            },
        )

mutants_xǁRuleEvaluatorǁevaluate__mutmut['_mutmut_orig'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_1'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_2'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_3'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_4'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_5'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_6'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_7'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_8'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_9'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_10'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_11'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_12'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_13'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_14'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_15'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_16'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_17'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_18'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_19'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_20'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_21'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_22'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_23'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_24'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_25'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_26'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_27'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_28'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_29'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_30'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_31'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_32'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_33'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_34'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_34 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_35'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_35 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_36'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_36 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_37'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_37 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_38'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_38 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_39'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_39 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_40'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_40 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_41'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_41 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_42'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_42 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_43'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_43 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_44'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_44 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_45'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_45 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_46'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_46 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_47'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_47 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_48'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_48 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_49'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_49 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_50'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_50 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁevaluate__mutmut['xǁRuleEvaluatorǁevaluate__mutmut_51'] = RuleEvaluator.xǁRuleEvaluatorǁevaluate__mutmut_51 # type: ignore # mutmut generated

mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['_mutmut_orig'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_1'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_2'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_3'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_4'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_5'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_6'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_7'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_8'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_9'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_10'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_11'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_12'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_13'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_14'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_15'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_16'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_17'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_18'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_19'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_20'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_21'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_22'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_23'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_24'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_25'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_26'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_27'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_28'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_29'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_30'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_31'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_32'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_33'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_34'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_34 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_35'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_35 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_36'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_36 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_37'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_37 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_38'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_38 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_39'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_39 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_40'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_40 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_41'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_41 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_42'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_42 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_43'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_43 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_44'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_44 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_45'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_45 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_46'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_46 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_47'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_47 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_48'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_48 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_49'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_49 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_50'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_50 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_51'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_51 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_52'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_52 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_document_exists__mutmut['xǁRuleEvaluatorǁ_document_exists__mutmut_53'] = RuleEvaluator.xǁRuleEvaluatorǁ_document_exists__mutmut_53 # type: ignore # mutmut generated

mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['_mutmut_orig'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_1'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_2'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_3'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_4'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_5'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_6'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_7'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_8'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_9'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_10'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_11'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_12'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_13'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_14'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_15'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_16'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_17'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_18'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_19'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_20'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_21'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_22'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_23'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_24'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_25'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_26'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_27'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_28'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_29'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_30'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_31'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_32'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_exists__mutmut['xǁRuleEvaluatorǁ_field_exists__mutmut_33'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_exists__mutmut_33 # type: ignore # mutmut generated

mutants_xǁRuleEvaluatorǁ_get_field__mutmut['_mutmut_orig'] = RuleEvaluator.xǁRuleEvaluatorǁ_get_field__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_get_field__mutmut['xǁRuleEvaluatorǁ_get_field__mutmut_1'] = RuleEvaluator.xǁRuleEvaluatorǁ_get_field__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_get_field__mutmut['xǁRuleEvaluatorǁ_get_field__mutmut_2'] = RuleEvaluator.xǁRuleEvaluatorǁ_get_field__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_get_field__mutmut['xǁRuleEvaluatorǁ_get_field__mutmut_3'] = RuleEvaluator.xǁRuleEvaluatorǁ_get_field__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_get_field__mutmut['xǁRuleEvaluatorǁ_get_field__mutmut_4'] = RuleEvaluator.xǁRuleEvaluatorǁ_get_field__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_get_field__mutmut['xǁRuleEvaluatorǁ_get_field__mutmut_5'] = RuleEvaluator.xǁRuleEvaluatorǁ_get_field__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_get_field__mutmut['xǁRuleEvaluatorǁ_get_field__mutmut_6'] = RuleEvaluator.xǁRuleEvaluatorǁ_get_field__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_get_field__mutmut['xǁRuleEvaluatorǁ_get_field__mutmut_7'] = RuleEvaluator.xǁRuleEvaluatorǁ_get_field__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_get_field__mutmut['xǁRuleEvaluatorǁ_get_field__mutmut_8'] = RuleEvaluator.xǁRuleEvaluatorǁ_get_field__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_get_field__mutmut['xǁRuleEvaluatorǁ_get_field__mutmut_9'] = RuleEvaluator.xǁRuleEvaluatorǁ_get_field__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_get_field__mutmut['xǁRuleEvaluatorǁ_get_field__mutmut_10'] = RuleEvaluator.xǁRuleEvaluatorǁ_get_field__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_get_field__mutmut['xǁRuleEvaluatorǁ_get_field__mutmut_11'] = RuleEvaluator.xǁRuleEvaluatorǁ_get_field__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_get_field__mutmut['xǁRuleEvaluatorǁ_get_field__mutmut_12'] = RuleEvaluator.xǁRuleEvaluatorǁ_get_field__mutmut_12 # type: ignore # mutmut generated

mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['_mutmut_orig'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_1'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_2'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_3'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_4'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_5'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_6'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_7'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_8'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_9'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_10'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_11'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_12'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_13'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_14'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_15'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_16'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_17'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_18'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_19'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_20'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_21'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_22'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_23'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_24'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_25'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_26'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_27'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_28'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_29'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_30'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_31'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_32'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_33'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_34'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_34 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_35'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_35 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_36'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_36 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_37'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_37 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_38'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_38 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_39'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_39 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_40'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_40 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_41'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_41 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_42'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_42 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_equals__mutmut['xǁRuleEvaluatorǁ_field_equals__mutmut_43'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_equals__mutmut_43 # type: ignore # mutmut generated

mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['_mutmut_orig'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_1'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_2'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_3'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_4'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_5'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_6'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_7'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_8'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_9'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_10'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_11'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_12'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_13'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_14'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_15'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_16'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_17'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_18'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_19'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_20'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_21'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_22'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_23'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_24'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_25'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_26'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_27'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_28'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_29'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_30'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_31'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_32'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_33'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_34'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_34 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_35'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_35 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_36'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_36 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_37'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_37 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_38'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_38 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_39'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_39 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_40'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_40 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_41'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_41 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_42'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_42 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_43'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_43 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_44'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_44 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_not_equals__mutmut['xǁRuleEvaluatorǁ_field_not_equals__mutmut_45'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_not_equals__mutmut_45 # type: ignore # mutmut generated

mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut['_mutmut_orig'] = RuleEvaluator.xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut['xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_1'] = RuleEvaluator.xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut['xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_2'] = RuleEvaluator.xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut['xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_3'] = RuleEvaluator.xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut['xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_4'] = RuleEvaluator.xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut['xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_5'] = RuleEvaluator.xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut['xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_6'] = RuleEvaluator.xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut['xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_7'] = RuleEvaluator.xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut['xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_8'] = RuleEvaluator.xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut['xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_9'] = RuleEvaluator.xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut['xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_10'] = RuleEvaluator.xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut['xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_11'] = RuleEvaluator.xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut['xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_12'] = RuleEvaluator.xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut['xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_13'] = RuleEvaluator.xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut['xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_14'] = RuleEvaluator.xǁRuleEvaluatorǁ_numeric_value_or_review__mutmut_14 # type: ignore # mutmut generated

mutants_xǁRuleEvaluatorǁ_field_min__mutmut['_mutmut_orig'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_1'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_2'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_3'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_4'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_5'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_6'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_7'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_8'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_9'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_10'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_11'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_12'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_13'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_14'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_15'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_16'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_17'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_18'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_19'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_20'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_21'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_22'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_23'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_24'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_25'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_26'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_27'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_28'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_29'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_30'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_31'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_32'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_33'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_34'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_34 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_35'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_35 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_36'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_36 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_37'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_37 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_38'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_38 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_39'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_39 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_40'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_40 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_41'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_41 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_42'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_42 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_43'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_43 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_44'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_44 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_45'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_45 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_46'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_46 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_min__mutmut['xǁRuleEvaluatorǁ_field_min__mutmut_47'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_min__mutmut_47 # type: ignore # mutmut generated

mutants_xǁRuleEvaluatorǁ_field_max__mutmut['_mutmut_orig'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_1'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_2'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_3'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_4'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_5'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_6'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_7'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_8'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_9'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_10'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_11'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_12'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_13'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_14'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_15'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_16'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_17'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_18'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_19'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_20'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_21'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_22'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_23'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_24'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_25'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_26'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_27'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_28'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_29'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_30'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_31'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_32'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_33'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_34'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_34 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_35'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_35 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_36'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_36 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_37'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_37 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_38'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_38 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_39'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_39 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_40'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_40 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_41'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_41 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_42'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_42 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_43'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_43 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_44'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_44 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_45'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_45 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_46'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_46 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_max__mutmut['xǁRuleEvaluatorǁ_field_max__mutmut_47'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_max__mutmut_47 # type: ignore # mutmut generated

mutants_xǁRuleEvaluatorǁ_field_range__mutmut['_mutmut_orig'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_1'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_2'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_3'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_4'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_5'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_6'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_7'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_8'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_9'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_10'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_11'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_12'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_13'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_14'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_15'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_16'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_17'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_18'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_19'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_20'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_21'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_22'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_23'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_24'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_25'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_26'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_27'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_28'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_29'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_30'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_31'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_32'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_33'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_34'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_34 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_35'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_35 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_36'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_36 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_37'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_37 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_38'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_38 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_39'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_39 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_40'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_40 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_41'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_41 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_42'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_42 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_43'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_43 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_44'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_44 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_45'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_45 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_46'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_46 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_47'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_47 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_48'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_48 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_49'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_49 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_50'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_50 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_51'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_51 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_52'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_52 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_53'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_53 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_54'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_54 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_55'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_55 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_56'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_56 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_57'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_57 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_58'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_58 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_59'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_59 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_60'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_60 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_61'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_61 # type: ignore # mutmut generated
mutants_xǁRuleEvaluatorǁ_field_range__mutmut['xǁRuleEvaluatorǁ_field_range__mutmut_62'] = RuleEvaluator.xǁRuleEvaluatorǁ_field_range__mutmut_62 # type: ignore # mutmut generated