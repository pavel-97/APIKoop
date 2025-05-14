from datetime import datetime

from pydantic import BaseModel


class SInventory(BaseModel):
    pk: int
    part_id: str
    name: str
    current_quantity: int
    min_quantity: int
    optimal_quantity: int
    location: str
    last_updated: datetime
    pending_in: int
    reserved: int
    

class SListInventory(BaseModel):
    inventory: list[SInventory]
    