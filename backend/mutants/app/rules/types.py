"""
PropertyGuard Rule Engine Types & Enums
---------------------------------------
Defines core enumeration types for evaluation outcomes (PASS, FAIL, NEEDS_REVIEW,
NOT_APPLICABLE) and supported logical/assertion operators.
"""

from enum import StrEnum


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class EvaluationOutcome(StrEnum):
    PASS = "PASS"
    FAIL = "FAIL"
    NEEDS_REVIEW = "NEEDS_REVIEW"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class EvaluationOperator(StrEnum):
    DOCUMENT_EXISTS = "DOCUMENT_EXISTS"
    FIELD_EXISTS = "FIELD_EXISTS"
    FIELD_EQUALS = "FIELD_EQUALS"
    FIELD_NOT_EQUALS = "FIELD_NOT_EQUALS"
    FIELD_MIN = "FIELD_MIN"
    FIELD_MAX = "FIELD_MAX"
    FIELD_RANGE = "FIELD_RANGE"