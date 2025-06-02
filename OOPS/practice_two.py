class Payment:

    def process_payment(self):
        raise NotImplemented
    
class CreditCardPaymment(Payment):

    def __init__(self,card_number):
        super().__init__()
        self.card_number = card_number

    def process_payment(self):
        return f"Payment processing with {self.card_number}"
    
class PayPalPayment(Payment):
    
    def __init__(self,email):
        super().__init__()
        self.email = email

    def process_payment(self):
        return f"Payment processing with {self.email}"
    

p1=CreditCardPaymment(123)
print(p1.process_payment())

p2 = PayPalPayment('abhi@gmail.com')
print(p2.process_payment())
