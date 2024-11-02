"""Crear relacion 1 N entre pokemon y equipo

Revision ID: 6c4d4b91eb55
Revises: 8462fc51a152
Create Date: 2024-10-29 19:40:02.299690

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6c4d4b91eb55"
down_revision: Union[str, None] = "37562ef96d81"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("equipo") as batch_op:
        batch_op.add_column(sa.Column("pokemon_id", sa.Integer))
        batch_op.create_foreign_key(
            "fk_equipo_pokemon", "pokemon", ["pokemon_id"], ["id"]
        )


def downgrade() -> None:
    with op.batch_alter_table("equipo") as batch_op:
        batch_op.drop_constraint("fk_equipo_pokemon", type_="foreignkey")
        batch_op.drop_column("pokemon_id")
