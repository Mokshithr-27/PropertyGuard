from pydantic import BaseModel, Field


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