"""Crear tabla tipos

Revision ID: 459bfcb5a180
Revises: 6c4d4b91eb55
Create Date: 2024-11-01 21:52:34.626127

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '459bfcb5a180'
down_revision: Union[str, None] = '6c4d4b91eb55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tipo',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nombre', sa.String, nullable=False)
    )

def downgrade() -> None:
    op.drop_table('tipo')
