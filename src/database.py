from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.exc import DBAPIError

from src.conf import settings


if settings.MODE == "TEST":
    DATABASE_URL = settings.database_url_test
else:
    DATABASE_URL = settings.database_url


async_engine = create_async_engine(DATABASE_URL)

async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


class Base(DeclarativeBase):
    ...


async def get_db():
    async with async_session_maker() as session:
        try:
            yield session
        except DBAPIError as e:
            print(f"logging: {e}")
            await session.rollback()
            raise e
