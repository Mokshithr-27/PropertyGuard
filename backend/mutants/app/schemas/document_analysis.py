"""
PropertyGuard Document Analysis Schemas
---------------------------------------
Defines Pydantic models for serializing AI document analysis results and individual
evidence records (field name, value, page number, confidence, snippet).
"""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DocumentEvidenceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    analysis_id: UUID
    field_name: str
    field_value: str | None
    page_number: int | None
    confidence: float | None
    source: str | None
    evidence_text: str | None
    created_at: datetime


class DocumentAnalysisResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    document_version_id: UUID
    status: str
    provider: str | None
    model_name: str | None
    detected_document_type: str | None
    summary: str | None
    structured_data: dict | None
    overall_confidence: float | None
    error_message: str | None
    created_at: datetime
    completed_at: datetime | None
    evidence: list[DocumentEvidenceResponse] = []
