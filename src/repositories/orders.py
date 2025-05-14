from datetime import datetime

from sqlalchemy import insert, select
from sqlalchemy.orm import selectinload

from src.models.orders import Order, Part
from src.utils.repository import Repository


class PartRepository(Repository):
    
    model = Part

    async def create(self, data:dict):
        query = insert(Part).values(
            part_id=data.get("part_id"),
            quantity=data.get("quantity")
        ).returning(Part)
        result = (await self.session.execute(query)).scalar()
        return result


class OrderRepository(Repository):

    model = Order
    query_all = select(model).options(selectinload(model.parts))

    async def load(self, data: dict):
        order = Order(
            order_id=data.get("order_id"),
            customer=data.get("customer"),
            deadline=datetime.strptime(data.get("deadline"), r"%Y-%m-%dT%H:%M:%S"),
            priority=data.get("priority"),
            created_at=datetime.strptime(data.get("created_at"), r"%Y-%m-%dT%H:%M:%S")
        )

        parts = [
            await PartRepository(self.session).create(data=part)
            for part in data.get("parts")
        ]
        order.parts.extend(parts)

        return order