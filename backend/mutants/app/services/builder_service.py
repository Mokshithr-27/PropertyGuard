"""
PropertyGuard Builder Profile Business Service
----------------------------------------------
Manages retrieval and creation of BuilderProfile records linked to registered
builder user accounts.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.builder import BuilderProfile
from app.models.user import User


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_builder_profile__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_builder_profile__mutmut)
def get_builder_profile(
    db: Session,
    user: User,
) -> BuilderProfile | None:
    return db.scalar(
        select(BuilderProfile).where(
            BuilderProfile.user_id == user.id
        )
    )


def x_get_builder_profile__mutmut_orig(
    db: Session,
    user: User,
) -> BuilderProfile | None:
    return db.scalar(
        select(BuilderProfile).where(
            BuilderProfile.user_id == user.id
        )
    )


def x_get_builder_profile__mutmut_1(
    db: Session,
    user: User,
) -> BuilderProfile | None:
    return db.scalar(
        None
    )


def x_get_builder_profile__mutmut_2(
    db: Session,
    user: User,
) -> BuilderProfile | None:
    return db.scalar(
        select(BuilderProfile).where(
            None
        )
    )


def x_get_builder_profile__mutmut_3(
    db: Session,
    user: User,
) -> BuilderProfile | None:
    return db.scalar(
        select(None).where(
            BuilderProfile.user_id == user.id
        )
    )


def x_get_builder_profile__mutmut_4(
    db: Session,
    user: User,
) -> BuilderProfile | None:
    return db.scalar(
        select(BuilderProfile).where(
            BuilderProfile.user_id != user.id
        )
    )

mutants_x_get_builder_profile__mutmut['_mutmut_orig'] = x_get_builder_profile__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_builder_profile__mutmut['x_get_builder_profile__mutmut_1'] = x_get_builder_profile__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_builder_profile__mutmut['x_get_builder_profile__mutmut_2'] = x_get_builder_profile__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_builder_profile__mutmut['x_get_builder_profile__mutmut_3'] = x_get_builder_profile__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_builder_profile__mutmut['x_get_builder_profile__mutmut_4'] = x_get_builder_profile__mutmut_4 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_create_builder_profile__mutmut)
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


def x_create_builder_profile__mutmut_orig(
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


def x_create_builder_profile__mutmut_1(
    db: Session,
    user: User,
    company_name: str,
    registration_number: str | None = None,
    address: str | None = None,
) -> BuilderProfile:
    existing = None

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


def x_create_builder_profile__mutmut_2(
    db: Session,
    user: User,
    company_name: str,
    registration_number: str | None = None,
    address: str | None = None,
) -> BuilderProfile:
    existing = get_builder_profile(None, user)

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


def x_create_builder_profile__mutmut_3(
    db: Session,
    user: User,
    company_name: str,
    registration_number: str | None = None,
    address: str | None = None,
) -> BuilderProfile:
    existing = get_builder_profile(db, None)

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


def x_create_builder_profile__mutmut_4(
    db: Session,
    user: User,
    company_name: str,
    registration_number: str | None = None,
    address: str | None = None,
) -> BuilderProfile:
    existing = get_builder_profile(user)

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


def x_create_builder_profile__mutmut_5(
    db: Session,
    user: User,
    company_name: str,
    registration_number: str | None = None,
    address: str | None = None,
) -> BuilderProfile:
    existing = get_builder_profile(db, )

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


def x_create_builder_profile__mutmut_6(
    db: Session,
    user: User,
    company_name: str,
    registration_number: str | None = None,
    address: str | None = None,
) -> BuilderProfile:
    existing = get_builder_profile(db, user)

    if existing is None:
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


def x_create_builder_profile__mutmut_7(
    db: Session,
    user: User,
    company_name: str,
    registration_number: str | None = None,
    address: str | None = None,
) -> BuilderProfile:
    existing = get_builder_profile(db, user)

    if existing is not None:
        raise ValueError(None)

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


def x_create_builder_profile__mutmut_8(
    db: Session,
    user: User,
    company_name: str,
    registration_number: str | None = None,
    address: str | None = None,
) -> BuilderProfile:
    existing = get_builder_profile(db, user)

    if existing is not None:
        raise ValueError("XXBuilder profile already existsXX")

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


def x_create_builder_profile__mutmut_9(
    db: Session,
    user: User,
    company_name: str,
    registration_number: str | None = None,
    address: str | None = None,
) -> BuilderProfile:
    existing = get_builder_profile(db, user)

    if existing is not None:
        raise ValueError("builder profile already exists")

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


def x_create_builder_profile__mutmut_10(
    db: Session,
    user: User,
    company_name: str,
    registration_number: str | None = None,
    address: str | None = None,
) -> BuilderProfile:
    existing = get_builder_profile(db, user)

    if existing is not None:
        raise ValueError("BUILDER PROFILE ALREADY EXISTS")

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


def x_create_builder_profile__mutmut_11(
    db: Session,
    user: User,
    company_name: str,
    registration_number: str | None = None,
    address: str | None = None,
) -> BuilderProfile:
    existing = get_builder_profile(db, user)

    if existing is not None:
        raise ValueError("Builder profile already exists")

    profile = None

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile


def x_create_builder_profile__mutmut_12(
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
        user_id=None,
        company_name=company_name,
        registration_number=registration_number,
        address=address,
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile


def x_create_builder_profile__mutmut_13(
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
        company_name=None,
        registration_number=registration_number,
        address=address,
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile


def x_create_builder_profile__mutmut_14(
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
        registration_number=None,
        address=address,
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile


def x_create_builder_profile__mutmut_15(
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
        address=None,
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile


def x_create_builder_profile__mutmut_16(
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
        company_name=company_name,
        registration_number=registration_number,
        address=address,
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile


def x_create_builder_profile__mutmut_17(
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
        registration_number=registration_number,
        address=address,
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile


def x_create_builder_profile__mutmut_18(
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
        address=address,
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile


def x_create_builder_profile__mutmut_19(
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
        )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile


def x_create_builder_profile__mutmut_20(
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

    db.add(None)
    db.commit()
    db.refresh(profile)

    return profile


def x_create_builder_profile__mutmut_21(
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
    db.refresh(None)

    return profile

mutants_x_create_builder_profile__mutmut['_mutmut_orig'] = x_create_builder_profile__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_1'] = x_create_builder_profile__mutmut_1 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_2'] = x_create_builder_profile__mutmut_2 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_3'] = x_create_builder_profile__mutmut_3 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_4'] = x_create_builder_profile__mutmut_4 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_5'] = x_create_builder_profile__mutmut_5 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_6'] = x_create_builder_profile__mutmut_6 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_7'] = x_create_builder_profile__mutmut_7 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_8'] = x_create_builder_profile__mutmut_8 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_9'] = x_create_builder_profile__mutmut_9 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_10'] = x_create_builder_profile__mutmut_10 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_11'] = x_create_builder_profile__mutmut_11 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_12'] = x_create_builder_profile__mutmut_12 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_13'] = x_create_builder_profile__mutmut_13 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_14'] = x_create_builder_profile__mutmut_14 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_15'] = x_create_builder_profile__mutmut_15 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_16'] = x_create_builder_profile__mutmut_16 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_17'] = x_create_builder_profile__mutmut_17 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_18'] = x_create_builder_profile__mutmut_18 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_19'] = x_create_builder_profile__mutmut_19 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_20'] = x_create_builder_profile__mutmut_20 # type: ignore # mutmut generated
mutants_x_create_builder_profile__mutmut['x_create_builder_profile__mutmut_21'] = x_create_builder_profile__mutmut_21 # type: ignore # mutmut generated