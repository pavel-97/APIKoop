"""create inventory

Revision ID: e281b7d5002b
Revises: 52fa47c2de56
Create Date: 2025-05-08 17:13:48.097310

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e281b7d5002b'
down_revision: Union[str, None] = '52fa47c2de56'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventory',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('part_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('current_quantity', sa.Integer(), nullable=False),
    sa.Column('min_quantity', sa.Integer(), nullable=False),
    sa.Column('optimal_quantity', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('pending_in', sa.Integer(), nullable=False),
    sa.Column('reserved', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('pk')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inventory')
    # ### end Alembic commands ###
