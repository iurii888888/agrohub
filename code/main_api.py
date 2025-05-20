from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from code.analysis import HealthAnalyzer
from code.recommendations import Recommender

app = FastAPI()
analyzer = HealthAnalyzer()
recommender = Recommender()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>AgroHub AI API</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f8f8f8;
                    color: #333;
                    padding: 40px;
                }
                h1 {
                    color: #4caf50;
                }
                code {
                    background-color: #eee;
                    padding: 2px 4px;
                    border-radius: 4px;
                }
                a {
                    color: #2196f3;
                }
            </style>
        </head>
        <body>
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
    image_path = sensor_data.get('image_path')
    if not image_path:
        return {"error": "Missing image_path"}
    report = analyzer.analyze_plant_health(image_path, sensor_data)
    return report


@app.post("/recommend/")
async def get_recommendations(data: dict):
    return recommender.recommend_actions(
        data.get('image_path'),
        data.get('sensor_dict', {}),
        data.get('animal_metrics', {})
    )

