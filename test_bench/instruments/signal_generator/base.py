from abc import ABC, abstractmethod


class BaseSignalGenerator(ABC):
    def __init__(self, resource):
        self.resource = resource

    @abstractmethod
    def set_frequency(self, frequency_hz):
        pass

    @abstractmethod
    def set_power(self, power_dbm):
        pass

    @abstractmethod
    def rf_on(self):
        pass

    @abstractmethod
    def rf_off(self):
        pass
