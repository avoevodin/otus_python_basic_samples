from uuid import uuid4

from pydantic import BaseModel, constr, Field


class UserBase(BaseModel):
    username: constr(min_length=4)


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    id: int = Field(..., example=123)

    class Config:
        orm_mode = True
