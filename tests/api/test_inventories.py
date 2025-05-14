from httpx import AsyncClient


async def test_load(ac: AsyncClient):
    with open("inventory.json", "br") as f:
        response = await ac.post(
            "/inventory/load",
            files={
                "file": f
                }
            )
    assert response.status_code == 200
    

async def test_all(ac: AsyncClient):
    response = await ac.get("/inventory")
    assert response.status_code == 200
    