"""Crear tabla integrantes_movimientos

Revision ID: c38c663938c5
Revises: 1fd62f6fa3fa
Create Date: 2024-11-04 16:26:40.378898

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c38c663938c5"
down_revision: Union[str, None] = "1fd62f6fa3fa"
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
