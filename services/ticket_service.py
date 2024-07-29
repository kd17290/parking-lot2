from abc import ABC, abstractmethod

from factory.vehicle_factory import VehicleFactory
from models.parking import ParkingGate, ParkingSpot, ParkingSpotStatus
from models.ticket import Ticket
from models.vehicle import Vehicle
from repositories.gate_repository import ParkingGateRepository
from repositories.gate_spot import ParkingSpotRepository
from repositories.ticket_repository import TicketRepository
from repositories.vehicle_repository import VehicleRepository
from strategies.parking_spot_assignment_strategy import ParkingSpotAssignmentStrategy


class TicketService(ABC):
    @abstractmethod
    def generate_ticket(self, gate_id: int, vehicle_type: str, licence_number: str):
        ...


class TicketServiceImpl(TicketService):
    def __init__(self, parking_spot_assignment_strategy: ParkingSpotAssignmentStrategy):
        self.gate_repository = ParkingGateRepository()
        self.vehicle_repository = VehicleRepository()
        self.parking_spot_repository = ParkingSpotRepository()
        self.ticket_repository = TicketRepository()
        self.vehicle_factory = VehicleFactory()
        self.parking_spot_assignment_strategy = parking_spot_assignment_strategy

    def generate_ticket(self, gate_id: int, vehicle_type: str, licence_number: str):
        entry_gate: ParkingGate = self.gate_repository.get(gate_id)
        vehicle: Vehicle = self.vehicle_factory.get_vehicle(
            vehicle_type, licence_number
        )
        parking_spot: ParkingSpot | None = (
            self.parking_spot_assignment_strategy.get_spot(entry_gate, vehicle)
        )
        if not parking_spot:
            return "Parking Full"
        parking_spot.status = ParkingSpotStatus.OCCUPIED
        self.parking_spot_repository.update(parking_spot)
        self.vehicle_repository.create(vehicle)
        ticket = Ticket(
            parking_gate=entry_gate, parking_spot=parking_spot, vehicle=vehicle
        )
        self.ticket_repository.create(ticket)
        return ticket
