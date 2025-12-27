from pydantic import BaseModel, HttpUrl, Field


class SummaryRequest(BaseModel):
    url: HttpUrl = Field(..., example="https://pt.wikipedia.org/wiki/Ita%C3%BA_Unibanco")
    max_words: int = Field(..., gt=10, le=500, example=150)


class SummaryResponse(BaseModel):
    url: HttpUrl
    summary: str
