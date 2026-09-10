import uuid
from datetime import datetime

from sqlalchemy import (
    BigInteger,
    DateTime,
    Enum,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    Uuid,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    project_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    document_type: Mapped[str] = mapped_column(
        Enum(
            "RERA",
            "BUILDING_PERMISSION",
            "SANCTIONED_PLAN",
            "COMMENCEMENT_CERTIFICATE",
            "COMPLETION_OCCUPANCY",
            "LAND_TITLE",
            "ENCUMBRANCE_CERTIFICATE",
            "SALE_DEED_AGREEMENT",
            "FIRE_NOC",
            "OTHER_APPROVAL",
            name="document_type",
        ),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    visibility: Mapped[str] = mapped_column(
        Enum(
            "PRIVATE",
            "BUYER_VISIBLE",
            "PUBLIC_SUMMARY",
            name="document_visibility",
        ),
        nullable=False,
        default="PRIVATE",
    )

    authority_level: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    expiry_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        Enum(
            "ACTIVE",
            "EXPIRED",
            "INACTIVE",
            name="document_status",
        ),
        nullable=False,
        default="ACTIVE",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    project = relationship(
        "Project",
        back_populates="documents",
    )

    versions = relationship(
        "DocumentVersion",
        back_populates="document",
        cascade="all, delete-orphan",
    )


class DocumentVersion(Base):
    __tablename__ = "document_versions"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    document_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("documents.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    version_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    file_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    mime_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    file_size: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    file_hash: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
        index=True,
    )

    storage_key: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        unique=True,
    )

    uploaded_by: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False,
    )

    processing_status: Mapped[str] = mapped_column(
        Enum(
            "UPLOADED",
            "QUEUED",
            "PROCESSING",
            "COMPLETED",
            "FAILED",
            name="document_processing_status",
        ),
        nullable=False,
        default="UPLOADED",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
    )

    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    document = relationship(
        "Document",
        back_populates="versions",
    )

    uploaded_by_user = relationship(
        "User",
        foreign_keys=[uploaded_by],
    )

    __table_args__ = (
        Index(
            "uq_document_version_number",
            "document_id",
            "version_number",
            unique=True,
        ),
    )