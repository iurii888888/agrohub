from fastapi import FastAPI, File, UploadFile
from code.analysis import HealthAnalyzer
from code.recommendations import Recommender

app = FastAPI()
analyzer = HealthAnalyzer()
recommender = Recommender()

@app.post('/analyze_plant/')
async def analyze_plant(sensor_data: dict):
    report = analyzer.analyze_plant_health(sensor_data['image_path'], sensor_data)
    return report

@app.post('/recommend/')
async def get_recommendations(data: dict):
    return recommender.recommend_actions(
        data['image_path'],
        data['sensor_dict'],
        data['animal_metrics']
    )
