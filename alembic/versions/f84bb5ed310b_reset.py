"""reset

Revision ID: f84bb5ed310b
Revises: 
Create Date: 2025-01-30 12:37:25.125965

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f84bb5ed310b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'user_created_at',
               existing_type=postgresql.TIMESTAMP(),
               type_=postgresql.DATE(),
               existing_nullable=False,
               existing_server_default=sa.text('now()'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'user_created_at',
               existing_type=postgresql.DATE(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False,
               existing_server_default=sa.text('now()'))
    # ### end Alembic commands ###
