from decimal import Decimal
from datetime import date, time

from pydantic import BaseModel, Field


class SShift(BaseModel):
    pk: int
    shift_id: int
    available: bool
    start_time: time
    end_time: time


class SMaintenance(BaseModel):
    pk: int
    date: date
    shift_id: int
    duration_hours: int
    reason: str


class SEquipment(BaseModel):
    pk: int
    equipment_id: str
    name: str
    type: str
    quantity: int
    max_parts_per_shift: int
    efficiency_factor: Decimal = Field(decimal_places=2)
    shifts_availability: list[SShift]
    maintenance_schedule: list[SMaintenance]


class SListEquipment(BaseModel):
    equipment: list[SEquipment]
    

class SLoadEquipment(BaseModel):
    equipment_id: str
    name: str
    type: str
    quantity: int
    max_parts_per_shift: int
    efficiency_factor: Decimal = Field(decimal_places=2)


class SListLoadEquipment(BaseModel):
    equipments: list[SListEquipment]
