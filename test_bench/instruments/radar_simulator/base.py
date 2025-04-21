
from abc import ABC, abstractmethod

class BaseRadarSimulator(ABC):
    def __init__(self, resource):
        self.resource = resource

    @abstractmethod
    def configure_target(self, range_m, velocity_mps, rcs_dbsm):
        pass

    @abstractmethod
    def start_simulation(self):
        pass

    @abstractmethod
    def stop_simulation(self):
        pass
