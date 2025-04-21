import pyvisa

# Import instrument factory functions
from test_bench.instruments.power_supply import get_power_supply
from test_bench.instruments.oscilloscope import get_oscilloscope
from test_bench.instruments.signal_generator import get_signal_generator
from test_bench.instruments.power_meter import get_power_meter
from test_bench.instruments.radar_simulator import get_radar_simulator
from test_bench.instruments.spectrum_analyzer import get_spectrum_analyzer


class TestBench:
    def __init__(self):
        # self.rm = pyvisa.ResourceManager()
        self.rm = pyvisa.ResourceManager('@sim')

        self.resources = self.rm.list_resources()

        # Dictionaries to store instrument objects
        self.power_supplies = {}
        self.oscilloscopes = {}
        self.signal_generators = {}
        self.power_meters = {}
        self.radar_simulators = {}
        self.spectrum_analyzers = {}

        self._detect_instruments()

    def _detect_instruments(self):
        for res in self.resources:
            try:
                inst = self.rm.open_resource(res)
                idn = inst.query("*IDN?")
                inst.close()
            except:
                continue

            # Power Supply
            try:
                ps = get_power_supply(res, idn)
                self.power_supplies[res] = ps
                continue
            except:
                pass

            # Oscilloscope
            try:
                scope = get_oscilloscope(res, idn)
                self.oscilloscopes[res] = scope
                continue
            except:
                pass

            # Signal Generator
            try:
                sg = get_signal_generator(res, idn)
                self.signal_generators[res] = sg
                continue
            except:
                pass

            # Power Meter
            try:
                pm = get_power_meter(res, idn)
                self.power_meters[res] = pm
                continue
            except:
                pass

            # Radar Simulator
            try:
                radar = get_radar_simulator(res, idn)
                self.radar_simulators[res] = radar
                continue
            except:
                pass

            # Spectrum Analyzer
            try:
                sa = get_spectrum_analyzer(res, idn)
                self.spectrum_analyzers[res] = sa
                continue
            except:
                pass

    def list_all(self):
        return {
            "power_supplies": list(self.power_supplies.keys()),
            "oscilloscopes": list(self.oscilloscopes.keys()),
            "signal_generators": list(self.signal_generators.keys()),
            "power_meters": list(self.power_meters.keys()),
            "radar_simulators": list(self.radar_simulators.keys()),
            "spectrum_analyzers": list(self.spectrum_analyzers.keys()),
        }
