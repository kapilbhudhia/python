from Account import Account


class SavingsAccount(Account):

    def __init__(self, minimumBalance, **accountArgs):
        self.minimumBalance = minimumBalance
        super().__init__(**accountArgs)
        if (self.balance < self.minimumBalance):
            raise "Savings account needs to be created with at least the minimum balance of %s" % self.minimumBalance

    def AccountInfo(self):
        accountInfo = super().AccountInfo()
        savingsInfo = """
                Minimum Balance: %s
        """ % (str(self.minimumBalance))
        return accountInfo + "\n" + savingsInfo

    def Withdraw(self, amount):
        if self.balance - amount <= self.minimumBalance:
            raise "Not sufficient balance"
        else:
            self.balance -= amount
            return self.balance
