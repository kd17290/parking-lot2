from abc import ABC, abstractmethod
from datetime import datetime

from adapter.payment_adapter import PaymentAdapter
from factory.pricing_strategy_factory import PricingStrategyFactory
from models.parking import ParkingGate, ParkingSpotStatus
from models.ticket import Ticket, Invoice
from repositories.gate_repository import ParkingGateRepository
from repositories.gate_spot import ParkingSpotRepository
from repositories.invoice_repository import InvoiceRepository
from repositories.ticket_repository import TicketRepository
from strategies.pricing_strategy import PricingStrategy


class InvoiceService(ABC):
    @abstractmethod
    def checkout(self, ticket_id: int, gate_id: int):
        ...


class InvoiceServiceImpl(InvoiceService):
    def __init__(self, payment_adapter: PaymentAdapter):
        self.gate_repository = ParkingGateRepository()
        self.ticket_repository = TicketRepository()
        self.parking_spot_repository = ParkingSpotRepository()
        self.invoice_repository = InvoiceRepository()
        self.payment_adapter = payment_adapter
        self.pricing_strategy = PricingStrategyFactory.get_strategy()

    def checkout(self, ticket_id: int, gate_id: int):
        ticket: Ticket = self.ticket_repository.get(ticket_id)
        amount = self.pricing_strategy.calculate_price(
            ticket.entry_time, datetime.now(), ticket.vehicle
        )
        payment = self.payment_adapter.make_payment(ticket_id, amount)
        exit_gate: ParkingGate = self.gate_repository.get(gate_id)
        invoice = Invoice(
            parking_gate=exit_gate, ticket=ticket, payment=payment, amount=amount
        )
        self.invoice_repository.create(invoice)
        ticket.parking_spot.status = ParkingSpotStatus.FREE
        self.parking_spot_repository.update(ticket.parking_spot)
        return invoice
