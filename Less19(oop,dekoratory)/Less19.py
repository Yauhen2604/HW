import datetime
import time


class Car:

    def __init__(self, model):
        self.model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model

    def add_model(self):
        return 'god vipusk ' + str(self.model)


car_1 = Car(2005)
print(car_1.add_model())


def obramlenye(func):
    def wrapper():
        print('funkc obolochka')
        func()
        print('finish')

    return wrapper


def summ():
    print(10 + 20)


wrap = obramlenye(summ)
wrap()
summ()


@obramlenye
def default():
    print(50)


default()


def count(func_1):
    def wrapper(*args):
        wrapper.count += 1
        res = func_1(*args)
        print(f'{func_1.__name__} called {wrapper.count}')
        return res

    wrapper.count = 0
    return wrapper


@count
def hello():
    return 'hello'


hello()
hello()


def dekor_time(my_func):
    def wrapper():
        a = datetime.datetime.now()
        my_func()
        b = datetime.datetime.now() - a
        print(f'result func work {my_func.__name__}={b}')

    return wrapper


@dekor_time
def my_func():
    time.sleep(1)
    l = []
    for i in 'hello':
        l.append(i)
    print('standart funkc')
    print(l)


my_func()


def bold(f):
    def wrap():
        return '<b>' + f() + '<b>'

    return wrap


def italic(f):
    def wrap():
        return '<i>' + f() + '<i>'

    return wrap


@bold
@italic
def my_text():
    return 'Hello world'


print(my_text())


def decorator_witch_param(f):
    def wrap(arg):
        print(f'this is {f.__name__} and some argument {arg}')
        f(arg)

    return wrap


@decorator_witch_param
def my_cust_func(num):
    print(num * 2)


my_cust_func(9)

import logging


def logger(func):
    log = logging.getLogger(__name__)

    def wrapper(a, b):
        log.info('enter funkc', func.__name__)
        ret = func(a, b)
        log.info('enters funkc', func.__name__)
        return ret

    return wrapper


@logger
def add(a, b):
    print('a+b', a + b)
    return a + b


add(10, 20)
add(3, 2)

app = {}


def callback(route):
    def wrapper(func):
        app[route] = func

        def wrapped():
            ret = func()
            return ret

        return wrapped

    return wrapper


@callback('/')
def index():
    print('index')
    return 'OK'


print('> start')
route = app['/']
if route:
    resp = route()
    print('answer', resp)
print('> end')


