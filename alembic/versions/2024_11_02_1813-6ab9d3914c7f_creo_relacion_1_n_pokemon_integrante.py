"""Creo relacion 1:N pokemon-integrante

Revision ID: 6ab9d3914c7f
Revises: 380c98cbfce1
Create Date: 2024-11-02 18:13:01.899149

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6ab9d3914c7f"
down_revision: Union[str, None] = "380c98cbfce1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("integrante") as batch_op:
        batch_op.add_column(sa.Column("id_pokemon", sa.Integer))
        batch_op.create_foreign_key(
            "fk_integrante_pokemon", "pokemon", ["id_pokemon"], ["id"]
        )


def downgrade() -> None:
    with op.batch_alter_table("integrante") as batch_op:
        batch_op.drop_constraint("fk_integrante_pokemon", type_="foreignkey")
        batch_op.drop_column("id_pokemon")
