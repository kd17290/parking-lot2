from models.parking import ParkingGate, ParkingFloor, ParkingLot
from repositories.in_memory import InMemoryRepository


class ParkingLotRepository(InMemoryRepository[ParkingLot]):
    pass
