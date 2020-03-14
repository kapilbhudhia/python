from Account import Account


class SavingsAccount(Account):

    def __init__(self, minimumBalance, **accountArgs):
        self.MinimumBalance = minimumBalance
        super().__init__(**accountArgs)

    def AccountInfo(self):
        accountInfo = super().AccountInfo()
        savingsInfo = "\tMinimum Balance: %s" % (str(self.MinimumBalance))
        return accountInfo + "\n" + savingsInfo

    def Withdraw(self, amount):
        if self.Balance - amount <= self.MinimumBalance:
            raise "Not sufficient balance"
        else:
            self.Balance -= amount
            return self.Balance
