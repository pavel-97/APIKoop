from fastapi import APIRouter, UploadFile, Depends

from src.pyds.inventories import SListInventory, SInventory
from src.services.inventories import InventoryService
from src.database import get_db


router = APIRouter(
    prefix="/inventory",
    tags=["inventory"]
)


@router.get("")
async def all(session=Depends(get_db)) -> list[SInventory]:
    result = await InventoryService(session=session).all()
    return result


@router.post("/load")
async def load(file: UploadFile, session=Depends(get_db)) -> SListInventory:
    result = await InventoryService(session=session).load(file=file)
    return result
