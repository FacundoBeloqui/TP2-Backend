"""Creo tabla equipos

Revision ID: 2d88288887ca
Revises: 6b399131ada0
Create Date: 2024-11-05 12:42:57.889180

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2d88288887ca"
down_revision: Union[str, None] = "6b399131ada0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "equipo",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nombre", sa.Text, nullable=False),
        sa.Column("generacion", sa.Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("equipo")
