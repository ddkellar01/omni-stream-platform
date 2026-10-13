import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

app = FastAPI(title="Streaming Service - ABR Manifest Router")
CDN_BASE_URL = os.getenv("CDN_BASE_URL", "https://cdn.omnistream.io/videos")

@app.get("/v1/stream/{asset_id}/manifest.m3u8")
async def get_master_manifest(asset_id: str):
    # Route client to optimal edge CDN master HLS playlist
    edge_url = f"{CDN_BASE_URL}/{asset_id}/master.m3u8"
    return RedirectResponse(url=edge_url, status_code=302)

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "streaming-service"}
