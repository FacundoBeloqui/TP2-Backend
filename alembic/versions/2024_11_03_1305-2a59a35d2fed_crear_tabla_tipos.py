"""Crear tabla tipos

Revision ID: 2a59a35d2fed
Revises: 32a2d05b7351
Create Date: 2024-11-03 13:05:23.066173

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2a59a35d2fed"
down_revision: Union[str, None] = "32a2d05b7351"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tipo",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nombre", sa.String, nullable=False),
        sa.Column("pokemon_id", sa.String, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("tipo")
