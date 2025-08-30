# ...existing code...
from fastapi import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.session import get_db
from app.db.models.player import Player
from app.models import PlayerRead
from app.models import PlayerStatsRead

from fastapi import APIRouter

router = APIRouter(prefix="/players", tags=["players"])


@router.get("/{player_id}", response_model=PlayerStatsRead)
def get_player(player_id: int, db: Session = Depends(get_db)):
    # Fetch player using raw SQL
    player_row = (
        db.execute(
            text("SELECT * FROM players WHERE id = :player_id"),
            {"player_id": player_id},
        )
        .mappings()
        .first()
    )
    if not player_row:
        raise HTTPException(status_code=404, detail="Player not found")

    # Fetch stats using raw SQL
    stats_rows = (
        db.execute(
            text(
                "SELECT * FROM element_stats WHERE player_id = :player_id order by timestamp DESC"
            ),
            {"player_id": player_id},
        )
        .mappings()
        .all()
    )

    # Convert to dict for Pydantic
    player_dict = dict(player_row)
    player_dict["stats"] = [dict(row) for row in stats_rows]
    player_dict["player_code"] = str(player_dict["stats"][0].get("code"))
    return player_dict


@router.get("/", response_model=list[PlayerRead])
def list_players(db: Session = Depends(get_db)):
    return db.query(Player).all()
