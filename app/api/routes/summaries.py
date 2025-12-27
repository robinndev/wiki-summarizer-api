from fastapi import APIRouter
from app.schemas.summary import SummaryRequest, SummaryResponse

router = APIRouter(prefix="/summaries", tags=["Summaries"])


@router.post("/", response_model=SummaryResponse)
def create_summary(payload: SummaryRequest):
    return {
        "url": payload.url,
        "summary": f"Resumo fake com limite de {payload.max_words} palavras."
    }
