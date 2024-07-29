from models.ticket import Ticket, Invoice
from repositories.in_memory import InMemoryRepository


class InvoiceRepository(InMemoryRepository[Invoice]):
    pass
