from fastapi import FastAPI, HTTPException
from app.k8s_client import get_nodes, get_pods
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
    try:
        data = get_nodes()
        return {"count": len(data), "nodes": data}
    except Exception as e:
        logger.error(f"Nodes error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch nodes")


@app.get("/pods")
def pods():
    try:
        data = get_pods()
        return {"count": len(data), "pods": data}
    except Exception as e:
        logger.error(f"Pods error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch pods")
    