from sqlalchemy.orm import Session
from app.db.models import Summary


class SummaryRepository:

    def get_by_url(self, db: Session, url: str) -> Summary | None:
        return db.query(Summary).filter(Summary.url == url).first()

    def create(self, db, url, title, summary_text):
        new_summary = Summary(url=url, title=title, summary=summary_text)
        db.add(new_summary)
        db.commit()
        db.refresh(new_summary)
        return new_summary


