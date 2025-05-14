from fastapi import APIRouter, UploadFile, Depends, HTTPException
from fastapi import status

from sqlalchemy.exc import NoResultFound

from src.pyds.maps import SListMap, SMap
from src.services.maps import MapService
from src.database import get_db


router = APIRouter(
    prefix="/map",
    tags=["technical_map"]
)


@router.get("")
async def all(session=Depends(get_db)) -> list[SMap]:
    result = await MapService(session=session).all()
    return result


@router.post("/load")
async def laod(file: UploadFile, session=Depends(get_db)) -> SListMap:
    try:
        data = await MapService(session=session).load(file=file)
    except NoResultFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Нет данных"
        )
    return data
