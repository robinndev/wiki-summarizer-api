from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    def validate(self):
        if not self.OPENAI_API_KEY:
            raise RuntimeError("OPENAI_API_KEY não configurada")
        if not self.DATABASE_URL:
            raise RuntimeError("DATABASE_URL não configurada")


settings = Settings()
settings.validate()
