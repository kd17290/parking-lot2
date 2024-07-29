from dataclasses import dataclass, field
from datetime import datetime

from models.base_model import BaseModel
from models.parking import ParkingGate, ParkingSpot
from models.payment import Payment
from models.vehicle import Vehicle


@dataclass
class Ticket(BaseModel):
    parking_gate: ParkingGate
    parking_spot: ParkingSpot
    vehicle: Vehicle
    entry_time: datetime = field(default_factory=datetime.now)


@dataclass
class Invoice(BaseModel):
    parking_gate: ParkingGate
    ticket: Ticket
    payment: Payment
    amount: float
    exit_time: datetime = field(default_factory=datetime.now)
