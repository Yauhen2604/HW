def imt(a, b):
    res = ()
    imt_1 = b / (a ** 2)
    if imt_1 > 30:
        res = 'revival'
    elif 25 >= imt_1 < 30:
        res = 'overweight'
    elif imt_1 < 25:
        res = 'normal'
    return res


def figura(x):
    figure = ()
    if x == 3:
        figure = 'treugolnik'
    elif x == 4:
        figure = 'kvadrat'
    elif x == 5:
        figure = 'pentagon'
    elif x == 6:
        figure = 'geksagon'
    elif x == 7:
        figure = 'geptagon'
    elif x == 8:
        figure = 'oktagon'
    elif x == 9:
        figure = 'dekagon'
    elif x == 10:
        figure = 'tengon'
    else:
        figure = 'unkorrektly'
    return figure


from datetime import datetime, timedelta


def next_day(w):
    date = datetime.strptime(w, '%Y-%m-%d')
    res_1 = date + timedelta(days=1)
    return res_1.strftime('%Y-%m-%d')


print(next_day('2020-02-29'))


def delivery(num):
    first_product = 10.95
    next_product = 2.95
    prise_delivery = ()
    if num == 1:
        prise_delivery = first_product
    elif num > 1:
        prise_delivery = first_product + (next_product * num)
    return prise_delivery


print(delivery(5))

import math


def drobi(n1, n2):
    delitel = math.gcd(n1, n2)
    return n1 // delitel, n2 // delitel


print(drobi(6, 63))


# def list_1(l):
#     print(l[::-1])
#     print(l.sort())
#     print(l.reverse())
#     print(l[1:7])
#     print(l.remove(5))
#     print(set(l))
#
#
# print(list_1([1, 2, 3, 4, 5, 'hello', 'world', 8, 9, 10]))


def countrange(list2, min_1, max_1):
    res1 = 0
    for i in list2:
        if max_1 > i >= min_1:
            res1 = res1 + 1
    return res1


print(countrange([1, 2, 3, 4, 5], 2, 4))


def list3(list4):
    res2 = 0
    for i in list4:
        if type(i) == list:
            res2 = res2 + 1
    return res2


print(list3(([1, 2, 3], [4, 5, 6])))


def anogramma(sl1, sl2):
    if len(sl1) == len(sl2):
        if sl1.count(sl2) == sl2.count(sl1):
            print('anogramma')
        else:
            print('not anogramma')


anogramma('live', 'evil')

phone = {1: '.,?:!', 2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ', 0: ' '}
text = 'HELLO WORLD'
num_code = ''
for i in text:
    if i == phone.values():             #vlozheniy cikl
        num_code = str(num_code) + str(phone.keys())
