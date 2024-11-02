"""Mergeo heads

Revision ID: ee05e0b44995
Revises: 37562ef96d81, a38d114d6cc5
Create Date: 2024-11-02 11:20:05.289351

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ee05e0b44995"
down_revision: Union[str, None] = ("37562ef96d81", "a38d114d6cc5")
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
