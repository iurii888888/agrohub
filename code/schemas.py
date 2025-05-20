from pydantic import BaseModel
from typing import Dict, Any

class AnalyzePlantRequest(BaseModel):
    image_path: str
    sensor_data: Dict[str, float]

class RecommendRequest(BaseModel):
    image_path: str
    sensor_dict: Dict[str, float]
    animal_metrics: Dict[str, float]
