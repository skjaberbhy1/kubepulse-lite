# KubePulse Lite

Lightweight Kubernetes Monitoring API built with FastAPI.

## Features

- Kubernetes node listing
- Pod monitoring
- Health endpoint
- Docker support
- Kubernetes deployment
- GitHub Actions CI

## Run Locally

```bash
pip install -r app/requirements.txt
uvicorn app.main:app --reload
```

## Docker

```bash
docker build -t kubepulse-lite .
docker run -p 8000:8000 kubepulse-lite
```

## Kubernetes Deploy

```bash
kubectl apply -f k8s/
```

## API Endpoints

| Endpoint | Description |
|---|---|
| / | Home |
| /health | Health Check |
| /nodes | Kubernetes Nodes |
| /pods | Kubernetes Pods |

## Access

http://NODE-IP:30090
