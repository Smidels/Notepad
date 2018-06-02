"""notes table

Revision ID: 170fb9994345
Revises: 
Create Date: 2018-05-31 11:56:07.325354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '170fb9994345'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('counter_unique_words', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('note')
    # ### end Alembic commands ###
