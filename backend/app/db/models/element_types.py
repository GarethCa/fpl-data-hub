from sqlalchemy import Column, Integer, String, Boolean, JSON
from app.db.session import Base


class ElementType(Base):
    __tablename__ = "element_types"

    id = Column(Integer, primary_key=True)
    plural_name = Column(String(32), nullable=False)
    plural_name_short = Column(String(16), nullable=False)
    singular_name = Column(String(32), nullable=False)
    singular_name_short = Column(String(16), nullable=False)
    squad_select = Column(Integer)
    squad_min_select = Column(Integer, nullable=True)
    squad_max_select = Column(Integer, nullable=True)
    squad_min_play = Column(Integer)
    squad_max_play = Column(Integer)
    ui_shirt_specific = Column(Boolean)
    sub_positions_locked = Column(JSON)
    element_count = Column(Integer)
