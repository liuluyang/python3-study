
import asyncio
import threading
import time

def main():
    for i in range(1,5):
        time.sleep(0.2)
    return [1,2,3]


def fib_2(n):
    a,b = 0,1
    m = 0
    while m<n:
        a,b = b,a+b
        m+=1
        yield a

print (fib_2(10))

@asyncio.coroutine
def func_sleep():
    print ('sleep 1 seconde')
    #time.sleep(1)
    yield from asyncio.sleep(1)

@asyncio.coroutine
def hello():
    print ('hello word %s'%(threading.current_thread().name))
    r = yield from func_sleep()
    print ('hello end %s'%(threading.current_thread().name))

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()