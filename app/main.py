from fastapi import FastAPI
from app.k8s_client import get_nodes, get_pods

app = FastAPI(
    title="KubePulse Lite",
    description="Lightweight Kubernetes Monitoring API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "KubePulse Lite Running"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }

@app.get("/nodes")
def nodes():
    return get_nodes()

@app.get("/pods")
def pods():
    return get_pods()
