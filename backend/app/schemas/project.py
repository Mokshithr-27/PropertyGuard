from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


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