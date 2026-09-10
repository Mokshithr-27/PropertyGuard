from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class BuilderProfileCreate(BaseModel):
    company_name: str = Field(min_length=1, max_length=255)
    registration_number: str | None = Field(
        default=None,
        max_length=100,
    )
    address: str | None = None


class BuilderProfileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    company_name: str
    registration_number: str | None
    address: str | None
    verification_status: str
    created_at: datetime
    updated_at: datetime