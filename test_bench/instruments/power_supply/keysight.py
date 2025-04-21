from .base import BasePowerSupply
import pyvisa


class KeysightPowerSupply(BasePowerSupply):
    def __init__(self, resource):
        super().__init__(resource)
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(resource)
        self.model = self._detect_model()

    def _detect_model(self):
        try:
            idn = self.inst.query("*IDN?")
            if "E3631A" in idn:
                return "E3631A"
            elif "N6700B" in idn:
                return "N6700B"
            else:
                return "GenericKeysight"
        except:
            return "Unknown"

    def set_voltage(self, channel, voltage):
        if self.model == "E3631A":
            # E3631A doesn't support channel selection
            self.inst.write(f"VOLT {voltage}")
        elif self.model == "N6700B":
            # N6700B supports multiple channels
            self.inst.write(f"INST:NSEL {channel}")
            self.inst.write(f"VOLT {voltage}")
        else:
            # Generic fallback
            self.inst.write(f"VOLT {voltage}, (@{channel})")

    def output_on(self, channel):
        if self.model == "E3631A":
            self.inst.write("OUTP ON")
        elif self.model == "N6700B":
            self.inst.write(f"INST:NSEL {channel}")
            self.inst.write("OUTP ON")
        else:
            self.inst.write(f"OUTP ON, (@{channel})")

    def output_off(self, channel):
        if self.model == "E3631A":
            self.inst.write("OUTP OFF")
        elif self.model == "N6700B":
            self.inst.write(f"INST:NSEL {channel}")
            self.inst.write("OUTP OFF")
        else:
            self.inst.write(f"OUTP OFF, (@{channel})")

    def measure_voltage(self, channel):
        """Measure the voltage on the specified channel."""
        if self.model == "E3631A":
            # E3631A doesn't support channel selection
            return float(self.inst.query("MEAS:VOLT?"))
        elif self.model == "N6700B":
            self.inst.write(f"INST:NSEL {channel}")
            return float(self.inst.query("MEAS:VOLT?"))
        else:
            return float(self.inst.query(f"MEAS:VOLT? (@{channel})"))

    def measure_current(self, channel):
        """Measure the current on the specified channel."""
        if self.model == "E3631A":
            # E3631A doesn't support channel selection
            return float(self.inst.query("MEAS:CURR?"))
        elif self.model == "N6700B":
            self.inst.write(f"INST:NSEL {channel}")
            return float(self.inst.query("MEAS:CURR?"))
        else:
            return float(self.inst.query(f"MEAS:CURR? (@{channel})"))

    def set_current_limit(self, channel, current):
        """Set the current limit for the specified channel."""
        if self.model == "E3631A":
            # E3631A doesn't support channel selection
            self.inst.write(f"CURR {current}")
        elif self.model == "N6700B":
            self.inst.write(f"INST:NSEL {channel}")
            self.inst.write(f"CURR {current}")
        else:
            self.inst.write(f"CURR {current}, (@{channel})")

    def enable_overvoltage_protection(self, channel):
        """Enable overvoltage protection for the specified channel."""
        if self.model == "E3631A":
            # E3631A doesn't support channel selection
            self.inst.write("VOLT:PROT:STAT ON")
        elif self.model == "N6700B":
            self.inst.write(f"INST:NSEL {channel}")
            self.inst.write("VOLT:PROT:STAT ON")
        else:
            self.inst.write(f"VOLT:PROT:STAT ON, (@{channel})")

    def disable_overvoltage_protection(self, channel):
        """Disable overvoltage protection for the specified channel."""
        if self.model == "E3631A":
            # E3631A doesn't support channel selection
            self.inst.write("VOLT:PROT:STAT OFF")
        elif self.model == "N6700B":
            self.inst.write(f"INST:NSEL {channel}")
            self.inst.write("VOLT:PROT:STAT OFF")
        else:
            self.inst.write(f"VOLT:PROT:STAT OFF, (@{channel})")

    def reset(self):
        """Reset the power supply to its default state."""
        self.inst.write("*RST")

    def identify(self):
        """Query and return the identification string of the power supply."""
        return self.inst.query("*IDN?")
