from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any


class BaseRepository(ABC):
    @abstractmethod
    def create(self, session: AsyncSession, object: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self, session: AsyncSession, id: str) -> Any:
        raise NotImplementedError
