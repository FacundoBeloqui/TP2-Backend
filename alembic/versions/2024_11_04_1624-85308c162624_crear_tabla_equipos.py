"""Crear tabla equipos

Revision ID: 85308c162624
Revises: f0ad080f88fd
Create Date: 2024-11-04 16:24:34.917416

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "85308c162624"
down_revision: Union[str, None] = "f0ad080f88fd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "equipo",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nombre", sa.Text, nullable=False),
        sa.Column("generación", sa.Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("equipo")
