from .keysight import KeysightSpectrumAnalyzer
from .rohde_schwarz import RohdeSchwarzSpectrumAnalyzer


def get_spectrum_analyzer(resource, idn):
    if "KEYSIGHT" in idn.upper() or "AGILENT" in idn.upper():
        return KeysightSpectrumAnalyzer(resource)
    elif "ROHDE" in idn.upper():
        return RohdeSchwarzSpectrumAnalyzer(resource)
    else:
        raise ValueError(f"Unknown spectrum analyzer manufacturer: {idn}")
