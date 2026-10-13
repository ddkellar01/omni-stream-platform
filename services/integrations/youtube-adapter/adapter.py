import json
import os
from kafka import KafkaConsumer

KAFKA_BROKERS = os.getenv("KAFKA_BROKERS", "kafka:9092")

def consume_youtube_queue():
    consumer = KafkaConsumer(
        'promo-youtube',
        bootstrap_servers=[KAFKA_BROKERS],
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    print("[*] YouTube Shorts/Video Adapter online...")
    for message in consumer:
        event = message.value
        payload = event.get('payload', {})
        print(f"[+] Initiating YouTube resumable upload for asset: {payload.get('asset_id')}")

if __name__ == "__main__":
    consume_youtube_queue()
