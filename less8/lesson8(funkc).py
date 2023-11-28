# import math
#
# a = math.pow(3, 2)
# print(a)
#
# from math import *   #importiruet wse
#
# a = pow(3, 2)
# b = sqrt(9)
# print(a, b)

# from math import pow, sqrt  # tak pravilno neskolko import delat
#
# a = pow(3, 2)
# b = sqrt(9)
# print(a, b)

# from math import pow as pw
#
# a = pw(3, 2)
# print(a)

# def func():
#     print('Hello world')
#
#
# func()
#
#
# def empty_func():
#     pass

# def summ():
#     mass = [2, 3, 4]
#     summa = 0
#     for i in mass:
#         summa = summa + i
#     print(summa)
#
#
# summ()

# def add(a, b):
#     print(a + b)
#
#
# add(1, 2)

# def add(a, b):
#     return a + b
#
#
# print(add(10, 200))
# print(add(a=10, b=200))
# print(add(10, b=200))
# print(add(b=200, a=10))

# def f_1():
#     global a
#     a = 1
#     b = 2
#     return a + b
#
#
# def f_2():
#     c = 3
#     return a + c
#
#
# print(f_1())
# print(f_2())

# def summ(a, b): return a + b
#
#
# print(summ(1, 2))


# product = lambda x, y: x + y
# print(product(1, 2))
# pw = lambda a=2, b=3: a * b
# print(pw())


# def is_year_leap(year):
#     if year % 4 == 0 or (year % 100 == 0 and year % 4 == 0):
#         return True
#     else:
#         return False
#
#
# print(is_year_leap(2000))


# def square(storona):
#     return storona * 4, storona ** 2
#
#
# print(square(5))


def season(numb):
    if 1 < numb <= 2:
        seas = 'Zima'
    elif numb == 12:
        seas = 'Zima'
    elif 6 > numb >= 3:
        seas = 'Vesna'
    elif 9 > numb >= 6:
        seas = 'Leto'
    elif 11 > numb >= 9:
        seas = 'Osen'
    else:
        seas = 'Not found'
    return seas
#
#
# print(season(8))

def is_prime(a):
    b = 2
    while a % b != 0:
        b += 1
    return b == a


print(is_prime(2))


