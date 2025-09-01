"""Add default value to updated_at column

Revision ID: 1ac1f231ae25
Revises: 6c79b481dd96
Create Date: 2025-08-28 11:26:57.148558

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ac1f231ae25'
down_revision: Union[str, None] = '6c79b481dd96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass

def downgrade() -> None:
    pass
