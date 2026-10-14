"""
PropertyGuard Real Estate Project Management Service
----------------------------------------------------
Coordinates project creation, version incrementing, modification, soft deletion,
and physical hierarchy management (buildings, units) with builder ownership checks.
"""

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.builder import BuilderProfile
from app.models.project import (
    Building,
    Project,
    ProjectVersion,
    Unit,
)


# ---------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------

def get_builder_profile(
    db: Session,
    user_id: UUID,
) -> BuilderProfile | None:
    return db.scalar(
        select(BuilderProfile).where(
            BuilderProfile.user_id == user_id
        )
    )


# ---------------------------------------------------------------------------
# Projects
# ---------------------------------------------------------------------------

def create_project(
    db: Session,
    builder_profile_id: UUID,
    name: str,
    description: str | None,
    project_type: str,
    address: str | None,
) -> Project:
    builder = db.scalar(
        select(BuilderProfile).where(
            BuilderProfile.id == builder_profile_id
        )
    )

    if builder is None:
        raise ValueError("Builder profile not found")

    if builder.verification_status != "VERIFIED":
        raise ValueError(
            "Builder must be VERIFIED to create projects"
        )

    project = Project(
        builder_id=builder.id,
        name=name,
        description=description,
        project_type=project_type,
        address=address,
        status="DRAFT",
    )

    db.add(project)
    db.flush()

    # Automatically initialize initial ProjectVersion (v1 DRAFT)
    initial_version = ProjectVersion(
        project_id=project.id,
        version_number=1,
        status="DRAFT",
        submitted_by=builder.user_id if hasattr(builder, "user_id") else None,
    )
    db.add(initial_version)

    db.commit()
    db.refresh(project)

    return project


def update_project(
    db: Session,
    project: Project,
    *,
    name: str,
    description: str | None,
    project_type: str,
    address: str | None,
) -> Project:
    if project.deleted_at is not None:
        raise ValueError("Project has been deleted")

    project.name = name
    project.description = description
    project.project_type = project_type
    project.address = address

    from datetime import datetime, timezone
    project.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(project)
    return project


def get_project(
    db: Session,
    project_id: UUID,
) -> Project | None:
    return db.scalar(
        select(Project).where(
            Project.id == project_id,
            Project.deleted_at.is_(None),
        )
    )


def get_builder_project(
    db: Session,
    project_id: UUID,
    builder_profile_id: UUID,
) -> Project | None:
    return db.scalar(
        select(Project).where(
            Project.id == project_id,
            Project.builder_id == builder_profile_id,
            Project.deleted_at.is_(None),
        )
    )


def get_builder_projects(
    db: Session,
    builder_profile_id: UUID,
) -> list[Project]:
    return list(
        db.scalars(
            select(Project)
            .where(
                Project.builder_id == builder_profile_id,
                Project.deleted_at.is_(None),
            )
            .order_by(Project.created_at.desc())
        ).all()
    )


def get_required_documents(project_type: str) -> list[dict]:
    """
    Returns statutory and compliance document requirements for property projects
    in accordance with Telangana real estate and municipal building regulations.
    """
    normalized_type = (project_type or "").upper().strip()

    requirements = [
        {
            "document_type": "SANCTIONED_PLAN",
            "name": "Municipal Sanctioned Building Plan",
            "description": "Approved architectural & structural blueprint from GHMC, HMDA, or DTCP validating permissible FSI, setbacks, and floor limits.",
            "is_mandatory": True,
            "authority": "Competent Municipal Planning Authority (GHMC / HMDA / DTCP)",
            "category": "DOCUMENTATION",
            "accepted_formats": ["application/pdf", "image/png", "image/jpeg"],
        },
        {
            "document_type": "LAND_TITLE",
            "name": "30-Year Title Search & Sale Deed",
            "description": "Title ownership deed establishing clear, marketable, and unencumbered ownership of the subject plot footprint.",
            "is_mandatory": True,
            "authority": "Registration & Stamps Department, Telangana",
            "category": "LEGAL",
            "accepted_formats": ["application/pdf", "image/png", "image/jpeg"],
        },
        {
            "document_type": "ENCUMBRANCE_CERTIFICATE",
            "name": "Encumbrance Certificate (EC Form 15/16)",
            "description": "Current non-encumbrance certificate verifying freedom from prior mortgages, legal liens, or statutory attachments.",
            "is_mandatory": True,
            "authority": "Sub-Registrar Office (Registration & Stamps Dept)",
            "category": "LEGAL",
            "accepted_formats": ["application/pdf", "image/png", "image/jpeg"],
        },
    ]

    if normalized_type in ("APARTMENT", "VILLA"):
        requirements.append({
            "document_type": "RERA",
            "name": "Telangana RERA Registration Certificate",
            "description": "Statutory registration under TS-RERA Section 3/4 protecting prospective buyers and validating project completion timelines.",
            "is_mandatory": True,
            "authority": "Telangana Real Estate Regulatory Authority (TSRERA)",
            "category": "REGULATORY",
            "accepted_formats": ["application/pdf", "image/png", "image/jpeg"],
        })
    else:
        requirements.append({
            "document_type": "RERA",
            "name": "RERA Exemption / Registration Certificate",
            "description": "RERA registration certificate or statutory exemption declaration if plot footprint is below threshold.",
            "is_mandatory": False,
            "authority": "Telangana Real Estate Regulatory Authority (TSRERA)",
            "category": "REGULATORY",
            "accepted_formats": ["application/pdf", "image/png", "image/jpeg"],
        })

    if normalized_type == "APARTMENT":
        requirements.append({
            "document_type": "FIRE_NOC",
            "name": "Chief Fire Officer (CFO) Provisional NOC",
            "description": "Provisional Fire NOC certifying fire engine driveways, minimum turning radius, pressurized staircases, and wet risers.",
            "is_mandatory": True,
            "authority": "Telangana State Disaster Response and Fire Services",
            "category": "SAFETY",
            "accepted_formats": ["application/pdf", "image/png", "image/jpeg"],
        })
    else:
        requirements.append({
            "document_type": "FIRE_NOC",
            "name": "Fire Safety NOC / Exemption",
            "description": "Fire clearance or exemption certificate for individual / low-rise residential structures.",
            "is_mandatory": False,
            "authority": "Telangana State Disaster Response and Fire Services",
            "category": "SAFETY",
            "accepted_formats": ["application/pdf", "image/png", "image/jpeg"],
        })

    requirements.append({
        "document_type": "COMMENCEMENT_CERTIFICATE",
        "name": "Commencement Certificate (Plinth Level)",
        "description": "Plinth verification certification from the planning authority allowing structural superstructure work to proceed.",
        "is_mandatory": False,
        "authority": "Municipal Town Planning Section",
        "category": "DOCUMENTATION",
        "accepted_formats": ["application/pdf", "image/png", "image/jpeg"],
    })

    return requirements



# ---------------------------------------------------------------------------
# Project Versions
# ---------------------------------------------------------------------------

def create_project_version(
    db: Session,
    project_id: UUID,
    submitted_by: UUID,
) -> ProjectVersion:
    project = get_project(
        db,
        project_id,
    )

    if project is None:
        raise ValueError("Project not found")

    latest_version = db.scalar(
        select(ProjectVersion)
        .where(
            ProjectVersion.project_id == project.id
        )
        .order_by(
            ProjectVersion.version_number.desc()
        )
        .limit(1)
    )

    next_version = (
        latest_version.version_number + 1
        if latest_version
        else 1
    )

    pending_version = db.scalar(
        select(ProjectVersion).where(
            ProjectVersion.project_id == project.id,
            ProjectVersion.status == "PENDING_APPROVAL",
        )
    )

    if pending_version is not None:
        raise ValueError(
            "Project already has a version pending approval"
        )

    version = ProjectVersion(
        project_id=project.id,
        version_number=next_version,
        status="DRAFT",
        submitted_by=submitted_by,
    )

    db.add(version)
    db.commit()
    db.refresh(version)

    return version


# ---------------------------------------------------------------------------
# Buildings
# ---------------------------------------------------------------------------

def add_building(
    db: Session,
    project_version_id: UUID,
    builder_profile_id: UUID,
    name: str,
    building_number: str | None,
    floors: int | None,
) -> Building:
    version = db.scalar(
        select(ProjectVersion).where(
            ProjectVersion.id == project_version_id
        )
    )

    if version is None:
        raise ValueError("Project version not found")

    if version.status != "DRAFT":
        raise ValueError(
            "Buildings can only be added to a DRAFT version"
        )

    project = db.scalar(
        select(Project).where(
            Project.id == version.project_id,
            Project.builder_id == builder_profile_id,
            Project.deleted_at.is_(None),
        )
    )

    if project is None:
        raise ValueError(
            "Builder does not own this project"
        )

    building = Building(
        project_version_id=version.id,
        name=name,
        building_number=building_number,
        floors=floors,
    )

    db.add(building)
    db.commit()
    db.refresh(building)

    return building


# ---------------------------------------------------------------------------
# Units
# ---------------------------------------------------------------------------

def add_unit(
    db: Session,
    building_id: UUID,
    builder_profile_id: UUID,
    unit_number: str,
    floor_number: int | None,
    unit_type: str | None,
    area_sqft: int | None,
) -> Unit:
    """
    Add a unit to a building.

    Authorization chain:

        Builder
            ↓
        Project
            ↓
        Project Version
            ↓
        Building
            ↓
        Unit

    The builder must own the project containing the building.
    Units can only be added to a DRAFT project version.
    """

    # ---------------------------------------------------------------
    # 1. Find building
    # ---------------------------------------------------------------

    building = db.scalar(
        select(Building).where(
            Building.id == building_id
        )
    )

    if building is None:
        raise ValueError("Building not found")

    # ---------------------------------------------------------------
    # 2. Find project version
    # ---------------------------------------------------------------

    version = db.scalar(
        select(ProjectVersion).where(
            ProjectVersion.id == building.project_version_id
        )
    )

    if version is None:
        raise ValueError("Project version not found")

    # ---------------------------------------------------------------
    # 3. Version must still be editable
    # ---------------------------------------------------------------

    if version.status != "DRAFT":
        raise ValueError(
            "Units can only be added to a DRAFT version"
        )

    # ---------------------------------------------------------------
    # 4. Verify builder owns the project
    # ---------------------------------------------------------------

    project = db.scalar(
        select(Project).where(
            Project.id == version.project_id,
            Project.builder_id == builder_profile_id,
            Project.deleted_at.is_(None),
        )
    )

    if project is None:
        raise ValueError(
            "Builder does not own this project"
        )

    # ---------------------------------------------------------------
    # 5. Create unit
    # ---------------------------------------------------------------

    unit = Unit(
        building_id=building.id,
        unit_number=unit_number,
        floor_number=floor_number,
        unit_type=unit_type,
        area_sqft=area_sqft,
    )

    db.add(unit)
    db.commit()
    db.refresh(unit)

    return unit


# ---------------------------------------------------------------------------
# Submit Project Version
# ---------------------------------------------------------------------------

def submit_project_version_for_approval(
    db: Session,
    project_version_id: UUID,
    builder_profile_id: UUID,
    submitted_by: UUID,
) -> ProjectVersion:
    version = db.scalar(
        select(ProjectVersion).where(
            ProjectVersion.id == project_version_id
        )
    )

    if version is None:
        raise ValueError("Project version not found")

    project = get_project(
        db,
        version.project_id,
    )

    if project is None:
        raise ValueError("Project not found")

    if project.builder_id != builder_profile_id:
        raise ValueError(
            "You are not authorized to submit this project version"
        )

    if version.status != "DRAFT":
        raise ValueError(
            "Only a DRAFT version can be submitted for approval"
        )

    version.status = "PENDING_APPROVAL"
    version.submitted_by = submitted_by

    db.commit()
    db.refresh(version)

    return version