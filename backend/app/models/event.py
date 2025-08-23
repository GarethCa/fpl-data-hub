from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class EventBase(BaseModel):
    id: int
    name: str
    deadline_time: Optional[datetime] = None
    finished: bool = False
    data_checked: bool = False


class EventCreate(BaseModel):
    id: int
    name: str
    deadline_time: Optional[datetime] = None
    finished: bool = False
    data_checked: bool = False


class EventRead(EventBase):
    class Config:
        orm_mode = True
