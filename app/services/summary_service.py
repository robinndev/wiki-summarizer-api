from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories.summary_repository import SummaryRepository
from app.services.wikipedia_scraper import WikipediaScraper
from app.services.llm_summary_service import LLMSummaryService


class SummaryService:
    def __init__(self):
        self.repository = SummaryRepository()
        self.scraper = WikipediaScraper()
        self.llm = LLMSummaryService()

    def get_or_create_summary(
        self,
        db: Session,
        url: str,
        max_words: int
    ) -> dict:
        existing = self.repository.get_by_url(db, url)
        if existing:
            return {
                "title": existing.title,
                "summary": existing.summary,
                "has_cached": True
            }

        title, full_text = self.scraper.scrape(url)

        summary_text = self.llm.summarize(
            text=full_text,
            max_words=max_words,
        )

        summary_obj = self.repository.create(
            db=db,
            url=url,
            title=title,
            summary_text=summary_text,
        )

        return {
            "title": summary_obj.title,
            "summary": summary_obj.summary,
            "has_cached": False
        }
    
    def get_cached_summary(self, db: Session, url: str):
        summary = self.repository.get_by_url(db, url)

        if not summary:
            raise HTTPException(
                status_code=404,
                detail="Resumo não encontrado no cache"
            )

        return summary