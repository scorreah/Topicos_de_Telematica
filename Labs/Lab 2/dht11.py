#Sensor temperatura y humedad
import time
import pika
import json
import config
import random

def build_payload(variable_1,variable_2):
    # Creates two random values for sending data
    value_1 = round(random.uniform(15, 27), 2) #Temperature
    value_2 = round(random.uniform(77, 83), 2)  #Humidity

    payload = {variable_1: value_1,
               variable_2: value_2,
            }
    return payload

def main():
    payload = build_payload(config.VARIABLE_LABEL_1, config.VARIABLE_LABEL_2)
    
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