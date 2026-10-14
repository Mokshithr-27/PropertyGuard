"""Auditable online verification against the official Telangana RERA portal."""
from dataclasses import asdict
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.dependencies import get_current_user, get_db
from app.models.user import User
from app.models.project import Project
from app.models.rera_verification import ReraVerification
from app.schemas.rera_verification import ReraVerificationRequest, ReraVerificationResponse
from app.services.project_service import get_builder_profile
from app.services.rera_verification_service import verify_telangana_rera

router = APIRouter(prefix="/projects", tags=["Official Verification"])


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict

@router.post("/{project_id}/rera-verifications", response_model=ReraVerificationResponse, status_code=status.HTTP_201_CREATED)
def verify_project_rera(project_id: UUID, payload: ReraVerificationRequest,
                        current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    roles = {ur.role.name for ur in current_user.roles if ur.role}
    if not roles.intersection({"BUILDER", "ADMIN", "SUPER_ADMIN"}):
        raise HTTPException(status_code=403, detail="BUILDER or ADMIN role required")
    project = db.query(Project).filter(Project.id == project_id, Project.deleted_at.is_(None)).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    if not roles.intersection({"ADMIN", "SUPER_ADMIN"}):
        builder_profile = get_builder_profile(db, current_user.id)
        if builder_profile is None or builder_profile.id != project.builder_id:
            raise HTTPException(status_code=404, detail="Project not found")

    result = verify_telangana_rera(payload.registration_number,
                                   payload.expected_project_name or project.name,
                                   payload.expected_promoter_name)
    record = ReraVerification(
        project_id=project.id,
        registration_number=payload.registration_number.strip(),
        source_url=result.source_url,
        status=result.status,
        source_title=result.source_title,
        matched_project_name=result.matched_project_name,
        matched_promoter_name=result.matched_promoter_name,
        evidence=result.evidence,
        message=result.message,
        verified_by_user_id=current_user.id,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

@router.get("/{project_id}/rera-verifications", response_model=list[ReraVerificationResponse])
def list_project_rera_verifications(project_id: UUID, current_user: User = Depends(get_current_user),
                                    db: Session = Depends(get_db)):
    roles = {ur.role.name for ur in current_user.roles if ur.role}
    if not roles.intersection({"BUILDER", "ADMIN", "SUPER_ADMIN"}):
        raise HTTPException(status_code=403, detail="BUILDER or ADMIN role required")
    project = db.query(Project).filter(Project.id == project_id, Project.deleted_at.is_(None)).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    if not roles.intersection({"ADMIN", "SUPER_ADMIN"}):
        builder_profile = get_builder_profile(db, current_user.id)
        if builder_profile is None or builder_profile.id != project.builder_id:
            raise HTTPException(status_code=404, detail="Project not found")
    return db.query(ReraVerification).filter(ReraVerification.project_id == project_id).order_by(ReraVerification.checked_at.desc()).limit(50).all()
