import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2

app = FastAPI(title="Metadata Service")
DB_URI = os.getenv("DB_URI", "postgres://admin:password@postgres-db:5432/omnistream")

def get_db_connection():
    return psycopg2.connect(DB_URI)

class MetadataRecord(BaseModel):
    asset_id: str
    title: str
    description: str
    user_id: str

@app.post("/v1/metadata")
async def save_metadata(record: MetadataRecord):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO videos (asset_id, title, description, user_id) VALUES (%s, %s, %s, %s)",
            (record.asset_id, record.title, record.description, record.user_id)
        )
        conn.commit()
        cur.close()
        conn.close()
        return {"status": "success", "asset_id": record.asset_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
