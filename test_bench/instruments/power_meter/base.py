
from abc import ABC, abstractmethod

class BasePowerMeter(ABC):
    def __init__(self, resource):
        self.resource = resource

    @abstractmethod
    def read_power(self):
        pass
