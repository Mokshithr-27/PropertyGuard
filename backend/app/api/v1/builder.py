from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_db, require_role
from app.models.user import User
from app.schemas.builder import (
    BuilderProfileCreate,
    BuilderProfileResponse,
)
from app.services.builder_service import (
    create_builder_profile,
    get_builder_profile,
)


router = APIRouter(
    prefix="/builder",
    tags=["Builder"],
)


@router.get(
    "/profile",
    response_model=BuilderProfileResponse,
)
def get_my_builder_profile(
    current_user: User = Depends(
        require_role("BUILDER")
    ),
    db: Session = Depends(get_db),
):
    profile = get_builder_profile(db, current_user)

    if profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Builder profile not found",
        )

    return profile


@router.post(
    "/profile",
    response_model=BuilderProfileResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_my_builder_profile(
    data: BuilderProfileCreate,
    current_user: User = Depends(
        require_role("BUILDER")
    ),
    db: Session = Depends(get_db),
):
    try:
        return create_builder_profile(
            db=db,
            user=current_user,
            company_name=data.company_name,
            registration_number=data.registration_number,
            address=data.address,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        )