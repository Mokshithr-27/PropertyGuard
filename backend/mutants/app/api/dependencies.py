"""
PropertyGuard API Request Dependencies
--------------------------------------
Provides FastAPI dependency injection providers: database session lifecycle management (get_db),
JWT bearer token authentication (get_current_user), and role-based access gates (require_role).
"""

from collections.abc import Generator
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.core.jwt import decode_access_token
from app.models.user import User

from collections.abc import Callable

bearer_scheme = HTTPBearer()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_db__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_db__mutmut)
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def x_get_db__mutmut_orig() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def x_get_db__mutmut_1() -> Generator[Session, None, None]:
    db = None

    try:
        yield db
    finally:
        db.close()

mutants_x_get_db__mutmut['_mutmut_orig'] = x_get_db__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_db__mutmut['x_get_db__mutmut_1'] = x_get_db__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_current_user__mutmut)
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_orig(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_1(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = None
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_2(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = None

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_3(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=None,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_4(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=None,
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_5(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers=None,
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_6(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_7(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_8(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_9(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="XXCould not validate credentialsXX",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_10(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_11(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="COULD NOT VALIDATE CREDENTIALS",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_12(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"XXWWW-AuthenticateXX": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_13(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"www-authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_14(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-AUTHENTICATE": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_15(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "XXBearerXX"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_16(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_17(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "BEARER"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_18(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = None
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_19(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(None)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_20(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = None

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_21(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get(None)

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_22(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("XXsubXX")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_23(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("SUB")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_24(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_25(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = None

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_26(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(None)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_27(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = None

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_28(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        None
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_29(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(None)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_30(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(None).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_31(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id != user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_32(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is not None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_33(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_34(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=None,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_35(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=None,
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_36(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers=None,
        )

    return user


def x_get_current_user__mutmut_37(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_38(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_39(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            )

    return user


def x_get_current_user__mutmut_40(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="XXInactive userXX",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_41(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_42(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="INACTIVE USER",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_43(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"XXWWW-AuthenticateXX": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_44(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"www-authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_45(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-AUTHENTICATE": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_46(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "XXBearerXX"},
        )

    return user


def x_get_current_user__mutmut_47(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "bearer"},
        )

    return user


def x_get_current_user__mutmut_48(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise credentials_exception

        user_uuid = UUID(user_id)

    except (ValueError, TypeError):
        raise credentials_exception

    except Exception:
        raise credentials_exception

    user = db.scalar(
        select(User).where(User.id == user_uuid)
    )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "BEARER"},
        )

    return user

mutants_x_get_current_user__mutmut['_mutmut_orig'] = x_get_current_user__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_1'] = x_get_current_user__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_2'] = x_get_current_user__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_3'] = x_get_current_user__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_4'] = x_get_current_user__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_5'] = x_get_current_user__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_6'] = x_get_current_user__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_7'] = x_get_current_user__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_8'] = x_get_current_user__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_9'] = x_get_current_user__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_10'] = x_get_current_user__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_11'] = x_get_current_user__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_12'] = x_get_current_user__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_13'] = x_get_current_user__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_14'] = x_get_current_user__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_15'] = x_get_current_user__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_16'] = x_get_current_user__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_17'] = x_get_current_user__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_18'] = x_get_current_user__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_19'] = x_get_current_user__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_20'] = x_get_current_user__mutmut_20 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_21'] = x_get_current_user__mutmut_21 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_22'] = x_get_current_user__mutmut_22 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_23'] = x_get_current_user__mutmut_23 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_24'] = x_get_current_user__mutmut_24 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_25'] = x_get_current_user__mutmut_25 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_26'] = x_get_current_user__mutmut_26 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_27'] = x_get_current_user__mutmut_27 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_28'] = x_get_current_user__mutmut_28 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_29'] = x_get_current_user__mutmut_29 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_30'] = x_get_current_user__mutmut_30 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_31'] = x_get_current_user__mutmut_31 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_32'] = x_get_current_user__mutmut_32 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_33'] = x_get_current_user__mutmut_33 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_34'] = x_get_current_user__mutmut_34 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_35'] = x_get_current_user__mutmut_35 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_36'] = x_get_current_user__mutmut_36 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_37'] = x_get_current_user__mutmut_37 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_38'] = x_get_current_user__mutmut_38 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_39'] = x_get_current_user__mutmut_39 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_40'] = x_get_current_user__mutmut_40 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_41'] = x_get_current_user__mutmut_41 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_42'] = x_get_current_user__mutmut_42 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_43'] = x_get_current_user__mutmut_43 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_44'] = x_get_current_user__mutmut_44 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_45'] = x_get_current_user__mutmut_45 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_46'] = x_get_current_user__mutmut_46 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_47'] = x_get_current_user__mutmut_47 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_48'] = x_get_current_user__mutmut_48 # type: ignore # mutmut generated
mutants_x_require_role__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_require_role__mutmut)
def require_role(required_role: str) -> Callable:
    def role_dependency(
        current_user: User = Depends(get_current_user),
    ) -> User:
        has_role = any(
            user_role.role.name == required_role
            for user_role in current_user.roles
        )

        if not has_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"{required_role} role required",
            )

        return current_user

    return role_dependency


def x_require_role__mutmut_orig(required_role: str) -> Callable:
    def role_dependency(
        current_user: User = Depends(get_current_user),
    ) -> User:
        has_role = any(
            user_role.role.name == required_role
            for user_role in current_user.roles
        )

        if not has_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"{required_role} role required",
            )

        return current_user

    return role_dependency


def x_require_role__mutmut_1(required_role: str) -> Callable:
    def role_dependency(
        current_user: User = Depends(get_current_user),
    ) -> User:
        has_role = None

        if not has_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"{required_role} role required",
            )

        return current_user

    return role_dependency


def x_require_role__mutmut_2(required_role: str) -> Callable:
    def role_dependency(
        current_user: User = Depends(get_current_user),
    ) -> User:
        has_role = any(
            None
        )

        if not has_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"{required_role} role required",
            )

        return current_user

    return role_dependency


def x_require_role__mutmut_3(required_role: str) -> Callable:
    def role_dependency(
        current_user: User = Depends(get_current_user),
    ) -> User:
        has_role = any(
            user_role.role.name != required_role
            for user_role in current_user.roles
        )

        if not has_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"{required_role} role required",
            )

        return current_user

    return role_dependency


def x_require_role__mutmut_4(required_role: str) -> Callable:
    def role_dependency(
        current_user: User = Depends(get_current_user),
    ) -> User:
        has_role = any(
            user_role.role.name == required_role
            for user_role in current_user.roles
        )

        if has_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"{required_role} role required",
            )

        return current_user

    return role_dependency


def x_require_role__mutmut_5(required_role: str) -> Callable:
    def role_dependency(
        current_user: User = Depends(get_current_user),
    ) -> User:
        has_role = any(
            user_role.role.name == required_role
            for user_role in current_user.roles
        )

        if not has_role:
            raise HTTPException(
                status_code=None,
                detail=f"{required_role} role required",
            )

        return current_user

    return role_dependency


def x_require_role__mutmut_6(required_role: str) -> Callable:
    def role_dependency(
        current_user: User = Depends(get_current_user),
    ) -> User:
        has_role = any(
            user_role.role.name == required_role
            for user_role in current_user.roles
        )

        if not has_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=None,
            )

        return current_user

    return role_dependency


def x_require_role__mutmut_7(required_role: str) -> Callable:
    def role_dependency(
        current_user: User = Depends(get_current_user),
    ) -> User:
        has_role = any(
            user_role.role.name == required_role
            for user_role in current_user.roles
        )

        if not has_role:
            raise HTTPException(
                detail=f"{required_role} role required",
            )

        return current_user

    return role_dependency


def x_require_role__mutmut_8(required_role: str) -> Callable:
    def role_dependency(
        current_user: User = Depends(get_current_user),
    ) -> User:
        has_role = any(
            user_role.role.name == required_role
            for user_role in current_user.roles
        )

        if not has_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                )

        return current_user

    return role_dependency

mutants_x_require_role__mutmut['_mutmut_orig'] = x_require_role__mutmut_orig # type: ignore # mutmut generated
mutants_x_require_role__mutmut['x_require_role__mutmut_1'] = x_require_role__mutmut_1 # type: ignore # mutmut generated
mutants_x_require_role__mutmut['x_require_role__mutmut_2'] = x_require_role__mutmut_2 # type: ignore # mutmut generated
mutants_x_require_role__mutmut['x_require_role__mutmut_3'] = x_require_role__mutmut_3 # type: ignore # mutmut generated
mutants_x_require_role__mutmut['x_require_role__mutmut_4'] = x_require_role__mutmut_4 # type: ignore # mutmut generated
mutants_x_require_role__mutmut['x_require_role__mutmut_5'] = x_require_role__mutmut_5 # type: ignore # mutmut generated
mutants_x_require_role__mutmut['x_require_role__mutmut_6'] = x_require_role__mutmut_6 # type: ignore # mutmut generated
mutants_x_require_role__mutmut['x_require_role__mutmut_7'] = x_require_role__mutmut_7 # type: ignore # mutmut generated
mutants_x_require_role__mutmut['x_require_role__mutmut_8'] = x_require_role__mutmut_8 # type: ignore # mutmut generated