from .base import BaseSignalGenerator
import pyvisa


class RohdeSchwarzSignalGenerator(BaseSignalGenerator):
    def __init__(self, resource):
        super().__init__(resource)
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(resource)
        self.model = self._detect_model()

    def _detect_model(self):
        try:
            idn = self.inst.query("*IDN?")
            if "SMBV" in idn:
                return "SMBV100A"
            elif "SMU" in idn:
                return "SMU200A"
            else:
                return "GenericRohdeSchwarz"
        except:
            return "Unknown"

    def set_frequency(self, frequency_hz):
        self.inst.write(f"SOUR:FREQ {frequency_hz}")

    def set_power(self, power_dbm):
        self.inst.write(f"SOUR:POW {power_dbm}")

    def rf_on(self):
        self.inst.write("OUTP:STAT ON")

    def rf_off(self):
        self.inst.write("OUTP:STAT OFF")
