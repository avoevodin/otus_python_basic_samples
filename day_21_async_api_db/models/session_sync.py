from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import config

engine = create_engine(
    url=config.SQLALCHEMY_DB_URI,
    echo=config.SQLALCHEMY_DB_ECHO,
    pool_size=config.SQLALCHEMY_POOL_SIZE,
    max_overflow=config.SQLALCHEMY_MAX_OVERFLOW,
)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
