"""Crear tabla equipos

Revision ID: fc8ee7664c8d
Revises: dfa545eded31
Create Date: 2024-11-03 13:01:52.472232

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fc8ee7664c8d"
down_revision: Union[str, None] = "dfa545eded31"
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
