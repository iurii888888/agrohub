"""
Module: recommendations.py
Purpose: Generate detailed, context-aware recommendations for plant and livestock health
based on analysis outputs. Integrates with HealthAnalyzer for end-to-end advisory.
"""

import json
from typing import Dict, List, Any
from code.analysis import HealthAnalyzer

class Recommender:
    def __init__(self):
        self.analyzer = HealthAnalyzer()

    def generate_plant_recommendations(
        self, report: Dict[str, Any]
    ) -> List[str]:
        """Create plant care actions based on health report."""
        actions = []
        hs = report['health_score']
        if hs < 0.4:
            actions.append("Significant stress detected: adjust irrigation schedule and check soil pH.")
        elif hs < 0.7:
            actions.append("Moderate stress: monitor moisture and nutrient levels closely.")
        else:
            actions.append("Plant is healthy: maintain current regimen.")

        # Disease-specific advice
        for disease, prob in report['diseases'].items():
            if prob > 0.2:
                actions.append(f"Detected {disease} (probability {prob:.2f}): "
                               f"apply targeted treatment protocol.")

        # NDVI-based actions
        if report['ndvi'] < 0.3:
            actions.append("Low vegetation index: consider increasing lighting intensity by 10%.")
        return actions

    def generate_animal_recommendations(
        self, report: Dict[str, Any]
    ) -> List[str]:
        """Create livestock care actions based on health report."""
        actions = []
        hs = report['health_score']
        if hs < 0.5:
            actions.append("Animal shows low overall health: schedule veterinary checkup.")
        else:
            actions.append("Animal is within healthy parameters.")

        # Body temperature
        temp = report['body_temp']
        if temp > 39.0:
            actions.append("Elevated body temperature: monitor for fever and provide cooling.")
        # Weight management
        weight = report['weight']
        ideal = 500  # example ideal weight
        if weight < ideal * 0.9:
            actions.append("Underweight: increase feed protein content by 15%.")
        elif weight > ideal * 1.1:
            actions.append("Overweight: adjust diet to reduce caloric intake by 10%.")
        return actions

    def recommend_actions(
    self, plant_image: str, plant_sensors: Dict[str, float], animal_metrics: Dict[str, float]
) -> Dict[str, List[str]]:
    """Combined recommendations pipeline for both plants and animals."""
    try:
        plant_sensors = plant_sensors or {}
        animal_metrics = animal_metrics or {}

        plant_report = self.analyzer.analyze_plant_health(plant_image, plant_sensors)
        animal_report = self.analyzer.analyze_animal_health(animal_metrics)

        return {
            'plant_recommendations': self.generate_plant_recommendations(plant_report),
            'animal_recommendations': self.generate_animal_recommendations(animal_report)
        }

    except Exception as e:
        return {
            "error": f"Recommendation generation failed: {str(e)}"
        }


if __name__ == '__main__':
    rec = Recommender()
    actions = rec.recommend_actions(
        'images/plant.jpg',
        {'temperature': 24, 'humidity': 0.6, 'soil_moisture': 0.4, 'light': 14000},
        {'weight': 450, 'body_temp': 38.2, 'activity_level': 0.75}
    )
    print(json.dumps(actions, indent=2))
