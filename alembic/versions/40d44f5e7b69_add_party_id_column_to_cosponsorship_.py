"""add party_id column to cosponsorship table

Revision ID: 40d44f5e7b69
Revises: 225b82afbf55
Create Date: 2014-07-16 19:37:44.977381

"""

# revision identifiers, used by Alembic.
revision = '40d44f5e7b69'
down_revision = '225b82afbf55'

from alembic import op
import sqlalchemy as sa

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cosponsorship', sa.Column('party_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_cosponsorship_party_id'), 'cosponsorship', ['party_id'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_cosponsorship_party_id'), table_name='cosponsorship')
    op.drop_column('cosponsorship', 'party_id')
