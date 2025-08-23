# ...existing code...
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.player import Player
from app.models import PlayerRead

from fastapi import APIRouter

router = APIRouter(prefix="/players", tags=["players"])


@router.get("/players/{player_id}", response_model=PlayerRead)
def get_player(player_id: int, db: Session = Depends(get_db)):
    return db.query(Player).get(player_id)
