"""Crear tabla Naturalezas

Revision ID: 8809acf2faed
Revises: a38d114d6cc5
Create Date: 2024-10-26 11:55:53.574029

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8809acf2faed"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "naturaleza",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nombre", sa.String, nullable=False),
        sa.Column("stat_decreciente", sa.String),
        sa.Column("stat_creciente", sa.String),
        sa.Column("id_gusto_preferido", sa.Integer),
        sa.Column("id_gusto_menos_preferido", sa.Integer),
        sa.Column("indice_juego", sa.Integer),
    )


def downgrade() -> None:
    op.drop_table("naturaleza")
