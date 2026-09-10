from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    Response,
    UploadFile,
    status,
)
from sqlalchemy.orm import Session

from app.api.dependencies import get_db, require_role
from app.models.user import User
from app.schemas.document import (
    DocumentDetailResponse,
    DocumentResponse,
    DocumentVersionResponse,
)
from app.services.document_service import (
    create_document,
    create_document_version,
    delete_document,
)
from app.services.project_service import get_builder_project
from app.repositories.document_repository import (
    get_document,
    get_document_versions,
    get_latest_version,
    get_project_documents,
)

from app.integrations.storage import download_bytes


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)



@router.get("/health")
def document_api_health():
    return {
        "status": "healthy",
        "service": "document-api",
    }

@router.get(
    "/project/{project_id}",
    response_model=list[DocumentResponse],
)
def get_documents_for_project(
    project_id: UUID,
    current_user: User = Depends(require_role("BUILDER")),
    db: Session = Depends(get_db),
):
    from app.services.project_service import get_builder_profile

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

    return get_project_documents(
        db,
        project_id,
    )

@router.get(
    "/{document_id}",
    response_model=DocumentDetailResponse,
)
def get_document_detail(
    document_id: UUID,
    current_user: User = Depends(require_role("BUILDER")),
    db: Session = Depends(get_db),
):
    from app.services.project_service import get_builder_profile

    builder_profile = get_builder_profile(
        db,
        current_user.id,
    )

    if builder_profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Builder profile not found",
        )

    document = get_document(
        db,
        document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )

    project = get_builder_project(
        db,
        document.project_id,
        builder_profile.id,
    )

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )

    versions = get_document_versions(
        db,
        document.id,
    )

    return DocumentDetailResponse(
        **{
            "id": document.id,
            "project_id": document.project_id,
            "document_type": document.document_type,
            "title": document.title,
            "description": document.description,
            "visibility": document.visibility,
            "authority_level": document.authority_level,
            "expiry_date": document.expiry_date,
            "status": document.status,
            "created_at": document.created_at,
            "updated_at": document.updated_at,
            "deleted_at": document.deleted_at,
            "versions": versions,
        }
    )

@router.get(
    "/{document_id}/download",
)
def download_document(
    document_id: UUID,
    current_user: User = Depends(require_role("BUILDER")),
    db: Session = Depends(get_db),
):
    from app.services.project_service import get_builder_profile

    builder_profile = get_builder_profile(
        db,
        current_user.id,
    )

    if builder_profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Builder profile not found",
        )

    document = get_document(
        db,
        document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )

    project = get_builder_project(
        db,
        document.project_id,
        builder_profile.id,
    )

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )

    version = get_latest_version(
        db,
        document.id,
    )

    if version is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document version not found",
        )

    try:
        data = download_bytes(
            version.storage_key,
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document file not found",
        )

    return Response(
        content=data,
        media_type=version.mime_type,
        headers={
            "Content-Disposition": (
                f'attachment; filename="{version.file_name}"'
            )
        },
    )


@router.post(
    "/{document_id}/versions",
    response_model=DocumentVersionResponse,
)
async def upload_document_version(
    document_id: UUID,
    file: UploadFile = File(...),
    current_user: User = Depends(require_role("BUILDER")),
    db: Session = Depends(get_db),
):
    from app.services.project_service import get_builder_profile

    builder_profile = get_builder_profile(
        db,
        current_user.id,
    )

    if builder_profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Builder profile not found",
        )

    document = get_document(
        db,
        document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )

    project = get_builder_project(
        db,
        document.project_id,
        builder_profile.id,
    )

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )

    data = await file.read()

    if not data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded file is empty",
        )

    try:
        version = create_document_version(
            db=db,
            document=document,
            uploaded_by=current_user.id,
            file_name=file.filename or "uploaded_file",
            mime_type=file.content_type or "application/octet-stream",
            data=data,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        )

    return version

@router.post(
    "",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_document(
    project_id: UUID = Form(...),
    document_type: str = Form(...),
    title: str = Form(...),
    file: UploadFile = File(...),
    description: str | None = Form(None),
    visibility: str = Form("PRIVATE"),
    authority_level: int | None = Form(None),
    expiry_date: str | None = Form(None),
    current_user: User = Depends(require_role("BUILDER")),
    db: Session = Depends(get_db),
):
    # Get the builder profile associated with the authenticated user.
    from app.services.project_service import get_builder_profile

    builder_profile = get_builder_profile(
        db,
        current_user.id,
    )

    if builder_profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Builder profile not found",
        )

    # Verify that this builder owns the project.
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

    # Read the uploaded file.
    data = await file.read()

    if not data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded file is empty",
        )

    # Convert expiry date if supplied.
    parsed_expiry_date = None

    if expiry_date:
        from datetime import datetime

        try:
            parsed_expiry_date = datetime.fromisoformat(
                expiry_date.replace("Z", "+00:00")
            )
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid expiry_date format",
            )

    try:
        return create_document(
            db=db,
            project_id=project_id,
            uploaded_by=current_user.id,
            document_type=document_type,
            title=title,
            file_name=file.filename or "uploaded_file",
            mime_type=file.content_type or "application/octet-stream",
            data=data,
            description=description,
            visibility=visibility,
            authority_level=authority_level,
            expiry_date=parsed_expiry_date,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )

@router.delete(
    "/{document_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_document_endpoint(
    document_id: UUID,
    current_user: User = Depends(require_role("BUILDER")),
    db: Session = Depends(get_db),
):
    from app.services.project_service import get_builder_profile

    builder_profile = get_builder_profile(
        db,
        current_user.id,
    )

    if builder_profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Builder profile not found",
        )

    document = get_document(
        db,
        document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )

    project = get_builder_project(
        db,
        document.project_id,
        builder_profile.id,
    )

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )

    try:
        delete_document(
            db=db,
            document=document,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        )

    return None
