from abc import ABC, abstractmethod


class BaseOscilloscope(ABC):
    def __init__(self, resource):
        self.resource = resource

    @abstractmethod
    def identify(self):
        pass

    @abstractmethod
    def set_channel(self, channel):
        pass

    @abstractmethod
    def get_waveform(self, channel):
        pass
