from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.builder import BuilderProfile
from app.models.user import User


def get_builder_profile(
    db: Session,
    user: User,
) -> BuilderProfile | None:
    return db.scalar(
        select(BuilderProfile).where(
            BuilderProfile.user_id == user.id
        )
    )


def create_builder_profile(
    db: Session,
    user: User,
    company_name: str,
    registration_number: str | None = None,
    address: str | None = None,
) -> BuilderProfile:
    existing = get_builder_profile(db, user)

    if existing is not None:
        raise ValueError("Builder profile already exists")

    profile = BuilderProfile(
        user_id=user.id,
        company_name=company_name,
        registration_number=registration_number,
        address=address,
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile