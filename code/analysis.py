"""
Module: analysis.py
Purpose: Advanced health analysis for plants and livestock integrating computer vision,
sensor fusion, and pre-trained models for disease classification.

This module defines the HealthAnalyzer class that:
- Loads a pre-trained disease classification model.
- Computes vegetation indices (NDVI) from multispectral images.
- Performs sensor data normalization and composite scoring.
- Analyzes plant and animal health metrics.
- Provides detailed diagnostic output for downstream recommendations.

Usage:
    analyzer = HealthAnalyzer(model_path='models/disease_classifier.pkl')
    plant_metrics = analyzer.analyze_plant_health('images/plant.jpg', {
        'temperature': 23.5, 'humidity': 0.65, 'soil_moisture': 0.4, 'light': 12000
    })
    animal_metrics = analyzer.analyze_animal_health({
        'weight': 450, 'body_temp': 38.2, 'activity_level': 0.8
    })
"""

import os
import cv2
import numpy as np
import logging
import json
from typing import Dict, Any
from sklearn.preprocessing import MinMaxScaler
from sklearn.externals import joblib

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HealthAnalyzer:
    def __init__(self, model_path: str = 'models/disease_classifier.pkl'):
        if os.path.exists(model_path):
            self.disease_model = joblib.load(model_path)
            logger.info(f'Loaded disease model from {model_path}')
        else:
            self.disease_model = None
            logger.warning('Disease classification model not found; classification disabled')
        self.scaler = MinMaxScaler()

    def compute_ndvi(self, image_path: str) -> float:
        """Compute NDVI (Normalized Difference Vegetation Index) from multispectral image."""
        img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        # Assume channels: [NIR, R, G, B]
        nir = img[:, :, 0].astype(np.float32)
        red = img[:, :, 1].astype(np.float32)
        ndvi = (nir - red) / (nir + red + 1e-6)
        ndvi_mean = float(np.nanmean(ndvi))
        logger.debug(f'NDVI mean: {ndvi_mean:.3f}')
        return float(np.clip(ndvi_mean, -1.0, 1.0))

    def classify_disease(self, image_path: str) -> Dict[str, float]:
        """Predict disease probabilities using a pre-trained classifier."""
        if self.disease_model is None:
            return {}
        img = cv2.imread(image_path)
        img_resized = cv2.resize(img, (224, 224))
        features = img_resized.flatten().reshape(1, -1)
        probs = self.disease_model.predict_proba(features)[0]
        labels = self.disease_model.classes_
        result = {label: float(prob) for label, prob in zip(labels, probs)}
        logger.debug(f'Disease classification: {result}')
        return result

    def compute_sensor_index(self, sensor_dict: Dict[str, float]) -> float:
        """Normalize sensors and compute a composite environmental health score."""
        keys = ['temperature', 'humidity', 'soil_moisture', 'light']
        values = np.array([sensor_dict.get(k, 0) for k in keys]).reshape(-1, 1)
        normalized = self.scaler.fit_transform(values).flatten()
        weights = np.array([0.25, 0.25, 0.25, 0.25])
        score = float(np.dot(normalized, weights))
        logger.debug(f'Sensor index: {score:.3f}')
        return score

    def analyze_plant_health(self, image_path: str, sensor_dict: Dict[str, float]) -> Dict[str, Any]:
        """Combine NDVI, sensor index, and disease classification into a report."""
        ndvi = self.compute_ndvi(image_path)
        sensor_score = self.compute_sensor_index(sensor_dict)
        disease_probs = self.classify_disease(image_path)
        health_score = 0.5 * sensor_score + 0.5 * max(ndvi, 0)
        report = {
            'ndvi': ndvi,
            'sensor_score': sensor_score,
            'health_score': float(np.clip(health_score, 0, 1)),
            'diseases': disease_probs
        }
        logger.info(f'Plant health report: {report}')
        return report

    def analyze_animal_health(self, metrics: Dict[str, float]) -> Dict[str, Any]:
        """Compute animal health index based on vitals and activity."""
        weight = metrics.get('weight', 0)
        temp = metrics.get('body_temp', 0)
        activity = metrics.get('activity_level', 0)
        # Normalize values
        norm = self.scaler.fit_transform(np.array([[weight, temp, activity]])).flatten()
        score = float(np.mean(norm))
        report = {
            'weight': weight,
            'body_temp': temp,
            'activity_level': activity,
            'health_score': float(np.clip(score, 0, 1))
        }
        logger.info(f'Animal health report: {report}')
        return report

if __name__ == '__main__':
    analyzer = HealthAnalyzer()
    plant_report = analyzer.analyze_plant_health('images/plant.jpg', {
        'temperature': 24, 'humidity': 0.7, 'soil_moisture': 0.5, 'light': 15000
    })
    print(json.dumps(plant_report, indent=2))
    animal_report = analyzer.analyze_animal_health({
        'weight': 450, 'body_temp': 38.1, 'activity_level': 0.8
    })
    print(json.dumps(animal_report, indent=2))
