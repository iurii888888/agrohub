from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from code.analysis import HealthAnalyzer
from code.recommendations import Recommender

app = FastAPI()
analyzer = HealthAnalyzer()
recommender = Recommender()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>AgroHub AI API</title>
        </head>
        <body style="font-family:Arial; background-color:#f8f8f8; padding:40px;">
            <h1>🌱 AgroHub API is Live!</h1>
            <p>Use the endpoints below:</p>
            <ul>
                <li><b>POST</b> <code>/analyze_plant/</code> — Analyze plant health</li>
                <li><b>POST</b> <code>/recommend/</code> — Get smart recommendations</li>
            </ul>
            <p>🔗 <a href="/docs">Try it via Swagger UI</a></p>
        </body>
    </html>
    """

@app.post("/analyze_plant/")
async def analyze_plant(sensor_data: dict):
    report = analyzer.analyze_plant_health(sensor_data['image_path'], sensor_data)
    return report

@app.post("/recommend/")
async def get_recommendations(data: dict):
    return recommender.recommend_actions(
        data['image_path'],
        data['sensor_dict'],
        data['animal_metrics']
    )
