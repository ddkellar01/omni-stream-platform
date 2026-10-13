"""initial schema

Revision ID: 001_initial
Revises: 
Create Date: 2026-05-01 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = '001_initial'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'videos',
        sa.Column('asset_id', sa.String(36), primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('user_id', sa.String(64), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )

def downgrade() -> None:
    op.drop_table('videos')
