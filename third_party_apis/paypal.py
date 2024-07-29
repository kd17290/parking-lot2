import uuid


class PayPal:
    def make_transaction(self, amount):
        print(f"Transferring {amount} via paypal APIs")
        return uuid.uuid4().hex
