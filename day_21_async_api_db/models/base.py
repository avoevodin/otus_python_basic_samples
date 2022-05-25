from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base, declared_attr

from .session_sync import engine


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


Base = declarative_base(cls=Base)
