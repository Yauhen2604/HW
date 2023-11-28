import random


def my_func(a=1, b=2):
    res = a + b
    return res  # 3


print(my_func(3, 4))  # 7


def mixed_function(a, b=2, c=3):
    return a + b + c


print(mixed_function(1))  # pozitionniy bez znachenia, imenovanniy so znacheniem


def many(*args, **kwargs):  # mozno peredavat skolko ugodno argumentow
    print(args, type(args))  # type tuple kortezh
    print(kwargs, type(kwargs))  # type dict  slowary


many(0, 1, 2, name='Fiodar', age=39)


def factorial(n):  # naity factorial chisla n
    if n != 0:
        return n * factorial(n - 1)
    else:
        return 1


print(factorial(5))


def add(a, b):
    return a + b


print(add(1, 2))
data = add(3, 4)
print(data)
add_1 = add
add_2 = add_1
print(add, type(add))
print(add_1, type(add_1))
print(add_2, type(add_2))
print(add_2(5, 6))  # nepriamoy vizov funkciy


def sq(x):
    return x * x


print(sq(2))
square = sq
print(square(3))


def func_1(x):
    def func_2(y):
        return x * y

    return func_2


print(func_1(2)(3))  # peredayie znachenie funkc 1 and funkc 2
func_3 = func_1(5)
print(func_3(500))

print('*' * 10)


def razr(num):
    i = 0
    while num > 0:
        num = num // 10
        i = i + 1
    return i


print(razr(264))

R = 10
my_list = [0] * 10


#
# def mass(x, y):
#     for i in range(R):
#         my_list[i] = random.randint(x, y)
#
#
# print(mass(x=int(input('enter num_1')), y=int(input('enter num_2'))))


def time(z):
    day = z // (24 * 3600)
    z = z % (24 * 3600)
    hour = z // 3600
    z = z % 3600
    minutes = z // 60
    z = z % 60
    sec = z

    return day, hour, minutes, sec


print(time(86425))

my_len = [15, 48, 'hello', 6, 19, 'world']


def alpha(x):
    soglasn = 0
    glasn = 0
    for i in x:
        if i in 'aeiouy':
            glasn = glasn + 1
        else:
            soglasn = soglasn + 1
    return glasn, soglasn


print(alpha('hello'))
