from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.jwt import create_access_token
from app.core.security import hash_password, verify_password
from app.models.role import Role, UserRole
from app.models.user import User


def register_user(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == email)
    )

    if existing_user is not None:
        raise ValueError("A user with this email already exists")

    buyer_role = db.scalar(
        select(Role).where(Role.name == "BUYER")
    )

    if buyer_role is None:
        raise ValueError("BUYER role is not configured")

    user = User(
        email=email,
        password_hash=hash_password(password),
        full_name=full_name,
        phone=phone,
    )

    db.add(user)
    db.flush()

    user_role = UserRole(
        user_id=user.id,
        role_id=buyer_role.id,
    )

    db.add(user_role)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(
    db: Session,
    email: str,
    password: str,
) -> User | None:
    user = db.scalar(
        select(User).where(User.email == email)
    )

    if user is None:
        return None

    if not verify_password(password, user.password_hash):
        return None

    if not user.is_active:
        return None

    return user


def create_user_access_token(user: User) -> str:
    return create_access_token(user.id)