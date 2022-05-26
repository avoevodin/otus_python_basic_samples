from typing import List, Optional

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession as SessionType
from starlette.status import HTTP_404_NOT_FOUND

from models import User
from . import crud_async as crud
from .dependencies import get_user_by_auth_token_async, get_db_async
from .schemas import UserIn, UserOut

router = APIRouter(tags=["Users async"])


@router.get("", response_model=list[UserOut])
async def list_users(session: SessionType = Depends(get_db_async)) -> List[User]:
    return await crud.list_users(session)


@router.post("", response_model=UserOut)
async def create_user(
    user_in: UserIn, session: SessionType = Depends(get_db_async)
) -> User:
    return await crud.create_user(session, user_in)


@router.get("/me", response_model=UserOut)
async def get_me(user: User = Depends(get_user_by_auth_token_async)) -> User:
    return user


@router.get(
    "/{user_id}",
    response_model=UserOut,
    responses={
        HTTP_404_NOT_FOUND: {
            "description": "user not found",
            "content": {
                "application/json": {
                    "schema": {
                        "title": "Not Found",
                        "type": "object",
                        "properties": {
                            "detail": {
                                "title": "Detail",
                                "type": "string",
                                "example": "user #0 not found",
                            },
                        },
                    },
                },
            },
        },
    },
)
async def get_user_by_id(
    user_id: int, session: SessionType = Depends(get_db_async)
) -> Optional[User]:
    user = await crud.get_user(session, user_id)
    if user:
        return user

    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"user #{user_id} not found!",
    )
