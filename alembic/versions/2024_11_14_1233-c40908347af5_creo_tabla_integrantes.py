"""Creo tabla integrantes

Revision ID: c40908347af5
Revises: 8a514caf11c2
Create Date: 2024-11-14 12:33:19.346365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c40908347af5'
down_revision: Union[str, None] = '8a514caf11c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        "integrante",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nombre", sa.Text, nullable=False),
        sa.Column("id_equipo", sa.Integer, nullable=False),
        sa.Column("id_movimientos", sa.Integer),
    )


def downgrade() -> None:
    op.drop_table("integrante")
