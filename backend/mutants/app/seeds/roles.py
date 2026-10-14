"""
PropertyGuard Role Seeding Script
---------------------------------
Seeds initial RBAC system roles (BUYER, BUILDER, ADMIN, SUPER_ADMIN)
into the database if they do not already exist.
"""

from sqlalchemy import select

from app.core.database import SessionLocal
from app.models.role import Role


ROLES = [
    {
        "name": "BUYER",
        "description": "Property buyer who can search projects and view verified information.",
    },
    {
        "name": "BUILDER",
        "description": "Builder who can manage projects, documents, compliance findings, and submissions.",
    },
    {
        "name": "ADMIN",
        "description": "Administrator who manages verification, approvals, governance, and oversight.",
    },
    {
        "name": "SUPER_ADMIN",
        "description": "System-level administrator with unrestricted administrative authority.",
    },
]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_seed_roles__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_seed_roles__mutmut)
def seed_roles() -> None:
    db = SessionLocal()

    try:
        for role_data in ROLES:
            existing_role = db.scalar(
                select(Role).where(Role.name == role_data["name"])
            )

            if existing_role is None:
                db.add(Role(**role_data))

        db.commit()

        print("Roles seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def x_seed_roles__mutmut_orig() -> None:
    db = SessionLocal()

    try:
        for role_data in ROLES:
            existing_role = db.scalar(
                select(Role).where(Role.name == role_data["name"])
            )

            if existing_role is None:
                db.add(Role(**role_data))

        db.commit()

        print("Roles seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def x_seed_roles__mutmut_1() -> None:
    db = None

    try:
        for role_data in ROLES:
            existing_role = db.scalar(
                select(Role).where(Role.name == role_data["name"])
            )

            if existing_role is None:
                db.add(Role(**role_data))

        db.commit()

        print("Roles seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def x_seed_roles__mutmut_2() -> None:
    db = SessionLocal()

    try:
        for role_data in ROLES:
            existing_role = None

            if existing_role is None:
                db.add(Role(**role_data))

        db.commit()

        print("Roles seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def x_seed_roles__mutmut_3() -> None:
    db = SessionLocal()

    try:
        for role_data in ROLES:
            existing_role = db.scalar(
                None
            )

            if existing_role is None:
                db.add(Role(**role_data))

        db.commit()

        print("Roles seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def x_seed_roles__mutmut_4() -> None:
    db = SessionLocal()

    try:
        for role_data in ROLES:
            existing_role = db.scalar(
                select(Role).where(None)
            )

            if existing_role is None:
                db.add(Role(**role_data))

        db.commit()

        print("Roles seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def x_seed_roles__mutmut_5() -> None:
    db = SessionLocal()

    try:
        for role_data in ROLES:
            existing_role = db.scalar(
                select(None).where(Role.name == role_data["name"])
            )

            if existing_role is None:
                db.add(Role(**role_data))

        db.commit()

        print("Roles seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def x_seed_roles__mutmut_6() -> None:
    db = SessionLocal()

    try:
        for role_data in ROLES:
            existing_role = db.scalar(
                select(Role).where(Role.name != role_data["name"])
            )

            if existing_role is None:
                db.add(Role(**role_data))

        db.commit()

        print("Roles seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def x_seed_roles__mutmut_7() -> None:
    db = SessionLocal()

    try:
        for role_data in ROLES:
            existing_role = db.scalar(
                select(Role).where(Role.name == role_data["XXnameXX"])
            )

            if existing_role is None:
                db.add(Role(**role_data))

        db.commit()

        print("Roles seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def x_seed_roles__mutmut_8() -> None:
    db = SessionLocal()

    try:
        for role_data in ROLES:
            existing_role = db.scalar(
                select(Role).where(Role.name == role_data["NAME"])
            )

            if existing_role is None:
                db.add(Role(**role_data))

        db.commit()

        print("Roles seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def x_seed_roles__mutmut_9() -> None:
    db = SessionLocal()

    try:
        for role_data in ROLES:
            existing_role = db.scalar(
                select(Role).where(Role.name == role_data["name"])
            )

            if existing_role is not None:
                db.add(Role(**role_data))

        db.commit()

        print("Roles seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def x_seed_roles__mutmut_10() -> None:
    db = SessionLocal()

    try:
        for role_data in ROLES:
            existing_role = db.scalar(
                select(Role).where(Role.name == role_data["name"])
            )

            if existing_role is None:
                db.add(None)

        db.commit()

        print("Roles seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def x_seed_roles__mutmut_11() -> None:
    db = SessionLocal()

    try:
        for role_data in ROLES:
            existing_role = db.scalar(
                select(Role).where(Role.name == role_data["name"])
            )

            if existing_role is None:
                db.add(Role(**role_data))

        db.commit()

        print(None)

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def x_seed_roles__mutmut_12() -> None:
    db = SessionLocal()

    try:
        for role_data in ROLES:
            existing_role = db.scalar(
                select(Role).where(Role.name == role_data["name"])
            )

            if existing_role is None:
                db.add(Role(**role_data))

        db.commit()

        print("XXRoles seeded successfully.XX")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def x_seed_roles__mutmut_13() -> None:
    db = SessionLocal()

    try:
        for role_data in ROLES:
            existing_role = db.scalar(
                select(Role).where(Role.name == role_data["name"])
            )

            if existing_role is None:
                db.add(Role(**role_data))

        db.commit()

        print("roles seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def x_seed_roles__mutmut_14() -> None:
    db = SessionLocal()

    try:
        for role_data in ROLES:
            existing_role = db.scalar(
                select(Role).where(Role.name == role_data["name"])
            )

            if existing_role is None:
                db.add(Role(**role_data))

        db.commit()

        print("ROLES SEEDED SUCCESSFULLY.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()

mutants_x_seed_roles__mutmut['_mutmut_orig'] = x_seed_roles__mutmut_orig # type: ignore # mutmut generated
mutants_x_seed_roles__mutmut['x_seed_roles__mutmut_1'] = x_seed_roles__mutmut_1 # type: ignore # mutmut generated
mutants_x_seed_roles__mutmut['x_seed_roles__mutmut_2'] = x_seed_roles__mutmut_2 # type: ignore # mutmut generated
mutants_x_seed_roles__mutmut['x_seed_roles__mutmut_3'] = x_seed_roles__mutmut_3 # type: ignore # mutmut generated
mutants_x_seed_roles__mutmut['x_seed_roles__mutmut_4'] = x_seed_roles__mutmut_4 # type: ignore # mutmut generated
mutants_x_seed_roles__mutmut['x_seed_roles__mutmut_5'] = x_seed_roles__mutmut_5 # type: ignore # mutmut generated
mutants_x_seed_roles__mutmut['x_seed_roles__mutmut_6'] = x_seed_roles__mutmut_6 # type: ignore # mutmut generated
mutants_x_seed_roles__mutmut['x_seed_roles__mutmut_7'] = x_seed_roles__mutmut_7 # type: ignore # mutmut generated
mutants_x_seed_roles__mutmut['x_seed_roles__mutmut_8'] = x_seed_roles__mutmut_8 # type: ignore # mutmut generated
mutants_x_seed_roles__mutmut['x_seed_roles__mutmut_9'] = x_seed_roles__mutmut_9 # type: ignore # mutmut generated
mutants_x_seed_roles__mutmut['x_seed_roles__mutmut_10'] = x_seed_roles__mutmut_10 # type: ignore # mutmut generated
mutants_x_seed_roles__mutmut['x_seed_roles__mutmut_11'] = x_seed_roles__mutmut_11 # type: ignore # mutmut generated
mutants_x_seed_roles__mutmut['x_seed_roles__mutmut_12'] = x_seed_roles__mutmut_12 # type: ignore # mutmut generated
mutants_x_seed_roles__mutmut['x_seed_roles__mutmut_13'] = x_seed_roles__mutmut_13 # type: ignore # mutmut generated
mutants_x_seed_roles__mutmut['x_seed_roles__mutmut_14'] = x_seed_roles__mutmut_14 # type: ignore # mutmut generated


if __name__ == "__main__":
    seed_roles()