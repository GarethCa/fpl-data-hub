from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)  # FPL element id
    web_name = Column(String(64), index=True)
    first_name = Column(String(64))
    second_name = Column(String(64))
    position = Column(String(32), index=True)  # e.g. 'FWD', 'MID'
    team_id = Column(Integer, ForeignKey("teams.id"), index=True)
    now_cost = Column(Integer)  # Stored in tenths per FPL (e.g. 55 = 5.5m)
    selected_by_percent = Column(Float)
    total_points = Column(Integer, default=0)

    team = relationship("Team", back_populates="players")

    def display_price(self) -> float:
        return self.now_cost / 10.0

    def __repr__(self):
        return f"<Player id={self.id} name={self.web_name} pos={self.position} team_id={self.team_id}>"
