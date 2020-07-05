"""added flask login feature

Revision ID: 4c06853740fa
Revises: d7e8b602710d
Create Date: 2020-05-17 15:45:08.387966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c06853740fa'
down_revision = 'd7e8b602710d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.String(length=300), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###