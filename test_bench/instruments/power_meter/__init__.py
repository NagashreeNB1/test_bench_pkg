from .keysight import KeysightPowerMeter
from .rohde_schwarz import RohdeSchwarzPowerMeter


def get_power_meter(resource, idn):
    if "KEYSIGHT" in idn.upper() or "AGILENT" in idn.upper():
        return KeysightPowerMeter(resource)
    elif "ROHDE" in idn.upper():
        return RohdeSchwarzPowerMeter(resource)
    else:
        raise ValueError(f"Unknown power meter manufacturer: {idn}")
