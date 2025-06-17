from account import Account

class SavingsAccount(Account):
    def __init__(self,balance=0.0,withdrawal_limit=10000):
        super().__init__(balance)
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self,amount):
        if amount > self.withdrawal_limit:
            return False
        return super().withdraw(amount)

    def deposit(self, amount):
        self.balance= self.balance + amount
        pass
