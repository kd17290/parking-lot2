from adapter.payment_adapter import PaymentAdapter
from models.payment import Payment, PaymentStatus
from repositories.payment_repository import PaymentRepository
from third_party_apis.paypal import PayPal


class PaypalPaymentAdapter(PaymentAdapter):
    def __init__(self):
        self.paypal_api = PayPal()
        self.payment_repository = PaymentRepository()

    def make_payment(self, ticket_id: int, amount: float):
        payment = Payment(ticket_id=ticket_id, amount=amount)
        self.payment_repository.create(payment)
        paypal_txn_id = self.paypal_api.make_transaction(payment.amount)
        payment.third_party_txn_id = paypal_txn_id
        payment.status = PaymentStatus.SUCCEEDED
        self.payment_repository.update(payment)
        return payment
