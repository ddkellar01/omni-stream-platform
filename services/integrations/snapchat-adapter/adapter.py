import json
import os
from kafka import KafkaConsumer

KAFKA_BROKERS = os.getenv("KAFKA_BROKERS", "kafka:9092")

def consume_snapchat_queue():
    consumer = KafkaConsumer(
        'promo-snapchat',
        bootstrap_servers=[KAFKA_BROKERS],
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    print("[*] Snapchat Adapter online...")
    for message in consumer:
        event = message.value
        payload = event.get('payload', {})
        print(f"[+] Publishing vertical asset to Snapchat Spotlight: {payload.get('asset_id')}")

if __name__ == "__main__":
    consume_snapchat_queue()
