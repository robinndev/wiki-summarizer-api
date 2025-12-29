from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from sqlalchemy import text
from app.api.routes.health import router as health_router
from app.api.routes.summaries import router as summaries_router

app = FastAPI(title="Wikipedia Summarizer LLM API")

Base.metadata.create_all(bind=engine)

app.include_router(health_router)
app.include_router(summaries_router)

@app.on_event("startup")
def startup_check():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("Database connection OK")
    except Exception as e:
        print("Database connection failed")
        raise e
