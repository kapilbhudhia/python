from abc import ABC, abstractmethod
from typing import Optional


class Bank(ABC):

    def __init__(self, ifsc, name, branch, location):
        self.IFSCCode = ifsc
        self.Name = name
        self.BranchName = branch
        self.Location = location

    def BankInfo(self):
        return "Bank Details: \n\tIFSC Code = %s\n\tName = %s\n\tBranch = %s\n\tLoc=%s" \
            % (self.IFSCCode, self.Name, self.BranchName, self.Location)

    @abstractmethod
    def AccountInfo(self):
        pass
