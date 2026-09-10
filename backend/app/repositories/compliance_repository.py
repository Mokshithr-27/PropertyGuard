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


# ---------------------------------------------------------------------------
# Compliance Rules
# ---------------------------------------------------------------------------

def get_rule(
    db: Session,
    rule_id: UUID,
) -> ComplianceRule | None:
    return db.scalar(
        select(ComplianceRule).where(
            ComplianceRule.id == rule_id,
        )
    )


def get_rule_by_code(
    db: Session,
    rule_code: str,
) -> ComplianceRule | None:
    return db.scalar(
        select(ComplianceRule).where(
            ComplianceRule.rule_code == rule_code,
        )
    )


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


def create_rule(
    db: Session,
    rule: ComplianceRule,
) -> ComplianceRule:
    db.add(rule)
    db.flush()
    return rule


# ---------------------------------------------------------------------------
# Rule Versions
# ---------------------------------------------------------------------------

def get_rule_version(
    db: Session,
    rule_version_id: UUID,
) -> RuleVersion | None:
    return db.scalar(
        select(RuleVersion).where(
            RuleVersion.id == rule_version_id,
        )
    )


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


def create_rule_version(
    db: Session,
    rule_version: RuleVersion,
) -> RuleVersion:
    db.add(rule_version)
    db.flush()
    return rule_version


# ---------------------------------------------------------------------------
# Rule Applicability
# ---------------------------------------------------------------------------

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


def create_rule_applicability(
    db: Session,
    applicability: RuleApplicability,
) -> RuleApplicability:
    db.add(applicability)
    db.flush()
    return applicability


# ---------------------------------------------------------------------------
# Rule Dependencies
# ---------------------------------------------------------------------------

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


def create_rule_dependency(
    db: Session,
    dependency: RuleDependency,
) -> RuleDependency:
    db.add(dependency)
    db.flush()
    return dependency


# ---------------------------------------------------------------------------
# Compliance Results
# ---------------------------------------------------------------------------

def get_compliance_result(
    db: Session,
    result_id: UUID,
) -> ComplianceResult | None:
    return db.scalar(
        select(ComplianceResult).where(
            ComplianceResult.id == result_id,
        )
    )


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


def get_project_rule_compliance_result(
    db: Session,
    project_id: UUID,
    rule_version_id: UUID,
) -> ComplianceResult | None:
    return db.scalar(
        select(ComplianceResult)
        .where(
            ComplianceResult.project_id == project_id,
            ComplianceResult.rule_version_id == rule_version_id,
        )
        .order_by(ComplianceResult.evaluated_at.desc())
        .limit(1)
    )



def create_compliance_result(
    db: Session,
    result: ComplianceResult,
) -> ComplianceResult:
    db.add(result)
    db.flush()
    return result


# ---------------------------------------------------------------------------
# Findings
# ---------------------------------------------------------------------------

def get_finding(
    db: Session,
    finding_id: UUID,
) -> Finding | None:
    return db.scalar(
        select(Finding).where(
            Finding.id == finding_id,
        )
    )


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


def create_finding(
    db: Session,
    finding: Finding,
) -> Finding:
    db.add(finding)
    db.flush()
    return finding


# ---------------------------------------------------------------------------
# Discrepancies
# ---------------------------------------------------------------------------

def get_discrepancy(
    db: Session,
    discrepancy_id: UUID,
) -> Discrepancy | None:
    return db.scalar(
        select(Discrepancy).where(
            Discrepancy.id == discrepancy_id,
        )
    )


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


def create_discrepancy(
    db: Session,
    discrepancy: Discrepancy,
) -> Discrepancy:
    db.add(discrepancy)
    db.flush()
    return discrepancy