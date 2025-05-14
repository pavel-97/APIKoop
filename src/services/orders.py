from src.repositories.orders import OrderRepository

from src.utils.services import Service
from src.repositories.orders import OrderRepository


class OrderService(Service):

    repository = OrderRepository
    model_name = "orders"
    