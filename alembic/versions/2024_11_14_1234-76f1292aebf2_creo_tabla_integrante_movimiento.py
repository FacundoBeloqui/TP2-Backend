"""Creo tabla integrante_movimiento

Revision ID: 76f1292aebf2
Revises: c40908347af5
Create Date: 2024-11-14 12:34:19.336523

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76f1292aebf2'
down_revision: Union[str, None] = 'c40908347af5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "integrante_movimiento",
        sa.Column("integrante_id", sa.Integer, primary_key=True),
        sa.Column("movimiento_id", sa.Integer, primary_key=True),
        sa.ForeignKeyConstraint(
            ["integrante_id"],
            ["integrante.id"],
        ),
        sa.ForeignKeyConstraint(
            ["movimiento_id"],
            ["movimiento.id"],
        ),
    )


def downgrade() -> None:
    op.drop_table("integrante_movimiento")

