from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from app.schemas.summary import SummaryRequest, SummaryResponse, CachedSummaryResponse
from app.db.session import get_db
from app.services.summary_service import SummaryService

router = APIRouter(prefix="/summaries", tags=["Summaries"])

summary_service = SummaryService()

def get_summary_service():
    return summary_service


@router.post("/", response_model=SummaryResponse)
def create_summary(
    payload: SummaryRequest,
    db: Session = Depends(get_db),
    service: SummaryService = Depends(get_summary_service),
):
    summary = service.get_or_create_summary(
        db=db,
        url=str(payload.url),
        max_words=payload.max_words,
    )

    return SummaryResponse(
        url=payload.url,
        title=summary["title"],
        summary=summary["summary"],
        has_cached=summary["has_cached"],
    )


@router.get("/cache", response_model=CachedSummaryResponse)
def get_cached_summary(
    url: str = Query(..., description="URL da página do Wikipedia"),
    db: Session = Depends(get_db),
    service: SummaryService = Depends(get_summary_service),
):
    summary = service.get_cached_summary(db=db, url=url)

    if not summary:
        raise HTTPException(
            status_code=404,
            detail="Resumo não encontrado no cache",
        )

    return summary
