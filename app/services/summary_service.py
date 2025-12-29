from urllib.parse import urlparse, urlunparse

from sqlalchemy.orm import Session

from app.repositories.summary_repository import SummaryRepository
from app.services.wikipedia_scraper import WikipediaScraper
from app.services.llm_summary_service import LLMSummaryService


class SummaryService:
    def __init__(
        self,
        repository: SummaryRepository | None = None,
        scraper: WikipediaScraper | None = None,
        llm_service: LLMSummaryService | None = None,
    ):
        self.repository = repository or SummaryRepository()
        self.scraper = scraper or WikipediaScraper()
        self.llm = llm_service or LLMSummaryService()

    def _normalize_url(self, url: str) -> str:
        parsed = urlparse(url)

        normalized = urlunparse(
            parsed._replace(
                query="",
                fragment="",
            )
        )

        return normalized.rstrip("/")

    def get_or_create_summary(
        self,
        db: Session,
        url: str,
        max_words: int,
    ) -> dict:
        normalized_url = self._normalize_url(url)

        existing = self.repository.get_by_url(db, normalized_url)
        if existing:
            return {
                "title": existing.title,
                "summary": existing.summary,
                "has_cached": True,
            }

        title, full_text = self.scraper.scrape(normalized_url)

        summary_text = self.llm.summarize(
            text=full_text,
            max_words=max_words,
        )

        summary_obj = self.repository.create(
            db=db,
            url=normalized_url,
            title=title,
            summary_text=summary_text,
        )

        return {
            "title": summary_obj.title,
            "summary": summary_obj.summary,
            "has_cached": False,
        }

    def get_cached_summary(
        self,
        db: Session,
        url: str,
    ):
        normalized_url = self._normalize_url(url)
        return self.repository.get_by_url(db, normalized_url)
