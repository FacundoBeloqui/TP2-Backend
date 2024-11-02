"""Creo tabla integrante_movimiento

Revision ID: 3228fb0ce46e
Revises: ee05e0b44995
Create Date: 2024-11-02 12:34:47.339156

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3228fb0ce46e"
down_revision: Union[str, None] = "ee05e0b44995"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "integrante_movimiento",
        sa.Column("integrante_nombre", sa.Integer, primary_key=True),
        sa.Column("movimiento_id", sa.Integer, primary_key=True),
        sa.ForeignKeyConstraint(
            ["integrante_nombre"],
            ["integrante.nombre"],
        ),
        sa.ForeignKeyConstraint(
            ["movimiento_id"],
            ["movimiento.id"],
        ),
    )


def downgrade() -> None:
    op.drop_table("integrante_movimiento")
