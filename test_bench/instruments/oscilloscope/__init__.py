from .keysight import KeysightOscilloscope
from .rohde_schwarz import RohdeSchwarzOscilloscope


def get_oscilloscope(resource, idn):
    if "KEYSIGHT" in idn.upper() or "AGILENT" in idn.upper():
        return KeysightOscilloscope(resource)
    elif "ROHDE" in idn.upper():
        return RohdeSchwarzOscilloscope(resource)
    else:
        raise ValueError(f"Unknown oscilloscope manufacturer: {idn}")
