class Account:
    def __init__(self):
        self.balance = 10000
        print("Account balance is: ", self.balance)

    def deposit(self, amount):
        self.balance = amount + self.balance
        print("Account balance is: ", self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Account balance is: ", self.balance)


