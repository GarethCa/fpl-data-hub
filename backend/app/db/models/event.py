from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.db.session import Base


class Event(Base):
    """
    Gameweek metadata (FPL 'events').
    """

    __tablename__ = "events"

    id = Column(Integer, primary_key=True)  # Gameweek number
    name = Column(String(32), nullable=False)
    deadline_time = Column(DateTime)
    finished = Column(Boolean, default=False)
    data_checked = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Event gw={self.id} name={self.name} finished={self.finished}>"
