from Account import Account

class CurrentAccount(Account):
    def __init__(self):
        Account.__init__(self)

current = CurrentAccount()
current.withdraw(2000)
