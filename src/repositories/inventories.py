from datetime import datetime

from sqlalchemy import insert, select

from src.models.inventories import Inventory
from src.utils.repository import Repository


class InventoryRepository(Repository):

    model = Inventory
    query_all = select(model)

    async def load(self, data: dict):
        query = insert(Inventory).values(
                part_id=data.get("part_id"),
                name=data.get("name"),
                current_quantity=data.get("current_quantity"),
                min_quantity=data.get("min_quantity"),
                optimal_quantity=data.get("optimal_quantity"),
                location=data.get("location"),
                last_updated=datetime.strptime(data.get("last_updated"), r"%Y-%m-%dT%H:%M:%S"),
                pending_in=data.get("pending_in"),
                reserved=data.get("reserved")
        ).returning(Inventory)
        result = (await self.session.execute(query)).scalar()
        return result
    