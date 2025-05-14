from fastapi import FastAPI

from src.routers.equipments import router as equipment_router
from src.routers.inventories import router as inventory_router
from src.routers.maps import router as map_router
from src.routers.orders import router as order_router


app = FastAPI()


app.include_router(equipment_router)
app.include_router(inventory_router)
app.include_router(map_router)
app.include_router(order_router)
