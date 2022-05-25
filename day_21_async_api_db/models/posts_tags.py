from datetime import datetime

from sqlalchemy import Table, Column, ForeignKey, DateTime, func

from .base import Base

posts_tags_association_table = Table(
    "posts_tags_association",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
    Column(
        "created_at",
        DateTime,
        nullable=False,
        server_default=func.now(),
        default=datetime.utcnow,
    ),
)
