from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field

class ReraVerificationRequest(BaseModel):
    registration_number: str = Field(min_length=3, max_length=150)
    expected_project_name: str | None = Field(default=None, max_length=255)
    expected_promoter_name: str | None = Field(default=None, max_length=255)

class ReraVerificationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    project_id: UUID
    registration_number: str
    source_url: str
    status: str
    source_title: str | None
    matched_project_name: str | None
    matched_promoter_name: str | None
    evidence: dict | None
    message: str
    verified_by_user_id: UUID
    checked_at: datetime
