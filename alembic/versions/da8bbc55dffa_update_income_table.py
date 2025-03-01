"""Update income table

Revision ID: da8bbc55dffa
Revises: 59c5014d91ba
Create Date: 2025-02-06 12:03:29.008435

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da8bbc55dffa'
down_revision: Union[str, None] = '59c5014d91ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('income', sa.Column('amount', sa.Float(), nullable=False))
    op.drop_column('income', 'income')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('income', sa.Column('income', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.drop_column('income', 'amount')
    # ### end Alembic commands ###
