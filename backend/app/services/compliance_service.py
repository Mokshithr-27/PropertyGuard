from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.compliance import ComplianceResult, Finding
from app.repositories.compliance_repository import (
    create_compliance_result,
    create_finding,
    get_project_rule_compliance_result,
    get_rule_applicability,
    get_rule_dependencies,
    get_rule_version,
)
from app.repositories.document_repository import (
    get_latest_version,
    get_project_documents,
)

from app.services.project_service import get_project
from app.rules.context import DocumentEvidence, EvidenceContext
from app.rules.evaluator import RuleEvaluator
from app.rules.results import EvaluationResult
from app.rules.types import EvaluationOutcome


class ComplianceService:
    def __init__(self) -> None:
        self.evaluator = RuleEvaluator()

    def build_evidence_context(
        self,
        db: Session,
        project_id: UUID,
    ) -> EvidenceContext:
        project = get_project(
            db,
            project_id,
        )

        if project is None:
            raise ValueError("Project not found")

        documents = get_project_documents(
            db,
            project_id,
        )

        document_evidence = []

        for document in documents:
            latest_version = get_latest_version(
                db,
                document.id,
            )

            document_evidence.append(
                DocumentEvidence(
                    document_id=document.id,
                    document_type=document.document_type,
                    title=document.title,
                    status=document.status,
                    visibility=document.visibility,
                    expiry_date=document.expiry_date,
                    latest_version_number=(
                        latest_version.version_number
                        if latest_version is not None
                        else None
                    ),
                )
            )

        return EvidenceContext(
            project_id=project.id,
            documents=tuple(document_evidence),
            fields={
                "project_type": project.project_type,
            },
            property_type=project.project_type,
            evaluation_time=datetime.now(timezone.utc),
        )

    def evaluate_rule(
        self,
        db: Session,
        project_id: UUID,
        rule_version_id: UUID,
        context: EvidenceContext,
    ) -> ComplianceResult:
        # ---------------------------------------------------------
        # 1. Load and validate rule version
        # ---------------------------------------------------------
        rule_version = get_rule_version(
            db,
            rule_version_id,
        )

        if rule_version is None:
            raise ValueError("Rule version not found")

        if not rule_version.is_active:
            raise ValueError("Rule version is inactive")

        if not rule_version.evaluation_logic:
            raise ValueError(
                "Rule version has no evaluation logic"
            )

        # ---------------------------------------------------------
        # 2. Check applicability
        # ---------------------------------------------------------
        applicability_rules = get_rule_applicability(
            db,
            rule_version_id,
        )

        if applicability_rules:
            is_applicable = any(
                applicability.property_type is None
                or applicability.property_type == context.property_type
                for applicability in applicability_rules
            )

            if not is_applicable:
                result = EvaluationResult(
                    outcome=EvaluationOutcome.NOT_APPLICABLE,
                    explanation=(
                        f"Rule is not applicable to property type "
                        f"'{context.property_type}'."
                    ),
                )

                compliance_result = ComplianceResult(
                    project_id=project_id,
                    rule_version_id=rule_version_id,
                    outcome=result.outcome.value,
                    explanation=result.explanation,
                    dependency_affected=result.dependency_affected,
                    evaluated_at=datetime.now(timezone.utc),
                )

                create_compliance_result(
                    db,
                    compliance_result,
                )

                db.commit()
                db.refresh(compliance_result)

                return compliance_result

        # ---------------------------------------------------------
        # 3. Check rule dependencies
        # ---------------------------------------------------------
        dependencies = get_rule_dependencies(
            db,
            rule_version_id,
        )

        for dependency in dependencies:
            dependency_result = get_project_rule_compliance_result(
                db,
                project_id,
                dependency.depends_on_rule_version_id,
            )

            # -----------------------------------------------------
            # Dependency has not been evaluated yet
            # -----------------------------------------------------
            if dependency_result is None:
                result = EvaluationResult(
                    outcome=EvaluationOutcome.NEEDS_REVIEW,
                    explanation=(
                        "A required dependency has not been "
                        "evaluated yet."
                    ),
                    dependency_affected=True,
                )

                compliance_result = ComplianceResult(
                    project_id=project_id,
                    rule_version_id=rule_version_id,
                    outcome=result.outcome.value,
                    explanation=result.explanation,
                    dependency_affected=result.dependency_affected,
                    evaluated_at=datetime.now(timezone.utc),
                )

                create_compliance_result(
                    db,
                    compliance_result,
                )

                db.commit()
                db.refresh(compliance_result)

                return compliance_result

            # -----------------------------------------------------
            # Dependency did not pass
            # -----------------------------------------------------
            if dependency_result.outcome != EvaluationOutcome.PASS.value:
                result = EvaluationResult(
                    outcome=EvaluationOutcome.NEEDS_REVIEW,
                    explanation=(
                        "A required dependency has not passed."
                    ),
                    dependency_affected=True,
                )

                compliance_result = ComplianceResult(
                    project_id=project_id,
                    rule_version_id=rule_version_id,
                    outcome=result.outcome.value,
                    explanation=result.explanation,
                    dependency_affected=result.dependency_affected,
                    evaluated_at=datetime.now(timezone.utc),
                )

                create_compliance_result(
                    db,
                    compliance_result,
                )

                db.commit()
                db.refresh(compliance_result)

                return compliance_result

        # ---------------------------------------------------------
        # 4. Evaluate the rule itself
        #
        # IMPORTANT:
        # This must be OUTSIDE the dependency loop.
        # If there are zero dependencies, the rule still needs
        # to be evaluated.
        # ---------------------------------------------------------
        result = self.evaluator.evaluate(
            rule_version.evaluation_logic,
            context,
        )

        # ---------------------------------------------------------
        # 5. Persist compliance result
        # ---------------------------------------------------------
        compliance_result = ComplianceResult(
            project_id=project_id,
            rule_version_id=rule_version_id,
            outcome=result.outcome.value,
            explanation=result.explanation,
            dependency_affected=result.dependency_affected,
            evaluated_at=datetime.now(timezone.utc),
        )

        create_compliance_result(
            db,
            compliance_result,
        )

        # ---------------------------------------------------------
        # 6. Create finding only for an actual rule failure
        # ---------------------------------------------------------
        if result.outcome == EvaluationOutcome.FAIL:
            finding = Finding(
                compliance_result_id=compliance_result.id,
                severity=rule_version.severity,
                title=rule_version.rule_text[:255],
                description=result.explanation,
                status="OPEN",
            )

            create_finding(
                db,
                finding,
            )

        # ---------------------------------------------------------
        # 7. Commit and return
        # ---------------------------------------------------------
        db.commit()
        db.refresh(compliance_result)

        return compliance_result