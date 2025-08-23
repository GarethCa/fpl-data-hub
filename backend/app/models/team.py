from typing import Optional
from pydantic import BaseModel


class TeamBase(BaseModel):
    id: int
    name: str
    short_name: str
    strength: Optional[int] = None


class TeamCreate(BaseModel):
    id: int
    name: str
    short_name: str
    strength: Optional[int] = None


class TeamRead(TeamBase):
    class Config:
        orm_mode = True
