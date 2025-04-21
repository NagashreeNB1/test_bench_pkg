
from .keysight import KeysightPowerSupply
from .rohde_schwarz import RohdeSchwarzPowerSupply

def get_power_supply(resource, idn):
    if "KEYSIGHT" in idn.upper():
        return KeysightPowerSupply(resource)
    elif "Rohde" in idn:
        return RohdeSchwarzPowerSupply(resource)
    else:
        raise ValueError(f"Unknown power supply manufacturer for: {idn}")
