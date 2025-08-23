from typing import Optional
from pydantic import BaseModel


class PlayerBase(BaseModel):
    id: int
    web_name: str
    first_name: Optional[str] = None
    second_name: Optional[str] = None
    position: Optional[str] = None
    team_id: Optional[int] = None
    now_cost: Optional[int] = None
    selected_by_percent: Optional[float] = None
    total_points: Optional[int] = None


class PlayerCreate(BaseModel):
    # FPL bootstrap provides these; id handled explicitly
    id: int
    web_name: str
    first_name: str
    second_name: str
    position: str
    team_id: int
    now_cost: int
    selected_by_percent: float
    total_points: int = 0


class PlayerUpdate(BaseModel):
    now_cost: Optional[int] = None
    selected_by_percent: Optional[float] = None
    total_points: Optional[int] = None


class PlayerRead(PlayerBase):
    class Config:
        orm_mode = True
