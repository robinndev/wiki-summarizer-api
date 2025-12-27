from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.summaries import router as summaries_router

app = FastAPI(title="Wikipedia Summarizer API")

app.include_router(health_router)
app.include_router(summaries_router)
