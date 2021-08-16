"""empty message

Revision ID: 28b03f9eb27b
Revises: fa468ab539fe
Create Date: 2020-10-25 17:18:04.058933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28b03f9eb27b'
down_revision = 'fa468ab539fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about', sa.String(length=300), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'about')
    # ### end Alembic commands ###
