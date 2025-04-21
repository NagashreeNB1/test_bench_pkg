
from abc import ABC, abstractmethod

class BasePowerSupply(ABC):
    def __init__(self, resource):
        self.resource = resource

    @abstractmethod
    def set_voltage(self, channel, voltage):
        pass

    @abstractmethod
    def output_on(self, channel):
        pass
