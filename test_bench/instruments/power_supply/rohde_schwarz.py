from .base import BasePowerSupply
import pyvisa


class RohdeSchwarzPowerSupply(BasePowerSupply):
    def __init__(self, resource):
        super().__init__(resource)
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(resource)
        self.model = self._detect_model()

    def _detect_model(self):
        try:
            idn = self.inst.query("*IDN?")
            if "HMP4040" in idn:
                return "HMP4040"
            elif "NGMO2" in idn:
                return "NGMO2"
            else:
                return "GenericRohdeSchwarz"
        except:
            return "Unknown"

    def set_voltage(self, channel, voltage):
        if self.model == "HMP4040":
            self.inst.write(f"INST:NSEL {channel}")
            self.inst.write(f"VOLT {voltage}")
        elif self.model == "NGMO2":
            self.inst.write(f"INST:SEL OUT{channel}")
            self.inst.write(f"SOUR:VOLT {voltage}")
        else:
            self.inst.write(f"VOLT {voltage}, (@{channel})")

    def output_on(self, channel):
        if self.model == "HMP4040":
            self.inst.write(f"INST:NSEL {channel}")
            self.inst.write("OUTP ON")
        elif self.model == "NGMO2":
            self.inst.write(f"INST:SEL OUT{channel}")
            self.inst.write("OUTP ON")
        else:
            self.inst.write(f"OUTP ON, (@{channel})")

    def output_off(self, channel):
        if self.model == "HMP4040":
            self.inst.write(f"INST:NSEL {channel}")
            self.inst.write("OUTP OFF")
        elif self.model == "NGMO2":
            self.inst.write(f"INST:SEL OUT{channel}")
            self.inst.write("OUTP OFF")
        else:
            self.inst.write(f"OUTP OFF, (@{channel})")

    def measure_voltage(self, channel):
        """Measure the voltage on the specified channel."""
        if self.model == "HMP4040":
            self.inst.write(f"INST:NSEL {channel}")
            return float(self.inst.query("MEAS:VOLT?"))
        elif self.model == "NGMO2":
            self.inst.write(f"INST:SEL OUT{channel}")
            return float(self.inst.query("MEAS:VOLT?"))
        else:
            return float(self.inst.query(f"MEAS:VOLT? (@{channel})"))

    def measure_current(self, channel):
        """Measure the current on the specified channel."""
        if self.model == "HMP4040":
            self.inst.write(f"INST:NSEL {channel}")
            return float(self.inst.query("MEAS:CURR?"))
        elif self.model == "NGMO2":
            self.inst.write(f"INST:SEL OUT{channel}")
            return float(self.inst.query("MEAS:CURR?"))
        else:
            return float(self.inst.query(f"MEAS:CURR? (@{channel})"))

    def set_current_limit(self, channel, current):
        """Set the current limit for the specified channel."""
        if self.model == "HMP4040":
            self.inst.write(f"INST:NSEL {channel}")
            self.inst.write(f"CURR {current}")
        elif self.model == "NGMO2":
            self.inst.write(f"INST:SEL OUT{channel}")
            self.inst.write(f"SOUR:CURR {current}")
        else:
            self.inst.write(f"CURR {current}, (@{channel})")

    def enable_overvoltage_protection(self, channel):
        """Enable overvoltage protection for the specified channel."""
        if self.model == "HMP4040":
            self.inst.write(f"INST:NSEL {channel}")
            self.inst.write("VOLT:PROT:STAT ON")
        elif self.model == "NGMO2":
            self.inst.write(f"INST:SEL OUT{channel}")
            self.inst.write("VOLT:PROT:STAT ON")
        else:
            self.inst.write(f"VOLT:PROT:STAT ON, (@{channel})")

    def disable_overvoltage_protection(self, channel):
        """Disable overvoltage protection for the specified channel."""
        if self.model == "HMP4040":
            self.inst.write(f"INST:NSEL {channel}")
            self.inst.write("VOLT:PROT:STAT OFF")
        elif self.model == "NGMO2":
            self.inst.write(f"INST:SEL OUT{channel}")
            self.inst.write("VOLT:PROT:STAT OFF")
        else:
            self.inst.write(f"VOLT:PROT:STAT OFF, (@{channel})")
