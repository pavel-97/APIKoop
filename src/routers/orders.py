from fastapi import APIRouter, UploadFile, Depends

from src.database import get_db
from src.services.orders import OrderService
from src.pyds.orders import SListOrders, SOrders


router = APIRouter(
    prefix="/order",
    tags=["order"]
)


@router.get("")
async def all(session=Depends(get_db)) -> list[SOrders]:
    result = await OrderService(session=session).all()
    return result


@router.post("/load")
async def load(file: UploadFile, session=Depends(get_db)) -> SListOrders:
    result = await OrderService(session=session).load(file=file)
    return result
