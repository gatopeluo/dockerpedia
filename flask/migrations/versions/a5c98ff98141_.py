"""empty message

Revision ID: a5c98ff98141
Revises: ca0995fe7554
Create Date: 2018-04-13 11:38:22.322664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5c98ff98141'
down_revision = 'ca0995fe7554'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tag', sa.Column('vulnerabilitycritical', sa.Integer(), nullable=True))
    op.add_column('tag', sa.Column('vulnerabilitydefcon1', sa.Integer(), nullable=True))
    op.add_column('tag', sa.Column('vulnerabilityhigh', sa.Integer(), nullable=True))
    op.add_column('tag', sa.Column('vulnerabilitylow', sa.Integer(), nullable=True))
    op.add_column('tag', sa.Column('vulnerabilitymedium', sa.Integer(), nullable=True))
    op.add_column('tag', sa.Column('vulnerabilitynegligible', sa.Integer(), nullable=True))
    op.add_column('tag', sa.Column('vulnerabilityunknown', sa.Integer(), nullable=True))
    op.drop_column('tag', 'vulnerabilityCritical')
    op.drop_column('tag', 'vulnerabilityDefcon1')
    op.drop_column('tag', 'vulnerabilityMedium')
    op.drop_column('tag', 'vulnerabilityHigh')
    op.drop_column('tag', 'vulnerabilityUnknown')
    op.drop_column('tag', 'vulnerabilityLow')
    op.drop_column('tag', 'vulnerabilityNegligible')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tag', sa.Column('vulnerabilityNegligible', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tag', sa.Column('vulnerabilityLow', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tag', sa.Column('vulnerabilityUnknown', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tag', sa.Column('vulnerabilityHigh', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tag', sa.Column('vulnerabilityMedium', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tag', sa.Column('vulnerabilityDefcon1', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tag', sa.Column('vulnerabilityCritical', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('tag', 'vulnerabilityunknown')
    op.drop_column('tag', 'vulnerabilitynegligible')
    op.drop_column('tag', 'vulnerabilitymedium')
    op.drop_column('tag', 'vulnerabilitylow')
    op.drop_column('tag', 'vulnerabilityhigh')
    op.drop_column('tag', 'vulnerabilitydefcon1')
    op.drop_column('tag', 'vulnerabilitycritical')
    # ### end Alembic commands ###
