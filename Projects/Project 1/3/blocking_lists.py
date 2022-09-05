# No Rights Reserved
# http://creativecommons.org/publicdomain/zero/1.0/

"""Simple message queue demo on Redis LPUSH / BRPOP for Python 3.3+ and asyncio.
See also "Pattern: Reliable queue" at http://redis.io/commands/rpoplpush to get
an idea for improvement.
"""
import asyncio
import aioredis #Libreria que provee interfaz de Redis para asincronicidad
import datetime
import random

hostname = "localhost"
password = "simsanmig"

loop = asyncio.get_event_loop() #Corre tareas y callbacks asincronos
redis_send = None
redis_recv = None
now = lambda: datetime.datetime.now().strftime("[%H:%M:%S.%f]") # %Y-%m-%d %H:%M:%S


@asyncio.coroutine
def connect():
    global redis_send, redis_recv
    redis_send = yield from aioredis.create_redis(
        ('localhost', 6379), loop=loop, db=10)
    redis_recv = yield from aioredis.create_redis(
        ('localhost', 6379), loop=loop, db=10)


@asyncio.coroutine
def sender():
    counter = 1
    while True:
        print(now(), 'send %s' % counter)
        redis_send.lpush('mylist', '%s' % counter)
        yield from asyncio.sleep(random.random() * 2.5)
        counter += 1


@asyncio.coroutine
def receiver():
    while True:
        val = yield from redis_recv.brpop('mylist', timeout=0)
        print(now(), 'recv %s' % val)


if __name__ == '__main__':
    loop.run_until_complete(connect())

    asyncio.async(receiver())
    loop.run_until_complete(sender())

    redis_send.close()
    redis_recv.close()