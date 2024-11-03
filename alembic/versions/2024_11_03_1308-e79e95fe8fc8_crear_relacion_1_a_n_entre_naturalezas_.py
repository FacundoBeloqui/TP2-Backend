"""Crear relacion 1 a n entre naturalezas e integrantes

Revision ID: e79e95fe8fc8
Revises: b9e4c5d5677e
Create Date: 2024-11-03 13:08:11.923483

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e79e95fe8fc8"
down_revision: Union[str, None] = "b9e4c5d5677e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("integrante") as batch_op:
        batch_op.add_column(sa.Column("id_naturaleza", sa.Integer))
        batch_op.create_foreign_key(
            "fk_integrante_naturaleza", "naturaleza", ["id_naturaleza"], ["id"]
        )


def downgrade() -> None:
    with op.batch_alter_table("integrante") as batch_op:
        batch_op.drop_constraint("fk_integrante_naturaleza", type_="foreignkey")
        batch_op.drop_column("id_naturaleza")
