from typing import Optional
from typing import List
from pydantic import BaseModel
from datetime import datetime


class PlayerBase(BaseModel):
    id: int
    web_name: str
    first_name: Optional[str] = None
    second_name: Optional[str] = None
    position: Optional[str] = None
    team_id: Optional[str] = None
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


class PlayerRead(PlayerBase):
    class Config:
        orm_mode = True


class ElementStatsRead(BaseModel):
    id: int
    player_id: int
    timestamp: datetime

    chance_of_playing_next_round: Optional[int]
    chance_of_playing_this_round: Optional[int]
    code: Optional[int]
    cost_change_event: Optional[int]
    cost_change_event_fall: Optional[int]
    cost_change_start: Optional[int]
    cost_change_start_fall: Optional[int]
    dreamteam_count: Optional[int]
    element_type: Optional[int]
    ep_next: Optional[str]
    ep_this: Optional[str]
    event_points: Optional[int]
    form: Optional[str]
    in_dreamteam: Optional[bool]
    news: Optional[str]
    news_added: Optional[str]
    points_per_game: Optional[str]
    special: Optional[bool]
    squad_number: Optional[int]
    status: Optional[str]
    team_code: Optional[int]
    transfers_in: Optional[int]
    transfers_in_event: Optional[int]
    transfers_out: Optional[int]
    transfers_out_event: Optional[int]
    value_form: Optional[str]
    value_season: Optional[str]
    minutes: Optional[int]
    goals_scored: Optional[int]
    assists: Optional[int]
    clean_sheets: Optional[int]
    goals_conceded: Optional[int]
    own_goals: Optional[int]
    penalties_saved: Optional[int]
    penalties_missed: Optional[int]
    yellow_cards: Optional[int]
    red_cards: Optional[int]
    saves: Optional[int]
    bonus: Optional[int]
    bps: Optional[int]
    influence: Optional[str]
    creativity: Optional[str]
    threat: Optional[str]
    ict_index: Optional[str]

    class Config:
        orm_mode = True


class PlayerStatsRead(PlayerBase):
    id: int
    web_name: str
    player_code: str
    # ...other fields...
    stats: List[ElementStatsRead] = []

    class Config:
        orm_mode = True
