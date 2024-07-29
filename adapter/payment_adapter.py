from abc import ABC, abstractmethod


class PaymentAdapter(ABC):
    @abstractmethod
    def make_payment(self, ticket_id: int, amount: float):
        ...
