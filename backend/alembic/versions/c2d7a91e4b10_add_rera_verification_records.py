"""add auditable online RERA verification records

Revision ID: c2d7a91e4b10
Revises: 9b7d2a6c4e11
Create Date: 2026-10-10
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "c2d7a91e4b10"
down_revision: Union[str, Sequence[str], None] = "9b7d2a6c4e11"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        "rera_verifications",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("project_id", sa.Uuid(), nullable=False),
        sa.Column("registration_number", sa.String(length=150), nullable=False),
        sa.Column("source_url", sa.Text(), nullable=False),
        sa.Column("status", sa.String(length=40), nullable=False),
        sa.Column("source_title", sa.String(length=255), nullable=True),
        sa.Column("matched_project_name", sa.String(length=255), nullable=True),
        sa.Column("matched_promoter_name", sa.String(length=255), nullable=True),
        sa.Column("evidence", sa.JSON(), nullable=True),
        sa.Column("message", sa.Text(), nullable=False),
        sa.Column("verified_by_user_id", sa.Uuid(), nullable=False),
        sa.Column("checked_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["project_id"], ["projects.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["verified_by_user_id"], ["users.id"], ondelete="RESTRICT"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_rera_verifications_project_id", "rera_verifications", ["project_id"])
    op.create_index("ix_rera_verifications_registration_number", "rera_verifications", ["registration_number"])
    op.create_index("ix_rera_verifications_status", "rera_verifications", ["status"])

def downgrade() -> None:
    op.drop_index("ix_rera_verifications_status", table_name="rera_verifications")
    op.drop_index("ix_rera_verifications_registration_number", table_name="rera_verifications")
    op.drop_index("ix_rera_verifications_project_id", table_name="rera_verifications")
    op.drop_table("rera_verifications")
