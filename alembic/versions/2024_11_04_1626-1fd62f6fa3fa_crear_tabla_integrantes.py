"""Crear tabla integrantes

Revision ID: 1fd62f6fa3fa
Revises: 8a514caf11c2
Create Date: 2024-11-04 16:26:26.552202

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1fd62f6fa3fa"
down_revision: Union[str, None] = "8a514caf11c2"
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
