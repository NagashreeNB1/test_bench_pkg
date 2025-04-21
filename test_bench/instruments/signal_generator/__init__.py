from .keysight import KeysightSignalGenerator
from .rohde_schwarz import RohdeSchwarzSignalGenerator


def get_signal_generator(resource, idn):
    if "KEYSIGHT" in idn.upper() or "AGILENT" in idn.upper():
        return KeysightSignalGenerator(resource)
    elif "ROHDE" in idn.upper():
        return RohdeSchwarzSignalGenerator(resource)
    else:
        raise ValueError(f"Unknown signal generator manufacturer: {idn}")
