class BankAccount:
    def __init__(self, owner:  str, balance: float = 0.00):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        else:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive!")

        elif amount > self.balance:
            raise ValueError("Balance is not enough!")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")



