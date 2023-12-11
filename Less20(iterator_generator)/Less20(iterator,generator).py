for i in [1, 2, 3]:
    print(i)

evens = [2, 4, 6, 8, 10]
even_iter = iter(evens)  # sozdaet ob'ekt iteratora
print(even_iter)

print(next(even_iter))  # hranit tekush i sled znachenie
print(next(even_iter))
print(next(even_iter))
print(next(even_iter))
print(next(even_iter))

iter_obj = iter([1, 2, 3, 4, 5])
while True:
    try:
        i = next(iter_obj)
        print(i)
    except StopIteration:
        break


class IterExample:
    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if self.x <= 100:
            y = self.x
            self.x += 1
            return y
        else:
            raise StopIteration  # kogda budet 100 iteraciy ostanovitsya


class_instance = IterExample()
elem = iter(class_instance)
print(next(elem))
print(next(elem))
print(next(elem))
print(next(elem))
print(next(elem))

for i in elem:  # budet beskonechno
    print(i)
    if i == 11:
        break

elements = [2, 4, 6, 8, 10]


def my_sqrt(num):
    for i in num:
        yield i ** 2


s = my_sqrt(elements)
print(s)

s_1 = (i ** 2 for i in elements)
print(s_1)
for i in s_1:
    print(i)
elements = [2, 4, 6, 8, 10]
s_1 = (i ** 2 for i in elements)
s_2 = [i ** 2 for i in elements]
print(s_1, type(s_1))
print(s_2, type(s_2))
from datetime import datetime
import time


def decor(v):
    def decowrap(func):
        def wrap(x):
            t1 = datetime.now()
            res = func(x)
            t2 = datetime.now() - t1
            if v:
                print(t2)
            return res

        return wrap

    return decowrap


@decor(v=True)  # dekorator s usloviem
def my_func(x):
    time.sleep(1)
    print(f'value => {x}')


my_func(15)
