from Bank import Bank
from Customer import Customer


class Account(Bank):
    def __init__(self, customer, balance, **bankArgs):
        self.Customer = customer
        self.Balance = balance
        super.__init__(bankArgs)
