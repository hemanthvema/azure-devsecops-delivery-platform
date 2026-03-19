import os
from fastapi import FastAPI, Response, status

app = FastAPI(title="Ops Demo Service", version="0.1.0")

@app.get("/")
def root():
    return {"service": "ops-demo-service", "version": "0.1.0"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ready")
def ready(response: Response):
    ready_flag = os.getenv("READY", "false").lower() == "true"
    if not ready_flag:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "not-ready", "hint": "Set READY=true"}
    return {"status": "ready"}