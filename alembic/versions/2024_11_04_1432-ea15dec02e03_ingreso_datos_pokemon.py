"""ingreso datos pokemon

Revision ID: ea15dec02e03
Revises: cf17f5e9ae87
Create Date: 2024-11-04 14:32:01.019745

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from modelos import Pokemon
from db import lista_pokemones

# revision identifiers, used by Alembic.
revision: str = "ea15dec02e03"
down_revision: Union[str, None] = "cf17f5e9ae87"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        Pokemon.__table__,
        [n.dict() for n in lista_pokemones],
    )


def downgrade() -> None:
    pokemon_table = sa.table(
        "pokemon",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("identificador", sa.String, nullable=False),
        sa.Column("id_especie", sa.Integer, nullable=False),
        sa.Column("altura", sa.Integer, nullable=False),
        sa.Column("peso", sa.Integer, nullable=False),
        sa.Column("experiencia_base", sa.Integer, nullable=False),
        sa.Column("imagen", sa.String, nullable=False),
        sa.Column("tipo", sa.BLOB(sa.String), nullable=False),
        sa.Column("grupo_de_huevo", sa.String, nullable=False),
        sa.Column("estadisticas", sa.JSON, nullable=False),
        sa.Column("habilidades", sa.BLOB(sa.String), nullable=True),
        sa.Column("evoluciones_inmediatas", sa.BLOB(sa.String), nullable=True),
    )

    op.execute(
        pokemon_table.delete().where(
            pokemon_table.c.nombre.in_([n.nombre for n in lista_pokemones])
        )
    )
