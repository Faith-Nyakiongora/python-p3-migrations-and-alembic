"""Added Student model

Revision ID: 94a2e5c4355d
Revises: b889788215c6
Create Date: 2023-10-01 03:53:15.067047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94a2e5c4355d'
down_revision = 'b889788215c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=55), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('enrolled_date', sa.DateTime(), nullable=True),
    sa.CheckConstraint('grade BETWEEN 1 AND 12', name='grade_between_1_and_12'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email', name='unique_email')
    )
    op.create_index(op.f('ix_students_name'), 'students', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_students_name'), table_name='students')
    op.drop_table('students')
    # ### end Alembic commands ###
