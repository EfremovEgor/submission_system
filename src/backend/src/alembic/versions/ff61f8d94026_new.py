"""new

Revision ID: ff61f8d94026
Revises: 9e2c0d492bc1
Create Date: 2024-03-12 10:40:40.966253

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff61f8d94026'
down_revision: Union[str, None] = '9e2c0d492bc1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('authors', sa.Column('first_name_ru', sa.String(length=255), nullable=True))
    op.add_column('authors', sa.Column('last_name_ru', sa.String(length=255), nullable=True))
    op.add_column('authors', sa.Column('surname_ru', sa.String(length=255), nullable=True))
    op.add_column('authors', sa.Column('affilation_ru', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('authors', 'affilation_ru')
    op.drop_column('authors', 'surname_ru')
    op.drop_column('authors', 'last_name_ru')
    op.drop_column('authors', 'first_name_ru')
    # ### end Alembic commands ###
