from httpx import AsyncClient


async def test_load(ac: AsyncClient):
    with open("technical_maps.json", "br") as f:
        response = await ac.post(
            "/map/load",
            files={
                "file": f
                }
            )
    assert response.status_code == 200
    print(response.json())


async def test_all(ac:AsyncClient):
    response = await ac.get("/map")
    assert response.status_code == 200
