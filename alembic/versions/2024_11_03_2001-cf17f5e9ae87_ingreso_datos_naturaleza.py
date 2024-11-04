"""ingreso datos naturaleza

Revision ID: cf17f5e9ae87
Revises: f101da84471f
Create Date: 2024-11-03 20:01:07.678459

"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from modelos import Naturaleza
from db import lista_naturalezas

# revision identifiers, used by Alembic.
revision: str = "cf17f5e9ae87"
down_revision: Union[str, None] = "f101da84471f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        Naturaleza.__table__,
        [n.dict() for n in lista_naturalezas],
    )


def downgrade() -> None:
    naturaleza_table = sa.table(
        "naturaleza",
        sa.column("nombre", sa.String),
        sa.column("stat_decreciente", sa.String),
        sa.column("stat_creciente", sa.String),
        sa.column("id_gusto_preferido", sa.Integer),
        sa.column("id_gusto_menos_preferido", sa.Integer),
        sa.column("indice_juego", sa.Integer),
    )

    op.execute(
        naturaleza_table.delete().where(
            naturaleza_table.c.nombre.in_([n.nombre for n in lista_naturalezas])
        )
    )
