"""Crear relacion 1 a n entre naturalezas e integrantes

Revision ID: f7b1ab3c95d3
Revises: 76f1292aebf2
Create Date: 2024-11-04 16:27:05.328358

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f7b1ab3c95d3"
down_revision: Union[str, None] = "76f1292aebf2"
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
