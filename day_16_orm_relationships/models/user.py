from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin


class User(TimestampMixin, Base):
    username = Column(String(20), unique=True)
    is_staff = Column(Boolean, default=True, server_default="FALSE")

    author = relationship("Author", back_populates="user", uselist=False)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"username={self.username!r}, "
            f"is_staff={self.is_staff}, "
            f"created_at={self.created_at}"
            ")"
        )
