from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import settings


engine = create_engine(settings.db.db_url, echo=True)
async_session_maker = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_session():
    async with async_session_maker() as session:
        yield session


class Base(DeclarativeBase):
    pass
