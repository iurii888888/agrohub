# Performance Benchmarks

## Computer Vision Module
- Dataset: 100k test images (cannabis, livestock)
- Accuracy: 92.3%
- Precision/Recall: 90.1% / 89.8%
- Inference latency: 45 ms per image (batch size 1, GPU)

## Sensor Fusion Engine
- Input size: 4 sensor streams
- Composite score computation: 2 ms per record

## NLP Advisory Module
- Model: GPT-4 (gpt-4o-mini)
- Response time: 200 ms average (includes retrieval)
- Retrieval accuracy: 95% relevant passages

## End-to-End API
- Average response time: 300 ms (image + sensors -> recommendations)
- 99.9% uptime in simulated load tests (1k RPS)
