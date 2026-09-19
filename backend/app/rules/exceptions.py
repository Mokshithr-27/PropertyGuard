class RuleEngineError(Exception):
    """Base exception for rule-engine errors."""


class InvalidRuleError(RuleEngineError):
    """Raised when a rule definition is invalid."""


class UnsupportedOperatorError(RuleEngineError):
    """Raised when a rule uses an unsupported evaluation operator."""


class InvalidEvidenceError(RuleEngineError):
    """Raised when the evidence supplied to the rule engine is invalid."""