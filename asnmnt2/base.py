from abc import ABC, abstractmethod

class base(ABC):

    def __init__(self,number):
        self.number = number

    @abstractmethod
    def run(self):
        return 0