class Accounts:

    def __init__(self,account_holder,balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def __str__(self):
        return f"this is the object defination function"

    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} is deposited now balance is {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Funds")
            return
        self.balance -= amount
        print(f"{amount} withdrawn now balance is {self.balance}")

a = Accounts('Abhishek',5)
print(a)
a.deposit(67)
a.deposit(55)
a.withdraw(10)
a.withdraw(1000)
print(a.balance)