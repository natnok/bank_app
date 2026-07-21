from fastapi import APIRouter
from src.api import health_check

api_router = APIRouter()

api_router.include_router(health_check.router, prefix="/health_check", tags=["health_check"])
