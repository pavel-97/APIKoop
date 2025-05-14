from abc import ABC, abstractmethod

from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from .repository import Repository
from .loared import ReaderJSONFile


class ABCService(ABC):

    @abstractmethod
    async def all(self):
        ...

    @abstractmethod
    async def create(self):
        ...

    @abstractmethod
    async def load(self):
        ...



class Service(ABCService):
    repository: type[Repository]
    model_name: str

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def all(self):
        result = await self.repository(session=self.session).all()
        return result
    
    async def create(self):
        raise NotImplementedError
    
    async def load(self, file: UploadFile):
        data = await ReaderJSONFile().load(file=file)
        result = [
            await self.repository(self.session).load(obj)
            for obj in data.get(self.model_name)
        ]
        self.session.add_all(result)
        await self.session.commit()
        result = await self.repository(self.session).all()
        return {self.model_name: result}
