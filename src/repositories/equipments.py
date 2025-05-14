from datetime import datetime

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.models.equipments import Equipment, Shift, Maintenance
from src.utils.repository import Repository


class ShiftRepository:
    
    async def create(self, session: AsyncSession, data: dict):
        query = insert(Shift).values(
            shift_id=data.get("shift_id"),
            available=data.get("available"),
            start_time=datetime.strptime(data.get("start_time"), "%H:%M:%S").time(),
            end_time=datetime.strptime(data.get("end_time"), "%H:%M:%S").time()
        ).returning(Shift)
        result = (await session.execute(query)).scalar()
        return result


class MaintenanceRepository:
    
    async def create(self, session: AsyncSession, data: dict, shift: Shift):
        query = insert(Maintenance).values(
            shift_pk=shift.pk,
            shift_id=data.get("shift_id"),
            reason=data.get("reason"),
            duration_hours=data.get("duration_hours"),
            date=datetime.strptime(data.get("date"), r"%Y-%M-%d")
        ).returning(Maintenance)
        result = (await session.execute(query)).scalar()
        return result


class EquipmentRepository(Repository):
    
    model = Equipment
    field = "equipment_id"
    query_get = select(model)
    query_all = select(model).options(
        selectinload(model.shifts_availability),
        selectinload(model.maintenance_schedule)
    )

    async def load(self, data: dict):
        
        equipment = Equipment(
            equipment_id=data.get("equipment_id"),
            name=data.get("name"),
            type=data.get("type"),
            quantity=data.get("quantity"),
            max_parts_per_shift=data.get("max_parts_per_shift"),
            efficiency_factor=data.get("efficiency_factor")
        )
        
        shifts_availability = [
            await ShiftRepository().create(self.session, shift_availability)
            for shift_availability in data.get("shifts_availability")
              ]
        equipment.shifts_availability.extend(shifts_availability)

        shifts_maintenance = [
            await MaintenanceRepository().create(self.session, maintenance, availability) 
            for maintenance in data.get("maintenance_schedule") 
            for availability  in shifts_availability 
            if maintenance.get("shift_id") == availability.shift_id
        ]
        equipment.maintenance_schedule.extend(shifts_maintenance)            
        return equipment
    