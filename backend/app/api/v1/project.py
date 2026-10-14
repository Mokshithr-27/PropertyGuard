"""
PropertyGuard Project & Compliance API Endpoints
------------------------------------------------
Provides endpoints for creating, listing, modifying, and soft-deleting projects;
managing physical hierarchies (buildings, units); retrieving required document catalogs;
and triggering compliance evaluations and querying findings/evaluation runs.
"""

from datetime import datetime, timezone
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
    ProjectActionResponse,
    ProjectCreate,
    ProjectListItemResponse,
    ProjectResponse,
    ProjectStatusUpdate,
    ProjectUpdate,
    ProjectVersionResponse,
    RequiredDocumentResponse,
    UnitCreate,
    UnitResponse,
)


from app.repositories.compliance_repository import (
    get_evaluation_run,
    get_evaluation_run_compliance_results,
    get_project_evaluation_runs,
    get_finding,
    get_project_findings,
)
from app.repositories.document_repository import get_project_documents

from app.schemas.compliance import (
    EvaluationRunResponse,
    EvaluationRunResultsResponse,
    FindingResponse,
    FindingUpdate,
)

from app.services.project_service import (
    add_building,
    add_unit,
    create_project,
    create_project_version,
    get_builder_profile,
    get_builder_project,
    get_builder_projects,
    get_project,
    get_required_documents,
    submit_project_version_for_approval,
    update_project,
)

from app.services.compliance_service import ComplianceService

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


# ============================================================
# REQUIRED DOCUMENTS CATALOG
# ============================================================

@router.get(
    "/required-documents",
    response_model=list[RequiredDocumentResponse],
)
def get_required_documents_api(
    project_type: str = "APARTMENT",
    current_user: User = Depends(get_current_user),
):
    """
    Returns statutory and compliance document requirements for property projects
    in accordance with Telangana real estate and municipal building regulations.
    """
    return get_required_documents(project_type)


# ============================================================
# LIST BUILDER PROJECTS
# ============================================================

@router.get(
    "",
    response_model=list[ProjectListItemResponse],
)
def list_builder_projects_api(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user_roles = [ur.role.name for ur in current_user.roles if ur.role] if hasattr(current_user, "roles") else []

    if "ADMIN" in user_roles or "SUPER_ADMIN" in user_roles or "BUYER" in user_roles:
        from app.models.project import Project
        projects = (
            db.query(Project)
            .filter(Project.deleted_at.is_(None))
            .all()
        )
    else:
        builder_profile = get_builder_profile(
            db,
            current_user.id,
        )
        if builder_profile is None:
            return []
        projects = get_builder_projects(db, builder_profile.id)

    items = []
    for p in projects:
        docs = get_project_documents(db, p.id)
        latest_ver = None
        if p.versions:
            latest_ver = max((v.version_number for v in p.versions), default=1)
        items.append(
            ProjectListItemResponse(
                id=p.id,
                builder_id=p.builder_id,
                name=p.name,
                description=p.description,
                project_type=p.project_type,
                address=p.address,
                status=p.status,
                created_at=p.created_at,
                updated_at=p.updated_at,
                latest_version_number=latest_ver,
                documents_count=len(docs),
                # A real compliance score is not implemented yet. Do not expose
                # a fabricated score as if it were an assessment result.
                compliance_score=None,
            )
        )
    return items


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

    if builder_profile.verification_status != "VERIFIED":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Builder must be VERIFIED to create projects",
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



@router.get(
    "/{project_id}/findings",
    response_model=list[FindingResponse],
)
def list_project_findings(
    project_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    user_roles = {
        user_role.role.name
        for user_role in current_user.roles
    }

    if not ({"BUILDER", "ADMIN"} & user_roles):
        raise HTTPException(
            status_code=403,
            detail="Insufficient permissions",
        )

    if "ADMIN" not in user_roles:
        builder_profile = get_builder_profile(
            db,
            current_user.id,
        )

        if builder_profile is None:
            raise HTTPException(
                status_code=404,
                detail="Builder profile not found",
            )

        project = get_builder_project(
            db,
            project_id,
            builder_profile.id,
        )

        if project is None:
            raise HTTPException(
                status_code=404,
                detail="Project not found",
            )

    return get_project_findings(
        db=db,
        project_id=project_id,
    )


# ============================================================
# UPDATE PROJECT DETAILS
# ============================================================

@router.patch(
    "/{project_id}",
    response_model=ProjectResponse,
)
def update_project_api(
    project_id: UUID,
    payload: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    user_roles = {
        ur.role.name for ur in current_user.roles if ur.role
    } if hasattr(current_user, "roles") else set()

    if not user_roles.intersection({"BUILDER", "ADMIN", "SUPER_ADMIN"}):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="BUILDER, ADMIN, or SUPER_ADMIN role required",
        )

    project = get_project(db, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    if not user_roles.intersection({"ADMIN", "SUPER_ADMIN"}):
        builder_profile = get_builder_profile(db, current_user.id)
        if builder_profile is None:
            raise HTTPException(status_code=404, detail="Builder profile not found")
        if project.builder_id != builder_profile.id:
            raise HTTPException(status_code=403, detail="Not authorized to modify this project")

    try:
        return update_project(
            db,
            project,
            name=payload.name,
            description=payload.description,
            project_type=payload.project_type,
            address=payload.address,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


# ============================================================
# SUSPEND / ACTIVATE / UPDATE PROJECT STATUS
# ============================================================

@router.patch(
    "/{project_id}/status",
    response_model=ProjectActionResponse,
)
def update_project_status_api(
    project_id: UUID,
    payload: ProjectStatusUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Suspends, activates, or updates project status.
    Available to Builders (for their own development projects) and Admins / Auditors (for any project).
    """
    user_roles = {
        ur.role.name for ur in current_user.roles if ur.role
    } if hasattr(current_user, "roles") else set()

    from app.models.project import Project
    project = (
        db.query(Project)
        .filter(
            Project.id == project_id,
            Project.deleted_at.is_(None),
        )
        .first()
    )
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    is_admin = bool({"ADMIN", "SUPER_ADMIN"} & user_roles)

    if not is_admin:
        builder_profile = get_builder_profile(db, current_user.id)
        if not builder_profile or project.builder_id != builder_profile.id:
            raise HTTPException(status_code=403, detail="Not authorized to modify this project")

    from datetime import datetime
    project.status = payload.status
    project.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(project)

    action_label = "suspended" if payload.status == "SUSPENDED" else "reactivated" if payload.status == "ACTIVE" else f"set to {payload.status}"
    return ProjectActionResponse(
        id=project.id,
        name=project.name,
        status=project.status,
        message=f"Project '{project.name}' successfully {action_label}.",
    )


# ============================================================
# DELETE PROJECT
# ============================================================

@router.delete(
    "/{project_id}",
    response_model=ProjectActionResponse,
)
def delete_project_api(
    project_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Permanently deletes a development project and its associated documents/findings.
    Available to Builders (for their own development projects) and Admins / Auditors (for any project).
    """
    user_roles = {
        ur.role.name for ur in current_user.roles if ur.role
    } if hasattr(current_user, "roles") else set()

    from app.models.project import Project
    project = (
        db.query(Project)
        .filter(
            Project.id == project_id,
            Project.deleted_at.is_(None),
        )
        .first()
    )
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    is_admin = bool({"ADMIN", "SUPER_ADMIN"} & user_roles)

    if not is_admin:
        builder_profile = get_builder_profile(db, current_user.id)
        if not builder_profile or project.builder_id != builder_profile.id:
            raise HTTPException(status_code=403, detail="Not authorized to delete this project")

    proj_name = project.name
    project.deleted_at = datetime.now(timezone.utc)
    project.status = "INACTIVE"
    project.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(project)

    return ProjectActionResponse(
        id=project_id,
        name=proj_name,
        status="DELETED",
        message=(
            f"Project '{proj_name}' was soft-deleted. "
            "Historical versions, documents, findings, and evaluation records were preserved."
        ),
    )




@router.patch(
    "/{project_id}/findings/{finding_id}",
    response_model=FindingResponse,
)
def update_project_finding(
    project_id: UUID,
    finding_id: UUID,
    payload: FindingUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    user_roles = {
        user_role.role.name
        for user_role in current_user.roles
    }

    if not ({"BUILDER", "ADMIN"} & user_roles):
        raise HTTPException(
            status_code=403,
            detail="Insufficient permissions",
        )

    finding = get_finding(
        db=db,
        finding_id=finding_id,
    )

    if finding is None:
        raise HTTPException(
            status_code=404,
            detail="Finding not found",
        )

    if (
        finding.compliance_result is None
        or finding.compliance_result.project_id != project_id
    ):
        raise HTTPException(
            status_code=404,
            detail="Finding not found",
        )

    if "ADMIN" not in user_roles:
        builder_profile = get_builder_profile(
            db,
            current_user.id,
        )

        if builder_profile is None:
            raise HTTPException(
                status_code=404,
                detail="Builder profile not found",
            )

        project = get_builder_project(
            db,
            project_id,
            builder_profile.id,
        )

        if project is None:
            raise HTTPException(
                status_code=404,
                detail="Project not found",
            )

    try:
        updated_finding = ComplianceService().update_finding_status(
            db=db,
            finding_id=finding_id,
            status=payload.status,
            resolution_note=payload.resolution_note,
        )

        db.commit()

        return updated_finding

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc

# ============================================================
# CREATE EVALUATION RUN
# ============================================================

@router.post(
    "/{project_id}/evaluations",
    response_model=EvaluationRunResponse,
    status_code=status.HTTP_201_CREATED,
)


def create_evaluation_run_api(
    project_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # --------------------------------------------------------
    # Verify that the user is a BUILDER or ADMIN
    # --------------------------------------------------------
    user_roles = {
        user_role.role.name
        for user_role in current_user.roles
    }

    if not user_roles.intersection({"BUILDER", "ADMIN"}):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="BUILDER or ADMIN role required",
        )

    # --------------------------------------------------------
    # Verify project access
    # --------------------------------------------------------
    if "ADMIN" not in user_roles:
        builder_profile = get_builder_profile(
            db,
            current_user.id,
        )

        if builder_profile is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Builder profile not found",
            )

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

    # --------------------------------------------------------
    # Create evaluation run
    # --------------------------------------------------------
    compliance_service = ComplianceService()

    try:
        return compliance_service.create_evaluation_run(
            db,
            project_id,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )


# ============================================================
# RUN PROJECT EVALUATION
# ============================================================

@router.post(
    "/{project_id}/evaluations/run",
    response_model=EvaluationRunResponse,
    status_code=status.HTTP_201_CREATED,
)
def run_evaluation_api(
    project_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user_roles = {
        user_role.role.name
        for user_role in current_user.roles
    }

    if not user_roles.intersection({"BUILDER", "ADMIN"}):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="BUILDER or ADMIN role required",
        )

    if "ADMIN" not in user_roles:
        builder_profile = get_builder_profile(
            db,
            current_user.id,
        )

        if builder_profile is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Builder profile not found",
            )

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

    compliance_service = ComplianceService()

    try:
        return compliance_service.run_evaluation(
            db,
            project_id,
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
    user_roles = {
        user_role.role.name
        for user_role in current_user.roles
        if user_role.role
    }

    if not user_roles.intersection({"BUILDER", "ADMIN", "SUPER_ADMIN"}):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="BUILDER, ADMIN, or SUPER_ADMIN role required",
        )

    if user_roles.intersection({"ADMIN", "SUPER_ADMIN"}):
        project = get_project(db, project_id)
    else:
        builder_profile = get_builder_profile(db, current_user.id)
        if builder_profile is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Builder profile not found",
            )
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

    return project



@router.get(
    "/{project_id}/evaluations",
    response_model=list[EvaluationRunResponse],
    status_code=status.HTTP_200_OK,
)


def get_evaluation_runs_api(
    project_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user_roles = {
        user_role.role.name
        for user_role in current_user.roles
    }

    if not user_roles.intersection({"BUILDER", "ADMIN"}):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="BUILDER or ADMIN role required",
        )

    if "ADMIN" not in user_roles:
        builder_profile = get_builder_profile(
            db,
            current_user.id,
        )

        if builder_profile is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Builder profile not found",
            )

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

    return get_project_evaluation_runs(
        db,
        project_id,
    )


# ============================================================
# GET PROJECT EVALUATION HISTORY
# ============================================================

@router.get(
    "/{project_id}/evaluations/history",
    response_model=list[EvaluationRunResultsResponse],
    status_code=status.HTTP_200_OK,
)
def get_project_evaluation_history_api(
    project_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user_roles = {
        user_role.role.name
        for user_role in current_user.roles
    }

    if not user_roles.intersection({"BUILDER", "ADMIN"}):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="BUILDER or ADMIN role required",
        )

    if "ADMIN" not in user_roles:
        builder_profile = get_builder_profile(
            db,
            current_user.id,
        )

        if builder_profile is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Builder profile not found",
            )

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

    compliance_service = ComplianceService()

    try:
        return compliance_service.get_project_evaluation_history(
            db,
            project_id,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )

# ============================================================
# GET EVALUATION RUN RESULTS
# ============================================================

@router.get(
    "/{project_id}/evaluations/{evaluation_run_id}/results",
    response_model=EvaluationRunResultsResponse,
    status_code=status.HTTP_200_OK,
)
def get_evaluation_run_results_api(
    project_id: UUID,
    evaluation_run_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user_roles = {
        user_role.role.name
        for user_role in current_user.roles
    }

    if not user_roles.intersection({"BUILDER", "ADMIN"}):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="BUILDER or ADMIN role required",
        )

    evaluation_run = get_evaluation_run(
        db,
        evaluation_run_id,
    )

    if (
        evaluation_run is None
        or evaluation_run.project_id != project_id
    ):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Evaluation run not found",
        )

    if "ADMIN" not in user_roles:
        builder_profile = get_builder_profile(
            db,
            current_user.id,
        )

        if builder_profile is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Builder profile not found",
            )

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

    results = get_evaluation_run_compliance_results(
        db,
        evaluation_run_id,
    )

    return EvaluationRunResultsResponse(
        evaluation_run=evaluation_run,
        results=results,
    )


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