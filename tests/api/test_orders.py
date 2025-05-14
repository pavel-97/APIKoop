from httpx import AsyncClient


async def test_laod(ac: AsyncClient):
    with open("orders.json", "br") as f:
        response = await ac.post(
            "/order/load",
            files={
                "file": f
                }
            )
    assert response.status_code == 200


async def test_all(ac: AsyncClient):
    response = await ac.get("/order")
    assert response.status_code == 200
