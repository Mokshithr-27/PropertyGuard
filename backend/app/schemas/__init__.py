"""
PropertyGuard Pydantic Schemas Package
--------------------------------------
Exports request validation and response serialization schemas for documents,
auth, projects, compliance, administration, and analysis entities.
"""

from app.schemas.document import (
    DocumentCreate,
    DocumentDetailResponse,
    DocumentResponse,
    DocumentVersionResponse,
)

__all__ = [
    "DocumentCreate",
    "DocumentDetailResponse",
    "DocumentResponse",
    "DocumentVersionResponse",
]