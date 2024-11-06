"""Relacion 1:N entre equipo e integrante

Revision ID: 2d88288887ca
Revises: 6b399131ada0
Create Date: 2024-11-05 12:42:57.889180

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2d88288887ca"
down_revision: Union[str, None] = "6b399131ada0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("integrante") as batch_op:
        batch_op.add_column(sa.Column("equipo_id", sa.Integer, nullable=True))
        batch_op.create_foreign_key(
            "fk_equipo_integrante",
            "equipo",
            ["equipo_id"],
            ["id"],
        )


def downgrade() -> None:
    with op.batch_alter_table("integrante") as batch_op:
        batch_op.drop_constraint("fk_equipo_integrante", type_="foreignkey")
        batch_op.drop_column("equipo_id")
