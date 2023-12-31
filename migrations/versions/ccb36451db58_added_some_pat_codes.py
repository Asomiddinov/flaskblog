"""Added some pat_codes

Revision ID: ccb36451db58
Revises: 
Create Date: 2023-07-30 18:57:04.551603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccb36451db58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('patient', sa.String(), nullable=False),
    sa.Column('pat_code', sa.String(), nullable=False),
    sa.Column('pat_code1', sa.String(), nullable=False),
    sa.Column('pat_code2', sa.String(), nullable=False),
    sa.Column('pat_code3', sa.String(), nullable=False),
    sa.Column('pat_code4', sa.String(), nullable=False),
    sa.Column('pat_code5', sa.String(), nullable=False),
    sa.Column('pat_code6', sa.String(), nullable=False),
    sa.Column('pat_code7', sa.String(), nullable=False),
    sa.Column('pat_code8', sa.String(), nullable=False),
    sa.Column('pat_code9', sa.String(), nullable=False),
    sa.Column('pat_code10', sa.String(), nullable=False),
    sa.Column('pat_code11', sa.String(), nullable=False),
    sa.Column('pat_code12', sa.String(), nullable=False),
    sa.Column('pat_code13', sa.String(), nullable=False),
    sa.Column('pat_code14', sa.String(), nullable=False),
    sa.Column('pat_code15', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('posts')
    op.drop_table('clients')
    # ### end Alembic commands ###
