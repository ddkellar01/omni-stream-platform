import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Video Ingest Service")

class UploadRequest(BaseModel):
    filename: str
    content_type: str
    user_id: str

@app.post("/v1/upload/presign")
async def generate_presigned_url(req: UploadRequest):
    asset_id = str(uuid.uuid4())
    # Mocking cloud presigned URL generation (S3/GCS)
    upload_url = f"https://storage.googleapis.com/omnistream-bucket/{req.user_id}/{asset_id}/{req.filename}?signature=mocked_presigned_token"
    
    return {
        "asset_id": asset_id,
        "upload_url": upload_url,
        "method": "PUT",
        "headers": {"Content-Type": req.content_type}
    }
