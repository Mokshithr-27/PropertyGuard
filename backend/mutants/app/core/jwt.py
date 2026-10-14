"""
PropertyGuard JWT Token Handler
-------------------------------
Provides utilities for creating and decoding cryptographic JSON Web Tokens (JWT)
for user authentication sessions, setting standard expiry and claims.
"""

from datetime import datetime, timedelta, timezone
from uuid import UUID

import jwt

from app.core.config import (
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
    JWT_ALGORITHM,
    JWT_SECRET_KEY,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_create_access_token__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_create_access_token__mutmut)
def create_access_token(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_orig(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_1(user_id: UUID) -> str:
    now = None
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_2(user_id: UUID) -> str:
    now = datetime.now(None)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_3(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = None

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_4(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now - timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_5(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=None
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_6(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = None

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_7(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "XXsubXX": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_8(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "SUB": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_9(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(None),
        "iat": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_10(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "XXiatXX": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_11(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "IAT": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_12(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "XXexpXX": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_13(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "EXP": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_14(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "XXtypeXX": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_15(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "TYPE": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_16(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "XXaccessXX",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_17(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "ACCESS",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_18(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        None,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_19(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        None,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_20(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=None,
    )


def x_create_access_token__mutmut_21(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_22(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        algorithm=JWT_ALGORITHM,
    )


def x_create_access_token__mutmut_23(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": expires_at,
        "type": "access",
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        )

mutants_x_create_access_token__mutmut['_mutmut_orig'] = x_create_access_token__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_1'] = x_create_access_token__mutmut_1 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_2'] = x_create_access_token__mutmut_2 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_3'] = x_create_access_token__mutmut_3 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_4'] = x_create_access_token__mutmut_4 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_5'] = x_create_access_token__mutmut_5 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_6'] = x_create_access_token__mutmut_6 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_7'] = x_create_access_token__mutmut_7 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_8'] = x_create_access_token__mutmut_8 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_9'] = x_create_access_token__mutmut_9 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_10'] = x_create_access_token__mutmut_10 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_11'] = x_create_access_token__mutmut_11 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_12'] = x_create_access_token__mutmut_12 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_13'] = x_create_access_token__mutmut_13 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_14'] = x_create_access_token__mutmut_14 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_15'] = x_create_access_token__mutmut_15 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_16'] = x_create_access_token__mutmut_16 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_17'] = x_create_access_token__mutmut_17 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_18'] = x_create_access_token__mutmut_18 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_19'] = x_create_access_token__mutmut_19 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_20'] = x_create_access_token__mutmut_20 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_21'] = x_create_access_token__mutmut_21 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_22'] = x_create_access_token__mutmut_22 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_23'] = x_create_access_token__mutmut_23 # type: ignore # mutmut generated
mutants_x_decode_access_token__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_decode_access_token__mutmut)
def decode_access_token(token: str) -> dict:
    return jwt.decode(
        token,
        JWT_SECRET_KEY,
        algorithms=[JWT_ALGORITHM],
    )


def x_decode_access_token__mutmut_orig(token: str) -> dict:
    return jwt.decode(
        token,
        JWT_SECRET_KEY,
        algorithms=[JWT_ALGORITHM],
    )


def x_decode_access_token__mutmut_1(token: str) -> dict:
    return jwt.decode(
        None,
        JWT_SECRET_KEY,
        algorithms=[JWT_ALGORITHM],
    )


def x_decode_access_token__mutmut_2(token: str) -> dict:
    return jwt.decode(
        token,
        None,
        algorithms=[JWT_ALGORITHM],
    )


def x_decode_access_token__mutmut_3(token: str) -> dict:
    return jwt.decode(
        token,
        JWT_SECRET_KEY,
        algorithms=None,
    )


def x_decode_access_token__mutmut_4(token: str) -> dict:
    return jwt.decode(
        JWT_SECRET_KEY,
        algorithms=[JWT_ALGORITHM],
    )


def x_decode_access_token__mutmut_5(token: str) -> dict:
    return jwt.decode(
        token,
        algorithms=[JWT_ALGORITHM],
    )


def x_decode_access_token__mutmut_6(token: str) -> dict:
    return jwt.decode(
        token,
        JWT_SECRET_KEY,
        )

mutants_x_decode_access_token__mutmut['_mutmut_orig'] = x_decode_access_token__mutmut_orig # type: ignore # mutmut generated
mutants_x_decode_access_token__mutmut['x_decode_access_token__mutmut_1'] = x_decode_access_token__mutmut_1 # type: ignore # mutmut generated
mutants_x_decode_access_token__mutmut['x_decode_access_token__mutmut_2'] = x_decode_access_token__mutmut_2 # type: ignore # mutmut generated
mutants_x_decode_access_token__mutmut['x_decode_access_token__mutmut_3'] = x_decode_access_token__mutmut_3 # type: ignore # mutmut generated
mutants_x_decode_access_token__mutmut['x_decode_access_token__mutmut_4'] = x_decode_access_token__mutmut_4 # type: ignore # mutmut generated
mutants_x_decode_access_token__mutmut['x_decode_access_token__mutmut_5'] = x_decode_access_token__mutmut_5 # type: ignore # mutmut generated
mutants_x_decode_access_token__mutmut['x_decode_access_token__mutmut_6'] = x_decode_access_token__mutmut_6 # type: ignore # mutmut generated