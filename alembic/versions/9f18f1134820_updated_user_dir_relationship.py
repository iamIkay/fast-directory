"""Updated user-dir relationship

Revision ID: 9f18f1134820
Revises: 54d8235084a7
Create Date: 2024-03-24 20:28:10.796874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f18f1134820'
down_revision: Union[str, None] = '54d8235084a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('directories', sa.Column('user_id', sa.Integer(), nullable=False))
    op.drop_constraint('directories_owner_id_fkey', 'directories', type_='foreignkey')
    op.create_foreign_key(None, 'directories', 'users', ['user_id'], ['id'])
    op.drop_column('directories', 'owner_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('directories', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'directories', type_='foreignkey')
    op.create_foreign_key('directories_owner_id_fkey', 'directories', 'users', ['owner_id'], ['id'])
    op.drop_column('directories', 'user_id')
    # ### end Alembic commands ###