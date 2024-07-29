from models.parking import ParkingGate, ParkingSpot, ParkingSpotStatus
from models.vehicle import Vehicle
from strategies.parking_spot_assignment_strategy import ParkingSpotAssignmentStrategy


class FirstComeBasisParkingSpotAssignmentStrategy(ParkingSpotAssignmentStrategy):
    def get_spot(self, entry_gate: ParkingGate, vehicle: Vehicle) -> ParkingSpot | None:
        for parking_spot in self.parking_spot_repository.all():
            if parking_spot.status == ParkingSpotStatus.FREE:
                if (
                    vehicle.get_parking_lot_type().get_size()
                    == parking_spot.type.get_size()
                ):
                    return parking_spot
