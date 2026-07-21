from fastapi import FastAPI
import uvicorn
from src.config import settings
from src.api import api_router

app = FastAPI(
    title=settings.app_title,
    version=settings.app_version,
)
app.include_router(api_router)


def main():
    pass


if __name__ == "__main__":
    uvicorn.run(
        app="src.main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.app_reload,
    )
