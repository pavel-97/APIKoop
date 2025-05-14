from src.repositories.equipments import EquipmentRepository
from src.utils.services import Service


class EquipmentService(Service):

    repository = EquipmentRepository
    model_name = repository.model.__name__.lower()
