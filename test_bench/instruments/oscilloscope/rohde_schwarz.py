from .base import BaseOscilloscope
import pyvisa
import numpy as np


class RohdeSchwarzOscilloscope(BaseOscilloscope):
    def __init__(self, resource):
        super().__init__(resource)
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(resource)
        self.model = self.identify()

    def identify(self):
        try:
            return self.inst.query("*IDN?")
        except:
            return "Unknown Rohde & Schwarz"

    def set_channel(self, channel):
        self.inst.write(f"CHAN{channel}:DISP ON")
        self.inst.write(f"DATA:SOURCE CH{channel}")
        self.inst.write("DATA:ENCdg RIBINARY")
        self.inst.write("DATA:WIDTH 1")

    def get_waveform(self, channel):
        self.set_channel(channel)
        self.inst.write("ACQ:STATE RUN; *WAI")
        self.inst.write("ACQ:STOPAFTER SEQ")
        raw = self.inst.query_binary_values(
            "CURVe?", datatype='B', container=np.array)
        return raw
