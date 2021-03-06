from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import declarative_base, declared_attr, scoped_session, sessionmaker

import config as config


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


engine = create_engine(url=config.SQLALCHEMY_DB_URI, echo=config.SQLALCHEMY_DB_ECHO)
Base = declarative_base(bind=engine, cls=Base)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
