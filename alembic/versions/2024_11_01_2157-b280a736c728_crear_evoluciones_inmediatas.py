"""Crear tabla evoluciones inmediatas

Revision ID: b280a736c728
Revises: 459bfcb5a180
Create Date: 2024-11-01 21:57:57.379351

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b280a736c728"
down_revision: Union[str, None] = "459bfcb5a180"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
