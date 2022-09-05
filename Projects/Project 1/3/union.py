#!/usr/bin/python
from operator import ge
from redis import StrictRedis

hostname="localhost"
password="simsanmig"


r = StrictRedis(host=hostname,port=6379,password=password,db=0)

def union():
    print("ZADD votes 2 7wks 0 gog 9001 prag")
    print(f'{r.zadd("votes", {"7wks":2, "gog":0, "prag":9001})}')
    

    print("ZUNIONSTORE imp 2 visits votes WEIGHTS 1 2 AGGREGATE SUM")
    print(f'{r.zunionstore("imp",["votes","visits"],aggregate="SUM")}')
    
    print("ZRANGEBYSCORE imp -inf inf WITHSCORES")
    print(f'{r.zrangebyscore("imp", float("-inf"), float("inf"), withscores=True)}')
    
    # print(f'{r.zunionstore("votes", ["votes"], )}')

union()