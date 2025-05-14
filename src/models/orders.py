from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Table, Column, ForeignKey

from src.database import Base


association_table_order = Table(
    "association_table_order",
    Base.metadata,
    Column("part_pk", ForeignKey("part.pk")),
    Column("order_pk", ForeignKey("order.pk"))
)


class Part(Base):
    __tablename__ = "part"

    pk: Mapped[int] = mapped_column(primary_key=True)
    part_id: Mapped[str]
    quantity: Mapped[int]


class Order(Base):
    __tablename__ = "order"

    pk: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[str]
    customer: Mapped[str]
    parts: Mapped[list[Part]] = relationship(secondary=association_table_order)
    deadline: Mapped[datetime]
    priority: Mapped[int]
    created_at: Mapped[datetime]
