#!/usr/bin/python
from operator import ge
from redis import StrictRedis

hostname="localhost"
password="simsanmig"


r = StrictRedis(host=hostname,port=6379,password=password,db=0)
print(f"Logging to -> hostname:{hostname}, password:{password}\n")

def hmset_hvals_hkeys_hget():
    print("HMSET user:davita name 'davita' age 30")
    r.hmset("user-davita",{
        "name": "davita", 
        "age": 30
    })
    print("HVALS user:davita")
    val = r.hvals("user-davita")
    print(f'{val}')
    print("HKEYS user:davita")
    val2 = r.hkeys("user-davita")
    print(f'{val2}')
    print("HGET user:davita name")
    val1 = r.hget("user-davita","name")
    print(f'{val1}')

hmset_hvals_hkeys_hget()