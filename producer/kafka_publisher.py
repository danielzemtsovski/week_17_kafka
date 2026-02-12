import json
import time
from confluent_kafka import Producer
from mongo_connection import file_data

producer_config = {"bootstrap.servers": "localhost:9092"}

producer = Producer(producer_config)

def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode("utf-8")}")
        print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")

i = 0
while i < len(file_data):
    batch = file_data[i:i+50]
    for one_file in batch:
        value = json.dumps(one_file, default=str).encode("utf-8")
        producer.produce(
            topic="week_17_topic",
            value=value,
            callback=delivery_report)
        time.sleep(0.5)
    producer.flush()
    i += 50

