from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import config

engine = create_engine(url=config.SQLALCHEMY_DB_URI, echo=config.SQLALCHEMY_DB_ECHO)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
