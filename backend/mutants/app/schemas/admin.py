"""
PropertyGuard Admin Request Schemas
-----------------------------------
Defines Pydantic request models for administrator actions, such as verifying/rejecting
builder profiles and approving/rejecting real estate project versions.
"""

from pydantic import BaseModel, Field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class BuilderVerificationRequest(BaseModel):
    status: str = Field(
        pattern="^(VERIFIED|REJECTED|SUSPENDED)$"
    )
    reason: str | None = None


class ProjectVersionReviewRequest(BaseModel):
    status: str = Field(
        pattern="^(APPROVED|REJECTED)$"
    )
    reason: str | None = None