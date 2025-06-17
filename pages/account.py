class Account:
    def __init__(self, balance=0.0):
        self.balance = balance

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def deposit(self, amount):
        self.balance += amount

