"""Crear tabla evoluciones inmediatas

Revision ID: bd83c5f7bcf1
Revises: d27e896a01a4
Create Date: 2024-11-03 13:06:20.501925

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bd83c5f7bcf1"
down_revision: Union[str, None] = "d27e896a01a4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "evolucion",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nombre", sa.String, nullable=False),
        sa.Column(
            "pokemon_id", sa.Integer, sa.ForeignKey("pokemon.id"), nullable=False
        ),
    )


def downgrade() -> None:
    op.drop_table("evolucion")
