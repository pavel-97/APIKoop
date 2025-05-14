from src.repositories.maps import MapRepository
from src.utils.services import Service


class MapService(Service):

    repository = MapRepository
    model_name = "technical_maps"
