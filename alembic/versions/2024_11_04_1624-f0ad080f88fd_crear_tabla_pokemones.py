"""Crear tabla pokemones

Revision ID: f0ad080f88fd
Revises: 
Create Date: 2024-11-04 16:24:01.663155

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f0ad080f88fd"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
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
        sa.Column("generacion", sa.BLOB(sa.Integer), nullable=False),
        sa.Column("evoluciones_inmediatas", sa.BLOB(sa.String), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("pokemon")
