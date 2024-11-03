"""Crear tabla equipos

Revision ID: bff31a12b5ab
Revises: 8809acf2faed
Create Date: 2024-10-26 19:13:21.655082

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bff31a12b5ab'
down_revision: Union[str, None] = '8809acf2faed'
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


# def upgrade() -> None:
#     op.drop_column("equipo", "pokemon")


# def downgrade() -> None:
#     op.add_column("equipo", sa.Column("pokemon", sa.Integer, nullable=False))
