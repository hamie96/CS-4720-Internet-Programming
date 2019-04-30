

class bank_account:

    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > 0 and amount < self.balance:
            self.balance -= amount

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def get_balannce(self):
        return self.balance


ba1 = bank_account(5)
print("ba1 balance", ba1.balance)
ba2 = bank_account()

ba1.deposit(300)
print("ba1 balance", ba1.balance)

ba1.george = 453
print("ba1.george", ba1.george)

