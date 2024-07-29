from models.parking import ParkingGate
from models.vehicle import Vehicle
from repositories.in_memory import InMemoryRepository


class VehicleRepository(InMemoryRepository[Vehicle]):
    pass
