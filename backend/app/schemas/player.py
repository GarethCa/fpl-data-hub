from pydantic import BaseModel
from typing import Optional

class PlayerSchema(BaseModel):
    id: int
    name: str
    position: str
    team: str
    price: float
    points: Optional[int] = None

    class Config:
        orm_mode = True