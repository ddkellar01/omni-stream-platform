import json
import os
from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer

app = FastAPI(title="Promotion Orchestrator")
KAFKA_BROKERS = os.getenv("KAFKA_BROKERS", "kafka:9092")

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKERS],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

class PublishPayload(BaseModel):
    asset_id: str
    platforms: list[str]
    caption: str
    video_url: str

@app.post("/publish")
async def schedule_promotion(payload: PublishPayload):
    job_id = f"job_{payload.asset_id}"
    for platform in payload.platforms:
        topic = f"promo-{platform.lower()}"
        producer.send(topic, {"job_id": job_id, "payload": payload.dict()})
    
    producer.flush()
    return {"status": "queued", "job_id": job_id, "platforms": payload.platforms}
