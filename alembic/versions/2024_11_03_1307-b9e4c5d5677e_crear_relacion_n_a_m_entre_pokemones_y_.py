"""Crear relacion n a m entre pokemones y tipos

Revision ID: b9e4c5d5677e
Revises: d1cc481cec7d
Create Date: 2024-11-03 13:07:31.911382

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b9e4c5d5677e"
down_revision: Union[str, None] = "d1cc481cec7d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # op.create_table(
    #     "pokemon_tipo",
    #     sa.Column(
    #         "pokemon_id", sa.Integer, sa.ForeignKey("pokemon.id"), primary_key=True
    #     ),
    #     sa.Column("tipo_id", sa.Integer, sa.ForeignKey("tipo.id"), primary_key=True),
    # )
    op.create_table(
        "pokemon_tipo",
        sa.Column("pokemon_id", sa.Integer, primary_key=True),
        sa.Column("tipo_id", sa.Integer, primary_key=True),
        sa.ForeignKeyConstraint(["tipo_id"], ["tipo.id"]),
        sa.ForeignKeyConstraint(["pokemon_id"], ["pokemon.id"])
    )
    pass


def downgrade() -> None:
    op.drop_table("pokemon_tipo")
    pass
