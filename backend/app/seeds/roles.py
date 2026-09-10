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


if __name__ == "__main__":
    seed_roles()