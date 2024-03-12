"""new

Revision ID: 9e2c0d492bc1
Revises: b71151347d71
Create Date: 2024-03-12 10:15:54.233994

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e2c0d492bc1'
down_revision: Union[str, None] = 'b71151347d71'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('authors', sa.Column('title', sa.String(length=255), nullable=True))
    op.add_column('conferences', sa.Column('name_ru', sa.Text(), nullable=True))
    op.create_unique_constraint(None, 'conferences', ['name_ru'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'conferences', type_='unique')
    op.drop_column('conferences', 'name_ru')
    op.drop_column('authors', 'title')
    # ### end Alembic commands ###