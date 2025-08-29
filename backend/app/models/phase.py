from pydantic import BaseModel


class PhaseBase(BaseModel):
    id: int
    name: str
    start_event: int
    stop_event: int
    highest_score: int


class PhaseCreate(PhaseBase):
    pass


class PhaseRead(PhaseBase):
    class Config:
        orm_mode = True
