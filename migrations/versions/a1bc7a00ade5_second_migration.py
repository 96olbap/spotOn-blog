"""Second migration

Revision ID: a1bc7a00ade5
Revises: 2f2331d82437
Create Date: 2022-05-17 11:46:41.320570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1bc7a00ade5'
down_revision = '2f2331d82437'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'blog_pic_path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('blog_pic_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###