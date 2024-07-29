from models.parking import ParkingGate, ParkingFloor, ParkingAttendant
from repositories.in_memory import InMemoryRepository


class ParkingAttendantRepository(InMemoryRepository[ParkingAttendant]):
    pass
