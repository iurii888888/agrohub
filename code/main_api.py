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

# Подключение статических файлов (CSS, изображения и т.п.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Вспомогательная функция для вывода погодного блока
async def get_weather_html() -> str:
    return """
    <div class="weather-block">
      🌡️ Temperature: 15°C<br>
      💧 Humidity: 78%<br>
      ☁️ Condition: Light Rain
    </div>
    """

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    weather_block = await get_weather_html()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "weather_block": weather_block
    })

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
