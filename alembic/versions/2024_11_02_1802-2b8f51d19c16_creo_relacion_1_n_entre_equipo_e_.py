"""Creo relacion 1 N entre equipo e integrante

Revision ID: 2b8f51d19c16
Revises: 0665c92e41be
Create Date: 2024-11-02 18:02:09.653366

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b8f51d19c16'
down_revision: Union[str, None] = '0665c92e41be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("equipo") as batch_op:
        batch_op.add_column(sa.Column("integrante_id", sa.Integer))
        batch_op.create_foreign_key("fk_equipo_integrante", "integrante", ["integrante_id"], ["id"])


def downgrade() -> None:
    with op.batch_alter_table("equipo") as batch_op:
        batch_op.drop_constraint("fk_equipo_integrante", type_="foreignkey")
        batch_op.drop_column("integrante_id")
