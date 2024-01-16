import time
import asyncio

# async def fun1(x):
#     print('...launch fun1')
#     print(f'x ** 2 ={x ** 2}')
#     print('fun1 sleep...')
#     await asyncio.sleep(3)
#     print('...fun1 wake up and end')
#
#
# async def fun2(x):
#     print('...launch fun2')
#     print(f'x ** 0.5 ={x ** 0.5}')
#     print('fun2 sleep...')
#     await asyncio.sleep(3)
#     print('...fun2 wake up and end')
#
#
# async def main():
#     t1 = asyncio.create_task(fun1(4))
#     t2 = asyncio.create_task(fun2(4))
#     await t1
#     await t2
#
#
# print(type(fun1))
# print(type(fun1(4)))
# print(time.strftime('%X'), 'program launch')
#
# asyncio.run(main())
#
# print(time.strftime('%X'), 'program end')
#
#
# async def func1(x):
#     print(x + 1)
#     time.sleep(2)
#     print('func1 end')
#
#
# async def func2(x):
#     print(x + 2)
#     await asyncio.sleep(2)
#     print('func2 end')
#
#
# async def func3(x):
#     print(x + 3)
#     await asyncio.sleep(2)
#     print('func3 end')
#
#
# async def func4(x):
#     print(x + 4)
#     await asyncio.sleep(2)  # slozhnuiy zadachu peredaem kotoraya zanimaet vremya
#     print('func4 end')
#
#
# async def func5(x):
#     print(x + 5)
#     await asyncio.sleep(2)  # sinhronnaya zadacha
#     print('func5 end')
#
#
# async def main():
#     task1 = asyncio.create_task(func1(0))  # peredayem metod v asyncyo
#     task2 = asyncio.create_task(func2(0))
#     task3 = asyncio.create_task(func3(0))
#     task4 = asyncio.create_task(func4(0))
#     task5 = asyncio.create_task(func5(0))
#
#     await task1
#     await task2
#     await task3
#     await task4
#     await task5
#
#
# print(time.strftime('%X'))
# asyncio.run(main())
# print(time.strftime('%X'))


# async def fun_1(x):
#     print(x ** 2)
#     await asyncio.sleep(3)
#     print('fun_1 ended')
#
#
# async def fun_2(x):
#     print(x ** 0.5)
#     await asyncio.sleep(3)
#     print('fun_2 ended')
#
#
# print(time.strftime('%X'))
#
# loop = asyncio.get_event_loop()
# task1 = loop.create_task(fun_1(4))
# task2 = loop.create_task(fun_2(4))
# loop.run_until_complete(asyncio.wait([task1, task2]))
#
# print(time.strftime('%X'))


# async def func_1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print('func_1 ended')


# async def func_2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print('func_2 ended')
#
#
# async def main():
#     task1 = asyncio.create_task(func_1(4))
#     task2 = asyncio.create_task(func_2(4))
#     await task1
#     await task2
#
# print(time.strftime('%X'))
# asyncio.run(main())
# print(time.strftime('%X'))


# async def get_conn(host, port):
#     class Conn:
#         async def put_data(self):
#             print('send some data...')
#             await asyncio.sleep(2)
#             print('data send')
#
#         async def get_data(self):
#             print('get some data...')
#             await asyncio.sleep(2)
#             print('get data')
#
#         async def close(self):
#             print('close connection...')
#             await asyncio.sleep(2)
#             print('connection is close')
#
#     print('connection...')
#     await asyncio.sleep(2)
#     print('connect')


from aiohttp import ClientSession

# async def get_weather(my_city):             #code dliya parsynga
#     async with ClientSession() as session:
#         url = 'https://openweathermap.org/data/2.5/find'
#         params = {'q': my_city, 'appid': '439d4b804bc8187953eb36d2a8c26a02'}
#         async with session.get(url=url, params=params) as response:
#             wheather_data = await response.json()
#             print(f'{my_city}:{wheather_data["list"]}')
#
#
# async def main(cites):
#     tasks = []
#     for city in cites:
#         tasks.append(asyncio.create_task(get_weather(city)))
#
#     for task in tasks:
#         await task
#
#
# cities = ['Minsk', 'Hrodna']
# print(time.strftime('%X'))
# asyncio.run(main(cities))
# print(time.strftime('%X'))


import requests


def get_sync_weather(my_city):
    url = 'https://openweathermap.org/data/2.5/find'
    params = {'q': my_city, 'appid': '439d4b804bc8187953eb36d2a8c26a02'}
    weather_data = requests.get(url=url, params=params).json()
    print(f'{my_city}:{weather_data["list"]}')


def main(cites):
    for city in cites:
        get_sync_weather(city)


cities = ['Minsk', 'Hrodna','Brest']
print(time.strftime('%X'))
main(cities)
print(time.strftime('%X'))
