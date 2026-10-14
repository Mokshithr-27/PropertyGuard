"""
PropertyGuard User Authentication Service
-----------------------------------------
Handles user registration, password verification, role association (BUYER, BUILDER),
profile creation, and JWT access token generation.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.jwt import create_access_token
from app.core.security import hash_password, verify_password
from app.models.role import Role, UserRole
from app.models.user import User


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_register_user__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register_user__mutmut)
def register_user(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_orig(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_1(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = None

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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_2(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        None
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_3(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(User).where(None)
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_4(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(None).where(User.email == email)
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_5(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(User).where(User.email != email)
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_6(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == email)
    )

    if existing_user is None:
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_7(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == email)
    )

    if existing_user is not None:
        raise ValueError(None)

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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_8(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == email)
    )

    if existing_user is not None:
        raise ValueError("XXA user with this email already existsXX")

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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_9(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == email)
    )

    if existing_user is not None:
        raise ValueError("a user with this email already exists")

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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_10(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == email)
    )

    if existing_user is not None:
        raise ValueError("A USER WITH THIS EMAIL ALREADY EXISTS")

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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_11(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == email)
    )

    if existing_user is not None:
        raise ValueError("A user with this email already exists")

    buyer_role = None

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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_12(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == email)
    )

    if existing_user is not None:
        raise ValueError("A user with this email already exists")

    buyer_role = db.scalar(
        None
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_13(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == email)
    )

    if existing_user is not None:
        raise ValueError("A user with this email already exists")

    buyer_role = db.scalar(
        select(Role).where(None)
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_14(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == email)
    )

    if existing_user is not None:
        raise ValueError("A user with this email already exists")

    buyer_role = db.scalar(
        select(None).where(Role.name == "BUYER")
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_15(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == email)
    )

    if existing_user is not None:
        raise ValueError("A user with this email already exists")

    buyer_role = db.scalar(
        select(Role).where(Role.name != "BUYER")
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_16(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == email)
    )

    if existing_user is not None:
        raise ValueError("A user with this email already exists")

    buyer_role = db.scalar(
        select(Role).where(Role.name == "XXBUYERXX")
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_17(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == email)
    )

    if existing_user is not None:
        raise ValueError("A user with this email already exists")

    buyer_role = db.scalar(
        select(Role).where(Role.name == "buyer")
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_18(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == email)
    )

    if existing_user is not None:
        raise ValueError("A user with this email already exists")

    buyer_role = db.scalar(
        select(Role).where(Role.name == "BUYER")
    )

    if buyer_role is not None:
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_19(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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
        raise ValueError(None)

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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_20(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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
        raise ValueError("XXBUYER role is not configuredXX")

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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_21(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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
        raise ValueError("buyer role is not configured")

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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_22(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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
        raise ValueError("BUYER ROLE IS NOT CONFIGURED")

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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_23(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    user = None

    db.add(user)
    db.flush()

    user_role = UserRole(
        user_id=user.id,
        role_id=buyer_role.id,
    )
    db.add(user_role)

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_24(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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
        email=None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_25(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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
        password_hash=None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_26(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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
        full_name=None,
        phone=phone,
    )

    db.add(user)
    db.flush()

    user_role = UserRole(
        user_id=user.id,
        role_id=buyer_role.id,
    )
    db.add(user_role)

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_27(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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
        phone=None,
    )

    db.add(user)
    db.flush()

    user_role = UserRole(
        user_id=user.id,
        role_id=buyer_role.id,
    )
    db.add(user_role)

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_28(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_29(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_30(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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
        phone=phone,
    )

    db.add(user)
    db.flush()

    user_role = UserRole(
        user_id=user.id,
        role_id=buyer_role.id,
    )
    db.add(user_role)

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_31(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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
        )

    db.add(user)
    db.flush()

    user_role = UserRole(
        user_id=user.id,
        role_id=buyer_role.id,
    )
    db.add(user_role)

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_32(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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
        password_hash=hash_password(None),
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_33(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    db.add(None)
    db.flush()

    user_role = UserRole(
        user_id=user.id,
        role_id=buyer_role.id,
    )
    db.add(user_role)

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_34(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    user_role = None
    db.add(user_role)

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_35(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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
        user_id=None,
        role_id=buyer_role.id,
    )
    db.add(user_role)

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_36(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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
        role_id=None,
    )
    db.add(user_role)

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_37(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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
        role_id=buyer_role.id,
    )
    db.add(user_role)

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_38(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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
        )
    db.add(user_role)

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_39(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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
    db.add(None)

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_40(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = None
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_41(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").lower().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_42(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role and "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_43(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "XXXX").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_44(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role != "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_45(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "XXBUILDERXX":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_46(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "builder":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_47(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = None
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_48(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            None
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_49(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(None)
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_50(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(None).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_51(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name != "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_52(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "XXBUILDERXX")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_53(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "builder")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_54(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(None)
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_55(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=None, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_56(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=None))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_57(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_58(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, ))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_59(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                None
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_60(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=None,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_61(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=None,
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_62(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status=None,
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_63(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_64(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_65(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_66(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name and "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_67(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "XXBuilder EnterpriseXX",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_68(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "builder enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_69(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "BUILDER ENTERPRISE",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_70(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="XXPENDINGXX",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_71(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="pending",
                )
            )

    db.commit()
    db.refresh(user)

    return user


def x_register_user__mutmut_72(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str | None = None,
    role: str | None = None,
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

    req_role = (role or "").upper().strip()
    if req_role == "BUILDER":
        builder_role = db.scalar(
            select(Role).where(Role.name == "BUILDER")
        )
        if builder_role:
            db.add(UserRole(user_id=user.id, role_id=builder_role.id))
            from app.models.builder import BuilderProfile
            db.add(
                BuilderProfile(
                    user_id=user.id,
                    company_name=full_name or "Builder Enterprise",
                    # Builder verification is an administrative trust boundary.
                    # Newly registered builders must wait for admin verification.
                    verification_status="PENDING",
                )
            )

    db.commit()
    db.refresh(None)

    return user

mutants_x_register_user__mutmut['_mutmut_orig'] = x_register_user__mutmut_orig # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_1'] = x_register_user__mutmut_1 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_2'] = x_register_user__mutmut_2 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_3'] = x_register_user__mutmut_3 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_4'] = x_register_user__mutmut_4 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_5'] = x_register_user__mutmut_5 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_6'] = x_register_user__mutmut_6 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_7'] = x_register_user__mutmut_7 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_8'] = x_register_user__mutmut_8 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_9'] = x_register_user__mutmut_9 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_10'] = x_register_user__mutmut_10 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_11'] = x_register_user__mutmut_11 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_12'] = x_register_user__mutmut_12 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_13'] = x_register_user__mutmut_13 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_14'] = x_register_user__mutmut_14 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_15'] = x_register_user__mutmut_15 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_16'] = x_register_user__mutmut_16 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_17'] = x_register_user__mutmut_17 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_18'] = x_register_user__mutmut_18 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_19'] = x_register_user__mutmut_19 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_20'] = x_register_user__mutmut_20 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_21'] = x_register_user__mutmut_21 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_22'] = x_register_user__mutmut_22 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_23'] = x_register_user__mutmut_23 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_24'] = x_register_user__mutmut_24 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_25'] = x_register_user__mutmut_25 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_26'] = x_register_user__mutmut_26 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_27'] = x_register_user__mutmut_27 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_28'] = x_register_user__mutmut_28 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_29'] = x_register_user__mutmut_29 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_30'] = x_register_user__mutmut_30 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_31'] = x_register_user__mutmut_31 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_32'] = x_register_user__mutmut_32 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_33'] = x_register_user__mutmut_33 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_34'] = x_register_user__mutmut_34 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_35'] = x_register_user__mutmut_35 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_36'] = x_register_user__mutmut_36 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_37'] = x_register_user__mutmut_37 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_38'] = x_register_user__mutmut_38 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_39'] = x_register_user__mutmut_39 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_40'] = x_register_user__mutmut_40 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_41'] = x_register_user__mutmut_41 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_42'] = x_register_user__mutmut_42 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_43'] = x_register_user__mutmut_43 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_44'] = x_register_user__mutmut_44 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_45'] = x_register_user__mutmut_45 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_46'] = x_register_user__mutmut_46 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_47'] = x_register_user__mutmut_47 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_48'] = x_register_user__mutmut_48 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_49'] = x_register_user__mutmut_49 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_50'] = x_register_user__mutmut_50 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_51'] = x_register_user__mutmut_51 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_52'] = x_register_user__mutmut_52 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_53'] = x_register_user__mutmut_53 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_54'] = x_register_user__mutmut_54 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_55'] = x_register_user__mutmut_55 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_56'] = x_register_user__mutmut_56 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_57'] = x_register_user__mutmut_57 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_58'] = x_register_user__mutmut_58 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_59'] = x_register_user__mutmut_59 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_60'] = x_register_user__mutmut_60 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_61'] = x_register_user__mutmut_61 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_62'] = x_register_user__mutmut_62 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_63'] = x_register_user__mutmut_63 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_64'] = x_register_user__mutmut_64 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_65'] = x_register_user__mutmut_65 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_66'] = x_register_user__mutmut_66 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_67'] = x_register_user__mutmut_67 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_68'] = x_register_user__mutmut_68 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_69'] = x_register_user__mutmut_69 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_70'] = x_register_user__mutmut_70 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_71'] = x_register_user__mutmut_71 # type: ignore # mutmut generated
mutants_x_register_user__mutmut['x_register_user__mutmut_72'] = x_register_user__mutmut_72 # type: ignore # mutmut generated
mutants_x_authenticate_user__mutmut: MutantDict = {}  # type: ignore



@_mutmut_mutated(mutants_x_authenticate_user__mutmut)
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



def x_authenticate_user__mutmut_orig(
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



def x_authenticate_user__mutmut_1(
    db: Session,
    email: str,
    password: str,
) -> User | None:
    user = None

    if user is None:
        return None

    if not verify_password(password, user.password_hash):
        return None

    if not user.is_active:
        return None

    return user



def x_authenticate_user__mutmut_2(
    db: Session,
    email: str,
    password: str,
) -> User | None:
    user = db.scalar(
        None
    )

    if user is None:
        return None

    if not verify_password(password, user.password_hash):
        return None

    if not user.is_active:
        return None

    return user



def x_authenticate_user__mutmut_3(
    db: Session,
    email: str,
    password: str,
) -> User | None:
    user = db.scalar(
        select(User).where(None)
    )

    if user is None:
        return None

    if not verify_password(password, user.password_hash):
        return None

    if not user.is_active:
        return None

    return user



def x_authenticate_user__mutmut_4(
    db: Session,
    email: str,
    password: str,
) -> User | None:
    user = db.scalar(
        select(None).where(User.email == email)
    )

    if user is None:
        return None

    if not verify_password(password, user.password_hash):
        return None

    if not user.is_active:
        return None

    return user



def x_authenticate_user__mutmut_5(
    db: Session,
    email: str,
    password: str,
) -> User | None:
    user = db.scalar(
        select(User).where(User.email != email)
    )

    if user is None:
        return None

    if not verify_password(password, user.password_hash):
        return None

    if not user.is_active:
        return None

    return user



def x_authenticate_user__mutmut_6(
    db: Session,
    email: str,
    password: str,
) -> User | None:
    user = db.scalar(
        select(User).where(User.email == email)
    )

    if user is not None:
        return None

    if not verify_password(password, user.password_hash):
        return None

    if not user.is_active:
        return None

    return user



def x_authenticate_user__mutmut_7(
    db: Session,
    email: str,
    password: str,
) -> User | None:
    user = db.scalar(
        select(User).where(User.email == email)
    )

    if user is None:
        return None

    if verify_password(password, user.password_hash):
        return None

    if not user.is_active:
        return None

    return user



def x_authenticate_user__mutmut_8(
    db: Session,
    email: str,
    password: str,
) -> User | None:
    user = db.scalar(
        select(User).where(User.email == email)
    )

    if user is None:
        return None

    if not verify_password(None, user.password_hash):
        return None

    if not user.is_active:
        return None

    return user



def x_authenticate_user__mutmut_9(
    db: Session,
    email: str,
    password: str,
) -> User | None:
    user = db.scalar(
        select(User).where(User.email == email)
    )

    if user is None:
        return None

    if not verify_password(password, None):
        return None

    if not user.is_active:
        return None

    return user



def x_authenticate_user__mutmut_10(
    db: Session,
    email: str,
    password: str,
) -> User | None:
    user = db.scalar(
        select(User).where(User.email == email)
    )

    if user is None:
        return None

    if not verify_password(user.password_hash):
        return None

    if not user.is_active:
        return None

    return user



def x_authenticate_user__mutmut_11(
    db: Session,
    email: str,
    password: str,
) -> User | None:
    user = db.scalar(
        select(User).where(User.email == email)
    )

    if user is None:
        return None

    if not verify_password(password, ):
        return None

    if not user.is_active:
        return None

    return user



def x_authenticate_user__mutmut_12(
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

    if user.is_active:
        return None

    return user

mutants_x_authenticate_user__mutmut['_mutmut_orig'] = x_authenticate_user__mutmut_orig # type: ignore # mutmut generated
mutants_x_authenticate_user__mutmut['x_authenticate_user__mutmut_1'] = x_authenticate_user__mutmut_1 # type: ignore # mutmut generated
mutants_x_authenticate_user__mutmut['x_authenticate_user__mutmut_2'] = x_authenticate_user__mutmut_2 # type: ignore # mutmut generated
mutants_x_authenticate_user__mutmut['x_authenticate_user__mutmut_3'] = x_authenticate_user__mutmut_3 # type: ignore # mutmut generated
mutants_x_authenticate_user__mutmut['x_authenticate_user__mutmut_4'] = x_authenticate_user__mutmut_4 # type: ignore # mutmut generated
mutants_x_authenticate_user__mutmut['x_authenticate_user__mutmut_5'] = x_authenticate_user__mutmut_5 # type: ignore # mutmut generated
mutants_x_authenticate_user__mutmut['x_authenticate_user__mutmut_6'] = x_authenticate_user__mutmut_6 # type: ignore # mutmut generated
mutants_x_authenticate_user__mutmut['x_authenticate_user__mutmut_7'] = x_authenticate_user__mutmut_7 # type: ignore # mutmut generated
mutants_x_authenticate_user__mutmut['x_authenticate_user__mutmut_8'] = x_authenticate_user__mutmut_8 # type: ignore # mutmut generated
mutants_x_authenticate_user__mutmut['x_authenticate_user__mutmut_9'] = x_authenticate_user__mutmut_9 # type: ignore # mutmut generated
mutants_x_authenticate_user__mutmut['x_authenticate_user__mutmut_10'] = x_authenticate_user__mutmut_10 # type: ignore # mutmut generated
mutants_x_authenticate_user__mutmut['x_authenticate_user__mutmut_11'] = x_authenticate_user__mutmut_11 # type: ignore # mutmut generated
mutants_x_authenticate_user__mutmut['x_authenticate_user__mutmut_12'] = x_authenticate_user__mutmut_12 # type: ignore # mutmut generated
mutants_x_create_user_access_token__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_create_user_access_token__mutmut)
def create_user_access_token(user: User) -> str:
    return create_access_token(user.id)


def x_create_user_access_token__mutmut_orig(user: User) -> str:
    return create_access_token(user.id)


def x_create_user_access_token__mutmut_1(user: User) -> str:
    return create_access_token(None)

mutants_x_create_user_access_token__mutmut['_mutmut_orig'] = x_create_user_access_token__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_user_access_token__mutmut['x_create_user_access_token__mutmut_1'] = x_create_user_access_token__mutmut_1 # type: ignore # mutmut generated