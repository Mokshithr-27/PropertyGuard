from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.api.dependencies import (
    get_current_user,
    get_db,
    require_role,
)

from app.models.user import User

from app.schemas.project import (
    BuildingCreate,
    BuildingResponse,
    ProjectCreate,
    ProjectResponse,
    ProjectVersionResponse,
    UnitCreate,
    UnitResponse,
)

from app.services.project_service import (
    add_building,
    add_unit,
    create_project,
    create_project_version,
    get_builder_profile,
    get_builder_project,
    get_project,
    submit_project_version_for_approval,
)


router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


# ============================================================
# CREATE PROJECT
# ============================================================

@router.post(
    "",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_project_api(
    data: ProjectCreate,
    current_user: User = Depends(
        require_role("BUILDER")
    ),
    db: Session = Depends(get_db),
):
    builder_profile = get_builder_profile(
        db,
        current_user.id,
    )

    if builder_profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Builder profile not found",
        )

    try:
        return create_project(
            db,
            builder_profile.id,
            data.name,
            data.description,
            data.project_type,
            data.address,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )


# ============================================================
# GET PROJECT
# ============================================================

@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
)
def get_project_api(
    project_id: UUID,
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db),
):
    project = get_project(
        db,
        project_id,
    )

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )

    return project


# ============================================================
# CREATE PROJECT VERSION
# ============================================================

@router.post(
    "/{project_id}/versions",
    response_model=ProjectVersionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_project_version_api(
    project_id: UUID,
    current_user: User = Depends(
        require_role("BUILDER")
    ),
    db: Session = Depends(get_db),
):
    builder_profile = get_builder_profile(
        db,
        current_user.id,
    )

    if builder_profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Builder profile not found",
        )

    # Verify that this project belongs
    # to the logged-in builder.
    project = get_builder_project(
        db,
        project_id,
        builder_profile.id,
    )

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )

    try:
        return create_project_version(
            db,
            project.id,
            current_user.id,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )


# ============================================================
# SUBMIT PROJECT VERSION FOR APPROVAL
# ============================================================

@router.post(
    "/versions/{project_version_id}/submit",
    response_model=ProjectVersionResponse,
)
def submit_project_version_api(
    project_version_id: UUID,
    current_user: User = Depends(
        require_role("BUILDER")
    ),
    db: Session = Depends(get_db),
):
    builder_profile = get_builder_profile(
        db,
        current_user.id,
    )

    if builder_profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Builder profile not found",
        )

    try:
        return submit_project_version_for_approval(
            db,
            project_version_id,
            builder_profile.id,
            current_user.id,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )


# ============================================================
# ADD BUILDING
# ============================================================

@router.post(
    "/versions/{project_version_id}/buildings",
    response_model=BuildingResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_building_api(
    project_version_id: UUID,
    data: BuildingCreate,
    current_user: User = Depends(
        require_role("BUILDER")
    ),
    db: Session = Depends(get_db),
):
    builder_profile = get_builder_profile(
        db,
        current_user.id,
    )

    if builder_profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Builder profile not found",
        )

    try:
        return add_building(
            db,
            project_version_id,
            builder_profile.id,
            data.name,
            data.building_number,
            data.floors,
        )

    except ValueError as exc:
        if str(exc) == "Builder does not own this project":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=str(exc),
            )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )


# ============================================================
# ADD UNIT
# ============================================================

@router.post(
    "/buildings/{building_id}/units",
    response_model=UnitResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_unit_api(
    building_id: UUID,
    data: UnitCreate,
    current_user: User = Depends(
        require_role("BUILDER")
    ),
    db: Session = Depends(get_db),
):
    builder_profile = get_builder_profile(
        db,
        current_user.id,
    )

    if builder_profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Builder profile not found",
        )

    try:
        return add_unit(
            db,
            building_id,
            builder_profile.id,
            data.unit_number,
            data.floor_number,
            data.unit_type,
            data.area_sqft,
        )

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Unit with this unit number "
                "already exists in this building"
            ),
        )

    except ValueError as exc:
        if str(exc) == "Builder does not own this project":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=str(exc),
            )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )