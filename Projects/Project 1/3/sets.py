#!/usr/bin/python
from operator import ge
from redis import StrictRedis

hostname="localhost"
password="simsanmig"


r = StrictRedis(host=hostname,port=6379,password=password,db=0)
print(f"Logging to -> hostname:{hostname}, password:{password}\n")

def setsExample():
    print("SADD news nytimes.com pragprog.com picso.com.co ")
    print(f'{r.sadd("news", "nytimes.com", "pragprog.com", "picso.com.co")}')

    print("SMEMBERS news")
    print(f'{r.smembers("news")}')
    
    print("SADD tech bbc.com pragprog.com epic.com.co ")
    print(f'{r.sadd("tech", "bbc.com", "pragprog.com", "epic.com.co")}')

    print("SMEMBERS news")
    print(f'{r.smembers("tech")}')

    print("SINTER news tech ")
    print(f'{r.sinter("news", "tech")}')

    print("SDIFF news tech ")
    print(f'{r.sdiff("news", "tech")}')

    print("SUNION news tech ")
    print(f'{r.sunion("news", "tech")}')
    

    print("SUNIONSTORE websites news tech ")
    print(f'{r.sunionstore("websites", "news", "tech")}')

    

setsExample()