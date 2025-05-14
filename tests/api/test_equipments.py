from httpx import AsyncClient


async def test_load(ac: AsyncClient):
    with open("equipment.json", "br") as f:
        response = await ac.post(
            "/equipment/load",
            files={
                "file": f,
                }
            )
    assert response.status_code == 200


async def test_all(ac: AsyncClient):
    response = await ac.get("/equipment")
    assert response.status_code == 200
