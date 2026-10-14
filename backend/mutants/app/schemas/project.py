"""
PropertyGuard Real Estate Project Hierarchy Schemas
---------------------------------------------------
Defines Pydantic models for project creation, project updates, project details,
version tracking, and building/unit structure representations.
"""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ProjectCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    description: str | None = None
    project_type: str
    address: str | None = None


class ProjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    builder_id: UUID
    name: str
    description: str | None
    project_type: str
    address: str | None
    status: str
    created_at: datetime
    updated_at: datetime


class ProjectVersionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    project_id: UUID
    version_number: int
    status: str
    submitted_by: UUID | None
    reviewed_by: UUID | None
    review_reason: str | None
    created_at: datetime
    updated_at: datetime


class BuildingCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    building_number: str | None = Field(
        default=None,
        max_length=100,
    )
    floors: int | None = Field(
        default=None,
        ge=1,
    )


class BuildingResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    project_version_id: UUID
    name: str
    building_number: str | None
    floors: int | None
    created_at: datetime
    updated_at: datetime


class UnitCreate(BaseModel):
    unit_number: str = Field(
        min_length=1,
        max_length=100,
    )
    floor_number: int | None = None
    unit_type: str | None = Field(
        default=None,
        max_length=100,
    )
    area_sqft: int | None = Field(
        default=None,
        ge=1,
    )


class UnitResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    building_id: UUID
    unit_number: str
    floor_number: int | None
    unit_type: str | None
    area_sqft: int | None
    created_at: datetime


class RequiredDocumentResponse(BaseModel):
    document_type: str
    name: str
    description: str
    is_mandatory: bool
    authority: str
    category: str
    accepted_formats: list[str] = ["application/pdf", "image/png", "image/jpeg"]


class ProjectListItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    builder_id: UUID
    name: str
    description: str | None
    project_type: str
    address: str | None
    status: str
    created_at: datetime
    updated_at: datetime
    latest_version_number: int | None = None
    documents_count: int = 0
    compliance_score: int | None = None


class ProjectUpdate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    description: str | None = None
    project_type: str
    address: str | None = None


class ProjectStatusUpdate(BaseModel):
    status: str = Field(pattern="^(DRAFT|ACTIVE|INACTIVE|SUSPENDED)$")
    reason: str | None = None


class ProjectActionResponse(BaseModel):
    id: UUID
    name: str
    status: str
    message: str

