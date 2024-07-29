from adapter.paypal_adapter import PaypalPaymentAdapter
from models.parking import (
    ParkingAttendant,
    ParkingLot,
    ParkingFloor,
    ParkingGate,
    ParkingGateType,
    ParkingSpot,
    ParkingSpotStatus,
    SmallParkingSpotType,
    MediumParkingSpotType,
)
from repositories.attendant_repository import ParkingAttendantRepository
from repositories.floor_repository import ParkingFloorRepository
from repositories.gate_repository import ParkingGateRepository
from repositories.gate_spot import ParkingSpotRepository
from repositories.parking_lot_repository import ParkingLotRepository
from services.invoice_service import InvoiceServiceImpl
from services.ticket_service import TicketServiceImpl
from strategies.first_come_basis_spot_assignment_strategy import (
    FirstComeBasisParkingSpotAssignmentStrategy,
)
from strategies.random_parking_spot_assignment_strategy import (
    RandomParkingSpotAssignmentStrategy,
)


def demo_parking_lot():
    attendant = ParkingAttendant(
        email="Email", first_name="parking attendant", last_name="last name"
    )
    ParkingAttendantRepository().create(attendant)
    parking_lot = ParkingLot(name="Parking Lor", address="address")
    ParkingLotRepository().create(parking_lot)
    parking_floor = ParkingFloor(parking_lot=parking_lot, floor=0)
    ParkingFloorRepository().create(parking_floor)
    entry_gate = ParkingGate(
        parking_lot=parking_lot,
        parking_floor=parking_floor,
        type=ParkingGateType.ENTRY,
        attendant=attendant,
    )
    ParkingGateRepository().create(entry_gate)
    exit_gate = ParkingGate(
        parking_lot=parking_lot,
        parking_floor=parking_floor,
        type=ParkingGateType.EXIT,
        attendant=attendant,
    )
    ParkingGateRepository().create(exit_gate)
    parking_spot = ParkingSpot(
        name="Parking Spot",
        parking_floor=parking_floor,
        parking_lot=parking_lot,
        status=ParkingSpotStatus.FREE,
        type=SmallParkingSpotType(),
    )
    ParkingSpotRepository().create(parking_spot)
    parking_spot = ParkingSpot(
        name="Parking Spot",
        parking_floor=parking_floor,
        parking_lot=parking_lot,
        status=ParkingSpotStatus.FREE,
        type=MediumParkingSpotType(),
    )
    ParkingSpotRepository().create(parking_spot)

    ticket1 = TicketServiceImpl(
        parking_spot_assignment_strategy=FirstComeBasisParkingSpotAssignmentStrategy()
    ).generate_ticket(
        gate_id=entry_gate.id, vehicle_type="bike", licence_number="1234567"
    )
    print(ticket1)
    ticket2 = TicketServiceImpl(
        parking_spot_assignment_strategy=RandomParkingSpotAssignmentStrategy()
    ).generate_ticket(
        gate_id=entry_gate.id, vehicle_type="car", licence_number="1234567"
    )
    print(ticket2)
    ticket3 = TicketServiceImpl(
        parking_spot_assignment_strategy=FirstComeBasisParkingSpotAssignmentStrategy()
    ).generate_ticket(
        gate_id=entry_gate.id, vehicle_type="bike", licence_number="1234567"
    )
    print(ticket3)
    ticket4 = TicketServiceImpl(
        parking_spot_assignment_strategy=RandomParkingSpotAssignmentStrategy()
    ).generate_ticket(
        gate_id=entry_gate.id, vehicle_type="car", licence_number="1234567"
    )
    print(ticket4)
    paypal_invoice_service = InvoiceServiceImpl(
        payment_adapter=PaypalPaymentAdapter(),
    )
    invoice1 = paypal_invoice_service.checkout(
        ticket1.id,
        exit_gate.id,
    )
    print(invoice1)
    invoice1 = paypal_invoice_service.checkout(
        ticket2.id,
        exit_gate.id,
    )
    print(invoice1)


if __name__ == "__main__":
    demo_parking_lot()
