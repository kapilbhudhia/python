
class Customer:
    CustomerID = 1
    CustomerRepository = {}

    def __init__(self, name, address, contact):
        self.ID = str(Customer.CustomerID)
        self.Name = name
        self.Address = address
        self.ContactDetails = contact
        Customer.CustomerRepository[name] = self
        Customer.CustomerID += 1

    @staticmethod
    def get(name):
        return Customer.CustomerRepository.get(name)
