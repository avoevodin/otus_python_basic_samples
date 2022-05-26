from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session as SessionType
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_401_UNAUTHORIZED

from models import User
from models.session_sync import Session
from models.session_async import async_session
from . import crud, crud_async


def get_db_sync() -> SessionType:
    with Session() as session:  # type: Session
        yield session
    # session = Session()
    # try:
    #     yield session
    # finally:
    #     session.close()


async def get_db_async() -> AsyncSession:
    async with async_session() as session:  # type: AsyncSession
        yield session
    # session: AsyncSessionType = AsyncSession()
    # try:
    #     yield session
    # finally:
    #     await session.close()


def get_user_by_auth_token(
    session: SessionType = Depends(get_db_sync),
    token: str = Header(..., description="user auth token"),
) -> User:
    user = crud.get_user_by_token(session, token)
    if user:
        return user

    raise HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail={"message": "Invalid token!"},
    )


async def get_user_by_auth_token_async(
    session: AsyncSession = Depends(get_db_async),
    token: str = Header(..., description="user auth token"),
) -> User:
    user = await crud_async.get_user_by_token(session, token)
    if user:
        return user

    raise HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail={"message": "Invalid token!"},
    )
