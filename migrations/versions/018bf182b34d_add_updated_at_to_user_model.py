"""Add updated_at to User model

Revision ID: 018bf182b34d
Revises: 752e5c2fbef5
Create Date: 2025-06-15 18:52:57.063019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '018bf182b34d'
down_revision = '752e5c2fbef5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('updated_at')

    # ### end Alembic commands ###
