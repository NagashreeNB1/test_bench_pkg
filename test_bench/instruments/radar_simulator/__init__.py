
from .konrad import KonradRadarSimulator
from .rohde_schwarz import RohdeSchwarzRadarSimulator

def get_radar_simulator(resource, idn):
    if "KONRAD" in idn.upper():
        return KonradRadarSimulator(resource)
    elif "ROHDE" in idn.upper():
        return RohdeSchwarzRadarSimulator(resource)
    else:
        raise ValueError(f"Unknown radar simulator manufacturer for: {idn}")
