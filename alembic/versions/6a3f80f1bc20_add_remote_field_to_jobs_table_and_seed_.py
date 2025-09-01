"""Add remote field to jobs table and seed initial data

Revision ID: 6a3f80f1bc20
Revises: 
Create Date: 2025-08-27 17:19:34.375673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a3f80f1bc20'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create jobs table with all fields including remote
    op.create_table('jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('company', sa.String(length=100), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('salary', sa.String(length=50), nullable=True),
    sa.Column('job_type', sa.String(length=50), nullable=True),
    sa.Column('requirements', sa.Text(), nullable=True),
    sa.Column('remote', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_jobs_id'), 'jobs', ['id'], unique=False)

    # Insert sample jobs data
    jobs_table = sa.table('jobs',
        sa.column('title', sa.String),
        sa.column('company', sa.String),
        sa.column('description', sa.Text),
        sa.column('location', sa.String),
        sa.column('salary', sa.String),
        sa.column('job_type', sa.String),
        sa.column('remote', sa.Boolean),
        sa.column('is_active', sa.Boolean),
        sa.column('created_at', sa.DateTime),
        sa.column('updated_at', sa.DateTime)
    )
    
    op.bulk_insert(jobs_table, [
        {
            'title': 'Frontend Developer',
            'company': 'Tech Corp',
            'description': 'Build amazing user interfaces with Vue.js',
            'location': 'San Francisco, CA',
            'salary': '$80,000 - $120,000',
            'job_type': 'Full-time',
            'remote': True,
            'is_active': True
        },
        {
            'title': 'Backend Engineer',
            'company': 'StartupXYZ',
            'description': 'Build scalable APIs with Python and FastAPI',
            'location': 'New York, NY',
            'salary': '$90,000 - $140,000',
            'job_type': 'Full-time',
            'remote': False,
            'is_active': True
        },
        {
            'title': 'Data Analyst',
            'company': 'DataCorp',
            'description': 'Analyze data to help businesses make decisions',
            'location': 'Chicago, IL',
            'salary': '$70,000 - $110,000',
            'job_type': 'Full-time',
            'remote': True,
            'is_active': True
        },
        {
            'title': 'Software Engineer',
            'company': 'TechCorp',
            'description': 'Build scalable software solutions with Python and Django',
            'location': 'San Francisco, CA',
            'salary': '$100,000 - $150,000',
            'job_type': 'Full-time',
            'remote': True,
            'is_active': True
        },
        {
            'title': 'Product Manager',
            'company': 'ProductCorp',
            'description': 'Manage product development and ensure successful delivery',
            'location': 'New York, NY',
            'salary': '$120,000 - $180,000',
            'job_type': 'Full-time',
            'remote': False,
            'is_active': True
        },
        {
            'title': 'UX Designer',
            'company': 'DesignCorp',
            'description': 'Create intuitive user experiences with Figma and Adobe XD',
            'location': 'San Francisco, CA',
            'salary': '$80,000 - $120,000',
            'job_type': 'Full-time',
            'remote': True,
            'is_active': True
        }
    ])


def downgrade() -> None:
    op.drop_index(op.f('ix_jobs_id'), table_name='jobs')
    op.drop_table('jobs')
