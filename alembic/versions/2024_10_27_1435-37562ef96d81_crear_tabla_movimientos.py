"""crear tabla movimientos

Revision ID: 37562ef96d81
Revises: 8809acf2faed
Create Date: 2024-10-27 14:35:15.008476

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "37562ef96d81"
down_revision: Union[str, None] = "8809acf2faed"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'movimiento',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nombre', sa.String, nullable=False),
        sa.Column('generacion', sa.Integer),
        sa.Column('tipo', sa.String, nullable=False),
        sa.Column('poder', sa.String),
        sa.Column('accuracy', sa.String),
        sa.Column('pp', sa.String),
        sa.Column('categoria', sa.String),
        sa.Column('efecto', sa.Text),
        sa.Column('pokemones_subida_nivel', sa.BLOB(sa.String)),
        sa.Column('pokemones_tm', sa.BLOB(sa.String)),
        sa.Column('pokemones_grupo_huevo', sa.BLOB(sa.String)),
    )


def downgrade() -> None:
    op.drop_table("movimiento")
