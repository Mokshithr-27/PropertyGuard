import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, String, Text, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class BuilderProfile(Base):
    __tablename__ = "builder_profiles"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    company_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    registration_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    address: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    verification_status: Mapped[str] = mapped_column(
        Enum(
            "PENDING",
            "UNDER_REVIEW",
            "VERIFIED",
            "REJECTED",
            "SUSPENDED",
            name="builder_verification_status",
        ),
        nullable=False,
        default="PENDING",
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

    user = relationship(
        "User",
        back_populates="builder_profile",
    )

    verifications = relationship(
        "BuilderVerification",
        back_populates="builder_profile",
        cascade="all, delete-orphan",
    )


class BuilderVerification(Base):
    __tablename__ = "builder_verifications"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    builder_profile_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("builder_profiles.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    verification_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    reference_number: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    evidence_document_id: Mapped[uuid.UUID | None] = mapped_column(
        Uuid,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        Enum(
            "PENDING",
            "UNDER_REVIEW",
            "VERIFIED",
            "REJECTED",
            name="builder_verification_record_status",
        ),
        nullable=False,
        default="PENDING",
    )

    ai_assisted: Mapped[bool] = mapped_column(
        nullable=False,
        default=False,
    )

    admin_id: Mapped[uuid.UUID | None] = mapped_column(
        Uuid,
        nullable=True,
    )

    reason: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    verified_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
    )

    builder_profile = relationship(
        "BuilderProfile",
        back_populates="verifications",
    )