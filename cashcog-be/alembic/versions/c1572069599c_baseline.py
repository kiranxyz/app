"""baseline

Revision ID: c1572069599c
Revises: 
Create Date: 2020-03-02 18:07:10.536529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1572069599c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('create extension if not exists "uuid-ossp";')


def downgrade():
    pass
