from dataclasses import dataclass

from sqlalchemy import Integer, String, Column

from chret.dal.models.Base import Base


@dataclass
class TopSite(Base):
    __tablename__ = 'top_sites'
    url = Column(String)
    url_rank = Column(Integer)
    title = Column(String)
    redirects = Column(String)
