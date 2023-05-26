"""empty message

Revision ID: 8c95fce775f7
Revises: fa8e7416dfa6
Create Date: 2023-05-26 13:35:00.071093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c95fce775f7'
down_revision = 'fa8e7416dfa6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('registers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('subject', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'subjects', ['subject'], ['subject_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('registers', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('subject')

    # ### end Alembic commands ###