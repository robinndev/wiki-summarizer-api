from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base
from datetime import datetime

class Summary(Base):
    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True, nullable=False)
    title = Column(String, nullable=True)
    summary = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
