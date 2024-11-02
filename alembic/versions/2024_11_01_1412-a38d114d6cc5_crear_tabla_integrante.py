"""Crear tabla integrante

Revision ID: a38d114d6cc5
Revises: 753cee356db5
Create Date: 2024-11-01 14:12:11.778345

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a38d114d6cc5"
down_revision: Union[str, None] = "753cee356db5"
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
