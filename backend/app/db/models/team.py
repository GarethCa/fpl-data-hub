from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.session import Base


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    code = Column(Integer)
    draw = Column(Integer)
    form = Column(String(16), nullable=True)
    loss = Column(Integer)
    name = Column(String(64), nullable=False)
    played = Column(Integer)
    points = Column(Integer)
    position = Column(Integer)
    short_name = Column(String(16), nullable=False, index=True)
    strength = Column(Integer)
    team_division = Column(Integer, nullable=True)
    unavailable = Column(Boolean)
    win = Column(Integer)
    strength_overall_home = Column(Integer)
    strength_overall_away = Column(Integer)
    strength_attack_home = Column(Integer)
    strength_attack_away = Column(Integer)
    strength_defence_home = Column(Integer)
    strength_defence_away = Column(Integer)
    pulse_id = Column(Integer)

    players = relationship("Player", back_populates="team", cascade="all,delete-orphan")
    home_fixtures = relationship(
        "Fixture", back_populates="home_team", foreign_keys="Fixture.team_h_id"
    )
    away_fixtures = relationship(
        "Fixture", back_populates="away_team", foreign_keys="Fixture.team_a_id"
    )

    def __repr__(self):
        return f"<Team id={self.id} name={self.short_name}>"
