"""empty message

Revision ID: 50610c16be65
Revises: 94f13dc6f885
Create Date: 2020-08-26 08:33:12.082268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50610c16be65'
down_revision = '94f13dc6f885'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('avatar', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'avatar')
    # ### end Alembic commands ###
