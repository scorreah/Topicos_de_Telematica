#!/usr/bin/python
from operator import ge
from redis import StrictRedis

hostname="localhost"
password="simsanmig"


r = StrictRedis(host=hostname,port=6379,password=password,db=0)
print(f"Logging to -> hostname:{hostname}, password:{password}\n")

def list_example():
    print("RPUSH apolo:wishlist eafit intvir gog thm")
    print(f'{r.rpush("apolo:wishlist", "eafit", "intvir", "gog", "thm")}')

    print("LRANGE apolo:wishlist 0 -1")
    print(f'{r.lrange("apolo:wishlist", 0, -1)}')
    
    print("LREM apolo:wishlist 0 gog")
    print(f'{r.lrem("apolo:wishlist", 0, "thm")}')
    
    print("LPOP apolo:wishlist")
    print(f'{r.lpop("apolo:wishlist", 1)}')
    
    print("RPOPLPUSH apolo:wishlist apolo:visited")
    print(f'{r.rpoplpush("apolo:wishlist", "apolo:visited")}')

list_example()
