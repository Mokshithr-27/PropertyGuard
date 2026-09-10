import uuid
from datetime import datetime

from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
    Uuid,
    Index,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    builder_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("builder_profiles.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    project_type: Mapped[str] = mapped_column(
        Enum(
            "APARTMENT",
            "VILLA",
            "INDIVIDUAL_HOUSE",
            name="project_type",
        ),
        nullable=False,
    )

    address: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        Enum(
            "DRAFT",
            "ACTIVE",
            "INACTIVE",
            name="project_status",
        ),
        nullable=False,
        default="DRAFT",
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

    versions = relationship(
        "ProjectVersion",
        back_populates="project",
        cascade="all, delete-orphan",
    )

    documents = relationship(
        "Document",
        back_populates="project",
        cascade="all, delete-orphan",
    )


class ProjectVersion(Base):
    __tablename__ = "project_versions"

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

    version_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        Enum(
            "DRAFT",
            "PENDING_APPROVAL",
            "APPROVED",
            "REJECTED",
            "SUPERSEDED",
            name="project_version_status",
        ),
        nullable=False,
        default="DRAFT",
    )

    submitted_by: Mapped[uuid.UUID | None] = mapped_column(
        Uuid,
        nullable=True,
    )

    reviewed_by: Mapped[uuid.UUID | None] = mapped_column(
        Uuid,
        nullable=True,
    )

    review_reason: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
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

    project = relationship(
        "Project",
        back_populates="versions",
    )

    buildings = relationship(
        "Building",
        back_populates="project_version",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        Index(
            "uq_project_version_number",
            "project_id",
            "version_number",
            unique=True,
        ),
        Index(
            "uq_project_pending_approval",
            "project_id",
            unique=True,
            postgresql_where=(
                status == "PENDING_APPROVAL"
            ),
        ),
    )


class Building(Base):
    __tablename__ = "buildings"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    project_version_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("project_versions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    building_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    floors: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
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

    project_version = relationship(
        "ProjectVersion",
        back_populates="buildings",
    )

    units = relationship(
        "Unit",
        back_populates="building",
        cascade="all, delete-orphan",
    )


class Unit(Base):
    __tablename__ = "units"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    building_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("buildings.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    unit_number: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    floor_number: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    unit_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    area_sqft: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
    )

    building = relationship(
        "Building",
        back_populates="units",
    )

    __table_args__ = (
        Index(
            "uq_building_unit_number",
            "building_id",
            "unit_number",
            unique=True,
        ),
    )