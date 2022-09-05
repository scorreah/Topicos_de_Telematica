#!/usr/bin/python
# MULTI - EXEC 
from operator import ge
from redis import StrictRedis

hostname="localhost"
password="simsanmig"


r = StrictRedis(host=hostname,port=6379,password=password,db=0)
print(f"Logging to -> hostname:{hostname}, password:{password}\n")

def multi_exec():
    print("MULTI")
    p = r.pipeline()    #In redis-py MULTI and EXEC can only be used through a Pipeline object.
    print("SET prag http://pragprog.com")
    print(f"{p.set('prag', 'http://pragprog.com')}")
    print("INCR count")
    print(f"{p.incr('count')}")
    print('EXEC')
    print(f"{p.execute()}")

multi_exec()