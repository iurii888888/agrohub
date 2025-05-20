# System Architecture

```mermaid
graph LR
    subgraph Edge Layer
        A[Cameras & Sensors] -->|MQTT/HTTPS| B[Data Ingestion Service]
    end
    subgraph Ingestion & Preprocessing
        B --> C[Data Validation & Enrichment]
        C --> D[Preprocessing Pipeline]
    end
    subgraph AI Services
        D --> E[Computer Vision API]
        D --> F[Sensor Fusion Engine]
        E --> G[Prediction Orchestrator]
        F --> G
        G --> H[NLP Advisory Module]
    end
    subgraph Application Layer
        H --> I[Desktop Client (Electron + React)]
        H --> J[Web Dashboard (Next.js)]
    end
    subgraph Infrastructure
        B --> K[Message Broker (Kafka)]
        G --> L[Model Registry & Monitoring]
        I --> M[Local Cache & Offline Inference]
        J --> N[Authentication Service (OAuth2)]
    end
```

**Components & Technologies:**
- **Edge Layer:** Raspberry Pi / NVIDIA Jetson Nano with camera (multispectral & RGB) and sensors (DHT22, soil moisture, light). Communication via MQTT over TLS or HTTPS.
- **Data Ingestion Service:** Python microservice using FastAPI, validates incoming payloads, enriches metadata, and pushes to Kafka topics.
- **Preprocessing Pipeline:** Dockerized batch jobs in Kubernetes (K8s) for image normalization (OpenCV), time-series alignment, and data quality checks.
- **Computer Vision API:** PyTorch-based EfficientNet/Vision Transformer ensemble, served via TorchServe for real-time inference.
- **Sensor Fusion Engine:** Python service leveraging Pandas and Scikit-learn for feature scaling, composite score computation, and anomaly detection.
- **Prediction Orchestrator:** Coordinates CV and sensor results, applies business logic, and routes to NLP module.
- **NLP Advisory Module:** Fine-tuned GPT-4 model accessed via OpenAI API with retrieval-augmented generation (RAG) using a FAISS vector store for knowledge base lookups.
- **Desktop Client:** Built with Electron.js + React, supports offline inference using ONNX runtime and local storage for data caching.
- **Web Dashboard:** Next.js application with SSR/SSG, real-time websockets for live alerts, and user management.
- **Message Broker:** Apache Kafka for event streaming and decoupling microservices.
- **Model Registry & Monitoring:** MLflow for model versioning, Prometheus + Grafana for metrics and alerts.
- **Security & Authentication:** OAuth2 + JWT tokens, TLS encryption, role-based access controls (RBAC).
- **Offline Mode:** Local edge inference fallback ensures functionality when connectivity is lost, synchronizing queued events upon reconnection.

**Scalability & Reliability:**
- Microservices deployed in Kubernetes with auto-scaling.
- CI/CD pipeline with GitHub Actions: automated tests, linting, container builds, and blue-green deployments.
- High availability through multi-zone clusters and data replication.
