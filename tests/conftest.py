import pytest
import asyncio

from httpx import ASGITransport, AsyncClient

from src.conf import settings
from src.database import async_engine, Base
from src.main import app
from src.models.equipments import *
from src.models.maps import *
from src.models.orders import *


@pytest.fixture(scope="session", autouse=True)
async def prepare_db():
    assert settings.MODE == "TEST"

    async with async_engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

    yield

    async with async_engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="session", autouse=True)
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


transport = ASGITransport(app=app)


@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
