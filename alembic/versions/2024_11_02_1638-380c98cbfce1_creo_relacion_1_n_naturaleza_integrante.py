"""creo relacion 1:N naturaleza-integrante

Revision ID: 380c98cbfce1
Revises: 3228fb0ce46e
Create Date: 2024-11-02 16:38:20.848570

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "380c98cbfce1"
down_revision: Union[str, None] = "3228fb0ce46e"
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
