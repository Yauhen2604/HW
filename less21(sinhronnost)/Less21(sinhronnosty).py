import asyncio
import multiprocessing
import time
from aiohttp import ClientSession
from threading import Thread
import random

# async def async_func(task):
#     print(f'Start...{task}')
#     await asyncio.sleep(1)
#     print(f'...Finish{task}')
#
#
# async def head_func():
#     task_a = loop.create_task(async_func('task_a'))
#     task_b = loop.create_task(async_func('task_b'))
#     task_c = loop.create_task(async_func('task_c'))
#     await asyncio.wait([task_a, task_b, task_c])
#
#
# if __name__ == '__main__':
#     try:
#         loop = asyncio.get_event_loop()
#         loop.run_until_complete(head_func())
#     except:
#         pass


# async def fetch_url_data(session, url):
#     try:
#         async with session.get(url, timeout=60) as response:
#             res = await response.read()
#     except Exception as e:
#         print(e)
#     else:
#         return res
#     return
#
#
# async def fetch_async(loop, r):
#     url = 'https://www.uefa.com/uefachampionsleague/'
#     tasks = []
#     async with ClientSession() as session:
#         for i in range(r):
#             task = asyncio.ensure_future(fetch_url_data(session, url))
#             tasks.append(task)
#         resp = await asyncio.gather(*tasks)
#     return resp
#
#
# if __name__ == '__main__':
#     for count in [1, 10, 100, 1000]:
#         start_time = time.time()
#         loop = asyncio.get_event_loop()
#         future = asyncio.ensure_future(fetch_async(loop, count))
#         loop.run_until_complete(future)
#         responses = future.result()
#         print(f'we have {count} results on {time.time()-start_time} sek')


# def worker(num):
#     sleep = random.randrange(1, 10)
#     time.sleep(sleep)
#     print(f"i'm worker {num}, i was sleep {sleep} sek")
#
#
# for i in range(3):
#     tr = threading.Thread(target=worker, args=(i,))
#     tr.start()
#
# print('***finish***. If you see me, our do it dont mistakes')


# class My_Custom_Thread(Thread):
#     def __init__(self, num):
#         Thread.__init__(self)
#         self.num = num
#
#     def run(self):
#         for i in range(self.num):
#             print(f'stream My_Custom_Thread # {i}')
#             time.sleep(1)
#
#
# mct = My_Custom_Thread(3)
# mct.run()


# from threading import Thread, Lock
#
# lock = Lock()
# stop_thread = False
#
#
# def my_worker():
#     print('start my_worker()')
#     while True:
#         print('THREAD IS WORK')
#         lock.acquire()
#         if stop_thread is True:
#             break
#         lock.release()
#         time.sleep(1)
#     print('finish my_worker()')
#
#
# th = Thread(target=my_worker)
# th.start()
# time.sleep(2)
# lock.acquire()
# stop_thread = True
# lock.release()


from threading import Thread, Lock

# def my_func():
#     for i in range(3):
#         print(f'Hello from daughters thread{i}')
#         time.sleep(1)
#
#
# th = Thread(target=my_func)
# th.start()
# print('ALL STOP!!!')

# def my_func():
#     for i in range(3):
#         print(f'Hello from daughters thread{i}')
#         time.sleep(1)
#
#
# th = Thread(target=my_func, daemon=True)
# th.start()
# print('ALL STOP!!!')

from multiprocessing import Process


# def disp():
#     print('Hello, welcome to Py tutorial')
#     if __name__ == '__main__':
#         p = Process(target=disp)
#     p.start()
#     p.join()

def cube(n):
    print(f'cube = {n * n * n}')


def square(n):
    print(f'square = {n * n}')


if __name__ == '__main__':
    process_1 = multiprocessing.Process(target=cube, args=(2,))
    process_2 = multiprocessing.Process(target=square, args=(3,))

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()

    print('ALL FINISH')
