from models.parking import ParkingGate
from repositories.in_memory import InMemoryRepository


class ParkingGateRepository(InMemoryRepository[ParkingGate]):
    pass
