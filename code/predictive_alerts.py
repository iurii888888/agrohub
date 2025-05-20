"""
Module: predictive_alerts.py
Purpose: Generate alerts based on time-series anomalies in sensor and livestock data.
"""
import numpy as np

def detect_anomalies(data_series, threshold=3):
    mean = np.mean(data_series)
    std = np.std(data_series)
    return [i for i, v in enumerate(data_series) if abs(v - mean) > threshold * std]

def generate_alerts(sensor_data, animal_data):
    alerts = []
    plant_anoms = detect_anomalies(sensor_data)
    if plant_anoms:
        alerts.append(f"Plant sensor anomalies at indices: {plant_anoms}")
    if animal_data.get('activity_level', 1) < 0.2:
        alerts.append("Low animal activity detected")
    return alerts
