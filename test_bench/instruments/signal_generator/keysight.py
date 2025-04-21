from .base import BaseSignalGenerator
import pyvisa


class KeysightSignalGenerator(BaseSignalGenerator):
    def __init__(self, resource):
        super().__init__(resource)
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(resource)
        self.model = self._detect_model()

    def _detect_model(self):
        try:
            idn = self.inst.query("*IDN?")
            if "N5183B" in idn:
                return "N5183B"
            elif "E4438C" in idn:
                return "E4438C"
            else:
                return "GenericKeysight"
        except:
            return "Unknown"

    def set_frequency(self, frequency_hz):
        self.inst.write(f"FREQ {frequency_hz}")

    def set_power(self, power_dbm):
        self.inst.write(f"POW {power_dbm}")

    def rf_on(self):
        self.inst.write("OUTP ON")

    def rf_off(self):
        self.inst.write("OUTP OFF")
