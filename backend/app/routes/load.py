from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException, Depends
import httpx
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.player import Player, ElementStats
from app.db.models.team import Team
from app.db.models.event import Event
from app.db.models.phase import Phase

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
    # ...inside load_fpl_data...
    for t in teams:
        db_team = db.query(Team).get(t["id"])
        team_data = {
            "id": t["id"],
            "code": t["code"],
            "draw": t["draw"],
            "form": t.get("form"),
            "loss": t["loss"],
            "name": t["name"],
            "played": t["played"],
            "points": t["points"],
            "position": t["position"],
            "short_name": t["short_name"],
            "strength": t["strength"],
            "team_division": t.get("team_division"),
            "unavailable": t["unavailable"],
            "win": t["win"],
            "strength_overall_home": t["strength_overall_home"],
            "strength_overall_away": t["strength_overall_away"],
            "strength_attack_home": t["strength_attack_home"],
            "strength_attack_away": t["strength_attack_away"],
            "strength_defence_home": t["strength_defence_home"],
            "strength_defence_away": t["strength_defence_away"],
            "pulse_id": t["pulse_id"],
        }
        if db_team:
            for key, value in team_data.items():
                setattr(db_team, key, value)
        else:
            db_team = Team(**team_data)
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

    # --- Load Players and ElementStats ---
    for p in players:
        # Player fields
        player_data = {
            "id": p["id"],
            "web_name": p["web_name"],
            "first_name": p["first_name"],
            "second_name": p["second_name"],
            "position": str(p["element_type"]),
            "team_id": p["team"],
            "now_cost": p["now_cost"],
            "selected_by_percent": float(p.get("selected_by_percent", 0.0)),
            "total_points": p["total_points"],
        }
        db_player = db.query(Player).get(p["id"])
        if db_player:
            for key, value in player_data.items():
                setattr(db_player, key, value)
        else:
            db_player = Player(**player_data)
            db.add(db_player)
            db.flush()  # Ensure db_player.id is available

        # ElementStats fields
        stats_data = {
            "player_id": db_player.id,
            "chance_of_playing_next_round": p.get("chance_of_playing_next_round"),
            "chance_of_playing_this_round": p.get("chance_of_playing_this_round"),
            "code": p.get("code"),
            "cost_change_event": p.get("cost_change_event"),
            "cost_change_event_fall": p.get("cost_change_event_fall"),
            "cost_change_start": p.get("cost_change_start"),
            "cost_change_start_fall": p.get("cost_change_start_fall"),
            "dreamteam_count": p.get("dreamteam_count"),
            "element_type": p.get("element_type"),
            "ep_next": p.get("ep_next"),
            "ep_this": p.get("ep_this"),
            "event_points": p.get("event_points"),
            "form": p.get("form"),
            "in_dreamteam": p.get("in_dreamteam"),
            "news": p.get("news"),
            "news_added": p.get("news_added"),
            "points_per_game": p.get("points_per_game"),
            "special": p.get("special"),
            "squad_number": p.get("squad_number"),
            "status": p.get("status"),
            "team_code": p.get("team_code"),
            "transfers_in": p.get("transfers_in"),
            "transfers_in_event": p.get("transfers_in_event"),
            "transfers_out": p.get("transfers_out"),
            "transfers_out_event": p.get("transfers_out_event"),
            "value_form": p.get("value_form"),
            "value_season": p.get("value_season"),
            "minutes": p.get("minutes"),
            "goals_scored": p.get("goals_scored"),
            "assists": p.get("assists"),
            "clean_sheets": p.get("clean_sheets"),
            "goals_conceded": p.get("goals_conceded"),
            "own_goals": p.get("own_goals"),
            "penalties_saved": p.get("penalties_saved"),
            "penalties_missed": p.get("penalties_missed"),
            "yellow_cards": p.get("yellow_cards"),
            "red_cards": p.get("red_cards"),
            "saves": p.get("saves"),
            "bonus": p.get("bonus"),
            "bps": p.get("bps"),
            "influence": p.get("influence"),
            "creativity": p.get("creativity"),
            "threat": p.get("threat"),
            "ict_index": p.get("ict_index"),
        }
        element_stats = ElementStats(**stats_data)
        db.add(element_stats)
    # ...after events...
    phases = data.get("phases", [])
    for ph in phases:
        db_phase = db.query(Phase).get(ph["id"])
        if db_phase:
            db_phase.name = ph["name"]
            db_phase.start_event = ph["start_event"]
            db_phase.stop_event = ph["stop_event"]
            db_phase.highest_score = ph["highest_score"]
        else:
            db_phase = Phase(
                id=ph["id"],
                name=ph["name"],
                start_event=ph["start_event"],
                stop_event=ph["stop_event"],
                highest_score=ph["highest_score"],
            )
            db.add(db_phase)
    db.commit()

    return {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "players_count": len(players),
        "teams_count": len(teams),
        "events_count": len(events),
        "status": "Data loaded to DB",
    }
