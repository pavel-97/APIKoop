from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Select

from src.database import Base


class ABCRepository(ABC):

    @abstractmethod
    async def get(self):
        ...

    @abstractmethod
    async def all(self):
        ...

    @abstractmethod
    async def create(self):
        ...

    @abstractmethod
    async def load(self):
        ...


class Repository(ABCRepository):

    model: type[Base]
    query_get: Select
    field: str
    query_all: Select

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get(self, field: str):
        result = (
            await self.session.execute(
                self.query_get.where(
                    object.__getattribute__(self.model, self.field) == field
                    )
                )
            ).scalar_one()
        return result
    
    async def all(self):
        result = (await self.session.execute(self.query_all)).scalars().all()
        return result
    
    async def load():
        raise NotImplementedError
    
    async def create(self):
        raise NotImplementedError
    