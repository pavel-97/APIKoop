from decimal import Decimal

from pydantic import BaseModel, Field

from .equipments import SEquipment


class SMaterial(BaseModel):
    material_id: str
    quantity_per_unit: Decimal = Field(decimal_places=1)


class SMap(BaseModel):
    part_id: str
    name: str
    production_time_minutes: int
    compatible_equipment: list[SEquipment]
    setup_time_minutes: int
    material_requirements: list[SMaterial]
    description: str
    technical_requirements: str
    

class SListMap(BaseModel):
    technical_maps: list[SMap]
