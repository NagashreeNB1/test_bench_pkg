
from .base import BaseOscilloscope
import pyvisa

class TektronixOscilloscope(BaseOscilloscope):
    def __init__(self, resource):
        super().__init__(resource)
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(resource)

    def capture_waveform(self, channel):
        self.inst.write(f"DATA:SOURCE CH{channel}")
        return self.inst.query("CURVE?")
