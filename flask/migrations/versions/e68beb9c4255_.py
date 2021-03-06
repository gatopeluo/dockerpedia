"""empty message

Revision ID: e68beb9c4255
Revises: 2306f0ee0b23
Create Date: 2018-04-16 21:13:36.972060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e68beb9c4255'
down_revision = '2306f0ee0b23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('featureversion_feature_id_tag_key', 'tag_featureversion', ['tag_id', 'featureversion_id'], unique=False)
    op.create_unique_constraint(None, 'tag_featureversion', ['tag_id', 'featureversion_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tag_featureversion', type_='unique')
    op.drop_index('featureversion_feature_id_tag_key', table_name='tag_featureversion')
    # ### end Alembic commands ###
