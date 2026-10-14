"""
PropertyGuard Compliance Repository
------------------------------------
Provides low-level database query and persistence methods for compliance rules,
rule versions, applicability queries, evaluation runs, results, findings, and discrepancies.
"""

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.compliance import (
    ComplianceResult,
    ComplianceRule,
    Discrepancy,
    Finding,
    RuleApplicability,
    RuleDependency,
    RuleVersion,
)

from app.models.evaluation import EvaluationRun


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_create_evaluation_run__mutmut: MutantDict = {}  # type: ignore


# ---------------------------------------------------------------------------
# Evaluation Runs
# ---------------------------------------------------------------------------


@_mutmut_mutated(mutants_x_create_evaluation_run__mutmut)
def create_evaluation_run(
    db: Session,
    evaluation_run: EvaluationRun,
) -> EvaluationRun:
    db.add(evaluation_run)
    db.flush()
    return evaluation_run


# ---------------------------------------------------------------------------
# Evaluation Runs
# ---------------------------------------------------------------------------


def x_create_evaluation_run__mutmut_orig(
    db: Session,
    evaluation_run: EvaluationRun,
) -> EvaluationRun:
    db.add(evaluation_run)
    db.flush()
    return evaluation_run


# ---------------------------------------------------------------------------
# Evaluation Runs
# ---------------------------------------------------------------------------


def x_create_evaluation_run__mutmut_1(
    db: Session,
    evaluation_run: EvaluationRun,
) -> EvaluationRun:
    db.add(None)
    db.flush()
    return evaluation_run

mutants_x_create_evaluation_run__mutmut['_mutmut_orig'] = x_create_evaluation_run__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_evaluation_run__mutmut['x_create_evaluation_run__mutmut_1'] = x_create_evaluation_run__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_evaluation_run__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_evaluation_run__mutmut)
def get_evaluation_run(
    db: Session,
    evaluation_run_id: UUID,
) -> EvaluationRun | None:
    return db.scalar(
        select(EvaluationRun).where(
            EvaluationRun.id == evaluation_run_id,
        )
    )


def x_get_evaluation_run__mutmut_orig(
    db: Session,
    evaluation_run_id: UUID,
) -> EvaluationRun | None:
    return db.scalar(
        select(EvaluationRun).where(
            EvaluationRun.id == evaluation_run_id,
        )
    )


def x_get_evaluation_run__mutmut_1(
    db: Session,
    evaluation_run_id: UUID,
) -> EvaluationRun | None:
    return db.scalar(
        None
    )


def x_get_evaluation_run__mutmut_2(
    db: Session,
    evaluation_run_id: UUID,
) -> EvaluationRun | None:
    return db.scalar(
        select(EvaluationRun).where(
            None,
        )
    )


def x_get_evaluation_run__mutmut_3(
    db: Session,
    evaluation_run_id: UUID,
) -> EvaluationRun | None:
    return db.scalar(
        select(None).where(
            EvaluationRun.id == evaluation_run_id,
        )
    )


def x_get_evaluation_run__mutmut_4(
    db: Session,
    evaluation_run_id: UUID,
) -> EvaluationRun | None:
    return db.scalar(
        select(EvaluationRun).where(
            EvaluationRun.id != evaluation_run_id,
        )
    )

mutants_x_get_evaluation_run__mutmut['_mutmut_orig'] = x_get_evaluation_run__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_evaluation_run__mutmut['x_get_evaluation_run__mutmut_1'] = x_get_evaluation_run__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_evaluation_run__mutmut['x_get_evaluation_run__mutmut_2'] = x_get_evaluation_run__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_evaluation_run__mutmut['x_get_evaluation_run__mutmut_3'] = x_get_evaluation_run__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_evaluation_run__mutmut['x_get_evaluation_run__mutmut_4'] = x_get_evaluation_run__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_runs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_project_evaluation_runs__mutmut)
def get_project_evaluation_runs(
    db: Session,
    project_id: UUID,
) -> list[EvaluationRun]:
    return list(
        db.scalars(
            select(EvaluationRun)
            .where(
                EvaluationRun.project_id == project_id,
            )
            .order_by(EvaluationRun.started_at.desc())
        ).all()
    )


def x_get_project_evaluation_runs__mutmut_orig(
    db: Session,
    project_id: UUID,
) -> list[EvaluationRun]:
    return list(
        db.scalars(
            select(EvaluationRun)
            .where(
                EvaluationRun.project_id == project_id,
            )
            .order_by(EvaluationRun.started_at.desc())
        ).all()
    )


def x_get_project_evaluation_runs__mutmut_1(
    db: Session,
    project_id: UUID,
) -> list[EvaluationRun]:
    return list(
        None
    )


def x_get_project_evaluation_runs__mutmut_2(
    db: Session,
    project_id: UUID,
) -> list[EvaluationRun]:
    return list(
        db.scalars(
            None
        ).all()
    )


def x_get_project_evaluation_runs__mutmut_3(
    db: Session,
    project_id: UUID,
) -> list[EvaluationRun]:
    return list(
        db.scalars(
            select(EvaluationRun)
            .where(
                EvaluationRun.project_id == project_id,
            )
            .order_by(None)
        ).all()
    )


def x_get_project_evaluation_runs__mutmut_4(
    db: Session,
    project_id: UUID,
) -> list[EvaluationRun]:
    return list(
        db.scalars(
            select(EvaluationRun)
            .where(
                None,
            )
            .order_by(EvaluationRun.started_at.desc())
        ).all()
    )


def x_get_project_evaluation_runs__mutmut_5(
    db: Session,
    project_id: UUID,
) -> list[EvaluationRun]:
    return list(
        db.scalars(
            select(None)
            .where(
                EvaluationRun.project_id == project_id,
            )
            .order_by(EvaluationRun.started_at.desc())
        ).all()
    )


def x_get_project_evaluation_runs__mutmut_6(
    db: Session,
    project_id: UUID,
) -> list[EvaluationRun]:
    return list(
        db.scalars(
            select(EvaluationRun)
            .where(
                EvaluationRun.project_id != project_id,
            )
            .order_by(EvaluationRun.started_at.desc())
        ).all()
    )

mutants_x_get_project_evaluation_runs__mutmut['_mutmut_orig'] = x_get_project_evaluation_runs__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_project_evaluation_runs__mutmut['x_get_project_evaluation_runs__mutmut_1'] = x_get_project_evaluation_runs__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_runs__mutmut['x_get_project_evaluation_runs__mutmut_2'] = x_get_project_evaluation_runs__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_runs__mutmut['x_get_project_evaluation_runs__mutmut_3'] = x_get_project_evaluation_runs__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_runs__mutmut['x_get_project_evaluation_runs__mutmut_4'] = x_get_project_evaluation_runs__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_runs__mutmut['x_get_project_evaluation_runs__mutmut_5'] = x_get_project_evaluation_runs__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_runs__mutmut['x_get_project_evaluation_runs__mutmut_6'] = x_get_project_evaluation_runs__mutmut_6 # type: ignore # mutmut generated
mutants_x_update_evaluation_run__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_update_evaluation_run__mutmut)
def update_evaluation_run(
    db: Session,
    evaluation_run: EvaluationRun,
) -> EvaluationRun:
    db.add(evaluation_run)
    db.flush()
    return evaluation_run


def x_update_evaluation_run__mutmut_orig(
    db: Session,
    evaluation_run: EvaluationRun,
) -> EvaluationRun:
    db.add(evaluation_run)
    db.flush()
    return evaluation_run


def x_update_evaluation_run__mutmut_1(
    db: Session,
    evaluation_run: EvaluationRun,
) -> EvaluationRun:
    db.add(None)
    db.flush()
    return evaluation_run

mutants_x_update_evaluation_run__mutmut['_mutmut_orig'] = x_update_evaluation_run__mutmut_orig # type: ignore # mutmut generated
mutants_x_update_evaluation_run__mutmut['x_update_evaluation_run__mutmut_1'] = x_update_evaluation_run__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_results_by_run__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_project_evaluation_results_by_run__mutmut)
def get_project_evaluation_results_by_run(
    db: Session,
    project_id: UUID,
) -> dict[UUID, list[ComplianceResult]]:
    """Return compliance results grouped by evaluation run for a project."""

    evaluation_runs = get_project_evaluation_runs(
        db=db,
        project_id=project_id,
    )

    results_by_run: dict[UUID, list[ComplianceResult]] = {}

    for evaluation_run in evaluation_runs:
        results_by_run[evaluation_run.id] = (
            get_evaluation_run_compliance_results(
                db=db,
                evaluation_run_id=evaluation_run.id,
            )
        )

    return results_by_run


def x_get_project_evaluation_results_by_run__mutmut_orig(
    db: Session,
    project_id: UUID,
) -> dict[UUID, list[ComplianceResult]]:
    """Return compliance results grouped by evaluation run for a project."""

    evaluation_runs = get_project_evaluation_runs(
        db=db,
        project_id=project_id,
    )

    results_by_run: dict[UUID, list[ComplianceResult]] = {}

    for evaluation_run in evaluation_runs:
        results_by_run[evaluation_run.id] = (
            get_evaluation_run_compliance_results(
                db=db,
                evaluation_run_id=evaluation_run.id,
            )
        )

    return results_by_run


def x_get_project_evaluation_results_by_run__mutmut_1(
    db: Session,
    project_id: UUID,
) -> dict[UUID, list[ComplianceResult]]:
    """Return compliance results grouped by evaluation run for a project."""

    evaluation_runs = None

    results_by_run: dict[UUID, list[ComplianceResult]] = {}

    for evaluation_run in evaluation_runs:
        results_by_run[evaluation_run.id] = (
            get_evaluation_run_compliance_results(
                db=db,
                evaluation_run_id=evaluation_run.id,
            )
        )

    return results_by_run


def x_get_project_evaluation_results_by_run__mutmut_2(
    db: Session,
    project_id: UUID,
) -> dict[UUID, list[ComplianceResult]]:
    """Return compliance results grouped by evaluation run for a project."""

    evaluation_runs = get_project_evaluation_runs(
        db=None,
        project_id=project_id,
    )

    results_by_run: dict[UUID, list[ComplianceResult]] = {}

    for evaluation_run in evaluation_runs:
        results_by_run[evaluation_run.id] = (
            get_evaluation_run_compliance_results(
                db=db,
                evaluation_run_id=evaluation_run.id,
            )
        )

    return results_by_run


def x_get_project_evaluation_results_by_run__mutmut_3(
    db: Session,
    project_id: UUID,
) -> dict[UUID, list[ComplianceResult]]:
    """Return compliance results grouped by evaluation run for a project."""

    evaluation_runs = get_project_evaluation_runs(
        db=db,
        project_id=None,
    )

    results_by_run: dict[UUID, list[ComplianceResult]] = {}

    for evaluation_run in evaluation_runs:
        results_by_run[evaluation_run.id] = (
            get_evaluation_run_compliance_results(
                db=db,
                evaluation_run_id=evaluation_run.id,
            )
        )

    return results_by_run


def x_get_project_evaluation_results_by_run__mutmut_4(
    db: Session,
    project_id: UUID,
) -> dict[UUID, list[ComplianceResult]]:
    """Return compliance results grouped by evaluation run for a project."""

    evaluation_runs = get_project_evaluation_runs(
        project_id=project_id,
    )

    results_by_run: dict[UUID, list[ComplianceResult]] = {}

    for evaluation_run in evaluation_runs:
        results_by_run[evaluation_run.id] = (
            get_evaluation_run_compliance_results(
                db=db,
                evaluation_run_id=evaluation_run.id,
            )
        )

    return results_by_run


def x_get_project_evaluation_results_by_run__mutmut_5(
    db: Session,
    project_id: UUID,
) -> dict[UUID, list[ComplianceResult]]:
    """Return compliance results grouped by evaluation run for a project."""

    evaluation_runs = get_project_evaluation_runs(
        db=db,
        )

    results_by_run: dict[UUID, list[ComplianceResult]] = {}

    for evaluation_run in evaluation_runs:
        results_by_run[evaluation_run.id] = (
            get_evaluation_run_compliance_results(
                db=db,
                evaluation_run_id=evaluation_run.id,
            )
        )

    return results_by_run


def x_get_project_evaluation_results_by_run__mutmut_6(
    db: Session,
    project_id: UUID,
) -> dict[UUID, list[ComplianceResult]]:
    """Return compliance results grouped by evaluation run for a project."""

    evaluation_runs = get_project_evaluation_runs(
        db=db,
        project_id=project_id,
    )

    results_by_run: dict[UUID, list[ComplianceResult]] = None

    for evaluation_run in evaluation_runs:
        results_by_run[evaluation_run.id] = (
            get_evaluation_run_compliance_results(
                db=db,
                evaluation_run_id=evaluation_run.id,
            )
        )

    return results_by_run


def x_get_project_evaluation_results_by_run__mutmut_7(
    db: Session,
    project_id: UUID,
) -> dict[UUID, list[ComplianceResult]]:
    """Return compliance results grouped by evaluation run for a project."""

    evaluation_runs = get_project_evaluation_runs(
        db=db,
        project_id=project_id,
    )

    results_by_run: dict[UUID, list[ComplianceResult]] = {}

    for evaluation_run in evaluation_runs:
        results_by_run[evaluation_run.id] = None

    return results_by_run


def x_get_project_evaluation_results_by_run__mutmut_8(
    db: Session,
    project_id: UUID,
) -> dict[UUID, list[ComplianceResult]]:
    """Return compliance results grouped by evaluation run for a project."""

    evaluation_runs = get_project_evaluation_runs(
        db=db,
        project_id=project_id,
    )

    results_by_run: dict[UUID, list[ComplianceResult]] = {}

    for evaluation_run in evaluation_runs:
        results_by_run[evaluation_run.id] = (
            get_evaluation_run_compliance_results(
                db=None,
                evaluation_run_id=evaluation_run.id,
            )
        )

    return results_by_run


def x_get_project_evaluation_results_by_run__mutmut_9(
    db: Session,
    project_id: UUID,
) -> dict[UUID, list[ComplianceResult]]:
    """Return compliance results grouped by evaluation run for a project."""

    evaluation_runs = get_project_evaluation_runs(
        db=db,
        project_id=project_id,
    )

    results_by_run: dict[UUID, list[ComplianceResult]] = {}

    for evaluation_run in evaluation_runs:
        results_by_run[evaluation_run.id] = (
            get_evaluation_run_compliance_results(
                db=db,
                evaluation_run_id=None,
            )
        )

    return results_by_run


def x_get_project_evaluation_results_by_run__mutmut_10(
    db: Session,
    project_id: UUID,
) -> dict[UUID, list[ComplianceResult]]:
    """Return compliance results grouped by evaluation run for a project."""

    evaluation_runs = get_project_evaluation_runs(
        db=db,
        project_id=project_id,
    )

    results_by_run: dict[UUID, list[ComplianceResult]] = {}

    for evaluation_run in evaluation_runs:
        results_by_run[evaluation_run.id] = (
            get_evaluation_run_compliance_results(
                evaluation_run_id=evaluation_run.id,
            )
        )

    return results_by_run


def x_get_project_evaluation_results_by_run__mutmut_11(
    db: Session,
    project_id: UUID,
) -> dict[UUID, list[ComplianceResult]]:
    """Return compliance results grouped by evaluation run for a project."""

    evaluation_runs = get_project_evaluation_runs(
        db=db,
        project_id=project_id,
    )

    results_by_run: dict[UUID, list[ComplianceResult]] = {}

    for evaluation_run in evaluation_runs:
        results_by_run[evaluation_run.id] = (
            get_evaluation_run_compliance_results(
                db=db,
                )
        )

    return results_by_run

mutants_x_get_project_evaluation_results_by_run__mutmut['_mutmut_orig'] = x_get_project_evaluation_results_by_run__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_project_evaluation_results_by_run__mutmut['x_get_project_evaluation_results_by_run__mutmut_1'] = x_get_project_evaluation_results_by_run__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_results_by_run__mutmut['x_get_project_evaluation_results_by_run__mutmut_2'] = x_get_project_evaluation_results_by_run__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_results_by_run__mutmut['x_get_project_evaluation_results_by_run__mutmut_3'] = x_get_project_evaluation_results_by_run__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_results_by_run__mutmut['x_get_project_evaluation_results_by_run__mutmut_4'] = x_get_project_evaluation_results_by_run__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_results_by_run__mutmut['x_get_project_evaluation_results_by_run__mutmut_5'] = x_get_project_evaluation_results_by_run__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_results_by_run__mutmut['x_get_project_evaluation_results_by_run__mutmut_6'] = x_get_project_evaluation_results_by_run__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_results_by_run__mutmut['x_get_project_evaluation_results_by_run__mutmut_7'] = x_get_project_evaluation_results_by_run__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_results_by_run__mutmut['x_get_project_evaluation_results_by_run__mutmut_8'] = x_get_project_evaluation_results_by_run__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_results_by_run__mutmut['x_get_project_evaluation_results_by_run__mutmut_9'] = x_get_project_evaluation_results_by_run__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_results_by_run__mutmut['x_get_project_evaluation_results_by_run__mutmut_10'] = x_get_project_evaluation_results_by_run__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_project_evaluation_results_by_run__mutmut['x_get_project_evaluation_results_by_run__mutmut_11'] = x_get_project_evaluation_results_by_run__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_rule__mutmut: MutantDict = {}  # type: ignore



# ---------------------------------------------------------------------------
# Compliance Rules
# ---------------------------------------------------------------------------

@_mutmut_mutated(mutants_x_get_rule__mutmut)
def get_rule(
    db: Session,
    rule_id: UUID,
) -> ComplianceRule | None:
    return db.scalar(
        select(ComplianceRule).where(
            ComplianceRule.id == rule_id,
        )
    )



# ---------------------------------------------------------------------------
# Compliance Rules
# ---------------------------------------------------------------------------

def x_get_rule__mutmut_orig(
    db: Session,
    rule_id: UUID,
) -> ComplianceRule | None:
    return db.scalar(
        select(ComplianceRule).where(
            ComplianceRule.id == rule_id,
        )
    )



# ---------------------------------------------------------------------------
# Compliance Rules
# ---------------------------------------------------------------------------

def x_get_rule__mutmut_1(
    db: Session,
    rule_id: UUID,
) -> ComplianceRule | None:
    return db.scalar(
        None
    )



# ---------------------------------------------------------------------------
# Compliance Rules
# ---------------------------------------------------------------------------

def x_get_rule__mutmut_2(
    db: Session,
    rule_id: UUID,
) -> ComplianceRule | None:
    return db.scalar(
        select(ComplianceRule).where(
            None,
        )
    )



# ---------------------------------------------------------------------------
# Compliance Rules
# ---------------------------------------------------------------------------

def x_get_rule__mutmut_3(
    db: Session,
    rule_id: UUID,
) -> ComplianceRule | None:
    return db.scalar(
        select(None).where(
            ComplianceRule.id == rule_id,
        )
    )



# ---------------------------------------------------------------------------
# Compliance Rules
# ---------------------------------------------------------------------------

def x_get_rule__mutmut_4(
    db: Session,
    rule_id: UUID,
) -> ComplianceRule | None:
    return db.scalar(
        select(ComplianceRule).where(
            ComplianceRule.id != rule_id,
        )
    )

mutants_x_get_rule__mutmut['_mutmut_orig'] = x_get_rule__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_rule__mutmut['x_get_rule__mutmut_1'] = x_get_rule__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_rule__mutmut['x_get_rule__mutmut_2'] = x_get_rule__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_rule__mutmut['x_get_rule__mutmut_3'] = x_get_rule__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_rule__mutmut['x_get_rule__mutmut_4'] = x_get_rule__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_rule_by_code__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_rule_by_code__mutmut)
def get_rule_by_code(
    db: Session,
    rule_code: str,
) -> ComplianceRule | None:
    return db.scalar(
        select(ComplianceRule).where(
            ComplianceRule.rule_code == rule_code,
        )
    )


def x_get_rule_by_code__mutmut_orig(
    db: Session,
    rule_code: str,
) -> ComplianceRule | None:
    return db.scalar(
        select(ComplianceRule).where(
            ComplianceRule.rule_code == rule_code,
        )
    )


def x_get_rule_by_code__mutmut_1(
    db: Session,
    rule_code: str,
) -> ComplianceRule | None:
    return db.scalar(
        None
    )


def x_get_rule_by_code__mutmut_2(
    db: Session,
    rule_code: str,
) -> ComplianceRule | None:
    return db.scalar(
        select(ComplianceRule).where(
            None,
        )
    )


def x_get_rule_by_code__mutmut_3(
    db: Session,
    rule_code: str,
) -> ComplianceRule | None:
    return db.scalar(
        select(None).where(
            ComplianceRule.rule_code == rule_code,
        )
    )


def x_get_rule_by_code__mutmut_4(
    db: Session,
    rule_code: str,
) -> ComplianceRule | None:
    return db.scalar(
        select(ComplianceRule).where(
            ComplianceRule.rule_code != rule_code,
        )
    )

mutants_x_get_rule_by_code__mutmut['_mutmut_orig'] = x_get_rule_by_code__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_rule_by_code__mutmut['x_get_rule_by_code__mutmut_1'] = x_get_rule_by_code__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_rule_by_code__mutmut['x_get_rule_by_code__mutmut_2'] = x_get_rule_by_code__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_rule_by_code__mutmut['x_get_rule_by_code__mutmut_3'] = x_get_rule_by_code__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_rule_by_code__mutmut['x_get_rule_by_code__mutmut_4'] = x_get_rule_by_code__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_active_rules__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_active_rules__mutmut)
def get_active_rules(
    db: Session,
) -> list[ComplianceRule]:
    return list(
        db.scalars(
            select(ComplianceRule)
            .where(
                ComplianceRule.is_active.is_(True),
            )
            .order_by(ComplianceRule.rule_code.asc())
        ).all()
    )


def x_get_active_rules__mutmut_orig(
    db: Session,
) -> list[ComplianceRule]:
    return list(
        db.scalars(
            select(ComplianceRule)
            .where(
                ComplianceRule.is_active.is_(True),
            )
            .order_by(ComplianceRule.rule_code.asc())
        ).all()
    )


def x_get_active_rules__mutmut_1(
    db: Session,
) -> list[ComplianceRule]:
    return list(
        None
    )


def x_get_active_rules__mutmut_2(
    db: Session,
) -> list[ComplianceRule]:
    return list(
        db.scalars(
            None
        ).all()
    )


def x_get_active_rules__mutmut_3(
    db: Session,
) -> list[ComplianceRule]:
    return list(
        db.scalars(
            select(ComplianceRule)
            .where(
                ComplianceRule.is_active.is_(True),
            )
            .order_by(None)
        ).all()
    )


def x_get_active_rules__mutmut_4(
    db: Session,
) -> list[ComplianceRule]:
    return list(
        db.scalars(
            select(ComplianceRule)
            .where(
                None,
            )
            .order_by(ComplianceRule.rule_code.asc())
        ).all()
    )


def x_get_active_rules__mutmut_5(
    db: Session,
) -> list[ComplianceRule]:
    return list(
        db.scalars(
            select(None)
            .where(
                ComplianceRule.is_active.is_(True),
            )
            .order_by(ComplianceRule.rule_code.asc())
        ).all()
    )


def x_get_active_rules__mutmut_6(
    db: Session,
) -> list[ComplianceRule]:
    return list(
        db.scalars(
            select(ComplianceRule)
            .where(
                ComplianceRule.is_active.is_(None),
            )
            .order_by(ComplianceRule.rule_code.asc())
        ).all()
    )


def x_get_active_rules__mutmut_7(
    db: Session,
) -> list[ComplianceRule]:
    return list(
        db.scalars(
            select(ComplianceRule)
            .where(
                ComplianceRule.is_active.is_(False),
            )
            .order_by(ComplianceRule.rule_code.asc())
        ).all()
    )

mutants_x_get_active_rules__mutmut['_mutmut_orig'] = x_get_active_rules__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_active_rules__mutmut['x_get_active_rules__mutmut_1'] = x_get_active_rules__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_active_rules__mutmut['x_get_active_rules__mutmut_2'] = x_get_active_rules__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_active_rules__mutmut['x_get_active_rules__mutmut_3'] = x_get_active_rules__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_active_rules__mutmut['x_get_active_rules__mutmut_4'] = x_get_active_rules__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_active_rules__mutmut['x_get_active_rules__mutmut_5'] = x_get_active_rules__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_active_rules__mutmut['x_get_active_rules__mutmut_6'] = x_get_active_rules__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_active_rules__mutmut['x_get_active_rules__mutmut_7'] = x_get_active_rules__mutmut_7 # type: ignore # mutmut generated
mutants_x_create_rule__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_create_rule__mutmut)
def create_rule(
    db: Session,
    rule: ComplianceRule,
) -> ComplianceRule:
    db.add(rule)
    db.flush()
    return rule


def x_create_rule__mutmut_orig(
    db: Session,
    rule: ComplianceRule,
) -> ComplianceRule:
    db.add(rule)
    db.flush()
    return rule


def x_create_rule__mutmut_1(
    db: Session,
    rule: ComplianceRule,
) -> ComplianceRule:
    db.add(None)
    db.flush()
    return rule

mutants_x_create_rule__mutmut['_mutmut_orig'] = x_create_rule__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_rule__mutmut['x_create_rule__mutmut_1'] = x_create_rule__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_rule_version__mutmut: MutantDict = {}  # type: ignore




# ---------------------------------------------------------------------------
# Rule Versions
# ---------------------------------------------------------------------------

@_mutmut_mutated(mutants_x_get_rule_version__mutmut)
def get_rule_version(
    db: Session,
    rule_version_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion).where(
            RuleVersion.id == rule_version_id,
        )
    )




# ---------------------------------------------------------------------------
# Rule Versions
# ---------------------------------------------------------------------------

def x_get_rule_version__mutmut_orig(
    db: Session,
    rule_version_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion).where(
            RuleVersion.id == rule_version_id,
        )
    )




# ---------------------------------------------------------------------------
# Rule Versions
# ---------------------------------------------------------------------------

def x_get_rule_version__mutmut_1(
    db: Session,
    rule_version_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        None
    )




# ---------------------------------------------------------------------------
# Rule Versions
# ---------------------------------------------------------------------------

def x_get_rule_version__mutmut_2(
    db: Session,
    rule_version_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion).where(
            None,
        )
    )




# ---------------------------------------------------------------------------
# Rule Versions
# ---------------------------------------------------------------------------

def x_get_rule_version__mutmut_3(
    db: Session,
    rule_version_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(None).where(
            RuleVersion.id == rule_version_id,
        )
    )




# ---------------------------------------------------------------------------
# Rule Versions
# ---------------------------------------------------------------------------

def x_get_rule_version__mutmut_4(
    db: Session,
    rule_version_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion).where(
            RuleVersion.id != rule_version_id,
        )
    )

mutants_x_get_rule_version__mutmut['_mutmut_orig'] = x_get_rule_version__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_rule_version__mutmut['x_get_rule_version__mutmut_1'] = x_get_rule_version__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_rule_version__mutmut['x_get_rule_version__mutmut_2'] = x_get_rule_version__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_rule_version__mutmut['x_get_rule_version__mutmut_3'] = x_get_rule_version__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_rule_version__mutmut['x_get_rule_version__mutmut_4'] = x_get_rule_version__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_rule_versions__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_rule_versions__mutmut)
def get_rule_versions(
    db: Session,
    rule_id: UUID,
) -> list[RuleVersion]:
    return list(
        db.scalars(
            select(RuleVersion)
            .where(
                RuleVersion.rule_id == rule_id,
            )
            .order_by(RuleVersion.version_number.desc())
        ).all()
    )


def x_get_rule_versions__mutmut_orig(
    db: Session,
    rule_id: UUID,
) -> list[RuleVersion]:
    return list(
        db.scalars(
            select(RuleVersion)
            .where(
                RuleVersion.rule_id == rule_id,
            )
            .order_by(RuleVersion.version_number.desc())
        ).all()
    )


def x_get_rule_versions__mutmut_1(
    db: Session,
    rule_id: UUID,
) -> list[RuleVersion]:
    return list(
        None
    )


def x_get_rule_versions__mutmut_2(
    db: Session,
    rule_id: UUID,
) -> list[RuleVersion]:
    return list(
        db.scalars(
            None
        ).all()
    )


def x_get_rule_versions__mutmut_3(
    db: Session,
    rule_id: UUID,
) -> list[RuleVersion]:
    return list(
        db.scalars(
            select(RuleVersion)
            .where(
                RuleVersion.rule_id == rule_id,
            )
            .order_by(None)
        ).all()
    )


def x_get_rule_versions__mutmut_4(
    db: Session,
    rule_id: UUID,
) -> list[RuleVersion]:
    return list(
        db.scalars(
            select(RuleVersion)
            .where(
                None,
            )
            .order_by(RuleVersion.version_number.desc())
        ).all()
    )


def x_get_rule_versions__mutmut_5(
    db: Session,
    rule_id: UUID,
) -> list[RuleVersion]:
    return list(
        db.scalars(
            select(None)
            .where(
                RuleVersion.rule_id == rule_id,
            )
            .order_by(RuleVersion.version_number.desc())
        ).all()
    )


def x_get_rule_versions__mutmut_6(
    db: Session,
    rule_id: UUID,
) -> list[RuleVersion]:
    return list(
        db.scalars(
            select(RuleVersion)
            .where(
                RuleVersion.rule_id != rule_id,
            )
            .order_by(RuleVersion.version_number.desc())
        ).all()
    )

mutants_x_get_rule_versions__mutmut['_mutmut_orig'] = x_get_rule_versions__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_rule_versions__mutmut['x_get_rule_versions__mutmut_1'] = x_get_rule_versions__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_rule_versions__mutmut['x_get_rule_versions__mutmut_2'] = x_get_rule_versions__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_rule_versions__mutmut['x_get_rule_versions__mutmut_3'] = x_get_rule_versions__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_rule_versions__mutmut['x_get_rule_versions__mutmut_4'] = x_get_rule_versions__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_rule_versions__mutmut['x_get_rule_versions__mutmut_5'] = x_get_rule_versions__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_rule_versions__mutmut['x_get_rule_versions__mutmut_6'] = x_get_rule_versions__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_active_rule_version__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_active_rule_version__mutmut)
def get_active_rule_version(
    db: Session,
    rule_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion)
        .where(
            RuleVersion.rule_id == rule_id,
            RuleVersion.is_active.is_(True),
        )
        .order_by(RuleVersion.version_number.desc())
        .limit(1)
    )


def x_get_active_rule_version__mutmut_orig(
    db: Session,
    rule_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion)
        .where(
            RuleVersion.rule_id == rule_id,
            RuleVersion.is_active.is_(True),
        )
        .order_by(RuleVersion.version_number.desc())
        .limit(1)
    )


def x_get_active_rule_version__mutmut_1(
    db: Session,
    rule_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        None
    )


def x_get_active_rule_version__mutmut_2(
    db: Session,
    rule_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion)
        .where(
            RuleVersion.rule_id == rule_id,
            RuleVersion.is_active.is_(True),
        )
        .order_by(RuleVersion.version_number.desc())
        .limit(None)
    )


def x_get_active_rule_version__mutmut_3(
    db: Session,
    rule_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion)
        .where(
            RuleVersion.rule_id == rule_id,
            RuleVersion.is_active.is_(True),
        )
        .order_by(None)
        .limit(1)
    )


def x_get_active_rule_version__mutmut_4(
    db: Session,
    rule_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion)
        .where(
            None,
            RuleVersion.is_active.is_(True),
        )
        .order_by(RuleVersion.version_number.desc())
        .limit(1)
    )


def x_get_active_rule_version__mutmut_5(
    db: Session,
    rule_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion)
        .where(
            RuleVersion.rule_id == rule_id,
            None,
        )
        .order_by(RuleVersion.version_number.desc())
        .limit(1)
    )


def x_get_active_rule_version__mutmut_6(
    db: Session,
    rule_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion)
        .where(
            RuleVersion.is_active.is_(True),
        )
        .order_by(RuleVersion.version_number.desc())
        .limit(1)
    )


def x_get_active_rule_version__mutmut_7(
    db: Session,
    rule_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion)
        .where(
            RuleVersion.rule_id == rule_id,
            )
        .order_by(RuleVersion.version_number.desc())
        .limit(1)
    )


def x_get_active_rule_version__mutmut_8(
    db: Session,
    rule_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(None)
        .where(
            RuleVersion.rule_id == rule_id,
            RuleVersion.is_active.is_(True),
        )
        .order_by(RuleVersion.version_number.desc())
        .limit(1)
    )


def x_get_active_rule_version__mutmut_9(
    db: Session,
    rule_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion)
        .where(
            RuleVersion.rule_id != rule_id,
            RuleVersion.is_active.is_(True),
        )
        .order_by(RuleVersion.version_number.desc())
        .limit(1)
    )


def x_get_active_rule_version__mutmut_10(
    db: Session,
    rule_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion)
        .where(
            RuleVersion.rule_id == rule_id,
            RuleVersion.is_active.is_(None),
        )
        .order_by(RuleVersion.version_number.desc())
        .limit(1)
    )


def x_get_active_rule_version__mutmut_11(
    db: Session,
    rule_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion)
        .where(
            RuleVersion.rule_id == rule_id,
            RuleVersion.is_active.is_(False),
        )
        .order_by(RuleVersion.version_number.desc())
        .limit(1)
    )


def x_get_active_rule_version__mutmut_12(
    db: Session,
    rule_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion)
        .where(
            RuleVersion.rule_id == rule_id,
            RuleVersion.is_active.is_(True),
        )
        .order_by(RuleVersion.version_number.desc())
        .limit(2)
    )

mutants_x_get_active_rule_version__mutmut['_mutmut_orig'] = x_get_active_rule_version__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_active_rule_version__mutmut['x_get_active_rule_version__mutmut_1'] = x_get_active_rule_version__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_active_rule_version__mutmut['x_get_active_rule_version__mutmut_2'] = x_get_active_rule_version__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_active_rule_version__mutmut['x_get_active_rule_version__mutmut_3'] = x_get_active_rule_version__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_active_rule_version__mutmut['x_get_active_rule_version__mutmut_4'] = x_get_active_rule_version__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_active_rule_version__mutmut['x_get_active_rule_version__mutmut_5'] = x_get_active_rule_version__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_active_rule_version__mutmut['x_get_active_rule_version__mutmut_6'] = x_get_active_rule_version__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_active_rule_version__mutmut['x_get_active_rule_version__mutmut_7'] = x_get_active_rule_version__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_active_rule_version__mutmut['x_get_active_rule_version__mutmut_8'] = x_get_active_rule_version__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_active_rule_version__mutmut['x_get_active_rule_version__mutmut_9'] = x_get_active_rule_version__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_active_rule_version__mutmut['x_get_active_rule_version__mutmut_10'] = x_get_active_rule_version__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_active_rule_version__mutmut['x_get_active_rule_version__mutmut_11'] = x_get_active_rule_version__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_active_rule_version__mutmut['x_get_active_rule_version__mutmut_12'] = x_get_active_rule_version__mutmut_12 # type: ignore # mutmut generated
mutants_x_create_rule_version__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_create_rule_version__mutmut)
def create_rule_version(
    db: Session,
    rule_version: RuleVersion,
) -> RuleVersion:
    db.add(rule_version)
    db.flush()
    return rule_version


def x_create_rule_version__mutmut_orig(
    db: Session,
    rule_version: RuleVersion,
) -> RuleVersion:
    db.add(rule_version)
    db.flush()
    return rule_version


def x_create_rule_version__mutmut_1(
    db: Session,
    rule_version: RuleVersion,
) -> RuleVersion:
    db.add(None)
    db.flush()
    return rule_version

mutants_x_create_rule_version__mutmut['_mutmut_orig'] = x_create_rule_version__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_rule_version__mutmut['x_create_rule_version__mutmut_1'] = x_create_rule_version__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_rule_applicability__mutmut: MutantDict = {}  # type: ignore


# ---------------------------------------------------------------------------
# Rule Applicability
# ---------------------------------------------------------------------------

@_mutmut_mutated(mutants_x_get_rule_applicability__mutmut)
def get_rule_applicability(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleApplicability]:
    return list(
        db.scalars(
            select(RuleApplicability)
            .where(
                RuleApplicability.rule_version_id == rule_version_id,
                RuleApplicability.is_active.is_(True),
            )
            .order_by(RuleApplicability.created_at.asc())
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Applicability
# ---------------------------------------------------------------------------

def x_get_rule_applicability__mutmut_orig(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleApplicability]:
    return list(
        db.scalars(
            select(RuleApplicability)
            .where(
                RuleApplicability.rule_version_id == rule_version_id,
                RuleApplicability.is_active.is_(True),
            )
            .order_by(RuleApplicability.created_at.asc())
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Applicability
# ---------------------------------------------------------------------------

def x_get_rule_applicability__mutmut_1(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleApplicability]:
    return list(
        None
    )


# ---------------------------------------------------------------------------
# Rule Applicability
# ---------------------------------------------------------------------------

def x_get_rule_applicability__mutmut_2(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleApplicability]:
    return list(
        db.scalars(
            None
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Applicability
# ---------------------------------------------------------------------------

def x_get_rule_applicability__mutmut_3(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleApplicability]:
    return list(
        db.scalars(
            select(RuleApplicability)
            .where(
                RuleApplicability.rule_version_id == rule_version_id,
                RuleApplicability.is_active.is_(True),
            )
            .order_by(None)
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Applicability
# ---------------------------------------------------------------------------

def x_get_rule_applicability__mutmut_4(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleApplicability]:
    return list(
        db.scalars(
            select(RuleApplicability)
            .where(
                None,
                RuleApplicability.is_active.is_(True),
            )
            .order_by(RuleApplicability.created_at.asc())
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Applicability
# ---------------------------------------------------------------------------

def x_get_rule_applicability__mutmut_5(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleApplicability]:
    return list(
        db.scalars(
            select(RuleApplicability)
            .where(
                RuleApplicability.rule_version_id == rule_version_id,
                None,
            )
            .order_by(RuleApplicability.created_at.asc())
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Applicability
# ---------------------------------------------------------------------------

def x_get_rule_applicability__mutmut_6(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleApplicability]:
    return list(
        db.scalars(
            select(RuleApplicability)
            .where(
                RuleApplicability.is_active.is_(True),
            )
            .order_by(RuleApplicability.created_at.asc())
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Applicability
# ---------------------------------------------------------------------------

def x_get_rule_applicability__mutmut_7(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleApplicability]:
    return list(
        db.scalars(
            select(RuleApplicability)
            .where(
                RuleApplicability.rule_version_id == rule_version_id,
                )
            .order_by(RuleApplicability.created_at.asc())
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Applicability
# ---------------------------------------------------------------------------

def x_get_rule_applicability__mutmut_8(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleApplicability]:
    return list(
        db.scalars(
            select(None)
            .where(
                RuleApplicability.rule_version_id == rule_version_id,
                RuleApplicability.is_active.is_(True),
            )
            .order_by(RuleApplicability.created_at.asc())
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Applicability
# ---------------------------------------------------------------------------

def x_get_rule_applicability__mutmut_9(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleApplicability]:
    return list(
        db.scalars(
            select(RuleApplicability)
            .where(
                RuleApplicability.rule_version_id != rule_version_id,
                RuleApplicability.is_active.is_(True),
            )
            .order_by(RuleApplicability.created_at.asc())
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Applicability
# ---------------------------------------------------------------------------

def x_get_rule_applicability__mutmut_10(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleApplicability]:
    return list(
        db.scalars(
            select(RuleApplicability)
            .where(
                RuleApplicability.rule_version_id == rule_version_id,
                RuleApplicability.is_active.is_(None),
            )
            .order_by(RuleApplicability.created_at.asc())
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Applicability
# ---------------------------------------------------------------------------

def x_get_rule_applicability__mutmut_11(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleApplicability]:
    return list(
        db.scalars(
            select(RuleApplicability)
            .where(
                RuleApplicability.rule_version_id == rule_version_id,
                RuleApplicability.is_active.is_(False),
            )
            .order_by(RuleApplicability.created_at.asc())
        ).all()
    )

mutants_x_get_rule_applicability__mutmut['_mutmut_orig'] = x_get_rule_applicability__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_rule_applicability__mutmut['x_get_rule_applicability__mutmut_1'] = x_get_rule_applicability__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_rule_applicability__mutmut['x_get_rule_applicability__mutmut_2'] = x_get_rule_applicability__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_rule_applicability__mutmut['x_get_rule_applicability__mutmut_3'] = x_get_rule_applicability__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_rule_applicability__mutmut['x_get_rule_applicability__mutmut_4'] = x_get_rule_applicability__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_rule_applicability__mutmut['x_get_rule_applicability__mutmut_5'] = x_get_rule_applicability__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_rule_applicability__mutmut['x_get_rule_applicability__mutmut_6'] = x_get_rule_applicability__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_rule_applicability__mutmut['x_get_rule_applicability__mutmut_7'] = x_get_rule_applicability__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_rule_applicability__mutmut['x_get_rule_applicability__mutmut_8'] = x_get_rule_applicability__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_rule_applicability__mutmut['x_get_rule_applicability__mutmut_9'] = x_get_rule_applicability__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_rule_applicability__mutmut['x_get_rule_applicability__mutmut_10'] = x_get_rule_applicability__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_rule_applicability__mutmut['x_get_rule_applicability__mutmut_11'] = x_get_rule_applicability__mutmut_11 # type: ignore # mutmut generated
mutants_x_create_rule_applicability__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_create_rule_applicability__mutmut)
def create_rule_applicability(
    db: Session,
    applicability: RuleApplicability,
) -> RuleApplicability:
    db.add(applicability)
    db.flush()
    return applicability


def x_create_rule_applicability__mutmut_orig(
    db: Session,
    applicability: RuleApplicability,
) -> RuleApplicability:
    db.add(applicability)
    db.flush()
    return applicability


def x_create_rule_applicability__mutmut_1(
    db: Session,
    applicability: RuleApplicability,
) -> RuleApplicability:
    db.add(None)
    db.flush()
    return applicability

mutants_x_create_rule_applicability__mutmut['_mutmut_orig'] = x_create_rule_applicability__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_rule_applicability__mutmut['x_create_rule_applicability__mutmut_1'] = x_create_rule_applicability__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_rule_dependencies__mutmut: MutantDict = {}  # type: ignore


# ---------------------------------------------------------------------------
# Rule Dependencies
# ---------------------------------------------------------------------------

@_mutmut_mutated(mutants_x_get_rule_dependencies__mutmut)
def get_rule_dependencies(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleDependency]:
    return list(
        db.scalars(
            select(RuleDependency)
            .where(
                RuleDependency.rule_version_id == rule_version_id,
            )
            .order_by(RuleDependency.created_at.asc())
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Dependencies
# ---------------------------------------------------------------------------

def x_get_rule_dependencies__mutmut_orig(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleDependency]:
    return list(
        db.scalars(
            select(RuleDependency)
            .where(
                RuleDependency.rule_version_id == rule_version_id,
            )
            .order_by(RuleDependency.created_at.asc())
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Dependencies
# ---------------------------------------------------------------------------

def x_get_rule_dependencies__mutmut_1(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleDependency]:
    return list(
        None
    )


# ---------------------------------------------------------------------------
# Rule Dependencies
# ---------------------------------------------------------------------------

def x_get_rule_dependencies__mutmut_2(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleDependency]:
    return list(
        db.scalars(
            None
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Dependencies
# ---------------------------------------------------------------------------

def x_get_rule_dependencies__mutmut_3(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleDependency]:
    return list(
        db.scalars(
            select(RuleDependency)
            .where(
                RuleDependency.rule_version_id == rule_version_id,
            )
            .order_by(None)
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Dependencies
# ---------------------------------------------------------------------------

def x_get_rule_dependencies__mutmut_4(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleDependency]:
    return list(
        db.scalars(
            select(RuleDependency)
            .where(
                None,
            )
            .order_by(RuleDependency.created_at.asc())
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Dependencies
# ---------------------------------------------------------------------------

def x_get_rule_dependencies__mutmut_5(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleDependency]:
    return list(
        db.scalars(
            select(None)
            .where(
                RuleDependency.rule_version_id == rule_version_id,
            )
            .order_by(RuleDependency.created_at.asc())
        ).all()
    )


# ---------------------------------------------------------------------------
# Rule Dependencies
# ---------------------------------------------------------------------------

def x_get_rule_dependencies__mutmut_6(
    db: Session,
    rule_version_id: UUID,
) -> list[RuleDependency]:
    return list(
        db.scalars(
            select(RuleDependency)
            .where(
                RuleDependency.rule_version_id != rule_version_id,
            )
            .order_by(RuleDependency.created_at.asc())
        ).all()
    )

mutants_x_get_rule_dependencies__mutmut['_mutmut_orig'] = x_get_rule_dependencies__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_rule_dependencies__mutmut['x_get_rule_dependencies__mutmut_1'] = x_get_rule_dependencies__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_rule_dependencies__mutmut['x_get_rule_dependencies__mutmut_2'] = x_get_rule_dependencies__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_rule_dependencies__mutmut['x_get_rule_dependencies__mutmut_3'] = x_get_rule_dependencies__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_rule_dependencies__mutmut['x_get_rule_dependencies__mutmut_4'] = x_get_rule_dependencies__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_rule_dependencies__mutmut['x_get_rule_dependencies__mutmut_5'] = x_get_rule_dependencies__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_rule_dependencies__mutmut['x_get_rule_dependencies__mutmut_6'] = x_get_rule_dependencies__mutmut_6 # type: ignore # mutmut generated
mutants_x_create_rule_dependency__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_create_rule_dependency__mutmut)
def create_rule_dependency(
    db: Session,
    dependency: RuleDependency,
) -> RuleDependency:
    db.add(dependency)
    db.flush()
    return dependency


def x_create_rule_dependency__mutmut_orig(
    db: Session,
    dependency: RuleDependency,
) -> RuleDependency:
    db.add(dependency)
    db.flush()
    return dependency


def x_create_rule_dependency__mutmut_1(
    db: Session,
    dependency: RuleDependency,
) -> RuleDependency:
    db.add(None)
    db.flush()
    return dependency

mutants_x_create_rule_dependency__mutmut['_mutmut_orig'] = x_create_rule_dependency__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_rule_dependency__mutmut['x_create_rule_dependency__mutmut_1'] = x_create_rule_dependency__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_compliance_result__mutmut: MutantDict = {}  # type: ignore


# ---------------------------------------------------------------------------
# Compliance Results
# ---------------------------------------------------------------------------

@_mutmut_mutated(mutants_x_get_compliance_result__mutmut)
def get_compliance_result(
    db: Session,
    result_id: UUID,
) -> ComplianceResult | None:
    return db.scalar(
        select(ComplianceResult).where(
            ComplianceResult.id == result_id,
        )
    )


# ---------------------------------------------------------------------------
# Compliance Results
# ---------------------------------------------------------------------------

def x_get_compliance_result__mutmut_orig(
    db: Session,
    result_id: UUID,
) -> ComplianceResult | None:
    return db.scalar(
        select(ComplianceResult).where(
            ComplianceResult.id == result_id,
        )
    )


# ---------------------------------------------------------------------------
# Compliance Results
# ---------------------------------------------------------------------------

def x_get_compliance_result__mutmut_1(
    db: Session,
    result_id: UUID,
) -> ComplianceResult | None:
    return db.scalar(
        None
    )


# ---------------------------------------------------------------------------
# Compliance Results
# ---------------------------------------------------------------------------

def x_get_compliance_result__mutmut_2(
    db: Session,
    result_id: UUID,
) -> ComplianceResult | None:
    return db.scalar(
        select(ComplianceResult).where(
            None,
        )
    )


# ---------------------------------------------------------------------------
# Compliance Results
# ---------------------------------------------------------------------------

def x_get_compliance_result__mutmut_3(
    db: Session,
    result_id: UUID,
) -> ComplianceResult | None:
    return db.scalar(
        select(None).where(
            ComplianceResult.id == result_id,
        )
    )


# ---------------------------------------------------------------------------
# Compliance Results
# ---------------------------------------------------------------------------

def x_get_compliance_result__mutmut_4(
    db: Session,
    result_id: UUID,
) -> ComplianceResult | None:
    return db.scalar(
        select(ComplianceResult).where(
            ComplianceResult.id != result_id,
        )
    )

mutants_x_get_compliance_result__mutmut['_mutmut_orig'] = x_get_compliance_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_compliance_result__mutmut['x_get_compliance_result__mutmut_1'] = x_get_compliance_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_compliance_result__mutmut['x_get_compliance_result__mutmut_2'] = x_get_compliance_result__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_compliance_result__mutmut['x_get_compliance_result__mutmut_3'] = x_get_compliance_result__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_compliance_result__mutmut['x_get_compliance_result__mutmut_4'] = x_get_compliance_result__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_project_compliance_results__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_project_compliance_results__mutmut)
def get_project_compliance_results(
    db: Session,
    project_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(ComplianceResult)
            .where(
                ComplianceResult.project_id == project_id,
            )
            .order_by(ComplianceResult.evaluated_at.desc())
        ).all()
    )


def x_get_project_compliance_results__mutmut_orig(
    db: Session,
    project_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(ComplianceResult)
            .where(
                ComplianceResult.project_id == project_id,
            )
            .order_by(ComplianceResult.evaluated_at.desc())
        ).all()
    )


def x_get_project_compliance_results__mutmut_1(
    db: Session,
    project_id: UUID,
) -> list[ComplianceResult]:
    return list(
        None
    )


def x_get_project_compliance_results__mutmut_2(
    db: Session,
    project_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            None
        ).all()
    )


def x_get_project_compliance_results__mutmut_3(
    db: Session,
    project_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(ComplianceResult)
            .where(
                ComplianceResult.project_id == project_id,
            )
            .order_by(None)
        ).all()
    )


def x_get_project_compliance_results__mutmut_4(
    db: Session,
    project_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(ComplianceResult)
            .where(
                None,
            )
            .order_by(ComplianceResult.evaluated_at.desc())
        ).all()
    )


def x_get_project_compliance_results__mutmut_5(
    db: Session,
    project_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(None)
            .where(
                ComplianceResult.project_id == project_id,
            )
            .order_by(ComplianceResult.evaluated_at.desc())
        ).all()
    )


def x_get_project_compliance_results__mutmut_6(
    db: Session,
    project_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(ComplianceResult)
            .where(
                ComplianceResult.project_id != project_id,
            )
            .order_by(ComplianceResult.evaluated_at.desc())
        ).all()
    )

mutants_x_get_project_compliance_results__mutmut['_mutmut_orig'] = x_get_project_compliance_results__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_project_compliance_results__mutmut['x_get_project_compliance_results__mutmut_1'] = x_get_project_compliance_results__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_project_compliance_results__mutmut['x_get_project_compliance_results__mutmut_2'] = x_get_project_compliance_results__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_project_compliance_results__mutmut['x_get_project_compliance_results__mutmut_3'] = x_get_project_compliance_results__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_project_compliance_results__mutmut['x_get_project_compliance_results__mutmut_4'] = x_get_project_compliance_results__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_project_compliance_results__mutmut['x_get_project_compliance_results__mutmut_5'] = x_get_project_compliance_results__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_project_compliance_results__mutmut['x_get_project_compliance_results__mutmut_6'] = x_get_project_compliance_results__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_evaluation_run_compliance_results__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_get_evaluation_run_compliance_results__mutmut)
def get_evaluation_run_compliance_results(
    db: Session,
    evaluation_run_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(ComplianceResult)
            .where(
                ComplianceResult.evaluation_run_id == evaluation_run_id,
            )
            .order_by(ComplianceResult.evaluated_at.asc())
        ).all()
    )

def x_get_evaluation_run_compliance_results__mutmut_orig(
    db: Session,
    evaluation_run_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(ComplianceResult)
            .where(
                ComplianceResult.evaluation_run_id == evaluation_run_id,
            )
            .order_by(ComplianceResult.evaluated_at.asc())
        ).all()
    )

def x_get_evaluation_run_compliance_results__mutmut_1(
    db: Session,
    evaluation_run_id: UUID,
) -> list[ComplianceResult]:
    return list(
        None
    )

def x_get_evaluation_run_compliance_results__mutmut_2(
    db: Session,
    evaluation_run_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            None
        ).all()
    )

def x_get_evaluation_run_compliance_results__mutmut_3(
    db: Session,
    evaluation_run_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(ComplianceResult)
            .where(
                ComplianceResult.evaluation_run_id == evaluation_run_id,
            )
            .order_by(None)
        ).all()
    )

def x_get_evaluation_run_compliance_results__mutmut_4(
    db: Session,
    evaluation_run_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(ComplianceResult)
            .where(
                None,
            )
            .order_by(ComplianceResult.evaluated_at.asc())
        ).all()
    )

def x_get_evaluation_run_compliance_results__mutmut_5(
    db: Session,
    evaluation_run_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(None)
            .where(
                ComplianceResult.evaluation_run_id == evaluation_run_id,
            )
            .order_by(ComplianceResult.evaluated_at.asc())
        ).all()
    )

def x_get_evaluation_run_compliance_results__mutmut_6(
    db: Session,
    evaluation_run_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(ComplianceResult)
            .where(
                ComplianceResult.evaluation_run_id != evaluation_run_id,
            )
            .order_by(ComplianceResult.evaluated_at.asc())
        ).all()
    )

mutants_x_get_evaluation_run_compliance_results__mutmut['_mutmut_orig'] = x_get_evaluation_run_compliance_results__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_evaluation_run_compliance_results__mutmut['x_get_evaluation_run_compliance_results__mutmut_1'] = x_get_evaluation_run_compliance_results__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_evaluation_run_compliance_results__mutmut['x_get_evaluation_run_compliance_results__mutmut_2'] = x_get_evaluation_run_compliance_results__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_evaluation_run_compliance_results__mutmut['x_get_evaluation_run_compliance_results__mutmut_3'] = x_get_evaluation_run_compliance_results__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_evaluation_run_compliance_results__mutmut['x_get_evaluation_run_compliance_results__mutmut_4'] = x_get_evaluation_run_compliance_results__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_evaluation_run_compliance_results__mutmut['x_get_evaluation_run_compliance_results__mutmut_5'] = x_get_evaluation_run_compliance_results__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_evaluation_run_compliance_results__mutmut['x_get_evaluation_run_compliance_results__mutmut_6'] = x_get_evaluation_run_compliance_results__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_rule_compliance_results__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_rule_compliance_results__mutmut)
def get_rule_compliance_results(
    db: Session,
    rule_version_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(ComplianceResult)
            .where(
                ComplianceResult.rule_version_id == rule_version_id,
            )
            .order_by(ComplianceResult.evaluated_at.desc())
        ).all()
    )


def x_get_rule_compliance_results__mutmut_orig(
    db: Session,
    rule_version_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(ComplianceResult)
            .where(
                ComplianceResult.rule_version_id == rule_version_id,
            )
            .order_by(ComplianceResult.evaluated_at.desc())
        ).all()
    )


def x_get_rule_compliance_results__mutmut_1(
    db: Session,
    rule_version_id: UUID,
) -> list[ComplianceResult]:
    return list(
        None
    )


def x_get_rule_compliance_results__mutmut_2(
    db: Session,
    rule_version_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            None
        ).all()
    )


def x_get_rule_compliance_results__mutmut_3(
    db: Session,
    rule_version_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(ComplianceResult)
            .where(
                ComplianceResult.rule_version_id == rule_version_id,
            )
            .order_by(None)
        ).all()
    )


def x_get_rule_compliance_results__mutmut_4(
    db: Session,
    rule_version_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(ComplianceResult)
            .where(
                None,
            )
            .order_by(ComplianceResult.evaluated_at.desc())
        ).all()
    )


def x_get_rule_compliance_results__mutmut_5(
    db: Session,
    rule_version_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(None)
            .where(
                ComplianceResult.rule_version_id == rule_version_id,
            )
            .order_by(ComplianceResult.evaluated_at.desc())
        ).all()
    )


def x_get_rule_compliance_results__mutmut_6(
    db: Session,
    rule_version_id: UUID,
) -> list[ComplianceResult]:
    return list(
        db.scalars(
            select(ComplianceResult)
            .where(
                ComplianceResult.rule_version_id != rule_version_id,
            )
            .order_by(ComplianceResult.evaluated_at.desc())
        ).all()
    )

mutants_x_get_rule_compliance_results__mutmut['_mutmut_orig'] = x_get_rule_compliance_results__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_rule_compliance_results__mutmut['x_get_rule_compliance_results__mutmut_1'] = x_get_rule_compliance_results__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_rule_compliance_results__mutmut['x_get_rule_compliance_results__mutmut_2'] = x_get_rule_compliance_results__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_rule_compliance_results__mutmut['x_get_rule_compliance_results__mutmut_3'] = x_get_rule_compliance_results__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_rule_compliance_results__mutmut['x_get_rule_compliance_results__mutmut_4'] = x_get_rule_compliance_results__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_rule_compliance_results__mutmut['x_get_rule_compliance_results__mutmut_5'] = x_get_rule_compliance_results__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_rule_compliance_results__mutmut['x_get_rule_compliance_results__mutmut_6'] = x_get_rule_compliance_results__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_project_rule_compliance_result__mutmut)
def get_project_rule_compliance_result(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(ComplianceResult).where(
        ComplianceResult.project_id == project_id,
        ComplianceResult.rule_version_id == rule_version_id,
    )

    if evaluation_run_id is not None:
        query = query.where(
            ComplianceResult.evaluation_run_id == evaluation_run_id,
        )

    return db.scalar(
        query.order_by(
            ComplianceResult.evaluated_at.desc()
        ).limit(1)
    )


def x_get_project_rule_compliance_result__mutmut_orig(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(ComplianceResult).where(
        ComplianceResult.project_id == project_id,
        ComplianceResult.rule_version_id == rule_version_id,
    )

    if evaluation_run_id is not None:
        query = query.where(
            ComplianceResult.evaluation_run_id == evaluation_run_id,
        )

    return db.scalar(
        query.order_by(
            ComplianceResult.evaluated_at.desc()
        ).limit(1)
    )


def x_get_project_rule_compliance_result__mutmut_1(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = None

    if evaluation_run_id is not None:
        query = query.where(
            ComplianceResult.evaluation_run_id == evaluation_run_id,
        )

    return db.scalar(
        query.order_by(
            ComplianceResult.evaluated_at.desc()
        ).limit(1)
    )


def x_get_project_rule_compliance_result__mutmut_2(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(ComplianceResult).where(
        None,
        ComplianceResult.rule_version_id == rule_version_id,
    )

    if evaluation_run_id is not None:
        query = query.where(
            ComplianceResult.evaluation_run_id == evaluation_run_id,
        )

    return db.scalar(
        query.order_by(
            ComplianceResult.evaluated_at.desc()
        ).limit(1)
    )


def x_get_project_rule_compliance_result__mutmut_3(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(ComplianceResult).where(
        ComplianceResult.project_id == project_id,
        None,
    )

    if evaluation_run_id is not None:
        query = query.where(
            ComplianceResult.evaluation_run_id == evaluation_run_id,
        )

    return db.scalar(
        query.order_by(
            ComplianceResult.evaluated_at.desc()
        ).limit(1)
    )


def x_get_project_rule_compliance_result__mutmut_4(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(ComplianceResult).where(
        ComplianceResult.rule_version_id == rule_version_id,
    )

    if evaluation_run_id is not None:
        query = query.where(
            ComplianceResult.evaluation_run_id == evaluation_run_id,
        )

    return db.scalar(
        query.order_by(
            ComplianceResult.evaluated_at.desc()
        ).limit(1)
    )


def x_get_project_rule_compliance_result__mutmut_5(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(ComplianceResult).where(
        ComplianceResult.project_id == project_id,
        )

    if evaluation_run_id is not None:
        query = query.where(
            ComplianceResult.evaluation_run_id == evaluation_run_id,
        )

    return db.scalar(
        query.order_by(
            ComplianceResult.evaluated_at.desc()
        ).limit(1)
    )


def x_get_project_rule_compliance_result__mutmut_6(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(None).where(
        ComplianceResult.project_id == project_id,
        ComplianceResult.rule_version_id == rule_version_id,
    )

    if evaluation_run_id is not None:
        query = query.where(
            ComplianceResult.evaluation_run_id == evaluation_run_id,
        )

    return db.scalar(
        query.order_by(
            ComplianceResult.evaluated_at.desc()
        ).limit(1)
    )


def x_get_project_rule_compliance_result__mutmut_7(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(ComplianceResult).where(
        ComplianceResult.project_id != project_id,
        ComplianceResult.rule_version_id == rule_version_id,
    )

    if evaluation_run_id is not None:
        query = query.where(
            ComplianceResult.evaluation_run_id == evaluation_run_id,
        )

    return db.scalar(
        query.order_by(
            ComplianceResult.evaluated_at.desc()
        ).limit(1)
    )


def x_get_project_rule_compliance_result__mutmut_8(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(ComplianceResult).where(
        ComplianceResult.project_id == project_id,
        ComplianceResult.rule_version_id != rule_version_id,
    )

    if evaluation_run_id is not None:
        query = query.where(
            ComplianceResult.evaluation_run_id == evaluation_run_id,
        )

    return db.scalar(
        query.order_by(
            ComplianceResult.evaluated_at.desc()
        ).limit(1)
    )


def x_get_project_rule_compliance_result__mutmut_9(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(ComplianceResult).where(
        ComplianceResult.project_id == project_id,
        ComplianceResult.rule_version_id == rule_version_id,
    )

    if evaluation_run_id is None:
        query = query.where(
            ComplianceResult.evaluation_run_id == evaluation_run_id,
        )

    return db.scalar(
        query.order_by(
            ComplianceResult.evaluated_at.desc()
        ).limit(1)
    )


def x_get_project_rule_compliance_result__mutmut_10(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(ComplianceResult).where(
        ComplianceResult.project_id == project_id,
        ComplianceResult.rule_version_id == rule_version_id,
    )

    if evaluation_run_id is not None:
        query = None

    return db.scalar(
        query.order_by(
            ComplianceResult.evaluated_at.desc()
        ).limit(1)
    )


def x_get_project_rule_compliance_result__mutmut_11(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(ComplianceResult).where(
        ComplianceResult.project_id == project_id,
        ComplianceResult.rule_version_id == rule_version_id,
    )

    if evaluation_run_id is not None:
        query = query.where(
            None,
        )

    return db.scalar(
        query.order_by(
            ComplianceResult.evaluated_at.desc()
        ).limit(1)
    )


def x_get_project_rule_compliance_result__mutmut_12(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(ComplianceResult).where(
        ComplianceResult.project_id == project_id,
        ComplianceResult.rule_version_id == rule_version_id,
    )

    if evaluation_run_id is not None:
        query = query.where(
            ComplianceResult.evaluation_run_id != evaluation_run_id,
        )

    return db.scalar(
        query.order_by(
            ComplianceResult.evaluated_at.desc()
        ).limit(1)
    )


def x_get_project_rule_compliance_result__mutmut_13(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(ComplianceResult).where(
        ComplianceResult.project_id == project_id,
        ComplianceResult.rule_version_id == rule_version_id,
    )

    if evaluation_run_id is not None:
        query = query.where(
            ComplianceResult.evaluation_run_id == evaluation_run_id,
        )

    return db.scalar(
        None
    )


def x_get_project_rule_compliance_result__mutmut_14(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(ComplianceResult).where(
        ComplianceResult.project_id == project_id,
        ComplianceResult.rule_version_id == rule_version_id,
    )

    if evaluation_run_id is not None:
        query = query.where(
            ComplianceResult.evaluation_run_id == evaluation_run_id,
        )

    return db.scalar(
        query.order_by(
            ComplianceResult.evaluated_at.desc()
        ).limit(None)
    )


def x_get_project_rule_compliance_result__mutmut_15(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(ComplianceResult).where(
        ComplianceResult.project_id == project_id,
        ComplianceResult.rule_version_id == rule_version_id,
    )

    if evaluation_run_id is not None:
        query = query.where(
            ComplianceResult.evaluation_run_id == evaluation_run_id,
        )

    return db.scalar(
        query.order_by(
            None
        ).limit(1)
    )


def x_get_project_rule_compliance_result__mutmut_16(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
    evaluation_run_id: UUID | None = None,
) -> ComplianceResult | None:
    query = select(ComplianceResult).where(
        ComplianceResult.project_id == project_id,
        ComplianceResult.rule_version_id == rule_version_id,
    )

    if evaluation_run_id is not None:
        query = query.where(
            ComplianceResult.evaluation_run_id == evaluation_run_id,
        )

    return db.scalar(
        query.order_by(
            ComplianceResult.evaluated_at.desc()
        ).limit(2)
    )

mutants_x_get_project_rule_compliance_result__mutmut['_mutmut_orig'] = x_get_project_rule_compliance_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut['x_get_project_rule_compliance_result__mutmut_1'] = x_get_project_rule_compliance_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut['x_get_project_rule_compliance_result__mutmut_2'] = x_get_project_rule_compliance_result__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut['x_get_project_rule_compliance_result__mutmut_3'] = x_get_project_rule_compliance_result__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut['x_get_project_rule_compliance_result__mutmut_4'] = x_get_project_rule_compliance_result__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut['x_get_project_rule_compliance_result__mutmut_5'] = x_get_project_rule_compliance_result__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut['x_get_project_rule_compliance_result__mutmut_6'] = x_get_project_rule_compliance_result__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut['x_get_project_rule_compliance_result__mutmut_7'] = x_get_project_rule_compliance_result__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut['x_get_project_rule_compliance_result__mutmut_8'] = x_get_project_rule_compliance_result__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut['x_get_project_rule_compliance_result__mutmut_9'] = x_get_project_rule_compliance_result__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut['x_get_project_rule_compliance_result__mutmut_10'] = x_get_project_rule_compliance_result__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut['x_get_project_rule_compliance_result__mutmut_11'] = x_get_project_rule_compliance_result__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut['x_get_project_rule_compliance_result__mutmut_12'] = x_get_project_rule_compliance_result__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut['x_get_project_rule_compliance_result__mutmut_13'] = x_get_project_rule_compliance_result__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut['x_get_project_rule_compliance_result__mutmut_14'] = x_get_project_rule_compliance_result__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut['x_get_project_rule_compliance_result__mutmut_15'] = x_get_project_rule_compliance_result__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_project_rule_compliance_result__mutmut['x_get_project_rule_compliance_result__mutmut_16'] = x_get_project_rule_compliance_result__mutmut_16 # type: ignore # mutmut generated
mutants_x_create_compliance_result__mutmut: MutantDict = {}  # type: ignore



@_mutmut_mutated(mutants_x_create_compliance_result__mutmut)
def create_compliance_result(
    db: Session,
    result: ComplianceResult,
) -> ComplianceResult:
    db.add(result)
    db.flush()
    return result



def x_create_compliance_result__mutmut_orig(
    db: Session,
    result: ComplianceResult,
) -> ComplianceResult:
    db.add(result)
    db.flush()
    return result



def x_create_compliance_result__mutmut_1(
    db: Session,
    result: ComplianceResult,
) -> ComplianceResult:
    db.add(None)
    db.flush()
    return result

mutants_x_create_compliance_result__mutmut['_mutmut_orig'] = x_create_compliance_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_compliance_result__mutmut['x_create_compliance_result__mutmut_1'] = x_create_compliance_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_finding__mutmut: MutantDict = {}  # type: ignore


# ---------------------------------------------------------------------------
# Findings
# ---------------------------------------------------------------------------

@_mutmut_mutated(mutants_x_get_finding__mutmut)
def get_finding(
    db: Session,
    finding_id: UUID,
) -> Finding | None:
    return db.scalar(
        select(Finding).where(
            Finding.id == finding_id,
        )
    )


# ---------------------------------------------------------------------------
# Findings
# ---------------------------------------------------------------------------

def x_get_finding__mutmut_orig(
    db: Session,
    finding_id: UUID,
) -> Finding | None:
    return db.scalar(
        select(Finding).where(
            Finding.id == finding_id,
        )
    )


# ---------------------------------------------------------------------------
# Findings
# ---------------------------------------------------------------------------

def x_get_finding__mutmut_1(
    db: Session,
    finding_id: UUID,
) -> Finding | None:
    return db.scalar(
        None
    )


# ---------------------------------------------------------------------------
# Findings
# ---------------------------------------------------------------------------

def x_get_finding__mutmut_2(
    db: Session,
    finding_id: UUID,
) -> Finding | None:
    return db.scalar(
        select(Finding).where(
            None,
        )
    )


# ---------------------------------------------------------------------------
# Findings
# ---------------------------------------------------------------------------

def x_get_finding__mutmut_3(
    db: Session,
    finding_id: UUID,
) -> Finding | None:
    return db.scalar(
        select(None).where(
            Finding.id == finding_id,
        )
    )


# ---------------------------------------------------------------------------
# Findings
# ---------------------------------------------------------------------------

def x_get_finding__mutmut_4(
    db: Session,
    finding_id: UUID,
) -> Finding | None:
    return db.scalar(
        select(Finding).where(
            Finding.id != finding_id,
        )
    )

mutants_x_get_finding__mutmut['_mutmut_orig'] = x_get_finding__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_finding__mutmut['x_get_finding__mutmut_1'] = x_get_finding__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_finding__mutmut['x_get_finding__mutmut_2'] = x_get_finding__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_finding__mutmut['x_get_finding__mutmut_3'] = x_get_finding__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_finding__mutmut['x_get_finding__mutmut_4'] = x_get_finding__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_result_findings__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_result_findings__mutmut)
def get_result_findings(
    db: Session,
    compliance_result_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(Finding)
            .where(
                Finding.compliance_result_id == compliance_result_id,
            )
            .order_by(Finding.created_at.desc())
        ).all()
    )


def x_get_result_findings__mutmut_orig(
    db: Session,
    compliance_result_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(Finding)
            .where(
                Finding.compliance_result_id == compliance_result_id,
            )
            .order_by(Finding.created_at.desc())
        ).all()
    )


def x_get_result_findings__mutmut_1(
    db: Session,
    compliance_result_id: UUID,
) -> list[Finding]:
    return list(
        None
    )


def x_get_result_findings__mutmut_2(
    db: Session,
    compliance_result_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            None
        ).all()
    )


def x_get_result_findings__mutmut_3(
    db: Session,
    compliance_result_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(Finding)
            .where(
                Finding.compliance_result_id == compliance_result_id,
            )
            .order_by(None)
        ).all()
    )


def x_get_result_findings__mutmut_4(
    db: Session,
    compliance_result_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(Finding)
            .where(
                None,
            )
            .order_by(Finding.created_at.desc())
        ).all()
    )


def x_get_result_findings__mutmut_5(
    db: Session,
    compliance_result_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(None)
            .where(
                Finding.compliance_result_id == compliance_result_id,
            )
            .order_by(Finding.created_at.desc())
        ).all()
    )


def x_get_result_findings__mutmut_6(
    db: Session,
    compliance_result_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(Finding)
            .where(
                Finding.compliance_result_id != compliance_result_id,
            )
            .order_by(Finding.created_at.desc())
        ).all()
    )

mutants_x_get_result_findings__mutmut['_mutmut_orig'] = x_get_result_findings__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_result_findings__mutmut['x_get_result_findings__mutmut_1'] = x_get_result_findings__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_result_findings__mutmut['x_get_result_findings__mutmut_2'] = x_get_result_findings__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_result_findings__mutmut['x_get_result_findings__mutmut_3'] = x_get_result_findings__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_result_findings__mutmut['x_get_result_findings__mutmut_4'] = x_get_result_findings__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_result_findings__mutmut['x_get_result_findings__mutmut_5'] = x_get_result_findings__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_result_findings__mutmut['x_get_result_findings__mutmut_6'] = x_get_result_findings__mutmut_6 # type: ignore # mutmut generated
mutants_x_create_finding__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_create_finding__mutmut)
def create_finding(
    db: Session,
    finding: Finding,
) -> Finding:
    db.add(finding)
    db.flush()
    return finding


def x_create_finding__mutmut_orig(
    db: Session,
    finding: Finding,
) -> Finding:
    db.add(finding)
    db.flush()
    return finding


def x_create_finding__mutmut_1(
    db: Session,
    finding: Finding,
) -> Finding:
    db.add(None)
    db.flush()
    return finding

mutants_x_create_finding__mutmut['_mutmut_orig'] = x_create_finding__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_finding__mutmut['x_create_finding__mutmut_1'] = x_create_finding__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_project_findings__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_project_findings__mutmut)
def get_project_findings(
    db: Session,
    project_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(Finding)
            .join(
                ComplianceResult,
                Finding.compliance_result_id == ComplianceResult.id,
            )
            .where(
                ComplianceResult.project_id == project_id,
            )
            .order_by(Finding.created_at.desc())
        ).all()
    )


def x_get_project_findings__mutmut_orig(
    db: Session,
    project_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(Finding)
            .join(
                ComplianceResult,
                Finding.compliance_result_id == ComplianceResult.id,
            )
            .where(
                ComplianceResult.project_id == project_id,
            )
            .order_by(Finding.created_at.desc())
        ).all()
    )


def x_get_project_findings__mutmut_1(
    db: Session,
    project_id: UUID,
) -> list[Finding]:
    return list(
        None
    )


def x_get_project_findings__mutmut_2(
    db: Session,
    project_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            None
        ).all()
    )


def x_get_project_findings__mutmut_3(
    db: Session,
    project_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(Finding)
            .join(
                ComplianceResult,
                Finding.compliance_result_id == ComplianceResult.id,
            )
            .where(
                ComplianceResult.project_id == project_id,
            )
            .order_by(None)
        ).all()
    )


def x_get_project_findings__mutmut_4(
    db: Session,
    project_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(Finding)
            .join(
                ComplianceResult,
                Finding.compliance_result_id == ComplianceResult.id,
            )
            .where(
                None,
            )
            .order_by(Finding.created_at.desc())
        ).all()
    )


def x_get_project_findings__mutmut_5(
    db: Session,
    project_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(Finding)
            .join(
                None,
                Finding.compliance_result_id == ComplianceResult.id,
            )
            .where(
                ComplianceResult.project_id == project_id,
            )
            .order_by(Finding.created_at.desc())
        ).all()
    )


def x_get_project_findings__mutmut_6(
    db: Session,
    project_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(Finding)
            .join(
                ComplianceResult,
                None,
            )
            .where(
                ComplianceResult.project_id == project_id,
            )
            .order_by(Finding.created_at.desc())
        ).all()
    )


def x_get_project_findings__mutmut_7(
    db: Session,
    project_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(Finding)
            .join(
                Finding.compliance_result_id == ComplianceResult.id,
            )
            .where(
                ComplianceResult.project_id == project_id,
            )
            .order_by(Finding.created_at.desc())
        ).all()
    )


def x_get_project_findings__mutmut_8(
    db: Session,
    project_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(Finding)
            .join(
                ComplianceResult,
                )
            .where(
                ComplianceResult.project_id == project_id,
            )
            .order_by(Finding.created_at.desc())
        ).all()
    )


def x_get_project_findings__mutmut_9(
    db: Session,
    project_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(None)
            .join(
                ComplianceResult,
                Finding.compliance_result_id == ComplianceResult.id,
            )
            .where(
                ComplianceResult.project_id == project_id,
            )
            .order_by(Finding.created_at.desc())
        ).all()
    )


def x_get_project_findings__mutmut_10(
    db: Session,
    project_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(Finding)
            .join(
                ComplianceResult,
                Finding.compliance_result_id != ComplianceResult.id,
            )
            .where(
                ComplianceResult.project_id == project_id,
            )
            .order_by(Finding.created_at.desc())
        ).all()
    )


def x_get_project_findings__mutmut_11(
    db: Session,
    project_id: UUID,
) -> list[Finding]:
    return list(
        db.scalars(
            select(Finding)
            .join(
                ComplianceResult,
                Finding.compliance_result_id == ComplianceResult.id,
            )
            .where(
                ComplianceResult.project_id != project_id,
            )
            .order_by(Finding.created_at.desc())
        ).all()
    )

mutants_x_get_project_findings__mutmut['_mutmut_orig'] = x_get_project_findings__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_project_findings__mutmut['x_get_project_findings__mutmut_1'] = x_get_project_findings__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_project_findings__mutmut['x_get_project_findings__mutmut_2'] = x_get_project_findings__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_project_findings__mutmut['x_get_project_findings__mutmut_3'] = x_get_project_findings__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_project_findings__mutmut['x_get_project_findings__mutmut_4'] = x_get_project_findings__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_project_findings__mutmut['x_get_project_findings__mutmut_5'] = x_get_project_findings__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_project_findings__mutmut['x_get_project_findings__mutmut_6'] = x_get_project_findings__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_project_findings__mutmut['x_get_project_findings__mutmut_7'] = x_get_project_findings__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_project_findings__mutmut['x_get_project_findings__mutmut_8'] = x_get_project_findings__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_project_findings__mutmut['x_get_project_findings__mutmut_9'] = x_get_project_findings__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_project_findings__mutmut['x_get_project_findings__mutmut_10'] = x_get_project_findings__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_project_findings__mutmut['x_get_project_findings__mutmut_11'] = x_get_project_findings__mutmut_11 # type: ignore # mutmut generated
mutants_x_update_finding__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_update_finding__mutmut)
def update_finding(
    db: Session,
    finding: Finding,
) -> Finding:
    db.add(finding)
    db.flush()
    db.refresh(finding)
    return finding


def x_update_finding__mutmut_orig(
    db: Session,
    finding: Finding,
) -> Finding:
    db.add(finding)
    db.flush()
    db.refresh(finding)
    return finding


def x_update_finding__mutmut_1(
    db: Session,
    finding: Finding,
) -> Finding:
    db.add(None)
    db.flush()
    db.refresh(finding)
    return finding


def x_update_finding__mutmut_2(
    db: Session,
    finding: Finding,
) -> Finding:
    db.add(finding)
    db.flush()
    db.refresh(None)
    return finding

mutants_x_update_finding__mutmut['_mutmut_orig'] = x_update_finding__mutmut_orig # type: ignore # mutmut generated
mutants_x_update_finding__mutmut['x_update_finding__mutmut_1'] = x_update_finding__mutmut_1 # type: ignore # mutmut generated
mutants_x_update_finding__mutmut['x_update_finding__mutmut_2'] = x_update_finding__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_discrepancy__mutmut: MutantDict = {}  # type: ignore

# ---------------------------------------------------------------------------
# Discrepancies
# ---------------------------------------------------------------------------

@_mutmut_mutated(mutants_x_get_discrepancy__mutmut)
def get_discrepancy(
    db: Session,
    discrepancy_id: UUID,
) -> Discrepancy | None:
    return db.scalar(
        select(Discrepancy).where(
            Discrepancy.id == discrepancy_id,
        )
    )

# ---------------------------------------------------------------------------
# Discrepancies
# ---------------------------------------------------------------------------

def x_get_discrepancy__mutmut_orig(
    db: Session,
    discrepancy_id: UUID,
) -> Discrepancy | None:
    return db.scalar(
        select(Discrepancy).where(
            Discrepancy.id == discrepancy_id,
        )
    )

# ---------------------------------------------------------------------------
# Discrepancies
# ---------------------------------------------------------------------------

def x_get_discrepancy__mutmut_1(
    db: Session,
    discrepancy_id: UUID,
) -> Discrepancy | None:
    return db.scalar(
        None
    )

# ---------------------------------------------------------------------------
# Discrepancies
# ---------------------------------------------------------------------------

def x_get_discrepancy__mutmut_2(
    db: Session,
    discrepancy_id: UUID,
) -> Discrepancy | None:
    return db.scalar(
        select(Discrepancy).where(
            None,
        )
    )

# ---------------------------------------------------------------------------
# Discrepancies
# ---------------------------------------------------------------------------

def x_get_discrepancy__mutmut_3(
    db: Session,
    discrepancy_id: UUID,
) -> Discrepancy | None:
    return db.scalar(
        select(None).where(
            Discrepancy.id == discrepancy_id,
        )
    )

# ---------------------------------------------------------------------------
# Discrepancies
# ---------------------------------------------------------------------------

def x_get_discrepancy__mutmut_4(
    db: Session,
    discrepancy_id: UUID,
) -> Discrepancy | None:
    return db.scalar(
        select(Discrepancy).where(
            Discrepancy.id != discrepancy_id,
        )
    )

mutants_x_get_discrepancy__mutmut['_mutmut_orig'] = x_get_discrepancy__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_discrepancy__mutmut['x_get_discrepancy__mutmut_1'] = x_get_discrepancy__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_discrepancy__mutmut['x_get_discrepancy__mutmut_2'] = x_get_discrepancy__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_discrepancy__mutmut['x_get_discrepancy__mutmut_3'] = x_get_discrepancy__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_discrepancy__mutmut['x_get_discrepancy__mutmut_4'] = x_get_discrepancy__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_project_discrepancies__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_project_discrepancies__mutmut)
def get_project_discrepancies(
    db: Session,
    project_id: UUID,
) -> list[Discrepancy]:
    return list(
        db.scalars(
            select(Discrepancy)
            .where(
                Discrepancy.project_id == project_id,
            )
            .order_by(Discrepancy.created_at.desc())
        ).all()
    )


def x_get_project_discrepancies__mutmut_orig(
    db: Session,
    project_id: UUID,
) -> list[Discrepancy]:
    return list(
        db.scalars(
            select(Discrepancy)
            .where(
                Discrepancy.project_id == project_id,
            )
            .order_by(Discrepancy.created_at.desc())
        ).all()
    )


def x_get_project_discrepancies__mutmut_1(
    db: Session,
    project_id: UUID,
) -> list[Discrepancy]:
    return list(
        None
    )


def x_get_project_discrepancies__mutmut_2(
    db: Session,
    project_id: UUID,
) -> list[Discrepancy]:
    return list(
        db.scalars(
            None
        ).all()
    )


def x_get_project_discrepancies__mutmut_3(
    db: Session,
    project_id: UUID,
) -> list[Discrepancy]:
    return list(
        db.scalars(
            select(Discrepancy)
            .where(
                Discrepancy.project_id == project_id,
            )
            .order_by(None)
        ).all()
    )


def x_get_project_discrepancies__mutmut_4(
    db: Session,
    project_id: UUID,
) -> list[Discrepancy]:
    return list(
        db.scalars(
            select(Discrepancy)
            .where(
                None,
            )
            .order_by(Discrepancy.created_at.desc())
        ).all()
    )


def x_get_project_discrepancies__mutmut_5(
    db: Session,
    project_id: UUID,
) -> list[Discrepancy]:
    return list(
        db.scalars(
            select(None)
            .where(
                Discrepancy.project_id == project_id,
            )
            .order_by(Discrepancy.created_at.desc())
        ).all()
    )


def x_get_project_discrepancies__mutmut_6(
    db: Session,
    project_id: UUID,
) -> list[Discrepancy]:
    return list(
        db.scalars(
            select(Discrepancy)
            .where(
                Discrepancy.project_id != project_id,
            )
            .order_by(Discrepancy.created_at.desc())
        ).all()
    )

mutants_x_get_project_discrepancies__mutmut['_mutmut_orig'] = x_get_project_discrepancies__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_project_discrepancies__mutmut['x_get_project_discrepancies__mutmut_1'] = x_get_project_discrepancies__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_project_discrepancies__mutmut['x_get_project_discrepancies__mutmut_2'] = x_get_project_discrepancies__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_project_discrepancies__mutmut['x_get_project_discrepancies__mutmut_3'] = x_get_project_discrepancies__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_project_discrepancies__mutmut['x_get_project_discrepancies__mutmut_4'] = x_get_project_discrepancies__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_project_discrepancies__mutmut['x_get_project_discrepancies__mutmut_5'] = x_get_project_discrepancies__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_project_discrepancies__mutmut['x_get_project_discrepancies__mutmut_6'] = x_get_project_discrepancies__mutmut_6 # type: ignore # mutmut generated
mutants_x_create_discrepancy__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_create_discrepancy__mutmut)
def create_discrepancy(
    db: Session,
    discrepancy: Discrepancy,
) -> Discrepancy:
    db.add(discrepancy)
    db.flush()
    return discrepancy


def x_create_discrepancy__mutmut_orig(
    db: Session,
    discrepancy: Discrepancy,
) -> Discrepancy:
    db.add(discrepancy)
    db.flush()
    return discrepancy


def x_create_discrepancy__mutmut_1(
    db: Session,
    discrepancy: Discrepancy,
) -> Discrepancy:
    db.add(None)
    db.flush()
    return discrepancy

mutants_x_create_discrepancy__mutmut['_mutmut_orig'] = x_create_discrepancy__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_discrepancy__mutmut['x_create_discrepancy__mutmut_1'] = x_create_discrepancy__mutmut_1 # type: ignore # mutmut generated