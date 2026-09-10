from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ComplianceRuleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    rule_code: str
    name: str
    description: str | None
    category: str
    authority: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime


class RuleVersionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    rule_id: UUID
    version_number: int
    rule_text: str
    required_evidence: dict | None
    evaluation_logic: dict | None
    severity: str
    risk_floor_implication: bool
    effective_from: datetime | None
    effective_to: datetime | None
    is_active: bool
    created_at: datetime

class RuleApplicabilityResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    rule_version_id: UUID
    property_type: str | None
    conditions: dict | None
    is_active: bool
    created_at: datetime


class RuleDependencyResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    rule_version_id: UUID
    depends_on_rule_version_id: UUID
    created_at: datetime


class ComplianceResultResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    project_id: UUID
    rule_version_id: UUID
    outcome: str
    explanation: str | None
    dependency_affected: bool
    evaluated_at: datetime
    created_at: datetime


class FindingResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    compliance_result_id: UUID
    severity: str
    title: str
    description: str
    status: str
    resolution_note: str | None
    resolved_at: datetime | None
    created_at: datetime
    updated_at: datetime


class DiscrepancyResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    project_id: UUID
    field_name: str
    canonical_value: str | None
    conflicting_values: list | None
    severity: str
    status: str
    explanation: str | None
    resolution_note: str | None
    resolved_at: datetime | None
    created_at: datetime
    updated_at: datetime