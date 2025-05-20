# API Documentation

The FastAPI-based server exposes the following endpoints:

- **POST /analyze_plant/**  
  - **Request Body:**  
    ```json
    {
      "image_path": "path/to/image.jpg",
      "temperature": 24.0,
      "humidity": 0.65,
      "soil_moisture": 0.5,
      "light": 15000.0
    }
    ```
  - **Response:** JSON report with NDVI, sensor_score, health_score, diseases.

- **POST /recommend/**  
  - **Request Body:**
    ```json
    {
      "image_path": "path/to/image.jpg",
      "sensor_dict": {
        "temperature": 24.0,
        "humidity": 0.65,
        "soil_moisture": 0.5,
        "light": 15000.0
      },
      "animal_metrics": {
        "weight": 450,
        "body_temp": 38.1,
        "activity_level": 0.8
      }
    }
    ```
  - **Response:** JSON with `plant_recommendations` and `animal_recommendations`.

## Swagger UI
Interactive API docs are available at `/docs` when the server is running. Example:
```
uvicorn main_api:app --reload
open http://127.0.0.1:8000/docs
```
