from fastapi import APIRouter, UploadFile, Depends

from src.pyds.equipments import SListEquipment, SEquipment
from src.services.equipments import EquipmentService
from src.database import get_db


router = APIRouter(
    prefix="/equipment",
    tags=["equipment"]
)


@router.get("")
async def all(session=Depends(get_db)) -> list[SEquipment]:
    result = await EquipmentService(session=session).all()
    return result


@router.post("/load")
async def load(file: UploadFile, session=Depends(get_db)) -> SListEquipment:
    result = await EquipmentService(session=session).load(file=file)
    return result
