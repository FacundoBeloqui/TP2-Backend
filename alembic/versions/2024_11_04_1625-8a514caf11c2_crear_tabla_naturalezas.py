"""Crear tabla naturalezas

Revision ID: 8a514caf11c2
Revises: 6ec938b13351
Create Date: 2024-11-04 16:25:56.278398

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8a514caf11c2"
down_revision: Union[str, None] = "6ec938b13351"
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
