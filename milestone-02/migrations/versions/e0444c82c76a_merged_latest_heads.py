"""Merged latest heads

Revision ID: e0444c82c76a
Revises: 687592955894, a39a02475e4a, ce1567562de8, d0ff8dcdef1b, d82742c929ea
Create Date: 2024-09-25 21:31:42.425452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0444c82c76a'
down_revision = ('687592955894', 'a39a02475e4a', 'ce1567562de8', 'd0ff8dcdef1b', 'd82742c929ea')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
