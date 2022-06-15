"""add is_new col to products

Revision ID: 7676df28b655
Revises: 7170ad388ef3
Create Date: 2022-06-09 13:56:50.192849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7676df28b655"
down_revision = "7170ad388ef3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("product", sa.Column("is_new", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("product", "is_new")
    # ### end Alembic commands ###
