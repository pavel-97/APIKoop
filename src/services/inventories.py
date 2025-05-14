from src.repositories.inventories import InventoryRepository
from src.utils.services import Service
from src.repositories.inventories import InventoryRepository


class InventoryService(Service):

    repository = InventoryRepository
    model_name = repository.model.__name__.lower()
