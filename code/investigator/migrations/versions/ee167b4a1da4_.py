"""empty message

Revision ID: ee167b4a1da4
Revises: 9ba7c56f5bf2
Create Date: 2016-06-16 16:41:45.085226

"""

# revision identifiers, used by Alembic.
revision = 'ee167b4a1da4'
down_revision = '9ba7c56f5bf2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ad_info', sa.Column('post_id', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ad_info', 'post_id')
    ### end Alembic commands ###
