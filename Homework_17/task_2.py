class Payment:
    def process_payment(self, amount):
        self.amount = amount
        print("Payment is being processed")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid with credit card: {amount} GEL")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid with PayPal: {amount} GEL")

Payer1 = CreditCardPayment()
Payer1.process_payment(500)

Payer2 = PayPalPayment()
Payer2.process_payment(300) 

