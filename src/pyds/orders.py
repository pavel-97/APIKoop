from datetime import datetime

from pydantic import BaseModel


class SPart(BaseModel):
    part_id: str
    quantity: int


class SOrders(BaseModel):
    order_id: str
    customer: str
    parts: list[SPart]
    deadline: datetime
    priority: int
    created_at: datetime


class SListOrders(BaseModel):
    orders: list[SOrders]
    