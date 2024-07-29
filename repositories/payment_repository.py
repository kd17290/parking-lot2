from models.parking import ParkingGate, ParkingFloor, ParkingAttendant
from models.payment import Payment
from repositories.in_memory import InMemoryRepository


class PaymentRepository(InMemoryRepository[Payment]):
    pass
