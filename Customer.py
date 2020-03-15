
class Customer:
    ID = 1
    CustomerRepository = {}

    def __init__(self, name, address, contact):
        self.ID = str(Customer.ID)
        self.name = name
        self.address = address
        self.contactDetails = contact
        Customer.CustomerRepository[name] = self
        Customer.ID += 1

    @staticmethod
    def get(name):
        return Customer.CustomerRepository.get(name)
