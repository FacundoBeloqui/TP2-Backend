"""Relacion entre equipo e integrante

Revision ID: fb180cfd34fa
Revises: 2d88288887ca
Create Date: 2024-11-05 12:47:00.782951

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb180cfd34fa'
down_revision: Union[str, None] = '2d88288887ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
