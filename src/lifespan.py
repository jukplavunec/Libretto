from contextlib import asynccontextmanager
from src.storages.db import engine
from fastapi import HTTPException
from src.config import settings
import structlog
import redis.asyncio as aioredis
from sqlalchemy import text

logger = structlog.getLogger(__name__)
redis = None

async def check_database_connection():
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        logger.info("Database connection successful")
    except Exception as e:
        logger.info("Database connection failed", exception=e)
        raise HTTPException(status_code=500, detail="Database connection failed")


async def check_redis_connection():
    global redis
    try:
        redis = aioredis.from_url(
            settings.redis_settings.redis_url, encoding="utf-8", decode_responses=True
        )
        await redis.ping()
        logger.info("Redis connection successful")
    except Exception as e:
        logger.info("Redis connection failed", exception=e)
        raise HTTPException(status_code=500, detail="Redis connection failed")


@asynccontextmanager
async def lifespan(app):
    await check_database_connection()
    await check_redis_connection()
    yield
    if redis:
        await redis.close()
    engine.dispose()
