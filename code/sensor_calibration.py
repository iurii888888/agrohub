"""
Module: sensor_calibration.py
Purpose: Derive calibration curves and apply calibration to raw sensor data streams.
"""
import numpy as np

class SensorCalibrator:
    def __init__(self, calibration_params):
        self.params = calibration_params

    def calibrate(self, raw_value, sensor_type):
        a, b = self.params.get(sensor_type, (1, 0))
        return a * raw_value + b

    def derive_curve(self, raw_readings, true_readings):
        coeffs = np.polyfit(raw_readings, true_readings, 1)
        return coeffs  # a, b
