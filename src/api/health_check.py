from fastapi import APIRouter
from src.dependencies import DBDep
from sqlalchemy import text

router = APIRouter()


@router.get("")
async def health_check(db: DBDep):
    await db.session.execute(text("SELECT 1"))
    return {"status": "ok"}
