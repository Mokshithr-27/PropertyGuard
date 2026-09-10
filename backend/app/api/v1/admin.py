from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_db, require_role
from app.models.user import User
from app.schemas.admin import (
    BuilderVerificationRequest,
    ProjectVersionReviewRequest,
)
from app.schemas.builder import BuilderProfileResponse
from app.schemas.project import ProjectVersionResponse
from app.services.admin_service import (
    review_project_version,
    verify_builder_profile,
)


router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.patch(
    "/builders/{builder_profile_id}/verification",
    response_model=BuilderProfileResponse,
)
def update_builder_verification(
    builder_profile_id: UUID,
    data: BuilderVerificationRequest,
    current_user: User = Depends(
        require_role("ADMIN")
    ),
    db: Session = Depends(get_db),
):
    try:
        return verify_builder_profile(
            db=db,
            builder_profile_id=builder_profile_id,
            status=data.status,
            reason=data.reason,
            admin_user=current_user,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )


@router.patch(
    "/project-versions/{project_version_id}/review",
    response_model=ProjectVersionResponse,
)
def review_project_version_api(
    project_version_id: UUID,
    data: ProjectVersionReviewRequest,
    current_user: User = Depends(
        require_role("ADMIN")
    ),
    db: Session = Depends(get_db),
):
    try:
        return review_project_version(
            db=db,
            project_version_id=project_version_id,
            status=data.status,
            reason=data.reason,
            admin_user=current_user,
        )

    except ValueError as exc:
        message = str(exc)

        if message == "Project version not found":
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=message,
            )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message,
        )