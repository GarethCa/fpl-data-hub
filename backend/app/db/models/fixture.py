from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.session import Base


class Fixture(Base):
    __tablename__ = "fixtures"

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.id"), index=True, nullable=True)
    kickoff_time = Column(DateTime, index=True)
    team_h_id = Column(Integer, ForeignKey("teams.id"), index=True)
    team_a_id = Column(Integer, ForeignKey("teams.id"), index=True)
    team_h_score = Column(Integer)
    team_a_score = Column(Integer)
    finished = Column(Boolean, default=False)

    home_team = relationship(
        "Team", foreign_keys=[team_h_id], back_populates="home_fixtures"
    )
    away_team = relationship(
        "Team", foreign_keys=[team_a_id], back_populates="away_fixtures"
    )

    def __repr__(self):
        return f"<Fixture id={self.id} gw={self.event_id} {self.team_h_id} vs {self.team_a_id}>"
