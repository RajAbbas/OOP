from abc import ABC, abstractmethod

@abstractmethod
class Command(ABC):
    def execute(self,pen):
        pass