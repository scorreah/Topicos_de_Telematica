#!/usr/bin/python
from operator import ge
from redis import StrictRedis

hostname="localhost"
password="simsanmig"


r = StrictRedis(host=hostname,port=6379,password=password,db=0)
print(f"Logging to -> hostname:{hostname}, password:{password}\n")

def ranges():
    print("ZRANGE visits 0 1")
    print(f'{r.zrange("visits", 0, 1)}')

    print("ZREVRANGE visits 0 -1 WITHSCORES")
    print(f'{r.zrevrange("visits", 0,-1, withscores=True)}')

    print("ZRANGEBYSCORE visits 9 9999")
    print(f'{r.zrangebyscore("visits", 9, 9999)}')

    print("ZRANGEBYSCORE visits -inf inf")
    print(f'{r.zrangebyscore("visits", float("-inf"), float("inf"))}')
    
    print("ZREVRANGEBYSCORE  visits inf -inf")
    print(f'{r.zrevrangebyscore("visits", float("inf"), float("-inf"))}')

ranges()