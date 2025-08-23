from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)  # FPL team id (1..20)
    name = Column(String(64), nullable=False)
    short_name = Column(String(16), nullable=False, index=True)
    strength = Column(Integer)

    players = relationship("Player", back_populates="team", cascade="all,delete-orphan")
    home_fixtures = relationship(
        "Fixture", back_populates="home_team", foreign_keys="Fixture.team_h_id"
    )
    away_fixtures = relationship(
        "Fixture", back_populates="away_team", foreign_keys="Fixture.team_a_id"
    )

    def __repr__(self):
        return f"<Team id={self.id} name={self.short_name}>"
