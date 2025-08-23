from typing import Optional
from pydantic import BaseModel


class UserTeamBase(BaseModel):
    id: int
    user_identifier: str
    gameweek: int
    points: int
    value: int
    bank: int


class UserTeamCreate(BaseModel):
    user_identifier: str
    gameweek: int
    points: int = 0
    value: int = 0
    bank: int = 0


class UserTeamRead(UserTeamBase):
    class Config:
        orm_mode = True
