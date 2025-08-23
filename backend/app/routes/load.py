from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException, Depends
import httpx
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.player import Player
from app.db.models.team import Team
from app.db.models.event import Event

router = APIRouter(prefix="/fpl", tags=["fpl"])


@router.post("/load", summary="Fetch latest FPL bootstrap data")
async def load_fpl_data(db: Session = Depends(get_db)):
    """
    Fetch Fantasy Premier League bootstrap data and persist to DB.
    """
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.get(url)
            resp.raise_for_status()
            data = resp.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=502, detail=f"FPL upstream error: {e}") from e

    players = data.get("elements", [])
    teams = data.get("teams", [])
    events = data.get("events", [])

    # --- Load Teams ---
    for t in teams:
        db_team = db.query(Team).get(t["id"])
        if db_team:
            db_team.name = t["name"]
            db_team.short_name = t["short_name"]
            db_team.strength = t.get("strength")
        else:
            db_team = Team(
                id=t["id"],
                name=t["name"],
                short_name=t["short_name"],
                strength=t.get("strength"),
            )
            db.add(db_team)

    # --- Load Events (Gameweeks) ---
    for e in events:
        db_event = db.query(Event).get(e["id"])
        if db_event:
            db_event.name = e["name"]
            db_event.deadline_time = e.get("deadline_time")
            db_event.finished = e.get("finished", False)
            db_event.data_checked = e.get("data_checked", False)
        else:
            db_event = Event(
                id=e["id"],
                name=e["name"],
                deadline_time=e.get("deadline_time"),
                finished=e.get("finished", False),
                data_checked=e.get("data_checked", False),
            )
            db.add(db_event)

    # --- Load Players ---
    for p in players:
        db_player = db.query(Player).get(p["id"])
        if db_player:
            db_player.web_name = p["web_name"]
            db_player.first_name = p["first_name"]
            db_player.second_name = p["second_name"]
            db_player.position = str(p["element_type"])
            db_player.team_id = p["team"]
            db_player.now_cost = p["now_cost"]
            db_player.selected_by_percent = float(p.get("selected_by_percent", 0.0))
            db_player.total_points = p["total_points"]
        else:
            db_player = Player(
                id=p["id"],
                web_name=p["web_name"],
                first_name=p["first_name"],
                second_name=p["second_name"],
                position=str(p["element_type"]),
                team_id=p["team"],
                now_cost=p["now_cost"],
                selected_by_percent=float(p.get("selected_by_percent", 0.0)),
                total_points=p["total_points"],
            )
            db.add(db_player)

    db.commit()

    return {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "players_count": len(players),
        "teams_count": len(teams),
        "events_count": len(events),
        "status": "Data loaded to DB",
    }
