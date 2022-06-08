from sqlalchemy import Column, String, Integer
from .database import db


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name!r}>"
