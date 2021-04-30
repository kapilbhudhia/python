from Customer import Customer
from SavingsAccount import SavingsAccount
from Account import Account


class BankingConsole:
    def help(self) -> bool:
        print("""
            The new banking console provides the following functionalities
            Choose one of the following commands
                new account : Creates a new account
                new customer: Creates a new customer
                account info: Print the account information
                withraw:      Withdraw money from an account
                deposit:      Deposits money in an account
                balance:      Provides balance information
                exit:         Quits the banking console, so does (stop and quit also)
                help:         Prints this help options
            """)
        return True

    def createNewAccount(self):
        print("\nProvide details to create a new account\n")
        customerName = input("Enter existing Customer name: ")

        customer = Customer.get(customerName)

        if customer is not None:
            bankName = input("Enter Bank name: ")
            branch = input("Enter Branch name: ")
            ifscCode = input("Enter Branch IFSC code: ")
            location = input("Enter Branch location: ")
            accountBalance = input("Enter Account starting balance: ")
            account = SavingsAccount(minimumBalance=500, customer=customer, balance=float(accountBalance),
                                     ifsc=ifscCode, name=bankName, branch=branch, location=location)
            print("Created new Account with ID: %s\n" % account.ID)
        else:
            print(
                "\nCan not find customer with the provided name, check the spelling and try again\n")

        return True

    def createNewCustomer(self):
        print("Provide Customer details\n")
        name = input("Enter Customer name: ")
        address = input("Enter Customer address: ")
        contact = input("Enter Customer phone number: ")
        customer = Customer(
            name, address, contact)
        print("Created new Customer with name: %s\n" % customer.Name)

        return True

    def askAccountInfoAndGetAccount(self):
        accountID = input("Provide Account ID: ")
        account = Account.get(accountID)
        if account is None:
            print(
                "Invalid Account ID: %s, try again with a valid Account ID\n" % accountID)
        return account

    def withdraw(self):
        account = self.askAccountInfoAndGetAccount()
        if account is not None:
            debitAmount = input(
                "Enter the amount to be debited from the account: ")
            try:
                newBalance = account.Withdraw(float(debitAmount))
            except:
                print("Not enough balance\n")
            else:
                print("The new Balance is: %s\n" % newBalance)

        return True

    def printAccountInfo(self):
        account = self.askAccountInfoAndGetAccount()
        if account is not None:
            print(account.AccountInfo())
        return True

    def deposit(self):
        account = self.askAccountInfoAndGetAccount()
        if account is not None:
            creditAmount = input(
                "Enter the amount to be credited to the account: ")
            newBalance = account.Deposit(float(creditAmount))
            print("The new Balance is: %s\n" % newBalance)

        return True

    def getBalance(self):
        account = self.askAccountInfoAndGetAccount()
        if account is not None:
            print("Account Balance is: %s\n" % str(account.getBalance()))

        return True

    def wrongChoice(self):
        print("Could not understand your wish, check spelling and please try again\n")
        return True

    def stop(self):
        print("Wish you had a great banking experience, come again later\n")
        return False

    choices = {
        "help": help,
        "new account": createNewAccount,
        "new customer": createNewCustomer,
        "account info": printAccountInfo,
        "deposit": deposit,
        "withdraw": withdraw,
        "balance": getBalance,
        "exit": stop,
        "stop": stop,
        "quit": stop
    }

    def __init__(self, consoleString=">>> :"):
        self.consoleString = consoleString

    def Run(self):
        self.help()
        continueExecution = True
        while (continueExecution):

            choice = input("\n%s" % self.consoleString)

            chosenFunction = BankingConsole.choices.get(
                choice, BankingConsole.wrongChoice)

            continueExecution = chosenFunction(self)


bankingConsole = BankingConsole("$$$: ")
bankingConsole.Run()
