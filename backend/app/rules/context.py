from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import UUID


@dataclass(frozen=True)
class DocumentEvidence:
    document_id: UUID
    document_type: str
    title: str
    status: str
    visibility: str
    expiry_date: datetime | None
    latest_version_number: int | None = None


@dataclass(frozen=True)
class EvidenceContext:
    project_id: UUID

    documents: tuple[DocumentEvidence, ...] = ()

    fields: dict[str, Any] = field(default_factory=dict)

    property_type: str | None = None

    evaluation_time: datetime | None = None