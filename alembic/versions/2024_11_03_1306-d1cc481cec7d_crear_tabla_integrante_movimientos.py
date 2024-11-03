"""Crear tabla integrante_movimientos

Revision ID: d1cc481cec7d
Revises: bd83c5f7bcf1
Create Date: 2024-11-03 13:06:55.255702

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d1cc481cec7d"
down_revision: Union[str, None] = "bd83c5f7bcf1"
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
