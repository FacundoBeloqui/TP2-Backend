"""Crear relacion 1 a n entre pokemones e intregrantes

Revision ID: 6b399131ada0
Revises: f7b1ab3c95d3
Create Date: 2024-11-04 16:27:16.610315

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6b399131ada0"
down_revision: Union[str, None] = "f7b1ab3c95d3"
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
