#!/usr/bin/python
from cmath import exp
from redis import StrictRedis
from time import sleep

hostname="localhost"
password="simsanmig"


r = StrictRedis(host=hostname,port=6379,password=password,db=0)

def expiry_example():
    
    print("SET ice I m melting...")
    print(f'{r.set("ice", "I m melting...")}')
    
    print("EXPIRE ice 10")
    print(f'{r.expire("ice", 10)}')
    
    print("EXISTS ice")
    print(f'{r.exists("ice")}')

    sleep(10)
    
    print("EXISTS ice")
    print(f'{r.exists("ice")}')
    
    print("SETEX ice 10 I m melting...")
    print(f'{r.setex("ice", 10, "I m melting...")}')

    sleep(3)
    print("TTL ice")
    print(f'{r.ttl("ice")}')
    
    print("PERSIST ice")
    print(f'{r.persist("ice")}')

expiry_example()