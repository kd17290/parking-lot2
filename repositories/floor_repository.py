from models.parking import ParkingGate, ParkingFloor
from repositories.in_memory import InMemoryRepository


class ParkingFloorRepository(InMemoryRepository[ParkingFloor]):
    pass
