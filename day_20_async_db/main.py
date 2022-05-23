import asyncio
import logging

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

import config
from models import User
from models.base import Base

log = logging.getLogger(__name__)

async_engine = create_async_engine(config.SQLALCHEMY_ASYNC_DB_URI, echo=True)
async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(session: AsyncSession, username: str) -> User:
    pass


async def main_async():
    await create_tables()


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
