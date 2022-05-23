from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin
from .posts_tags import posts_tags_association_table


if TYPE_CHECKING:
    from .post import Post


class Tag(TimestampMixin, Base):
    name = Column(String, unique=True, nullable=False)

    posts = relationship(
        "Post", secondary=posts_tags_association_table, back_populates="tags"
    )

    if TYPE_CHECKING:
        posts: list[Post]

    def __str__(self):
        return self.name

    def __repr__(self):
        return repr(self.name)
