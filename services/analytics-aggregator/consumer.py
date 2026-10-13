import json
import os
from kafka import KafkaConsumer

KAFKA_BROKERS = os.getenv("KAFKA_BROKERS", "kafka:9092")

def consume_metrics():
    consumer = KafkaConsumer(
        'analytics-events',
        bootstrap_servers=[KAFKA_BROKERS],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='analytics-aggregator-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    print("[*] Analytics Aggregator listening for engagement metrics...")
    for message in consumer:
        event = message.value
        print(f"[+] Received metric update from {event.get('platform')}: Views={event.get('views')}, Likes={event.get('likes')}")

if __name__ == "__main__":
    consume_metrics()
