import logging

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

import config

log = logging.getLogger(__name__)

async_engine = create_async_engine(
    config.SQLALCHEMY_ASYNC_DB_URI,
    echo=config.SQLALCHEMY_DB_ECHO,
    pool_size=config.SQLALCHEMY_POOL_SIZE,
    max_overflow=config.SQLALCHEMY_MAX_OVERFLOW,
)
async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)
