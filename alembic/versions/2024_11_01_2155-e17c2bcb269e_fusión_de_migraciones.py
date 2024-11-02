"""crear tabla evoluciones inmediatas

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
    pass


def downgrade() -> None:
    pass
