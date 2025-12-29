from datetime import datetime
from pydantic import BaseModel, HttpUrl, Field


class SummaryRequest(BaseModel):
    url: HttpUrl = Field(
        ...,
        example="https://pt.wikipedia.org/wiki/Ita%C3%BA_Unibanco",
        description="URL da página do Wikipedia que você quer resumir"
    )
    max_words: int = Field(
        ...,
        gt=10,
        le=500,
        example=150,
        description="Número máximo de palavras para o resumo gerado"
    )


class SummaryResponse(BaseModel):
    url: HttpUrl = Field(
        ...,
        description="URL da página do Wikipedia resumida"
    )
    title: str = Field(
        ...,
        description="Título da página do Wikipedia"
    )
    summary: str = Field(
        ...,
        description="Resumo gerado da página, limitado pelo número de palavras informado"
    )
    has_cached: bool = Field(
        ...,
        example=True,
        description="Indica se o resumo foi retornado a partir do cache"
    )


class CachedSummaryResponse(BaseModel):
    url: HttpUrl
    title: str
    summary: str
    created_at: datetime