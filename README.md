# 🌿 AgroHub: AI-Driven Health Platform for Plants & Livestock

[![Live Demo](https://img.shields.io/badge/Live%20App-Open-green)](https://agrohub.onrender.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Build-Success-green)]()
[![Coverage](https://img.shields.io/badge/Test%20Coverage-100%25-brightgreen)]()

AgroHub is a full-stack AI web platform that diagnoses plant and animal health in real time using computer vision, sensor fusion, and predictive AI. Designed for modern agriculture, AgroHub offers rich UI, interactive dashboards, and actionable recommendations based on custom-trained models.

---

## 🔑 Features

- **🌱 Plant Analysis**: NDVI calculation, sensor scoring, disease classification.
- **🐄 Livestock Monitoring**: Body temperature, weight, and behavior assessment.
- **🧠 AI Integration**: Real-time feedback using trained ML classifiers.
- **📊 JSON API**: Flexible endpoints (`/analyze_plant/`, `/recommend/`).
- **🌗 Dark/Light Mode**: Dynamic theming and UI animations.
- **🖥️ Web Interface**: Modern Jinja2 frontend with async API and visual output.

---

## 🧬 Technologies Used

- **FastAPI** – backend API
- **OpenCV / NumPy** – image & sensor data processing
- **scikit-learn** – custom disease model
- **Jinja2** – server-side templating
- **HTML + JS** – dynamic frontend with theme toggle
- **Render.com** – deployment

---

## 🚀 Usage

### 1. Web Interface
Go to [Live Demo](https://agrohub.onrender.com)  
Enter plant image path and sensor data to get full diagnostics and recommendations.

### 2. API Endpoints

- **POST `/analyze_plant/`**
  ```json
  {
    "image_path": "images/plant.jpg",
    "temperature": 24,
    "humidity": 0.6,
    "soil_moisture": 0.4,
    "light": 14000
  }

