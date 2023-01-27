import asyncio
import multiprocessing
import threading
import time

loop = asyncio.get_event_loop()


# @asyncio.coroutine
async def worker():
    print('start')
    # yield from asyncio.sleep(2)
    await asyncio.sleep(2)
    print('stop')
# def g_hello():
#     yield 'hello 1'
#     yield 'hello 2'
#     yield 'hello 3'

if __name__ == '__main__':
    loop.run_until_complete(asyncio.wait([worker(), worker()]))
    loop.close()


