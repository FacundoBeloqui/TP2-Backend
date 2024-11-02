"""crear tabla habilidad

Revision ID: e17c2bcb269e
Revises: 753cee356db5, bff31a12b5ab
Create Date: 2024-11-01 21:55:18.995914

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e17c2bcb269e"
down_revision: Union[str, None] = ("753cee356db5", "bff31a12b5ab")
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'habilidad',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nombre', sa.String, nullable=False)
        sa.Column('pokemon_id', sa.Integer, sa.ForeignKey('pokemon.id'), nullable=False)
    )

def downgrade() -> None:
    op.drop_table('habilidad')
