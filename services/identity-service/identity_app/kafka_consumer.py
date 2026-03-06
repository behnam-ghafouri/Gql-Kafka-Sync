from confluent_kafka import Consumer
import json

def run_consumer():
    conf = {
        'bootstrap.servers': 'kafka:9092',
        'group.id': 'identity-group',
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(conf)
    consumer.subscribe(['crm-events'])

    print("Listening for CRM events on 'crm-events' topic...")
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None: 
                continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue

            # Decode the message
            data = json.loads(msg.value().decode('utf-8'))
            
            # Use .get() or use the exact keys we saw: "event", "name", etc.
            event_name = data.get('event', 'UNKNOWN')
            deal_name = data.get('name', 'N/A')
            
            print(f"RECEIVED EVENT: {event_name} | Deal: {deal_name}")
            
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()