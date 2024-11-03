"""Crear tabla integrantes

Revision ID: 32a2d05b7351
Revises: 0c6c0b31ecbf
Create Date: 2024-11-03 13:04:38.057442

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "32a2d05b7351"
down_revision: Union[str, None] = "0c6c0b31ecbf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "integrante",
        sa.Column("nombre", sa.Text, primary_key=True),
        sa.Column("id_equipo", sa.Integer, nullable=False),
        sa.Column("id_movimientos", sa.Integer),
    )


def downgrade() -> None:
    op.drop_table("integrante")
