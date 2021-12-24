"""initial migration

Revision ID: 94a7e636ac1f
Revises: 
Create Date: 2021-12-24 17:42:12.757292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94a7e636ac1f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('addr', sa.String(length=200), nullable=True),
    sa.Column('pin', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('student_id')
    )
    op.create_table('subjects',
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('subject_id')
    )
    op.create_table('registers',
    sa.Column('register_id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.Integer(), nullable=False),
    sa.Column('student', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['student'], ['students.student_id'], ),
    sa.ForeignKeyConstraint(['subject'], ['subjects.subject_id'], ),
    sa.PrimaryKeyConstraint('register_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('registers')
    op.drop_table('subjects')
    op.drop_table('students')
    # ### end Alembic commands ###