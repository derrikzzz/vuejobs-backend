"""Add missing columns to jobs table

Revision ID: 6c79b481dd96
Revises: 6a3f80f1bc20
Create Date: 2025-08-28 11:25:41.876300

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c79b481dd96'
down_revision: Union[str, None] = '6a3f80f1bc20'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('jobs', sa.Column('remote', sa.Boolean(), nullable=True))
    op.create_index(op.f('ix_jobs_id'), 'jobs', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_jobs_id'), table_name='jobs')
    op.drop_column('jobs', 'remote')

