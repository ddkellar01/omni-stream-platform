import os
from fastapi import FastAPI, HTTPException, Request
import httpx

app = FastAPI(title="OmniStream API Gateway", version="1.0.0")

ORCHESTRATOR_URL = os.getenv("ORCHESTRATOR_URL", "http://promotion-orchestrator:8081")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "api-gateway"}

@app.post("/v1/promotions/publish")
async def proxy_promotion(request: Request):
    payload = await request.json()
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"{ORCHESTRATOR_URL}/publish", json=payload, timeout=10.0)
            return response.json()
        except httpx.RequestError as exc:
            raise HTTPException(status_code=503, detail=f"Promotion service unavailable: {exc}")
