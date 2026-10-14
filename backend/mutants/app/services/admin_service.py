"""
PropertyGuard Administrator Business Service
--------------------------------------------
Implements platform administration logic: reviewing and verifying builder profiles,
and approving or rejecting real estate project versions with audit histories.
"""

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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_builder_profile_by_id__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_builder_profile_by_id__mutmut)
def get_builder_profile_by_id(
    db: Session,
    builder_profile_id: UUID,
) -> BuilderProfile | None:
    return db.scalar(
        select(BuilderProfile).where(
            BuilderProfile.id == builder_profile_id
        )
    )


def x_get_builder_profile_by_id__mutmut_orig(
    db: Session,
    builder_profile_id: UUID,
) -> BuilderProfile | None:
    return db.scalar(
        select(BuilderProfile).where(
            BuilderProfile.id == builder_profile_id
        )
    )


def x_get_builder_profile_by_id__mutmut_1(
    db: Session,
    builder_profile_id: UUID,
) -> BuilderProfile | None:
    return db.scalar(
        None
    )


def x_get_builder_profile_by_id__mutmut_2(
    db: Session,
    builder_profile_id: UUID,
) -> BuilderProfile | None:
    return db.scalar(
        select(BuilderProfile).where(
            None
        )
    )


def x_get_builder_profile_by_id__mutmut_3(
    db: Session,
    builder_profile_id: UUID,
) -> BuilderProfile | None:
    return db.scalar(
        select(None).where(
            BuilderProfile.id == builder_profile_id
        )
    )


def x_get_builder_profile_by_id__mutmut_4(
    db: Session,
    builder_profile_id: UUID,
) -> BuilderProfile | None:
    return db.scalar(
        select(BuilderProfile).where(
            BuilderProfile.id != builder_profile_id
        )
    )

mutants_x_get_builder_profile_by_id__mutmut['_mutmut_orig'] = x_get_builder_profile_by_id__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_builder_profile_by_id__mutmut['x_get_builder_profile_by_id__mutmut_1'] = x_get_builder_profile_by_id__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_builder_profile_by_id__mutmut['x_get_builder_profile_by_id__mutmut_2'] = x_get_builder_profile_by_id__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_builder_profile_by_id__mutmut['x_get_builder_profile_by_id__mutmut_3'] = x_get_builder_profile_by_id__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_builder_profile_by_id__mutmut['x_get_builder_profile_by_id__mutmut_4'] = x_get_builder_profile_by_id__mutmut_4 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_verify_builder_profile__mutmut)
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


def x_verify_builder_profile__mutmut_orig(
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


def x_verify_builder_profile__mutmut_1(
    db: Session,
    builder_profile_id: UUID,
    status: str,
    reason: str | None,
    admin_user: User,
) -> BuilderProfile:
    profile = None

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


def x_verify_builder_profile__mutmut_2(
    db: Session,
    builder_profile_id: UUID,
    status: str,
    reason: str | None,
    admin_user: User,
) -> BuilderProfile:
    profile = get_builder_profile_by_id(
        None,
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


def x_verify_builder_profile__mutmut_3(
    db: Session,
    builder_profile_id: UUID,
    status: str,
    reason: str | None,
    admin_user: User,
) -> BuilderProfile:
    profile = get_builder_profile_by_id(
        db,
        None,
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


def x_verify_builder_profile__mutmut_4(
    db: Session,
    builder_profile_id: UUID,
    status: str,
    reason: str | None,
    admin_user: User,
) -> BuilderProfile:
    profile = get_builder_profile_by_id(
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


def x_verify_builder_profile__mutmut_5(
    db: Session,
    builder_profile_id: UUID,
    status: str,
    reason: str | None,
    admin_user: User,
) -> BuilderProfile:
    profile = get_builder_profile_by_id(
        db,
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


def x_verify_builder_profile__mutmut_6(
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

    if profile is not None:
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


def x_verify_builder_profile__mutmut_7(
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
        raise ValueError(None)

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


def x_verify_builder_profile__mutmut_8(
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
        raise ValueError("XXBuilder profile not foundXX")

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


def x_verify_builder_profile__mutmut_9(
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
        raise ValueError("builder profile not found")

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


def x_verify_builder_profile__mutmut_10(
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
        raise ValueError("BUILDER PROFILE NOT FOUND")

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


def x_verify_builder_profile__mutmut_11(
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

    profile.verification_status = None

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


def x_verify_builder_profile__mutmut_12(
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

    verification = None

    db.add(verification)
    db.commit()
    db.refresh(profile)

    return profile


def x_verify_builder_profile__mutmut_13(
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
        builder_profile_id=None,
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


def x_verify_builder_profile__mutmut_14(
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
        verification_type=None,
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


def x_verify_builder_profile__mutmut_15(
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
        status=None,
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


def x_verify_builder_profile__mutmut_16(
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
        admin_id=None,
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


def x_verify_builder_profile__mutmut_17(
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
        reason=None,
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


def x_verify_builder_profile__mutmut_18(
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
        verified_at=None,
        ai_assisted=False,
    )

    db.add(verification)
    db.commit()
    db.refresh(profile)

    return profile


def x_verify_builder_profile__mutmut_19(
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
        ai_assisted=None,
    )

    db.add(verification)
    db.commit()
    db.refresh(profile)

    return profile


def x_verify_builder_profile__mutmut_20(
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


def x_verify_builder_profile__mutmut_21(
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


def x_verify_builder_profile__mutmut_22(
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


def x_verify_builder_profile__mutmut_23(
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


def x_verify_builder_profile__mutmut_24(
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


def x_verify_builder_profile__mutmut_25(
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
        ai_assisted=False,
    )

    db.add(verification)
    db.commit()
    db.refresh(profile)

    return profile


def x_verify_builder_profile__mutmut_26(
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
        )

    db.add(verification)
    db.commit()
    db.refresh(profile)

    return profile


def x_verify_builder_profile__mutmut_27(
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
        verification_type="XXADMIN_REVIEWXX",
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


def x_verify_builder_profile__mutmut_28(
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
        verification_type="admin_review",
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


def x_verify_builder_profile__mutmut_29(
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
            if (status in {"VERIFIED", "REJECTED", "SUSPENDED"}) and False
            else None
        ),
        ai_assisted=False,
    )

    db.add(verification)
    db.commit()
    db.refresh(profile)

    return profile


def x_verify_builder_profile__mutmut_30(
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
            if (status in {"VERIFIED", "REJECTED", "SUSPENDED"}) or True
            else None
        ),
        ai_assisted=False,
    )

    db.add(verification)
    db.commit()
    db.refresh(profile)

    return profile


def x_verify_builder_profile__mutmut_31(
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
            if status not in {"VERIFIED", "REJECTED", "SUSPENDED"}
            else None
        ),
        ai_assisted=False,
    )

    db.add(verification)
    db.commit()
    db.refresh(profile)

    return profile


def x_verify_builder_profile__mutmut_32(
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
            if status in {"XXVERIFIEDXX", "REJECTED", "SUSPENDED"}
            else None
        ),
        ai_assisted=False,
    )

    db.add(verification)
    db.commit()
    db.refresh(profile)

    return profile


def x_verify_builder_profile__mutmut_33(
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
            if status in {"verified", "REJECTED", "SUSPENDED"}
            else None
        ),
        ai_assisted=False,
    )

    db.add(verification)
    db.commit()
    db.refresh(profile)

    return profile


def x_verify_builder_profile__mutmut_34(
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
            if status in {"VERIFIED", "XXREJECTEDXX", "SUSPENDED"}
            else None
        ),
        ai_assisted=False,
    )

    db.add(verification)
    db.commit()
    db.refresh(profile)

    return profile


def x_verify_builder_profile__mutmut_35(
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
            if status in {"VERIFIED", "rejected", "SUSPENDED"}
            else None
        ),
        ai_assisted=False,
    )

    db.add(verification)
    db.commit()
    db.refresh(profile)

    return profile


def x_verify_builder_profile__mutmut_36(
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
            if status in {"VERIFIED", "REJECTED", "XXSUSPENDEDXX"}
            else None
        ),
        ai_assisted=False,
    )

    db.add(verification)
    db.commit()
    db.refresh(profile)

    return profile


def x_verify_builder_profile__mutmut_37(
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
            if status in {"VERIFIED", "REJECTED", "suspended"}
            else None
        ),
        ai_assisted=False,
    )

    db.add(verification)
    db.commit()
    db.refresh(profile)

    return profile


def x_verify_builder_profile__mutmut_38(
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
        ai_assisted=True,
    )

    db.add(verification)
    db.commit()
    db.refresh(profile)

    return profile


def x_verify_builder_profile__mutmut_39(
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

    db.add(None)
    db.commit()
    db.refresh(profile)

    return profile


def x_verify_builder_profile__mutmut_40(
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
    db.refresh(None)

    return profile

mutants_x_verify_builder_profile__mutmut['_mutmut_orig'] = x_verify_builder_profile__mutmut_orig # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_1'] = x_verify_builder_profile__mutmut_1 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_2'] = x_verify_builder_profile__mutmut_2 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_3'] = x_verify_builder_profile__mutmut_3 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_4'] = x_verify_builder_profile__mutmut_4 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_5'] = x_verify_builder_profile__mutmut_5 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_6'] = x_verify_builder_profile__mutmut_6 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_7'] = x_verify_builder_profile__mutmut_7 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_8'] = x_verify_builder_profile__mutmut_8 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_9'] = x_verify_builder_profile__mutmut_9 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_10'] = x_verify_builder_profile__mutmut_10 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_11'] = x_verify_builder_profile__mutmut_11 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_12'] = x_verify_builder_profile__mutmut_12 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_13'] = x_verify_builder_profile__mutmut_13 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_14'] = x_verify_builder_profile__mutmut_14 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_15'] = x_verify_builder_profile__mutmut_15 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_16'] = x_verify_builder_profile__mutmut_16 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_17'] = x_verify_builder_profile__mutmut_17 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_18'] = x_verify_builder_profile__mutmut_18 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_19'] = x_verify_builder_profile__mutmut_19 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_20'] = x_verify_builder_profile__mutmut_20 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_21'] = x_verify_builder_profile__mutmut_21 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_22'] = x_verify_builder_profile__mutmut_22 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_23'] = x_verify_builder_profile__mutmut_23 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_24'] = x_verify_builder_profile__mutmut_24 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_25'] = x_verify_builder_profile__mutmut_25 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_26'] = x_verify_builder_profile__mutmut_26 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_27'] = x_verify_builder_profile__mutmut_27 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_28'] = x_verify_builder_profile__mutmut_28 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_29'] = x_verify_builder_profile__mutmut_29 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_30'] = x_verify_builder_profile__mutmut_30 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_31'] = x_verify_builder_profile__mutmut_31 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_32'] = x_verify_builder_profile__mutmut_32 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_33'] = x_verify_builder_profile__mutmut_33 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_34'] = x_verify_builder_profile__mutmut_34 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_35'] = x_verify_builder_profile__mutmut_35 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_36'] = x_verify_builder_profile__mutmut_36 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_37'] = x_verify_builder_profile__mutmut_37 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_38'] = x_verify_builder_profile__mutmut_38 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_39'] = x_verify_builder_profile__mutmut_39 # type: ignore # mutmut generated
mutants_x_verify_builder_profile__mutmut['x_verify_builder_profile__mutmut_40'] = x_verify_builder_profile__mutmut_40 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_review_project_version__mutmut)
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_orig(
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_1(
    db: Session,
    project_version_id: UUID,
    status: str,
    reason: str | None,
    admin_user: User,
) -> ProjectVersion:
    version = None

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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_2(
    db: Session,
    project_version_id: UUID,
    status: str,
    reason: str | None,
    admin_user: User,
) -> ProjectVersion:
    version = db.scalar(
        None
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_3(
    db: Session,
    project_version_id: UUID,
    status: str,
    reason: str | None,
    admin_user: User,
) -> ProjectVersion:
    version = db.scalar(
        select(ProjectVersion).where(
            None
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_4(
    db: Session,
    project_version_id: UUID,
    status: str,
    reason: str | None,
    admin_user: User,
) -> ProjectVersion:
    version = db.scalar(
        select(None).where(
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_5(
    db: Session,
    project_version_id: UUID,
    status: str,
    reason: str | None,
    admin_user: User,
) -> ProjectVersion:
    version = db.scalar(
        select(ProjectVersion).where(
            ProjectVersion.id != project_version_id
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_6(
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

    if version is not None:
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_7(
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
        raise ValueError(None)

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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_8(
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
        raise ValueError("XXProject version not foundXX")

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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_9(
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
        raise ValueError("project version not found")

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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_10(
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
        raise ValueError("PROJECT VERSION NOT FOUND")

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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_11(
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

    if version.status == "PENDING_APPROVAL":
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_12(
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

    if version.status != "XXPENDING_APPROVALXX":
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_13(
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

    if version.status != "pending_approval":
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_14(
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
            None
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_15(
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
            "XXOnly PENDING_APPROVAL versions can be reviewedXX"
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_16(
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
            "only pending_approval versions can be reviewed"
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_17(
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
            "ONLY PENDING_APPROVAL VERSIONS CAN BE REVIEWED"
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_18(
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

    if status == "REJECTED" or not reason:
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_19(
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

    if status != "REJECTED" and not reason:
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_20(
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

    if status == "XXREJECTEDXX" and not reason:
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_21(
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

    if status == "rejected" and not reason:
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_22(
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

    if status == "REJECTED" and reason:
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_23(
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
            None
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_24(
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
            "XXA rejection reason is requiredXX"
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_25(
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
            "a rejection reason is required"
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_26(
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
            "A REJECTION REASON IS REQUIRED"
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_27(
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

    if status in {"APPROVED", "REJECTED"}:
        raise ValueError(
            "Invalid review status"
        )

    version.status = status
    version.reviewed_by = admin_user.id
    version.review_reason = reason

    if status == "APPROVED":
        project = db.scalar(
            select(Project).where(
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_28(
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

    if status not in {"XXAPPROVEDXX", "REJECTED"}:
        raise ValueError(
            "Invalid review status"
        )

    version.status = status
    version.reviewed_by = admin_user.id
    version.review_reason = reason

    if status == "APPROVED":
        project = db.scalar(
            select(Project).where(
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_29(
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

    if status not in {"approved", "REJECTED"}:
        raise ValueError(
            "Invalid review status"
        )

    version.status = status
    version.reviewed_by = admin_user.id
    version.review_reason = reason

    if status == "APPROVED":
        project = db.scalar(
            select(Project).where(
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_30(
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

    if status not in {"APPROVED", "XXREJECTEDXX"}:
        raise ValueError(
            "Invalid review status"
        )

    version.status = status
    version.reviewed_by = admin_user.id
    version.review_reason = reason

    if status == "APPROVED":
        project = db.scalar(
            select(Project).where(
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_31(
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

    if status not in {"APPROVED", "rejected"}:
        raise ValueError(
            "Invalid review status"
        )

    version.status = status
    version.reviewed_by = admin_user.id
    version.review_reason = reason

    if status == "APPROVED":
        project = db.scalar(
            select(Project).where(
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_32(
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
            None
        )

    version.status = status
    version.reviewed_by = admin_user.id
    version.review_reason = reason

    if status == "APPROVED":
        project = db.scalar(
            select(Project).where(
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_33(
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
            "XXInvalid review statusXX"
        )

    version.status = status
    version.reviewed_by = admin_user.id
    version.review_reason = reason

    if status == "APPROVED":
        project = db.scalar(
            select(Project).where(
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_34(
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
            "invalid review status"
        )

    version.status = status
    version.reviewed_by = admin_user.id
    version.review_reason = reason

    if status == "APPROVED":
        project = db.scalar(
            select(Project).where(
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_35(
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
            "INVALID REVIEW STATUS"
        )

    version.status = status
    version.reviewed_by = admin_user.id
    version.review_reason = reason

    if status == "APPROVED":
        project = db.scalar(
            select(Project).where(
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_36(
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

    version.status = None
    version.reviewed_by = admin_user.id
    version.review_reason = reason

    if status == "APPROVED":
        project = db.scalar(
            select(Project).where(
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_37(
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
    version.reviewed_by = None
    version.review_reason = reason

    if status == "APPROVED":
        project = db.scalar(
            select(Project).where(
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_38(
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
    version.review_reason = None

    if status == "APPROVED":
        project = db.scalar(
            select(Project).where(
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_39(
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

    if status != "APPROVED":
        project = db.scalar(
            select(Project).where(
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_40(
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

    if status == "XXAPPROVEDXX":
        project = db.scalar(
            select(Project).where(
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_41(
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

    if status == "approved":
        project = db.scalar(
            select(Project).where(
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_42(
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
        project = None

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_43(
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
            None
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_44(
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
                None,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_45(
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
                Project.id == version.project_id,
                None,
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_46(
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
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_47(
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
                Project.id == version.project_id,
                )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_48(
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
            select(None).where(
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_49(
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
                Project.id != version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_50(
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is not None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_51(
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError(None)

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_52(
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("XXProject not foundXX")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_53(
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_54(
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("PROJECT NOT FOUND")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_55(
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = None

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_56(
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "XXACTIVEXX"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_57(
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "active"

    db.commit()
    db.refresh(version)

    return version

def x_review_project_version__mutmut_58(
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
                Project.id == version.project_id,
                Project.deleted_at.is_(None),
            )
        )

        if project is None:
            raise ValueError("Project not found")

        project.status = "ACTIVE"

    db.commit()
    db.refresh(None)

    return version

mutants_x_review_project_version__mutmut['_mutmut_orig'] = x_review_project_version__mutmut_orig # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_1'] = x_review_project_version__mutmut_1 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_2'] = x_review_project_version__mutmut_2 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_3'] = x_review_project_version__mutmut_3 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_4'] = x_review_project_version__mutmut_4 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_5'] = x_review_project_version__mutmut_5 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_6'] = x_review_project_version__mutmut_6 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_7'] = x_review_project_version__mutmut_7 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_8'] = x_review_project_version__mutmut_8 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_9'] = x_review_project_version__mutmut_9 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_10'] = x_review_project_version__mutmut_10 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_11'] = x_review_project_version__mutmut_11 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_12'] = x_review_project_version__mutmut_12 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_13'] = x_review_project_version__mutmut_13 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_14'] = x_review_project_version__mutmut_14 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_15'] = x_review_project_version__mutmut_15 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_16'] = x_review_project_version__mutmut_16 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_17'] = x_review_project_version__mutmut_17 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_18'] = x_review_project_version__mutmut_18 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_19'] = x_review_project_version__mutmut_19 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_20'] = x_review_project_version__mutmut_20 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_21'] = x_review_project_version__mutmut_21 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_22'] = x_review_project_version__mutmut_22 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_23'] = x_review_project_version__mutmut_23 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_24'] = x_review_project_version__mutmut_24 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_25'] = x_review_project_version__mutmut_25 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_26'] = x_review_project_version__mutmut_26 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_27'] = x_review_project_version__mutmut_27 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_28'] = x_review_project_version__mutmut_28 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_29'] = x_review_project_version__mutmut_29 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_30'] = x_review_project_version__mutmut_30 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_31'] = x_review_project_version__mutmut_31 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_32'] = x_review_project_version__mutmut_32 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_33'] = x_review_project_version__mutmut_33 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_34'] = x_review_project_version__mutmut_34 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_35'] = x_review_project_version__mutmut_35 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_36'] = x_review_project_version__mutmut_36 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_37'] = x_review_project_version__mutmut_37 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_38'] = x_review_project_version__mutmut_38 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_39'] = x_review_project_version__mutmut_39 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_40'] = x_review_project_version__mutmut_40 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_41'] = x_review_project_version__mutmut_41 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_42'] = x_review_project_version__mutmut_42 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_43'] = x_review_project_version__mutmut_43 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_44'] = x_review_project_version__mutmut_44 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_45'] = x_review_project_version__mutmut_45 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_46'] = x_review_project_version__mutmut_46 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_47'] = x_review_project_version__mutmut_47 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_48'] = x_review_project_version__mutmut_48 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_49'] = x_review_project_version__mutmut_49 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_50'] = x_review_project_version__mutmut_50 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_51'] = x_review_project_version__mutmut_51 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_52'] = x_review_project_version__mutmut_52 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_53'] = x_review_project_version__mutmut_53 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_54'] = x_review_project_version__mutmut_54 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_55'] = x_review_project_version__mutmut_55 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_56'] = x_review_project_version__mutmut_56 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_57'] = x_review_project_version__mutmut_57 # type: ignore # mutmut generated
mutants_x_review_project_version__mutmut['x_review_project_version__mutmut_58'] = x_review_project_version__mutmut_58 # type: ignore # mutmut generated

