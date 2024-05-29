from Account import Account

class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)

    def savingsWithdraw(self, amount):
        if (amount < 10000):
            super().withdraw(amount)
        else:
            print("you can not withdraw above your limit")


savings = SavingsAccount()
savings.savingsWithdraw(11000)