from models.ticket import Ticket
from repositories.in_memory import InMemoryRepository


class TicketRepository(InMemoryRepository[Ticket]):
    pass
