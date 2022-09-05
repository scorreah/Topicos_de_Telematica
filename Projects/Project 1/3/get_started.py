#!/usr/bin/python
from operator import ge
from redis import StrictRedis

hostname="localhost"
password="simsanmig"


r = StrictRedis(host=hostname,port=6379,password=password,db=0)
print(f"Logging to -> hostname:{hostname}, password:{password}\n")

def get_set_example():
    print("SET yt https://www.youtube.com/")
    print(f"{r.set('yt', 'https://www.youtube.com/')}")
    print("GET yt")
    print(f"{r.get('yt')}")

def mget_mset_example():
    print("MSET intvir https://interactivavirtual.eafit.edu.co/ thm https://tryhackme.com/ ")
    print(f"{r.mset({'intvir': 'https://interactivavirtual.eafit.edu.co/','thm': 'https://tryhackme.com/'})}")
    print("MGET intvir thm")
    print(f"{r.mget('intvir', 'thm')}")

def incr_example():
    print("INCR count")
    print(f"{r.incr('count')}")
    print("GET count")
    print(f"{r.get('count')}")


get_set_example()
mget_mset_example()
incr_example()    