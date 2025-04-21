
from .base import BaseRadarSimulator
import pyvisa

class RohdeSchwarzRadarSimulator(BaseRadarSimulator):
    def __init__(self, resource):
        super().__init__(resource)
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(resource)

    def configure_target(self, range_m, velocity_mps, rcs_dbsm):
        self.inst.write(f"SOUR:RAD:SCEN:TARG1:RANG {range_m}")
        self.inst.write(f"SOUR:RAD:SCEN:TARG1:VELO {velocity_mps}")
        self.inst.write(f"SOUR:RAD:SCEN:TARG1:RCS {rcs_dbsm}")

    def start_simulation(self):
        self.inst.write("SOUR:RAD:SIM:STAT ON")

    def stop_simulation(self):
        self.inst.write("SOUR:RAD:SIM:STAT OFF")
