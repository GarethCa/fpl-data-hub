from sqlalchemy import Column, Integer, String
from app.db.session import Base


class Phase(Base):
    __tablename__ = "phases"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    start_event = Column(Integer, nullable=False)
    stop_event = Column(Integer, nullable=False)
    highest_score = Column(Integer)
