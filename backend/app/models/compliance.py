import uuid
from datetime import datetime

from sqlalchemy import (
    JSON,
    Boolean,
    CheckConstraint,
    DateTime,
    Enum,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    Uuid,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class ComplianceRule(Base):
    __tablename__ = "compliance_rules"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    rule_code: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    authority: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    versions = relationship(
        "RuleVersion",
        back_populates="rule",
        cascade="all, delete-orphan",
    )


class RuleVersion(Base):
    __tablename__ = "rule_versions"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    rule_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey(
            "compliance_rules.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    version_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    rule_text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )


    required_evidence: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    evaluation_logic: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    severity: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="MEDIUM",
    )

    risk_floor_implication: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    effective_from: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    effective_to: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
    )

    rule = relationship(
        "ComplianceRule",
        back_populates="versions",
    )

    applicability_rules = relationship(
        "RuleApplicability",
        back_populates="rule_version",
        cascade="all, delete-orphan",
    )

    dependencies = relationship(
        "RuleDependency",
        foreign_keys="RuleDependency.rule_version_id",
        back_populates="rule_version",
        cascade="all, delete-orphan",
    )

    dependent_on = relationship(
        "RuleDependency",
        foreign_keys="RuleDependency.depends_on_rule_version_id",
        back_populates="depends_on_rule_version",
    )

    compliance_results = relationship(
        "ComplianceResult",
        back_populates="rule_version",
    )

    __table_args__ = (
        Index(
            "uq_rule_version_number",
            "rule_id",
            "version_number",
            unique=True,
        ),
    )


class RuleApplicability(Base):
    __tablename__ = "rule_applicability"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    rule_version_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey(
            "rule_versions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    property_type: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    conditions: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
    )

    rule_version = relationship(
        "RuleVersion",
        back_populates="applicability_rules",
    )


class RuleDependency(Base):
    __tablename__ = "rule_dependencies"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    rule_version_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey(
            "rule_versions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    depends_on_rule_version_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey(
            "rule_versions.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
        index=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
    )

    rule_version = relationship(
        "RuleVersion",
        foreign_keys=[rule_version_id],
        back_populates="dependencies",
    )

    depends_on_rule_version = relationship(
        "RuleVersion",
        foreign_keys=[depends_on_rule_version_id],
        back_populates="dependent_on",
    )

    __table_args__ = (
        Index(
            "uq_rule_dependency",
            "rule_version_id",
            "depends_on_rule_version_id",
            unique=True,
        ),
        CheckConstraint(
            "rule_version_id <> depends_on_rule_version_id",
            name="ck_rule_dependency_not_self",
        ),
    )


class ComplianceResult(Base):
    __tablename__ = "compliance_results"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    project_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey(
            "projects.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    rule_version_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey(
            "rule_versions.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
        index=True,
    )

    outcome: Mapped[str] = mapped_column(
        Enum(
            "PASS",
            "FAIL",
            "NEEDS_REVIEW",
            "NOT_APPLICABLE",
            name="compliance_outcome",
        ),
        nullable=False,
    )

    explanation: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    dependency_affected: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    evaluated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
    )

    project = relationship(
        "Project",
    )

    rule_version = relationship(
        "RuleVersion",
        back_populates="compliance_results",
    )

    findings = relationship(
        "Finding",
        back_populates="compliance_result",
        cascade="all, delete-orphan",
    )


class Finding(Base):
    __tablename__ = "findings"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    compliance_result_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey(
            "compliance_results.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    severity: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="OPEN",
    )

    resolution_note: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    resolved_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    compliance_result = relationship(
        "ComplianceResult",
        back_populates="findings",
    )


class Discrepancy(Base):
    __tablename__ = "discrepancies"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    project_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey(
            "projects.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    field_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    canonical_value: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    conflicting_values: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    severity: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="OPEN",
    )

    explanation: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    resolution_note: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    resolved_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    project = relationship(
        "Project",
    )