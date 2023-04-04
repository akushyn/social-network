"""add about_me, last_seen

Revision ID: 101f7547c548
Revises: 918ab80239fb
Create Date: 2023-04-04 03:04:07.157165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '101f7547c548'
down_revision = '918ab80239fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
