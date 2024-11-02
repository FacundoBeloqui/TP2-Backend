"""Crear relacion N a M entre Pokemon y tipo

Revision ID: 0665c92e41be
Revises: e17c2bcb269e, b280a736c728
Create Date: 2024-11-02 13:50:15.766486

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0665c92e41be"
down_revision: Union[str, None] = ("e17c2bcb269e", "b280a736c728")
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
    # with op.batch_alter_table("pokemon") as batch_op:
    #     batch_op.add_column(sa.Column("tipo_id", sa.Integer))
    #     batch_op.create_foreign_key("fk_pokemon_tipo", "tipo", ["tipo_id"], ["id"])


def downgrade() -> None:
    op.drop_table("pokemon_tipo")
    # with op.batch_alter_table("pokemon") as batch_op:
    #     batch_op.drop_constraint("fk_pokemon_tipo", type_="foreignkey")
    #     batch_op.drop_column("tipo_id")
