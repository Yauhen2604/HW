import math


def summ(x):
    n = x
    n_2 = int(str(x) * 2)
    n_3 = int(str(x) * 3)
    return n + n_2 + n_3


print(summ(1))


def math_1(x):
    y = 0
    if -5 <= x <= 5:
        y = x ** 2
    elif x < -5:
        y = 2 * abs(x) - 1
    elif x > 5:
        y = 2 * x
    return y


print(math_1(5))


def examination(elem):
    if type(elem) == tuple:
        len_str = 0
        for i in elem:
            if i == type(str):
                len_str = len_str + len(i)
                return len_str
    elif type(elem) == list:
        alpha = 0
        digit = 0
        for y in elem:
            if y == type(int):
                digit = digit + 1
            elif y == type(str):
                alpha = alpha + 1
                return alpha, digit
    elif type(elem) == int:
        odd_digit = 0
        for z in str(elem):
            if z % 2 != 0:
                odd_digit = odd_digit + 1
                return odd_digit
    elif type(elem) == str:
        return len(elem)







