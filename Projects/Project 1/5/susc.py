#!/usr/bin/python
from redis import StrictRedis


hostname="localhost"
password="simsanmig"

# Establish connection
r = StrictRedis(host=hostname,port=6379,password=password,db=0)
print(f"Logging to -> hostname:{hostname}, password:{password}\n")
print(f"SUBSCRIBER \n")

def suscriber():
    sub = r.pubsub() 
    sub.subscribe('weather') # pubsub() and subscribe() methods to notify Redis that this is a subscriber
    for message in sub.listen():
        if message is not None:
            content = message.get('data') # Print the data incoming
            print(content)

if __name__ == "__main__":
    while True:
        suscriber()