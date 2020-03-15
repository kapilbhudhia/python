from abc import ABC, abstractmethod
from typing import Optional


class Bank(ABC):

    def __init__(self, ifsc, name, branch, location):
        self.ifscCode = ifsc
        self.name = name
        self.branchName = branch
        self.location = location

    def BankInfo(self):
        return "Bank Details: \n\tIFSC Code = %s\n\tName = %s\n\tBranch = %s\n\tLoc=%s" \
            % (self.ifscCode, self.name, self.branchName, self.location)
