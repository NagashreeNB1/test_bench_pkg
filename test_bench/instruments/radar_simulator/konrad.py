
from .base import BaseRadarSimulator
import pyvisa

class KonradRadarSimulator(BaseRadarSimulator):
    def __init__(self, resource):
        super().__init__(resource)
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(resource)

    def configure_target(self, range_m, velocity_mps, rcs_dbsm):
        self.inst.write(f"CONF:TARG:RANGE {range_m}")
        self.inst.write(f"CONF:TARG:VEL {velocity_mps}")
        self.inst.write(f"CONF:TARG:RCS {rcs_dbsm}")

    def start_simulation(self):
        self.inst.write("SIM:START")

    def stop_simulation(self):
        self.inst.write("SIM:STOP")
