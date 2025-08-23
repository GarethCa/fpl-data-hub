from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class FixtureBase(BaseModel):
    id: int
    event_id: Optional[int] = None
    kickoff_time: Optional[datetime] = None
    team_h_id: int
    team_a_id: int
    team_h_score: Optional[int] = None
    team_a_score: Optional[int] = None
    finished: bool = False


class FixtureCreate(BaseModel):
    id: int
    event_id: Optional[int] = None
    kickoff_time: Optional[datetime] = None
    team_h_id: int
    team_a_id: int
    team_h_score: Optional[int] = None
    team_a_score: Optional[int] = None
    finished: bool = False


class FixtureRead(FixtureBase):
    class Config:
        orm_mode = True
