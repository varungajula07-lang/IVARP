"""empty initial migration

Revision ID: 0001_initial
Revises: 
Create Date: 2026-08-05
"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # This initial migration intentionally does not alter the database.
    # The DB was created via SQLAlchemy `create_all` and will be stamped
    # as this revision to begin Alembic versioning.
    pass


def downgrade():
    pass
