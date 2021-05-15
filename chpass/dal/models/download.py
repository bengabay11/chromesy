from dataclasses import dataclass

from sqlalchemy import Integer, String, Column, LargeBinary

from chpass.dal.models.base import Base


@dataclass
class Download(Base):
    __tablename__ = 'downloads'
    id = Column(Integer, primary_key=True)
    guid = Column(String)
    current_path = Column(String)
    target_path = Column(String)
    start_time = Column(Integer)
    received_bytes = Column(Integer)
    total_bytes = Column(Integer)
    state = Column(Integer)
    danger_type = Column(Integer)
    interrupt_reason = Column(Integer)
    hash = Column(LargeBinary)
    end_time = Column(Integer)
    opened = Column(Integer)
    last_access_time = Column(Integer)
    transient = Column(Integer)
    referrer = Column(String)
    site_url = Column(String)
    tab_url = Column(String)
    tab_referrer_url = Column(String)
    http_method = Column(String)
    by_ext_id = Column(String)
    by_ext_name = Column(String)
    etag = Column(String)
    last_modified = Column(String)
    mime_type = Column(String)
    original_mime_type = Column(String)
