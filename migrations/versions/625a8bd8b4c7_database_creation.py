"""Database creation

Revision ID: 625a8bd8b4c7
Revises: 35bfc3cc34b4
Create Date: 2023-08-06 23:38:48.522429

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '625a8bd8b4c7'
down_revision: Union[str, None] = '35bfc3cc34b4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###