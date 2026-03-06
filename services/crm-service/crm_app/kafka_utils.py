import json
from confluent_kafka import Producer
import os

def get_kafka_producer():
    conf = {'bootstrap.servers': os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092')}
    return Producer(conf)

def emit_deal_created(deal_id, name, value):
    producer = get_kafka_producer()
    data = {
        'event': 'DEAL_CREATED',
        'id': deal_id,
        'name': name,
        'value': str(value)
    }
    producer.produce('crm-events', json.dumps(data).encode('utf-8'))
    producer.flush()
    print(f"🚀 Kafka Event Emitted: {data}")