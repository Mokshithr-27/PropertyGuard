import uuid
from datetime import datetime, timezone

import pytest

from app.rules.context import DocumentEvidence, EvidenceContext
from app.rules.evaluator import RuleEvaluator
from app.rules.exceptions import (
    InvalidRuleError,
    UnsupportedOperatorError,
)
from app.rules.types import EvaluationOutcome


@pytest.fixture
def evaluator():
    return RuleEvaluator()


@pytest.fixture
def context():
    return EvidenceContext(
        project_id=uuid.uuid4(),
        documents=(
            DocumentEvidence(
                document_id=uuid.uuid4(),
                document_type="RERA",
                title="RERA Certificate",
                status="APPROVED",
                visibility="PRIVATE",
                expiry_date=None,
                latest_version_number=1,
            ),
        ),
        fields={
            "number_of_floors": 10,
            "project_type": "APARTMENT",
            "area_sqft": 1500,
        },
        property_type="APARTMENT",
        evaluation_time=datetime.now(timezone.utc),
    )


def test_document_exists_pass(evaluator, context):
    result = evaluator.evaluate(
        {
            "type": "DOCUMENT_EXISTS",
            "document_type": "RERA",
        },
        context,
    )

    assert result.outcome == EvaluationOutcome.PASS


def test_document_exists_missing_needs_review(evaluator, context):
    result = evaluator.evaluate(
        {
            "type": "DOCUMENT_EXISTS",
            "document_type": "BUILDING_PLAN",
        },
        context,
    )

    assert result.outcome == EvaluationOutcome.NEEDS_REVIEW


def test_document_exists_wrong_status_fails(evaluator, context):
    result = evaluator.evaluate(
        {
            "type": "DOCUMENT_EXISTS",
            "document_type": "RERA",
            "required_status": "VERIFIED",
        },
        context,
    )

    assert result.outcome == EvaluationOutcome.FAIL


def test_field_exists_pass(evaluator, context):
    result = evaluator.evaluate(
        {
            "type": "FIELD_EXISTS",
            "field": "number_of_floors",
        },
        context,
    )

    assert result.outcome == EvaluationOutcome.PASS


def test_field_exists_missing_needs_review(evaluator, context):
    result = evaluator.evaluate(
        {
            "type": "FIELD_EXISTS",
            "field": "missing_field",
        },
        context,
    )

    assert result.outcome == EvaluationOutcome.NEEDS_REVIEW


def test_field_equals_pass(evaluator, context):
    result = evaluator.evaluate(
        {
            "type": "FIELD_EQUALS",
            "field": "project_type",
            "value": "APARTMENT",
        },
        context,
    )

    assert result.outcome == EvaluationOutcome.PASS


def test_field_equals_fail(evaluator, context):
    result = evaluator.evaluate(
        {
            "type": "FIELD_EQUALS",
            "field": "project_type",
            "value": "VILLA",
        },
        context,
    )

    assert result.outcome == EvaluationOutcome.FAIL


def test_field_not_equals_pass(evaluator, context):
    result = evaluator.evaluate(
        {
            "type": "FIELD_NOT_EQUALS",
            "field": "project_type",
            "value": "VILLA",
        },
        context,
    )

    assert result.outcome == EvaluationOutcome.PASS


def test_field_not_equals_fail(evaluator, context):
    result = evaluator.evaluate(
        {
            "type": "FIELD_NOT_EQUALS",
            "field": "project_type",
            "value": "APARTMENT",
        },
        context,
    )

    assert result.outcome == EvaluationOutcome.FAIL


def test_field_min_pass(evaluator, context):
    result = evaluator.evaluate(
        {
            "type": "FIELD_MIN",
            "field": "number_of_floors",
            "value": 5,
        },
        context,
    )

    assert result.outcome == EvaluationOutcome.PASS


def test_field_min_fail(evaluator, context):
    result = evaluator.evaluate(
        {
            "type": "FIELD_MIN",
            "field": "number_of_floors",
            "value": 15,
        },
        context,
    )

    assert result.outcome == EvaluationOutcome.FAIL


def test_field_max_pass(evaluator, context):
    result = evaluator.evaluate(
        {
            "type": "FIELD_MAX",
            "field": "number_of_floors",
            "value": 15,
        },
        context,
    )

    assert result.outcome == EvaluationOutcome.PASS


def test_field_max_fail(evaluator, context):
    result = evaluator.evaluate(
        {
            "type": "FIELD_MAX",
            "field": "number_of_floors",
            "value": 5,
        },
        context,
    )

    assert result.outcome == EvaluationOutcome.FAIL


def test_field_range_pass(evaluator, context):
    result = evaluator.evaluate(
        {
            "type": "FIELD_RANGE",
            "field": "number_of_floors",
            "minimum": 5,
            "maximum": 15,
        },
        context,
    )

    assert result.outcome == EvaluationOutcome.PASS


def test_field_range_fail(evaluator, context):
    result = evaluator.evaluate(
        {
            "type": "FIELD_RANGE",
            "field": "number_of_floors",
            "minimum": 11,
            "maximum": 15,
        },
        context,
    )

    assert result.outcome == EvaluationOutcome.FAIL


def test_missing_field_value_needs_review(evaluator, context):
    result = evaluator.evaluate(
        {
            "type": "FIELD_MIN",
            "field": "missing_field",
            "value": 5,
        },
        context,
    )

    assert result.outcome == EvaluationOutcome.NEEDS_REVIEW


def test_missing_operator_raises(evaluator, context):
    with pytest.raises(InvalidRuleError):
        evaluator.evaluate({}, context)


def test_unsupported_operator_raises(evaluator, context):
    with pytest.raises(UnsupportedOperatorError):
        evaluator.evaluate(
            {
                "type": "UNKNOWN_OPERATOR",
            },
            context,
        )


def test_field_range_requires_valid_bounds(evaluator, context):
    with pytest.raises(InvalidRuleError):
        evaluator.evaluate(
            {
                "type": "FIELD_RANGE",
                "field": "number_of_floors",
                "minimum": 20,
                "maximum": 10,
            },
            context,
        )