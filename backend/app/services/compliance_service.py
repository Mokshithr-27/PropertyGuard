"""
PropertyGuard Compliance Business Service
-----------------------------------------
Orchestrates compliance evaluation workflows: builds EvidenceContext from project
documents and parameters, filters applicable rules, evaluates dependencies, invokes
the RuleEvaluator engine, records EvaluationRun and ComplianceResult records, and manages Findings.
"""

from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.compliance import ComplianceResult, Finding
from app.models.evaluation import EvaluationRun
from app.repositories.compliance_repository import (
    create_compliance_result,
    create_finding,
    get_active_rules,
    get_active_rule_version,
    get_project_rule_compliance_result,
    get_rule_applicability,
    get_rule_dependencies,
    get_rule_version,
    get_project_evaluation_results_by_run,
    get_project_evaluation_runs,
    get_finding,
    get_project_findings,
    update_finding,
)
from app.repositories.document_repository import (
    get_latest_version,
    get_project_documents,
)

from app.repositories.document_analysis_repository import (
    get_document_analysis_evidence,
    get_latest_document_analysis,
)


from app.services.project_service import get_project
from app.rules.context import DocumentEvidence, EvidenceContext
from app.rules.evaluator import RuleEvaluator
from app.rules.results import EvaluationResult
from app.rules.types import EvaluationOutcome


class ComplianceService:
    def __init__(self) -> None:
        self.evaluator = RuleEvaluator()
    def create_evaluation_run(
        self,
        db: Session,
        project_id: UUID,
    ) -> EvaluationRun:
        project = get_project(
            db,
            project_id,
        )

        if project is None:
            raise ValueError("Project not found")

        evaluation_run = EvaluationRun(
            project_id=project_id,
            status="RUNNING",
            started_at=datetime.now(timezone.utc),
        )

        db.add(evaluation_run)
        db.commit()
        db.refresh(evaluation_run)

        return evaluation_run

    def get_project_evaluation_history(
        self,
        db: Session,
        project_id: UUID,
    ) -> list[dict]:
        """Return evaluation history with compliance results grouped by run."""

        project = get_project(
            db,
            project_id,
        )

        if project is None:
            raise ValueError("Project not found")

        evaluation_runs = get_project_evaluation_runs(
            db=db,
            project_id=project_id,
        )

        results_by_run = get_project_evaluation_results_by_run(
            db=db,
            project_id=project_id,
        )

        history = []

        for evaluation_run in evaluation_runs:
            history.append(
                {
                    "evaluation_run": evaluation_run,
                    "results": results_by_run.get(
                        evaluation_run.id,
                        [],
                    ),
                }
            )

        return history


    def get_project_findings(
        self,
        db: Session,
        project_id: UUID,
    ) -> list[Finding]:
        return get_project_findings(
            db=db,
            project_id=project_id,
        )


    def update_finding_status(
        self,
        db: Session,
        finding_id: UUID,
        status: str | None = None,
        resolution_note: str | None = None,
    ) -> Finding:
        finding = get_finding(
            db=db,
            finding_id=finding_id,
        )

        if finding is None:
            raise ValueError("Finding not found")

        if status is not None:
            finding.status = status

            if status == "RESOLVED":
                finding.resolved_at = datetime.now(timezone.utc)
            else:
                finding.resolved_at = None

        if resolution_note is not None:
            finding.resolution_note = resolution_note

        return update_finding(
            db=db,
            finding=finding,
        )

    def run_evaluation(
        self,
        db: Session,
        project_id: UUID,
    ) -> EvaluationRun:
        evaluation_run = self.create_evaluation_run(
            db,
            project_id,
        )

        try:
            context = self.build_evidence_context(
                db,
                project_id,
            )

            active_rules = get_active_rules(db)

            # Resolve active versions before evaluation so dependencies can be
            # evaluated first regardless of rule_code/database ordering.
            active_versions = {}
            for rule in active_rules:
                rule_version = get_active_rule_version(db, rule.id)
                if rule_version is None:
                    raise ValueError(
                        f"No active version found for rule '{rule.rule_code}'"
                    )
                active_versions[rule_version.id] = (rule, rule_version)

            ordered_versions = self._order_versions_by_dependencies(
                db, active_versions
            )

            for rule_version in ordered_versions:
                self.evaluate_rule(
                    db=db,
                    project_id=project_id,
                    rule_version_id=rule_version.id,
                    context=context,
                    evaluation_run_id=evaluation_run.id,
                )

            return self.complete_evaluation_run(
                db,
                evaluation_run,
            )

        except Exception as exc:
            self.fail_evaluation_run(
                db,
                evaluation_run,
                str(exc),
            )
            raise


    @staticmethod
    def _order_versions_by_dependencies(db: Session, active_versions: dict) -> list:
        """Return active rule versions in dependency-first order.

        Dependencies that are not active in this evaluation are intentionally
        not silently substituted; evaluate_rule will mark them NEEDS_REVIEW.
        Cycles are rejected instead of producing order-dependent results.
        """
        versions = {version_id: pair[1] for version_id, pair in active_versions.items()}
        dependencies = {
            version_id: [
                item.depends_on_rule_version_id
                for item in get_rule_dependencies(db, version_id)
                if item.depends_on_rule_version_id in versions
            ]
            for version_id in versions
        }
        state: dict = {}
        ordered = []

        def visit(version_id):
            status = state.get(version_id, 0)
            if status == 1:
                raise ValueError("Cycle detected in compliance rule dependencies")
            if status == 2:
                return
            state[version_id] = 1
            for dependency_id in dependencies[version_id]:
                visit(dependency_id)
            state[version_id] = 2
            ordered.append(versions[version_id])

        # Preserve the existing stable rule order when no dependency dictates otherwise.
        for version_id in versions:
            visit(version_id)
        return ordered

    def complete_evaluation_run(
        self,
        db: Session,
        evaluation_run: EvaluationRun,
    ) -> EvaluationRun:
        evaluation_run.status = "COMPLETED"
        evaluation_run.completed_at = datetime.now(timezone.utc)
        evaluation_run.error_message = None

        db.add(evaluation_run)
        db.commit()
        db.refresh(evaluation_run)

        return evaluation_run


    def fail_evaluation_run(
        self,
        db: Session,
        evaluation_run: EvaluationRun,
        error_message: str,
    ) -> EvaluationRun:
        evaluation_run.status = "FAILED"
        evaluation_run.completed_at = datetime.now(timezone.utc)
        evaluation_run.error_message = error_message

        db.add(evaluation_run)
        db.commit()
        db.refresh(evaluation_run)

        return evaluation_run

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

        # Project-level canonical fields.
        fields: dict[str, object] = {
            "project_type": project.project_type,
        }

        # Track semantic evidence values before promoting them
        # into the compliance context.
        semantic_values: dict[str, set[str]] = {}

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

            if latest_version is None:
                continue

            analysis = get_latest_document_analysis(
                db,
                latest_version.id,
            )

            if analysis is None:
                continue

            evidence_items = get_document_analysis_evidence(
                db,
                analysis.id,
            )

            for evidence in evidence_items:
                # Raw page text is retained as evidence but must not
                # become a compliance field.
                if evidence.field_name == "page_text":
                    continue

                if not evidence.field_name:
                    continue

                if evidence.field_value is None:
                    continue

                value = evidence.field_value.strip()

                if not value:
                    continue

                # Keep uncertain/unsupported AI output out of compliance facts.
                # It remains visible for human review through the analysis API.
                confidence = evidence.confidence
                if confidence is None or confidence < 0.75:
                    continue
                if not evidence.evidence_text or not evidence.evidence_text.strip():
                    continue

                semantic_values.setdefault(
                    evidence.field_name,
                    set(),
                ).add(value)

        # Only promote unambiguous semantic evidence.
        #
        # If multiple analyses/documents provide different values
        # for the same field, leave that field absent so the rule
        # evaluator conservatively returns NEEDS_REVIEW.
        for field_name, values in semantic_values.items():
            if len(values) == 1:
                fields[field_name] = next(iter(values))

        return EvidenceContext(
            project_id=project.id,
            documents=tuple(document_evidence),
            fields=fields,
            property_type=project.project_type,
            evaluation_time=datetime.now(timezone.utc),
        )



    def evaluate_rule(
        self,
        db: Session,
        project_id: UUID,
        rule_version_id: UUID,
        context: EvidenceContext,
        evaluation_run_id: UUID | None = None,
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
                    evaluation_run_id=evaluation_run_id,
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
            if evaluation_run_id is None:
                dependency_result = get_project_rule_compliance_result(
                    db,
                    project_id,
                    dependency.depends_on_rule_version_id,
                )
            else:
                dependency_result = get_project_rule_compliance_result(
                    db,
                    project_id,
                    dependency.depends_on_rule_version_id,
                    evaluation_run_id,
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
                    evaluation_run_id=evaluation_run_id,
                )

                create_compliance_result(
                    db,
                    compliance_result,
                )

                finding = Finding(
                    compliance_result_id=compliance_result.id,
                    severity=rule_version.severity,
                    title=rule_version.rule_text[:255],
                    description=result.explanation or "",
                    status="OPEN",
                )

                create_finding(
                    db=db,
                    finding=finding,
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
                    evaluation_run_id=evaluation_run_id,
                )

                create_compliance_result(
                    db,
                    compliance_result,
                )

                finding = Finding(
                    compliance_result_id=compliance_result.id,
                    severity=rule_version.severity,
                    title=rule_version.rule_text[:255],
                    description=result.explanation or "",
                    status="OPEN",
                )

                create_finding(
                    db=db,
                    finding=finding,
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
            evaluation_run_id=evaluation_run_id,
        )

        create_compliance_result(
            db,
            compliance_result,
        )

        # ---------------------------------------------------------
        # 6. Create finding for rule failure or manual review
        # ---------------------------------------------------------
        if result.outcome in (
            EvaluationOutcome.FAIL,
            EvaluationOutcome.NEEDS_REVIEW,
        ):
            finding = Finding(
                compliance_result_id=compliance_result.id,
                severity=rule_version.severity,
                title=rule_version.rule_text[:255],
                description=result.explanation or "",
                status="OPEN",
            )

            create_finding(
                db=db,
                finding=finding,
            )


        # ---------------------------------------------------------
        # 7. Commit and return
        # ---------------------------------------------------------
        db.commit()
        db.refresh(compliance_result)

        return compliance_result

    