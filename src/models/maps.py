from decimal import Decimal

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DECIMAL, Table, Column, ForeignKey

from src.database import Base
from src.models.equipments import Equipment


association_table_material = Table(
    "association_table_material",
    Base.metadata,
    Column("material_pk", ForeignKey("material.pk")),
    Column("map_pk", ForeignKey("map.pk"))
)

association_table_equipment = Table(
    "association_table_equipment",
    Base.metadata,
    Column("equipment_pk", ForeignKey("equipment.pk")),
    Column("map_pk", ForeignKey("map.pk"))
)


class Material(Base):
    __tablename__ = "material"

    pk: Mapped[int] = mapped_column(primary_key=True)
    material_id: Mapped[str]
    quantity_per_unit: Mapped[Decimal] = mapped_column(DECIMAL(precision=2))


class Map(Base):
    __tablename__ = "map"

    pk: Mapped[int] = mapped_column(primary_key=True)
    part_id: Mapped[str]
    name: Mapped[str]
    production_time_minutes: Mapped[int]
    setup_time_minutes: Mapped[int]
    description: Mapped[str]
    technical_requirements: Mapped[str]
    material_requirements: Mapped[list[Material]] = relationship(secondary=association_table_material)
    compatible_equipment: Mapped[list[Equipment]] = relationship(secondary=association_table_equipment)
    
