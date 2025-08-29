from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.session import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    web_name = Column(String(64), index=True)
    first_name = Column(String(64))
    second_name = Column(String(64))
    position = Column(String(32), index=True)
    team_id = Column(Integer, ForeignKey("teams.id"), index=True)
    now_cost = Column(Integer)
    selected_by_percent = Column(Float)
    total_points = Column(Integer, default=0)

    team = relationship("Team", back_populates="players")
    element_stats = relationship(
        "ElementStats", back_populates="player", cascade="all, delete-orphan"
    )

    def display_price(self) -> float:
        return self.now_cost / 10.0

    def __repr__(self):
        return f"<Player id={self.id} name={self.web_name} pos={self.position} team_id={self.team_id}>"


class ElementStats(Base):
    __tablename__ = "element_stats"

    id = Column(Integer, primary_key=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey("players.id"), index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)

    chance_of_playing_next_round = Column(Integer)
    chance_of_playing_this_round = Column(Integer)
    code = Column(Integer)
    cost_change_event = Column(Integer)
    cost_change_event_fall = Column(Integer)
    cost_change_start = Column(Integer)
    cost_change_start_fall = Column(Integer)
    dreamteam_count = Column(Integer)
    element_type = Column(Integer)
    ep_next = Column(String(16))
    ep_this = Column(String(16))
    event_points = Column(Integer)
    form = Column(String(16))
    in_dreamteam = Column(Boolean)
    news = Column(String(256))
    news_added = Column(String(64))
    points_per_game = Column(String(16))
    special = Column(Boolean)
    squad_number = Column(Integer)
    status = Column(String(8))
    team_code = Column(Integer)
    transfers_in = Column(Integer)
    transfers_in_event = Column(Integer)
    transfers_out = Column(Integer)
    transfers_out_event = Column(Integer)
    value_form = Column(String(16))
    value_season = Column(String(16))
    minutes = Column(Integer)
    goals_scored = Column(Integer)
    assists = Column(Integer)
    clean_sheets = Column(Integer)
    goals_conceded = Column(Integer)
    own_goals = Column(Integer)
    penalties_saved = Column(Integer)
    penalties_missed = Column(Integer)
    yellow_cards = Column(Integer)
    red_cards = Column(Integer)
    saves = Column(Integer)
    bonus = Column(Integer)
    bps = Column(Integer)
    influence = Column(String(16))
    creativity = Column(String(16))
    threat = Column(String(16))
    ict_index = Column(String(16))

    player = relationship("Player", back_populates="element_stats")

    def __repr__(self):
        return f"<ElementStats id={self.id} player_id={self.player_id} timestamp={self.timestamp}>"
