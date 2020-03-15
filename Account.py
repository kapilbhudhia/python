from Bank import Bank
from Customer import Customer
from abc import ABC, abstractmethod


class Account(Bank, ABC):
    AccountID = 1

    AccountRepository = {}

    def __init__(self, customer: Customer, balance, **bankArgs):
        self.customer = customer
        self.balance = balance
        self.ID = str(Account.AccountID)
        Account.AccountRepository[self.ID] = self
        Account.AccountID += 1
        super().__init__(**bankArgs)

    @abstractmethod
    def AccountInfo(self):
        bankInfo = super().BankInfo()
        accountInfo = """
            Account Details:
                Account ID : %s
                Customer Name : %s
                Balance : %s
                """ \
            % (self.ID, self.customer.name, self.balance)
        return bankInfo + "\n" + accountInfo

    @abstractmethod
    def Withdraw(self, amount):
        pass

    def Deposit(self, amount):
        self.balance += amount
        return self.balance

    def Balance(self):
        return self.balance

    @staticmethod
    def get(id):
        return Account.AccountRepository.get(id)
