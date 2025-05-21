from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import Dict, Optional
from code.analysis import HealthAnalyzer
from code.recommendations import Recommender

app = FastAPI(
    title="AgroHub AI API",
    description="""
    This API provides advanced plant and livestock health analysis powered by AI and sensor fusion.  
    You can analyze sensor data, submit environmental metrics, and receive AI-based recommendations.
    """,
    version="1.0.0"
)

analyzer = HealthAnalyzer()
recommender = Recommender()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Custom Models
class PlantSensorData(BaseModel):
    image_path: str = Field(..., example="images/sample_leaf.jpg", description="Path to the image used for analysis")
    temperature: Optional[float] = Field(None, example=23.5, description="Ambient temperature in Celsius")
    humidity: Optional[float] = Field(None, example=78.0, description="Humidity percentage")
    soil_moisture: Optional[float] = Field(None, example=34.2, description="Soil moisture percentage")
    ndvi: Optional[float] = Field(None, example=0.85, description="NDVI index value")

class RecommendationRequest(BaseModel):
    image_path: Optional[str] = Field(None, example="images/sample_leaf.jpg")
    sensor_dict: Optional[Dict[str, float]] = Field(None, example={"pH": 6.5, "moisture": 32.1})
    animal_metrics: Optional[Dict[str, float]] = Field(None, example={"heart_rate": 88, "temperature": 39.1})

# Weather block
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

@app.post("/analyze_plant/", summary="Analyze Plant Health", response_description="Analysis results for plant health")
async def analyze_plant(sensor_data: PlantSensorData):
    """Accepts image and optional environmental metrics, returns AI plant health diagnostics."""
    if not sensor_data.image_path:
        return {"error": "Missing image_path"}
    return analyzer.analyze_plant_health(sensor_data.image_path, sensor_data.dict())

@app.post("/recommend/", summary="Get AI-Based Recommendations", response_description="Suggested actions based on input data")
async def get_recommendations(data: RecommendationRequest):
    """Receives various sensor or livestock metrics and suggests AI-driven improvements."""
    return recommender.recommend_actions(
        data.image_path or "",
        data.sensor_dict or {},
        data.animal_metrics or {}
    )

# UI Routes
@app.get("/dashboard.html", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/plant_health.html", response_class=HTMLResponse)
async def plant_health(request: Request):
    return templates.TemplateResponse("plant_health.html", {"request": request})

@app.get("/livestock_health.html", response_class=HTMLResponse)
async def livestock_health(request: Request):
    return templates.TemplateResponse("livestock_health.html", {"request": request})

@app.get("/alerts.html", response_class=HTMLResponse)
async def alerts(request: Request):
    return templates.TemplateResponse("alerts.html", {"request": request})

@app.get("/insights.html", response_class=HTMLResponse)
async def insights(request: Request):
    return templates.TemplateResponse("insights.html", {"request": request})

@app.get("/reports.html", response_class=HTMLResponse)
async def reports(request: Request):
    return templates.TemplateResponse("reports.html", {"request": request})

@app.get("/sitemap.html", response_class=HTMLResponse)
async def sitemap(request: Request):
    return templates.TemplateResponse("sitemap.html", {"request": request})

# Шаблонные страницы AgroHub
@app.get("/dashboard.html", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/plant_health.html", response_class=HTMLResponse)
async def plant_health(request: Request):
    return templates.TemplateResponse("plant_health.html", {"request": request})

@app.get("/livestock_health.html", response_class=HTMLResponse)
async def livestock_health(request: Request):
    return templates.TemplateResponse("livestock_health.html", {"request": request})

@app.get("/alerts.html", response_class=HTMLResponse)
async def alerts(request: Request):
    return templates.TemplateResponse("alerts.html", {"request": request})

@app.get("/insights.html", response_class=HTMLResponse)
async def insights(request: Request):
    return templates.TemplateResponse("insights.html", {"request": request})

@app.get("/reports.html", response_class=HTMLResponse)
async def reports(request: Request):
    return templates.TemplateResponse("reports.html", {"request": request})