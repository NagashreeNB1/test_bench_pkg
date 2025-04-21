from .base import BaseSpectrumAnalyzer
import pyvisa
import numpy as np


class RohdeSchwarzSpectrumAnalyzer(BaseSpectrumAnalyzer):
    def __init__(self, resource):
        super().__init__(resource)
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(resource)
        self.model = self.identify()
        self.inst.write("FORM ASC")

    def identify(self):
        try:
            return self.inst.query("*IDN?")
        except:
            return "Unknown Rohde & Schwarz"

    def set_center_freq(self, frequency_hz):
        self.inst.write(f"FREQ:CENT {frequency_hz}")

    def set_span(self, span_hz):
        self.inst.write(f"FREQ:SPAN {span_hz}")

    def get_trace(self):
        self.inst.write("INIT;*WAI")
        trace_data = self.inst.query_ascii_values("TRAC? TRACE1")
        return np.array(trace_data)
