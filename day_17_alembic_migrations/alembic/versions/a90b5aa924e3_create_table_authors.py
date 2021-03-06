"""create table authors

Revision ID: a90b5aa924e3
Revises: 02d7eed4f8b1
Create Date: 2022-05-22 23:46:03.518001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a90b5aa924e3"
down_revision = "02d7eed4f8b1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "authors",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("name", sa.String(), server_default="", nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("authors")
    # ### end Alembic commands ###
