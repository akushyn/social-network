"""add follows table

Revision ID: f9d4d3a5f480
Revises: 7e4399c2833f
Create Date: 2023-04-06 00:30:54.391729

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f9d4d3a5f480'
down_revision = '7e4399c2833f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follows',
                    sa.Column('follower_id', sa.Integer(), nullable=False),
                    sa.Column('followee_id', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['followee_id'], ['user.id'], name='fk_follows_followee_id'),
                    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], name='fk_follows_follower_id'),
                    sa.PrimaryKeyConstraint('follower_id', 'followee_id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('follows')
    # ### end Alembic commands ###
