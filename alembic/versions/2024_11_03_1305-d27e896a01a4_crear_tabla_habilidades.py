"""Crear tabla habilidades

Revision ID: d27e896a01a4
Revises: 2a59a35d2fed
Create Date: 2024-11-03 13:05:55.728653

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d27e896a01a4"
down_revision: Union[str, None] = "2a59a35d2fed"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "habilidad",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nombre", sa.String, nullable=False),
        sa.Column(
            "pokemon_id", sa.Integer, sa.ForeignKey("pokemon.id"), nullable=False
        ),
    )


def downgrade() -> None:
    op.drop_table("habilidad")
