"""new

Revision ID: 332d2fc81918
Revises: 80d493deb8e1
Create Date: 2024-03-18 14:27:59.942889

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '332d2fc81918'
down_revision: Union[str, None] = '80d493deb8e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submissions', sa.Column('review_result', sa.Text(), nullable=True))
    op.drop_column('submissions', 'approved')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submissions', sa.Column('approved', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('submissions', 'review_result')
    # ### end Alembic commands ###
