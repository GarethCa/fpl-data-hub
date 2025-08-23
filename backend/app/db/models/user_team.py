from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.session import Base


class UserTeam(Base):
    """
    Represents a local user's saved squad snapshot (simplified).
    """

    __tablename__ = "user_teams"

    id = Column(Integer, primary_key=True)
    user_identifier = Column(
        String(64), index=True
    )  # Could be auth user id or email hash
    gameweek = Column(Integer, index=True)
    points = Column(Integer, default=0)
    value = Column(Integer, default=0)  # Stored in tenths (like FPL)
    bank = Column(Integer, default=0)

    __table_args__ = (
        UniqueConstraint("user_identifier", "gameweek", name="uq_user_team_gw"),
    )

    # (Optional) Relationship placeholders if you later create a linking table for squad players.

    def __repr__(self):
        return f"<UserTeam user={self.user_identifier} gw={self.gameweek} value={self.value}>"
