from decimal import Decimal
from datetime import time, date

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DECIMAL, Table, Column, ForeignKey

from src.database import Base


association_table = Table(
    "association_table",
    Base.metadata,
    Column("shift_pk", ForeignKey("shift.pk")),
    Column("equipment_pk", ForeignKey("equipment.pk"))
)


association_table_maintenance = Table(
    "association_table_maintenance",
    Base.metadata,
    Column("maintenance_pk", ForeignKey("maintenance.pk")),
    Column("equipment_pk", ForeignKey("equipment.pk"))
)


class Shift(Base):
    __tablename__ = "shift"

    pk: Mapped[int] = mapped_column(primary_key=True)
    shift_id: Mapped[int]
    available: Mapped[bool]
    start_time: Mapped[time]
    end_time: Mapped[time]

    maintenance: Mapped["Maintenance"] = relationship(back_populates="shift")


class Maintenance(Base):
    __tablename__ = "maintenance"

    pk: Mapped[int] = mapped_column(primary_key=True)
    shift_pk: Mapped[int] = mapped_column(ForeignKey("shift.pk"))
    shift_id: Mapped[int]
    reason: Mapped[str]
    duration_hours: Mapped[int]
    date: Mapped[date]

    shift: Mapped[Shift] = relationship(back_populates="maintenance")


class Equipment(Base):
    __tablename__ = "equipment"

    pk: Mapped[int] = mapped_column(primary_key=True)
    equipment_id: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str]
    type: Mapped[str]
    quantity: Mapped[int]
    max_parts_per_shift: Mapped[int]
    efficiency_factor: Mapped[Decimal] = mapped_column(DECIMAL(precision=2))
    
    shifts_availability: Mapped[list[Shift]] = relationship(secondary=association_table)
    maintenance_schedule: Mapped[list[Maintenance]] = relationship(secondary=association_table_maintenance)
