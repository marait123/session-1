"""empty message

Revision ID: eed60b8f0dca
Revises: b901762c2ba3
Create Date: 2023-05-26 19:55:38.953934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eed60b8f0dca'
down_revision = 'b901762c2ba3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(length=100), nullable=True))

    with op.batch_alter_table('subjects', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('subjects', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.VARCHAR(length=100), autoincrement=False, nullable=True))

    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###