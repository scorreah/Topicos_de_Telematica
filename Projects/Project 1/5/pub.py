#!/usr/bin/python
from redis import StrictRedis
#Sensor temperatura y humedad
import time
import json
import config
import random

hostname="localhost"
password="simsanmig"

def build_payload(variable_1,variable_2):
    # Creates two random values for sending data
    value_1 = round(random.uniform(15, 27), 2) #Temperature
    value_2 = round(random.uniform(77, 83), 2)  #Humidity

    payload = {variable_1: value_1,
               variable_2: value_2,
            }
    return payload


def main():
    # Establish connection
    r = StrictRedis(host=hostname,port=6379,password=password,db=0) #Provides a Python interface to all Redis commands and an implmentation of the Redis protocol.
    print(f"Logging to -> hostname:{hostname}, password:{password}\n")
    print(f"PUBLISHER\n")
    while True:
        payload = build_payload(config.VARIABLE_LABEL_1, config.VARIABLE_LABEL_2) #Creates a json file with random variables
        message = json.dumps(payload)
        channel = "weather"
        print(f"Publishing data...\n")
        r.publish(channel, message)  #Publish the data to the channel "weather" where a subscriber receives it
        time.sleep(4)
    

if __name__ == "__main__":
    main()
        