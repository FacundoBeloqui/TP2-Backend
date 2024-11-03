"""Crear relacion 1 a n entre pokemones e integrantes

Revision ID: f101da84471f
Revises: e79e95fe8fc8
Create Date: 2024-11-03 13:08:51.184447

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f101da84471f"
down_revision: Union[str, None] = "e79e95fe8fc8"
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
