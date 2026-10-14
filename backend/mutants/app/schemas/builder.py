"""
PropertyGuard Builder Profile Schemas
-------------------------------------
Defines Pydantic models for creating builder company profiles and serializing
profile records including verification status and corporate details.
"""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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