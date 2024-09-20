"""Add ticket sold information

Revision ID: 9a9cfeb65ea4
Revises: c89449e81bb3
Create Date: 2024-03-06 18:11:32.072355

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "9a9cfeb65ea4"
down_revision: Union[str, None] = "c89449e81bb3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "tickets",
        sa.Column(
            "sold",
            sa.Boolean(),
            nullable=False,
            default=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("tickets", "sold")
    # ### end Alembic commands ###