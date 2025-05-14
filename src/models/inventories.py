from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    pk: Mapped[int] = mapped_column(primary_key=True)
    part_id: Mapped[str]
    name: Mapped[str]
    current_quantity: Mapped[int]
    min_quantity: Mapped[int]
    optimal_quantity: Mapped[int]
    location: Mapped[str]
    last_updated: Mapped[datetime]
    pending_in: Mapped[int]
    reserved: Mapped[int]
