from .base import BasePowerMeter
import pyvisa


class RohdeSchwarzPowerMeter(BasePowerMeter):
    def __init__(self, resource):
        super().__init__(resource)
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(resource)
        self.model = self._detect_model()

    def _detect_model(self):
        try:
            idn = self.inst.query("*IDN?")
            if "NRP2" in idn:
                return "NRP2"
            elif "NRX" in idn:
                return "NRX"
            else:
                return "GenericRohdeSchwarz"
        except:
            return "Unknown"

    def set_frequency(self, frequency_hz):
        self.inst.write(f"SENS:FREQ {frequency_hz}")

    def read_power_dbm(self):
        return float(self.inst.query("READ?"))

    def zero_sensor(self):
        """Perform a zeroing operation on the power meter sensor."""
        self.inst.write("SENS:ZERO:INIT")
        self.inst.query("*OPC?")  # Wait for the operation to complete

    def set_power_unit(self, unit):
        """Set the power measurement unit (e.g., 'DBM', 'W')."""
        valid_units = ["DBM", "W"]
        if unit.upper() not in valid_units:
            raise ValueError(f"Invalid unit. Choose from {valid_units}.")
        self.inst.write(f"UNIT:POW {unit.upper()}")

    def get_power_unit(self):
        """Get the current power measurement unit."""
        return self.inst.query("UNIT:POW?").strip()

    def enable_continuous_mode(self):
        """Enable continuous measurement mode."""
        self.inst.write("INIT:CONT ON")

    def disable_continuous_mode(self):
        """Disable continuous measurement mode."""
        self.inst.write("INIT:CONT OFF")

    def fetch_power_dbm(self):
        """Fetch the latest power measurement in dBm."""
        return float(self.inst.query("FETC?"))

    def reset(self):
        """Reset the power meter to its default state."""
        self.inst.write("*RST")

    def identify(self):
        """Query and return the identification string of the power meter."""
        return self.inst.query("*IDN?")

    def set_average_count(self, count):
        """Set the number of averages for power measurements."""
        if count < 1:
            raise ValueError("Average count must be at least 1.")
        self.inst.write(f"SENS:AVER:COUN {count}")

    def enable_averaging(self):
        """Enable averaging for power measurements."""
        self.inst.write("SENS:AVER:STAT ON")

    def disable_averaging(self):
        """Disable averaging for power measurements."""
        self.inst.write("SENS:AVER:STAT OFF")

    def get_measurement_state(self):
        """Check if the power meter is currently measuring."""
        return self.inst.query("STAT:OPER:COND?").strip()
