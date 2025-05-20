import pytest
from fastapi.testclient import TestClient
from code.main_api import app

client = TestClient(app)

def test_analyze_plant_success(tmp_path):
    payload = {
        "image_path": "images/ui_1.png",
        "temperature": 24.0,
        "humidity": 0.65,
        "soil_moisture": 0.5,
        "light": 15000.0
    }
    response = client.post("/analyze_plant/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "health_score" in data
    assert 0 <= data["health_score"] <= 1

def test_analyze_plant_missing_field():
    payload = {"temperature": 24.0}
    response = client.post("/analyze_plant/", json=payload)
    assert response.status_code == 422  # Unprocessable Entity

def test_recommend_success():
    payload = {
        "image_path": "images/ui_1.png",
        "sensor_dict": {"temperature":24.0,"humidity":0.65,"soil_moisture":0.5,"light":15000.0},
        "animal_metrics": {"weight":450,"body_temp":38.1,"activity_level":0.8}
    }
    response = client.post("/recommend/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "plant_recommendations" in data and isinstance(data["plant_recommendations"], list)
    assert "animal_recommendations" in data and isinstance(data["animal_recommendations"], list)

def test_recommend_missing_body():
    response = client.post("/recommend/", json={})
    assert response.status_code == 422
