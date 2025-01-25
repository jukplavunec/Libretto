from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.base_repository import BaseRepository


class BookRepository(BaseRepository):
    def get_all(self, session: AsyncSession, id: str) -> list[object]:
        return []

    def create(self, session: AsyncSession, object: object) -> None:
        pass
