from models.parking import ParkingSpot
from repositories.in_memory import InMemoryRepository


class ParkingSpotRepository(InMemoryRepository[ParkingSpot]):
    pass
