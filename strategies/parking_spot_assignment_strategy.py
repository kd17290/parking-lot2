from abc import ABC, abstractmethod

from models.parking import ParkingSpot, ParkingGate
from models.vehicle import Vehicle
from repositories.gate_spot import ParkingSpotRepository


class ParkingSpotAssignmentStrategy(ABC):
    def __init__(self):
        self.parking_spot_repository = ParkingSpotRepository()

    @abstractmethod
    def get_spot(self, entry_gate: ParkingGate, vehicle: Vehicle) -> ParkingSpot | None:
        ...
