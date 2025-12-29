from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.db.base import Base

class Summary(Base):
    __tablename__ = "summaries"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    url: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    title: Mapped[str] = mapped_column(nullable=True)
    summary: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
