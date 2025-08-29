from pydantic import BaseModel
from typing import Optional


class TeamBase(BaseModel):
    id: int
    code: int
    draw: int
    form: Optional[str]
    loss: int
    name: str
    played: int
    points: int
    position: int
    short_name: str
    strength: int
    team_division: Optional[int]
    unavailable: bool
    win: int
    strength_overall_home: int
    strength_overall_away: int
    strength_attack_home: int
    strength_attack_away: int
    strength_defence_home: int
    strength_defence_away: int
    pulse_id: int


class TeamCreate(TeamBase):
    pass


class TeamRead(TeamBase):
    class Config:
        orm_mode = True
