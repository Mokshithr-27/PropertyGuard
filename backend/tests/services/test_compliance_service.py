import uuid
from types import SimpleNamespace

import pytest

from app.rules.context import EvidenceContext
from app.rules.types import EvaluationOutcome
from app.services.compliance_service import ComplianceService


def make_context():
    return EvidenceContext(
        project_id=uuid.uuid4(),
        documents=(),
        fields={
            "project_type": "APARTMENT",
        },
        property_type="APARTMENT",
    )


def make_rule_version(
    *,
    active=True,
    evaluation_logic=None,
    severity="HIGH",
):
    return SimpleNamespace(
        id=uuid.uuid4(),
        is_active=active,
        evaluation_logic=evaluation_logic,
        severity=severity,
        rule_text="RERA registration certificate is required",
    )


def make_applicability(
    *,
    property_type=None,
    active=True,
    conditions=None,
):
    return SimpleNamespace(
        id=uuid.uuid4(),
        rule_version_id=uuid.uuid4(),
        property_type=property_type,
        conditions=conditions,
        is_active=active,
    )


def make_fake_db():
    class FakeDB:
        def commit(self):
            pass

        def refresh(self, result):
            pass

    return FakeDB()


def fake_create_result(db, result):
    result.id = uuid.uuid4()
    return result


def test_evaluate_rule_rule_version_not_found(monkeypatch):
    service = ComplianceService()

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: None,
    )

    with pytest.raises(ValueError, match="Rule version not found"):
        service.evaluate_rule(
            db=None,
            project_id=uuid.uuid4(),
            rule_version_id=uuid.uuid4(),
            context=make_context(),
        )


def test_evaluate_rule_inactive_rule(monkeypatch):
    service = ComplianceService()

    rule_version = make_rule_version(active=False)

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: rule_version,
    )

    with pytest.raises(ValueError, match="Rule version is inactive"):
        service.evaluate_rule(
            db=None,
            project_id=uuid.uuid4(),
            rule_version_id=rule_version.id,
            context=make_context(),
        )


def test_evaluate_rule_missing_evaluation_logic(monkeypatch):
    service = ComplianceService()

    rule_version = make_rule_version(
        active=True,
        evaluation_logic=None,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: rule_version,
    )

    with pytest.raises(
        ValueError,
        match="Rule version has no evaluation logic",
    ):
        service.evaluate_rule(
            db=None,
            project_id=uuid.uuid4(),
            rule_version_id=rule_version.id,
            context=make_context(),
        )


def test_evaluate_rule_pass(monkeypatch):
    service = ComplianceService()

    rule_version = make_rule_version(
        evaluation_logic={
            "type": "FIELD_EXISTS",
            "field": "project_type",
        },
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: rule_version,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_dependencies",
        lambda db, rule_version_id: [],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_applicability",
        lambda db, rule_version_id: [],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_compliance_result",
        fake_create_result,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_finding",
        lambda db, finding: pytest.fail(
            "Finding should not be created for PASS"
        ),
    )

    result = service.evaluate_rule(
        db=make_fake_db(),
        project_id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        context=make_context(),
    )

    assert result.outcome == EvaluationOutcome.PASS.value


def test_evaluate_rule_fail_creates_finding(monkeypatch):
    service = ComplianceService()

    rule_version = make_rule_version(
        evaluation_logic={
            "type": "FIELD_EQUALS",
            "field": "project_type",
            "value": "VILLA",
        },
        severity="HIGH",
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: rule_version,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_dependencies",
        lambda db, rule_version_id: [],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_applicability",
        lambda db, rule_version_id: [],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_compliance_result",
        fake_create_result,
    )

    captured = {}

    def fake_create_finding(db, finding):
        captured["finding"] = finding
        return finding

    monkeypatch.setattr(
        "app.services.compliance_service.create_finding",
        fake_create_finding,
    )

    result = service.evaluate_rule(
        db=make_fake_db(),
        project_id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        context=make_context(),
    )

    assert result.outcome == EvaluationOutcome.FAIL.value

    finding = captured["finding"]

    assert finding.severity == "HIGH"
    assert finding.status == "OPEN"
    assert finding.compliance_result_id == result.id
    assert finding.title == rule_version.rule_text[:255]


def test_build_evidence_context_project_not_found(monkeypatch):
    service = ComplianceService()

    monkeypatch.setattr(
        "app.services.compliance_service.get_project",
        lambda db, project_id: None,
    )

    with pytest.raises(ValueError, match="Project not found"):
        service.build_evidence_context(
            db=None,
            project_id=uuid.uuid4(),
        )


def test_build_evidence_context(monkeypatch):
    service = ComplianceService()

    project_id = uuid.uuid4()
    document_id = uuid.uuid4()

    project = SimpleNamespace(
        id=project_id,
        project_type="APARTMENT",
    )

    document = SimpleNamespace(
        id=document_id,
        document_type="RERA",
        title="RERA Registration Certificate",
        status="ACTIVE",
        visibility="PRIVATE",
        expiry_date=None,
    )

    latest_version = SimpleNamespace(
        version_number=3,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_project",
        lambda db, project_id: project,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_project_documents",
        lambda db, project_id: [document],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_latest_version",
        lambda db, document_id: latest_version,
    )

    context = service.build_evidence_context(
        db=None,
        project_id=project_id,
    )

    assert context.project_id == project_id
    assert context.property_type == "APARTMENT"
    assert context.fields["project_type"] == "APARTMENT"

    assert len(context.documents) == 1

    evidence = context.documents[0]

    assert evidence.document_id == document_id
    assert evidence.document_type == "RERA"
    assert evidence.title == "RERA Registration Certificate"
    assert evidence.status == "ACTIVE"
    assert evidence.visibility == "PRIVATE"
    assert evidence.expiry_date is None
    assert evidence.latest_version_number == 3

    assert context.evaluation_time is not None
    assert context.evaluation_time.tzinfo is not None


def test_evaluate_rule_non_matching_property_type_is_not_applicable(
    monkeypatch,
):
    service = ComplianceService()

    rule_version = make_rule_version(
        evaluation_logic={
            "type": "FIELD_EXISTS",
            "field": "project_type",
        },
    )

    applicability = make_applicability(
        property_type="VILLA",
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: rule_version,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_applicability",
        lambda db, rule_version_id: [applicability],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_compliance_result",
        fake_create_result,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_finding",
        lambda db, finding: pytest.fail(
            "Finding should not be created for NOT_APPLICABLE"
        ),
    )

    result = service.evaluate_rule(
        db=make_fake_db(),
        project_id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        context=make_context(),
    )

    assert result.outcome == EvaluationOutcome.NOT_APPLICABLE.value


def test_evaluate_rule_matching_property_type_evaluates_normally(
    monkeypatch,
):
    service = ComplianceService()

    rule_version = make_rule_version(
        evaluation_logic={
            "type": "FIELD_EXISTS",
            "field": "project_type",
        },
    )

    applicability = make_applicability(
        property_type="APARTMENT",
    )

    context = EvidenceContext(
        project_id=uuid.uuid4(),
        documents=(),
        fields={
            "project_type": "APARTMENT",
        },
        property_type="APARTMENT",
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: rule_version,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_applicability",
        lambda db, rule_version_id: [applicability],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_dependencies",
        lambda db, rule_version_id: [],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_compliance_result",
        fake_create_result,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_finding",
        lambda db, finding: pytest.fail(
            "Finding should not be created for PASS"
        ),
    )

    result = service.evaluate_rule(
        db=make_fake_db(),
        project_id=context.project_id,
        rule_version_id=rule_version.id,
        context=context,
    )

    assert result.outcome == EvaluationOutcome.PASS.value


def test_evaluate_rule_without_applicability_is_universally_applicable(
    monkeypatch,
):
    service = ComplianceService()

    rule_version = make_rule_version(
        evaluation_logic={
            "type": "FIELD_EXISTS",
            "field": "project_type",
        },
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: rule_version,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_applicability",
        lambda db, rule_version_id: [],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_dependencies",
        lambda db, rule_version_id: [],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_compliance_result",
        fake_create_result,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_finding",
        lambda db, finding: pytest.fail(
            "Finding should not be created for PASS"
        ),
    )

    result = service.evaluate_rule(
        db=make_fake_db(),
        project_id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        context=make_context(),
    )

    assert result.outcome == EvaluationOutcome.PASS.value


def test_evaluate_rule_matches_any_applicability_record(
    monkeypatch,
):
    service = ComplianceService()

    rule_version = make_rule_version(
        evaluation_logic={
            "type": "FIELD_EXISTS",
            "field": "project_type",
        },
    )

    apartment_applicability = make_applicability(
        property_type="APARTMENT",
    )

    villa_applicability = make_applicability(
        property_type="VILLA",
    )

    context = EvidenceContext(
        project_id=uuid.uuid4(),
        documents=(),
        fields={
            "project_type": "VILLA",
        },
        property_type="VILLA",
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: rule_version,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_applicability",
        lambda db, rule_version_id: [
            apartment_applicability,
            villa_applicability,
        ],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_dependencies",
        lambda db, rule_version_id: [],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_compliance_result",
        fake_create_result,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_finding",
        lambda db, finding: pytest.fail(
            "Finding should not be created for PASS"
        ),
    )

    result = service.evaluate_rule(
        db=make_fake_db(),
        project_id=context.project_id,
        rule_version_id=rule_version.id,
        context=context,
    )

    assert result.outcome == EvaluationOutcome.PASS.value


def test_evaluate_rule_unrestricted_applicability_applies_to_any_property_type(
    monkeypatch,
):
    service = ComplianceService()

    rule_version = make_rule_version(
        evaluation_logic={
            "type": "FIELD_EXISTS",
            "field": "project_type",
        },
    )

    applicability = make_applicability(
        property_type=None,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: rule_version,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_applicability",
        lambda db, rule_version_id: [applicability],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_dependencies",
        lambda db, rule_version_id: [],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_compliance_result",
        fake_create_result,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_finding",
        lambda db, finding: pytest.fail(
            "Finding should not be created for PASS"
        ),
    )

    result = service.evaluate_rule(
        db=make_fake_db(),
        project_id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        context=make_context(),
    )

    assert result.outcome == EvaluationOutcome.PASS.value


def test_evaluate_rule_without_dependencies_evaluates_normally(
    monkeypatch,
):
    service = ComplianceService()

    rule_version = make_rule_version(
        evaluation_logic={
            "type": "FIELD_EXISTS",
            "field": "project_type",
        },
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: rule_version,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_dependencies",
        lambda db, rule_version_id: [],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_applicability",
        lambda db, rule_version_id: [],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_compliance_result",
        fake_create_result,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_finding",
        lambda db, finding: pytest.fail(
            "Finding should not be created for PASS"
        ),
    )

    result = service.evaluate_rule(
        db=make_fake_db(),
        project_id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        context=make_context(),
    )

    assert result.outcome == EvaluationOutcome.PASS.value
    assert result.dependency_affected is False


# ============================================================
# DEPENDENCY TESTS
# ============================================================


def test_evaluate_rule_dependency_failure_requires_review(
    monkeypatch,
):
    service = ComplianceService()

    rule_version = make_rule_version(
        evaluation_logic={
            "type": "FIELD_EXISTS",
            "field": "project_type",
        },
    )

    dependency = SimpleNamespace(
        id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        depends_on_rule_version_id=uuid.uuid4(),
    )

    dependency_result = SimpleNamespace(
        outcome=EvaluationOutcome.FAIL.value,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: rule_version,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_dependencies",
        lambda db, rule_version_id: [dependency],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_applicability",
        lambda db, rule_version_id: [],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_project_rule_compliance_result",
        lambda db, project_id, rule_version_id: dependency_result,
    )

    def fail_if_evaluator_runs(*args, **kwargs):
        pytest.fail(
            "RuleEvaluator should not run when a dependency has failed"
        )

    monkeypatch.setattr(
        service.evaluator,
        "evaluate",
        fail_if_evaluator_runs,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_compliance_result",
        fake_create_result,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_finding",
        lambda db, finding: pytest.fail(
            "Finding should not be created directly from dependency failure"
        ),
    )

    result = service.evaluate_rule(
        db=make_fake_db(),
        project_id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        context=make_context(),
    )

    assert result.outcome == EvaluationOutcome.NEEDS_REVIEW.value
    assert result.dependency_affected is True


def test_evaluate_rule_dependency_not_evaluated_requires_review(
    monkeypatch,
):
    service = ComplianceService()

    rule_version = make_rule_version(
        evaluation_logic={
            "type": "FIELD_EXISTS",
            "field": "project_type",
        },
    )

    dependency = SimpleNamespace(
        id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        depends_on_rule_version_id=uuid.uuid4(),
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: rule_version,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_dependencies",
        lambda db, rule_version_id: [dependency],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_applicability",
        lambda db, rule_version_id: [],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_project_rule_compliance_result",
        lambda db, project_id, rule_version_id: None,
    )

    def fail_if_evaluator_runs(*args, **kwargs):
        pytest.fail(
            "RuleEvaluator should not run when dependency has not been evaluated"
        )

    monkeypatch.setattr(
        service.evaluator,
        "evaluate",
        fail_if_evaluator_runs,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_compliance_result",
        fake_create_result,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_finding",
        lambda db, finding: pytest.fail(
            "Finding should not be created for missing dependency result"
        ),
    )

    result = service.evaluate_rule(
        db=make_fake_db(),
        project_id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        context=make_context(),
    )

    assert result.outcome == EvaluationOutcome.NEEDS_REVIEW.value
    assert result.dependency_affected is True
    assert "not been evaluated" in result.explanation


def test_evaluate_rule_dependency_pass_evaluates_normally(
    monkeypatch,
):
    service = ComplianceService()

    rule_version = make_rule_version(
        evaluation_logic={
            "type": "FIELD_EXISTS",
            "field": "project_type",
        },
    )

    dependency = SimpleNamespace(
        id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        depends_on_rule_version_id=uuid.uuid4(),
    )

    dependency_result = SimpleNamespace(
        outcome=EvaluationOutcome.PASS.value,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: rule_version,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_dependencies",
        lambda db, rule_version_id: [dependency],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_applicability",
        lambda db, rule_version_id: [],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_project_rule_compliance_result",
        lambda db, project_id, rule_version_id: dependency_result,
    )

    evaluator_called = {"value": False}

    def fake_evaluate(logic, context):
        evaluator_called["value"] = True

        from app.rules.results import EvaluationResult

        return EvaluationResult(
            outcome=EvaluationOutcome.PASS,
            explanation="Dependent rule passed.",
        )

    monkeypatch.setattr(
        service.evaluator,
        "evaluate",
        fake_evaluate,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_compliance_result",
        fake_create_result,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_finding",
        lambda db, finding: pytest.fail(
            "Finding should not be created for PASS"
        ),
    )

    result = service.evaluate_rule(
        db=make_fake_db(),
        project_id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        context=make_context(),
    )

    assert evaluator_called["value"] is True
    assert result.outcome == EvaluationOutcome.PASS.value
    assert result.dependency_affected is False


def test_evaluate_rule_dependency_needs_review_requires_review(
    monkeypatch,
):
    service = ComplianceService()

    rule_version = make_rule_version(
        evaluation_logic={
            "type": "FIELD_EXISTS",
            "field": "project_type",
        },
    )

    dependency = SimpleNamespace(
        id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        depends_on_rule_version_id=uuid.uuid4(),
    )

    dependency_result = SimpleNamespace(
        outcome=EvaluationOutcome.NEEDS_REVIEW.value,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: rule_version,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_dependencies",
        lambda db, rule_version_id: [dependency],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_applicability",
        lambda db, rule_version_id: [],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_project_rule_compliance_result",
        lambda db, project_id, rule_version_id: dependency_result,
    )

    def fail_if_evaluator_runs(*args, **kwargs):
        pytest.fail(
            "RuleEvaluator should not run when dependency needs review"
        )

    monkeypatch.setattr(
        service.evaluator,
        "evaluate",
        fail_if_evaluator_runs,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_compliance_result",
        fake_create_result,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_finding",
        lambda db, finding: pytest.fail(
            "Finding should not be created from dependency NEEDS_REVIEW"
        ),
    )

    result = service.evaluate_rule(
        db=make_fake_db(),
        project_id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        context=make_context(),
    )

    assert result.outcome == EvaluationOutcome.NEEDS_REVIEW.value
    assert result.dependency_affected is True


def test_evaluate_rule_dependency_not_applicable_requires_review(
    monkeypatch,
):
    service = ComplianceService()

    rule_version = make_rule_version(
        evaluation_logic={
            "type": "FIELD_EXISTS",
            "field": "project_type",
        },
    )

    dependency = SimpleNamespace(
        id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        depends_on_rule_version_id=uuid.uuid4(),
    )

    dependency_result = SimpleNamespace(
        outcome=EvaluationOutcome.NOT_APPLICABLE.value,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: rule_version,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_dependencies",
        lambda db, rule_version_id: [dependency],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_applicability",
        lambda db, rule_version_id: [],
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_project_rule_compliance_result",
        lambda db, project_id, rule_version_id: dependency_result,
    )

    def fail_if_evaluator_runs(*args, **kwargs):
        pytest.fail(
            "RuleEvaluator should not run when dependency is NOT_APPLICABLE"
        )

    monkeypatch.setattr(
        service.evaluator,
        "evaluate",
        fail_if_evaluator_runs,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_compliance_result",
        fake_create_result,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_finding",
        lambda db, finding: pytest.fail(
            "Finding should not be created from dependency NOT_APPLICABLE"
        ),
    )

    result = service.evaluate_rule(
        db=make_fake_db(),
        project_id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        context=make_context(),
    )

    assert result.outcome == EvaluationOutcome.NEEDS_REVIEW.value
    assert result.dependency_affected is True


def test_evaluate_rule_multiple_dependencies_require_all_to_pass(
    monkeypatch,
):
    service = ComplianceService()

    rule_version = make_rule_version(
        evaluation_logic={
            "type": "FIELD_EXISTS",
            "field": "project_type",
        },
    )

    dependency_one = SimpleNamespace(
        id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        depends_on_rule_version_id=uuid.uuid4(),
    )

    dependency_two = SimpleNamespace(
        id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        depends_on_rule_version_id=uuid.uuid4(),
    )

    dependency_three = SimpleNamespace(
        id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        depends_on_rule_version_id=uuid.uuid4(),
    )

    dependencies = [
        dependency_one,
        dependency_two,
        dependency_three,
    ]

    dependency_results = {
        dependency_one.depends_on_rule_version_id: SimpleNamespace(
            outcome=EvaluationOutcome.PASS.value,
        ),
        dependency_two.depends_on_rule_version_id: SimpleNamespace(
            outcome=EvaluationOutcome.PASS.value,
        ),
        dependency_three.depends_on_rule_version_id: SimpleNamespace(
            outcome=EvaluationOutcome.PASS.value,
        ),
    }

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_version",
        lambda db, rule_version_id: rule_version,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_dependencies",
        lambda db, rule_version_id: dependencies,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.get_rule_applicability",
        lambda db, rule_version_id: [],
    )

    checked_dependencies = []

    def fake_get_dependency_result(
        db,
        project_id,
        rule_version_id,
    ):
        checked_dependencies.append(rule_version_id)
        return dependency_results.get(rule_version_id)

    monkeypatch.setattr(
        "app.services.compliance_service.get_project_rule_compliance_result",
        fake_get_dependency_result,
    )

    evaluator_called = {"value": False}

    def fake_evaluate(logic, context):
        evaluator_called["value"] = True

        from app.rules.results import EvaluationResult

        return EvaluationResult(
            outcome=EvaluationOutcome.PASS,
            explanation="All dependencies passed.",
        )

    monkeypatch.setattr(
        service.evaluator,
        "evaluate",
        fake_evaluate,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_compliance_result",
        fake_create_result,
    )

    monkeypatch.setattr(
        "app.services.compliance_service.create_finding",
        lambda db, finding: pytest.fail(
            "Finding should not be created when all dependencies pass"
        ),
    )

    result = service.evaluate_rule(
        db=make_fake_db(),
        project_id=uuid.uuid4(),
        rule_version_id=rule_version.id,
        context=make_context(),
    )

    assert evaluator_called["value"] is True
    assert result.outcome == EvaluationOutcome.PASS.value
    assert result.dependency_affected is False

    assert len(checked_dependencies) == 3

    assert set(checked_dependencies) == {
        dependency_one.depends_on_rule_version_id,
        dependency_two.depends_on_rule_version_id,
        dependency_three.depends_on_rule_version_id,
    }