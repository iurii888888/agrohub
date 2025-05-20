from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from code.analysis import HealthAnalyzer
from code.recommendations import Recommender

app = FastAPI()
analyzer = HealthAnalyzer()
recommender = Recommender()
templates = Jinja2Templates(directory="templates")

# Подключение папки со статикой (если появятся стили, изображения и т.п.)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze_plant/")
async def analyze_plant(sensor_data: dict):
    image_path = sensor_data.get('image_path')
    if not image_path:
        return {"error": "Missing image_path"}
    return analyzer.analyze_plant_health(image_path, sensor_data)

@app.post("/recommend/")
async def get_recommendations(data: dict):
    return recommender.recommend_actions(
        data.get("image_path", ""),
        data.get("sensor_dict", {}),
        data.get("animal_metrics", {})
    )
