from abc import ABC, abstractmethod

class Schema(ABC):
    @abstractmethod
    def info(self):
        print("This should print all the info.")