import logging

# from asyncio import sleep
from typing import Optional, List

from aiohttp import ClientSession
from fastapi import HTTPException
from fastapi import status
from sqlalchemy import select
from sqlalchemy.engine.result import Result
from sqlalchemy.exc import DatabaseError
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from .schemas import UserIn as UserInSchema

log = logging.getLogger(__name__)


async def list_users(session: AsyncSession) -> List[User]:
    stmt = select(User)
    result: Result = await session.execute(stmt)
    users: List[User] = list(result.scalars())

    return users


async def create_user(session: AsyncSession, user_in: UserInSchema) -> User:
    user = User(**user_in.dict())
    session.add(user)

    try:
        await session.commit()
    except DatabaseError as e:
        log.exception("could not save user")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
    await session.refresh(user)
    return user


async def get_user(session: AsyncSession, user_id: int) -> Optional[User]:
    # await sleep(0.1)
    try:
        async with ClientSession() as client:
            async with client.get("https://httpbin.org/get") as response:
                await response.json()
    except:
        pass

    return await session.get(User, user_id)


async def get_user_by_token(session: AsyncSession, token: str) -> Optional[User]:
    stmt = select(User).where(User.token == token)
    result: Result = await session.execute(stmt)
    user: User = result.scalar_one()
    return user
