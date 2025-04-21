from abc import ABC, abstractmethod


class BaseSpectrumAnalyzer(ABC):
    def __init__(self, resource):
        self.resource = resource

    @abstractmethod
    def identify(self):
        pass

    @abstractmethod
    def set_center_freq(self, frequency_hz):
        pass

    @abstractmethod
    def set_span(self, span_hz):
        pass

    @abstractmethod
    def get_trace(self):
        pass
