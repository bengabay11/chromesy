from dataclasses import dataclass

from sqlalchemy import Integer, String, Column, Boolean

from chromesy.dal.models.Base import Base


@dataclass
class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    title = Column(String)
    visit_count = Column(Integer)
    typed_count = Column(Boolean)
    last_visit_time = Column(Integer)
    hidden = Column(Boolean)

