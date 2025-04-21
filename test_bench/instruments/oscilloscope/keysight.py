from .base import BaseOscilloscope
import pyvisa
import numpy as np


class KeysightOscilloscope(BaseOscilloscope):
    def __init__(self, resource):
        super().__init__(resource)
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(resource)
        self.model = self.identify()

    def identify(self):
        try:
            return self.inst.query("*IDN?")
        except:
            return "Unknown Keysight"

    def set_channel(self, channel):
        self.inst.write(f":WAV:SOUR CHAN{channel}")
        self.inst.write(":WAV:FORM BYTE")
        self.inst.write(":WAV:MODE NORMAL")

    def get_waveform(self, channel):
        self.set_channel(channel)
        self.inst.write(":DIGitize")
        raw = self.inst.query_binary_values(
            ":WAV:DATA?", datatype='B', container=np.array)
        return raw
