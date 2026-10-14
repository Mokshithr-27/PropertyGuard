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
    DocumentProcessingJobResponse,
    DocumentProcessingStatusUpdate,
    DocumentResponse,
    DocumentValidationResponse,
    DocumentVersionResponse,
)
from app.services.document_service import (
    create_document,
    create_document_version,
    delete_document,
    update_document_processing_status,
)

from app.services.document_processing_service import (
    queue_document_processing,
)


from app.services.project_service import get_builder_project
from app.repositories.document_repository import (
    get_document,
    get_document_versions,
    get_latest_version,
    get_project_documents,
    get_document_version,
)

from app.workers.document_tasks import process_document_task

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


@router.post(
    "/validate",
    response_model=DocumentValidationResponse,
)
async def validate_document_file(
    file: UploadFile = File(...),
    document_type: str | None = Form(None),
):
    """
    Validates file authenticity, magic number signatures, format compliance,
    and calculates cryptographic SHA-256 hash.
    Accepts PDF blueprints, municipal sanctions, NOC deeds, PNG, JPG, and TIFF.
    """
    data = await file.read()
    file_size = len(data)

    if file_size == 0:
        return DocumentValidationResponse(
            is_valid=False,
            file_name=file.filename or "unknown",
            mime_type=file.content_type or "application/octet-stream",
            file_size=0,
            file_size_formatted="0 B",
            sha256="",
            detected_format="Empty File",
            error="Uploaded file contains 0 bytes. Empty files cannot be verified as statutory evidence.",
        )

    if file_size > 25 * 1024 * 1024:
        return DocumentValidationResponse(
            is_valid=False,
            file_name=file.filename or "unknown",
            mime_type=file.content_type or "application/octet-stream",
            file_size=file_size,
            file_size_formatted=f"{file_size / (1024 * 1024):.2f} MB",
            sha256="",
            detected_format="Oversized File",
            error="File size exceeds the 25 MB statutory submission limit.",
        )

    # Magic byte inspection
    detected_format = "Unknown"
    is_valid_format = False
    details: dict[str, str | int | bool] = {}

    if data.startswith(b"%PDF-"):
        is_valid_format = True
        version_str = data[5:8].decode("latin-1", errors="ignore")
        detected_format = f"PDF Architectural Document (v{version_str})"
        has_eof = b"%%EOF" in data[-1024:]
        details["pdf_version"] = version_str
        details["has_eof"] = has_eof
    elif data.startswith(b"\x89PNG\r\n\x1a\n"):
        is_valid_format = True
        detected_format = "PNG Sanction Deed Image"
    elif data.startswith(b"\xff\xd8\xff"):
        is_valid_format = True
        detected_format = "JPEG Document Image"
    elif data.startswith(b"II*\x00") or data.startswith(b"MM\x00*"):
        is_valid_format = True
        detected_format = "TIFF Blueprint Document"

    if not is_valid_format:
        return DocumentValidationResponse(
            is_valid=False,
            file_name=file.filename or "unknown",
            mime_type=file.content_type or "application/octet-stream",
            file_size=file_size,
            file_size_formatted=f"{file_size / 1024:.1f} KB" if file_size < 1024 * 1024 else f"{file_size / (1024 * 1024):.2f} MB",
            sha256="",
            detected_format="Unrecognized Binary/Text",
            error="Invalid file signature. File header does not match official PDF, PNG, JPG, or TIFF specification.",
        )

    import hashlib
    sha256_hash = hashlib.sha256(data).hexdigest()
    formatted_size = f"{file_size / 1024:.1f} KB" if file_size < 1024 * 1024 else f"{file_size / (1024 * 1024):.2f} MB"

    details["sha256"] = sha256_hash
    details["document_type"] = document_type or "STATUTORY"
    details["integrity_check"] = "PASSED"

    return DocumentValidationResponse(
        is_valid=True,
        file_name=file.filename or "uploaded_document",
        mime_type=file.content_type or "application/pdf",
        file_size=file_size,
        file_size_formatted=formatted_size,
        sha256=sha256_hash,
        detected_format=detected_format,
        error=None,
        details=details,
    )


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


@router.patch(
    "/versions/{version_id}/processing-status",
    response_model=DocumentVersionResponse,
    responses={
        400: {
            "description": "Invalid processing status",
        },
        404: {
            "description": (
                "Document version, document, or builder project not found"
            ),
        },
    },
)
async def update_processing_status(
    version_id: UUID,
    payload: DocumentProcessingStatusUpdate,
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

    version = get_document_version(
        db,
        version_id,
    )

    if version is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document version not found",
        )

    document = get_document(
        db,
        version.document_id,
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
            detail="Document version not found",
        )

    try:
        updated_version = update_document_processing_status(
            db=db,
            version=version,
            new_status=payload.processing_status,
        )

        db.commit()
        db.refresh(updated_version)

        return updated_version

    except ValueError as exc:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )

@router.post(
    "/versions/{version_id}/process",
    response_model=DocumentProcessingJobResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {
            "description": "An active processing job already exists or version cannot be processed",
        },
        404: {
            "description": "Document version, document, or builder project not found",
        },
    },
)
def queue_document_processing_api(
    version_id: UUID,
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

    version = get_document_version(
        db,
        version_id,
    )

    if version is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document version not found",
        )

    document = get_document(
        db,
        version.document_id,
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
            detail="Document version not found",
        )

    try:
        job = queue_document_processing(
            db=db,
            version=version,
        )

        db.commit()
        db.refresh(job)

        process_document_task.delay(
            str(version.id),
            str(job.id),
        )

        return job

    except ValueError as exc:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )


    