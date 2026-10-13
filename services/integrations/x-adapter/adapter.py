import json
import os
from kafka import KafkaConsumer

KAFKA_BROKERS = os.getenv("KAFKA_BROKERS", "kafka:9092")

def consume_x_queue():
    consumer = KafkaConsumer(
        'promo-x',
        bootstrap_servers=[KAFKA_BROKERS],
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    print("[*] X (Twitter) Adapter online...")
    for message in consumer:
        event = message.value
        payload = event.get('payload', {})
        print(f"[+] Posting tweet with media for job {event.get('job_id')}: {payload.get('caption')}")

if __name__ == "__main__":
    consume_x_queue()
