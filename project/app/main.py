# ../app/main.py

from app.config import Settings, get_settings
from fastapi import Depends, FastAPI

app = FastAPI()


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
