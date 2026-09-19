from datetime import datetime
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.builder import (
    BuilderProfile,
    BuilderVerification,
)

from app.models.project import (
    Project,
    ProjectVersion,
)
from app.models.user import User


def get_builder_profile_by_id(
    db: Session,
    builder_profile_id: UUID,
) -> BuilderProfile | None:
    return db.scalar(
        select(BuilderProfile).where(
            BuilderProfile.id == builder_profile_id
        )
    )


def verify_builder_profile(
    db: Session,
    builder_profile_id: UUID,
    status: str,
    reason: str | None,
    admin_user: User,
) -> BuilderProfile:
    profile = get_builder_profile_by_id(
        db,
        builder_profile_id,
    )

    if profile is None:
        raise ValueError("Builder profile not found")

    profile.verification_status = status

    verification = BuilderVerification(
        builder_profile_id=profile.id,
        verification_type="ADMIN_REVIEW",
        status=status,
        admin_id=admin_user.id,
        reason=reason,
        verified_at=(
            datetime.utcnow()
            if status in {"VERIFIED", "REJECTED", "SUSPENDED"}
            else None
        ),
        ai_assisted=False,
    )

    db.add(verification)
    db.commit()
    db.refresh(profile)

    return profile

def review_project_version(
    db: Session,
    project_version_id: UUID,
    status: str,
    reason: str | None,
    admin_user: User,
) -> ProjectVersion:
    version = db.scalar(
        select(ProjectVersion).where(
            ProjectVersion.id == project_version_id
        )
    )

    if version is None:
        raise ValueError("Project version not found")

    if version.status != "PENDING_APPROVAL":
        raise ValueError(
            "Only PENDING_APPROVAL versions can be reviewed"
        )

    if status == "REJECTED" and not reason:
        raise ValueError(
            "A rejection reason is required"
        )

    if status not in {"APPROVED", "REJECTED"}:
        raise ValueError(
            "Invalid review status"
        )

    version.status = status
    version.reviewed_by = admin_user.id
    version.review_reason = reason

    if status == "APPROVED":
        project = db.scalar(
            select(Project).where(
                Project.id == version.project_id
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

