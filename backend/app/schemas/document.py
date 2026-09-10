from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DocumentCreate(BaseModel):
    project_id: UUID
    document_type: str
    title: str = Field(min_length=1, max_length=255)
    description: str | None = None
    visibility: str = "PRIVATE"
    authority_level: int | None = None
    expiry_date: datetime | None = None


class DocumentVersionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    document_id: UUID
    version_number: int
    file_name: str
    mime_type: str
    file_size: int
    file_hash: str
    storage_key: str
    uploaded_by: UUID
    processing_status: str
    created_at: datetime
    deleted_at: datetime | None


class DocumentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    project_id: UUID
    document_type: str
    title: str
    description: str | None
    visibility: str
    authority_level: int | None
    expiry_date: datetime | None
    status: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None


class DocumentDetailResponse(DocumentResponse):
    versions: list[DocumentVersionResponse] = []