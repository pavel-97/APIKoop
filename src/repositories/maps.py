from sqlalchemy import insert, select
from sqlalchemy.orm import selectinload

from src.models.maps import Map, Material
from src.models.equipments import Equipment
from src.utils.repository import Repository

from .equipments import EquipmentRepository


class MaterialRepository(Repository):
    
    async def create(self, data: dict):
        query = insert(Material).values(
            material_id=data.get("material_id"),
            quantity_per_unit=data.get("quantity_per_unit")
        ).returning(Material)
        result = (await self.session.execute(query)).scalar()
        return result


class MapRepository(Repository):

    async def all(self):
        query = select(Map).options(
            selectinload(Map.compatible_equipment).options(
                selectinload(Equipment.shifts_availability),
                selectinload(Equipment.maintenance_schedule)
                ),
            selectinload(Map.material_requirements))
        result = (await self.session.execute(query)).scalars().all()
        return result

    async def load(self, data: dict):
        map = Map(
            part_id=data.get("part_id"),
            name=data.get("name"),
            production_time_minutes=data.get("production_time_minutes"),
            setup_time_minutes=data.get("setup_time_minutes"),
            description=data.get("description"),
            technical_requirements=data.get("technical_requirements")
        )

        equipments = [
            await EquipmentRepository(self.session).get(field=equipment_id)
            for equipment_id in data.get("compatible_equipment")
        ]
        map.compatible_equipment.extend(equipments)

        materials = [
            await MaterialRepository(self.session).create(data=material)
            for material in data.get("material_requirements")
        ]
        map.material_requirements.extend(materials)

        return map

