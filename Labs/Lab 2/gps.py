#GPS
import time
import pika
import json
import config
import random

def build_payload(variable_3):
    # Creates a random gps coordinates
    lat = random.uniform(6.187, 6.217)
    lng = random.uniform(-75.400, -75.567)
    payload = {variable_3: {"value": 1, "context": {"lat": lat, "lng": lng}}}

    return payload

def main():
    payload = build_payload(config.VARIABLE_LABEL_3)
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(config.MOM_IP, config.MOM_PORT, '/',
    pika.PlainCredentials(config.MOM_USERNAME, config.MOM_PASSWD)))

    channel = connection.channel()

    
    channel.basic_publish(exchange='my_exchange', routing_key='test', body= json.dumps(payload) )

    print("Runnning Producer Application...")
    print(f" [x] Sent '{payload}'")
    connection.close()


if __name__ == '__main__':
    while(True):
        main()
        time.sleep(4)