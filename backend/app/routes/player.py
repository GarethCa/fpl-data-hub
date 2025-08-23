# ...existing code...
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.player import Player
from app.models import PlayerRead

from fastapi import APIRouter

router = APIRouter(prefix="/players", tags=["players"])


@router.get("/{player_id}", response_model=PlayerRead)
def get_player(player_id: int, db: Session = Depends(get_db)):
    return db.query(Player).get(player_id)


@router.get("/", response_model=list[PlayerRead])
def list_players(db: Session = Depends(get_db)):
    return db.query(Player).all()
