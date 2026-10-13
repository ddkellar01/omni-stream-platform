import json
import os
from kafka import KafkaConsumer
import httpx

KAFKA_BROKERS = os.getenv("KAFKA_BROKERS", "kafka:9092")
FB_GRAPH_URL = "https://graph.facebook.com/v18.0"

def consume_facebook_queue():
    consumer = KafkaConsumer(
        'promo-facebook',
        bootstrap_servers=[KAFKA_BROKERS],
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    print("[*] Facebook Adapter online, listening for cross-promo events...")
    for message in consumer:
        event = message.value
        payload = event.get('payload', {})
        print(f"[+] Publishing video {payload.get('asset_id')} to Facebook Reels...")
        # Simulated Graph API call
        # httpx.post(f"{FB_GRAPH_URL}/me/videos", json={...})

if __name__ == "__main__":
    consume_facebook_queue()
