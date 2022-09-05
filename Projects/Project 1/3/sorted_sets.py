#!/usr/bin/python
from operator import ge
from redis import StrictRedis

hostname="localhost"
password="simsanmig"


r = StrictRedis(host=hostname,port=6379,password=password,db=0)
print(f"Logging to -> hostname:{hostname}, password:{password}\n")

def sorted_sets():
    print("ZADD visits 500 7wks 9 gog 9999 prag")
    print(f'{r.zadd("visits", {"7wks":500, "gog":9, "prag":9999})}')

    print("ZINCRBY visits 1 prag")
    print(f'{r.zincrby("visits", 1, "prag")}')

sorted_sets()