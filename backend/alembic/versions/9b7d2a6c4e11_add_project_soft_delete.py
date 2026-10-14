"""PropertyGuard Alembic Migration: Add Project Soft Delete
Adds deleted_at timestamp column and index to the projects table for soft deletion.

Revision ID: 9b7d2a6c4e11
Revises: 72cc7b4c2798
Create Date: 2026-10-08 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "9b7d2a6c4e11"
down_revision: Union[str, Sequence[str], None] = "72cc7b4c2798"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "projects",
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index(
        op.f("ix_projects_deleted_at"),
        "projects",
        ["deleted_at"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_projects_deleted_at"), table_name="projects")
    op.drop_column("projects", "deleted_at")
