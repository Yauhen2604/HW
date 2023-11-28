import random

a = (1,)  # nuzha zapiataya dlya kortezha
t_1 = (1, 2, 3, 4)
l_1 = [1, 2, 3, 4]
print(t_1.__sizeof__())
print(l_1.__sizeof__())
print(t_1[0])
print(t_1[:2])
l_1[0] = 111  # nelzya menyat znachenia y tupla ili dobavlayt znachenia ili delete
print(l_1)

a_1 = (10, 2.13, 'square', 89, 'C')  # mozno meniat s pomosh vstroen komand .list i .tuple

# def f(l=[]):
#     l.append(1)
#     return l
#
#
# print(f())
# print(f())
# print(f())
# print(f([44]))

t_1_to_list = list(t_1)  # meniaet tupl v list
print(t_1_to_list)
t_1_to_list.append(55)
print(t_1_to_list)
t_1 = tuple(t_1_to_list)
print(t_1)
t_2 = (1, 'hello', ['world', 2])  # mozno imenit znachenia vnutry spiska
t_2[-1][0] = '!'
print(t_2)
t__1 = (1, 2, 3, 4, 55)
t__2 = (1, 'hello', ['!', 2])  # skliet 2 tupla no luchse s 1 tipom dannnih
t__3 = t__1 + t__2
print(t__3)

t_4 = t_1 * 2  # dubliruet spisok
print(t_4)
l = [22, 3, 7, 34]
print(len(t_1), t_1.count(55))  # eti  metodi rabotaiyt i dliya spiska rabotaut
print(max(t_1), min(t_1))  # min i max values, esli stroki to somyou dlinnuio
print(max(l), min(l))

t_5 = tuple(random.randint(0, 100) for i in range(10))
print(t_5, type(t_5))
print(max(t_5), min(t_5))

t_6 = tuple(random.randint(0, 5) for y in range(10))
t_7 = tuple(random.randint(-5, 0) for z in range(10))
t_8 = t_6 + t_7
summ = 0
for a in t_8:
    if a == 0:
        summ = summ + 1
summ_1 = t_8.count(0)
print(t_8)
print(summ)
print(summ_1)

t_9 = ('hello', 'world', 'five')
words = ()
print(t_9[0], ',', t_9[1], ',', t_9[2])

A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
summ_A = 0
summ_B = 0
for s in A:
    summ_A = summ_A + s
for d in B:
    summ_B = summ_B + d
if summ_A < summ_B:
    print('summa bolshe v B')
elif summ_A > summ_B:
    print('summa bolshe v A')
print(A.index(min(A)) + 1)
print(B.index(min(B)) + 1)

my_set = {1, 2, 3, 4}
my_list = [1, 2, 2, 2, 2, 2, 1, 3, 56, 56, 7, 89, 9, 9, 0]
my_orig_data = set(my_list)
print(my_set, type(my_set))
print(my_orig_data, type(my_orig_data))
my_list_str = ['he', 'he', 'hello']
my_orig_data_str = set(my_list_str)
print(my_orig_data_str)
empty_set = set()  # sozdaet pustoe mnozhestwo
for i in my_orig_data:  # mozno proitis
    print(i)
print('world' in my_orig_data)  # rabotaet
my_orig_data_str.add('world')  # .add dobavliaeet
print(my_orig_data_str)
num_set = {1, 2, 3, 4, 5, 6}
# my_orig_data_str.discard('world')           # .discard ydaliet element
print(my_orig_data_str)
# my_orig_data_str.remove('he')           # .remove delete and dont mistake
my_orig_data_str.pop()  # .pop delete random element
# .clear delete all
new_union = num_set.union(my_set)
print(new_union)  # .union ob'ed dwa seta

print(num_set | my_set | {99, 50, 88})  # tozhe ob"ed
print(new_union & my_set)
s_a = {1, 2, 3}
s_b = {3, 4, 6}  # pokaziveat kakih elementow net v seth a or b
print(s_a - s_b)
print(s_b - s_a)
copy_set = s_a.copy()
print(copy_set)

data_1 = s_a.isdisjoint(s_b)  # vozvr True libo False est li elementi iz odnogo mnozhestwa vo vtorom
data_2 = s_b.isdisjoint(s_a)
print(data_1)
print(data_2)
print(len(s_a))  # vozvr dlinnu
# izmen spisok, slowary, set

lent = [1, 2, 2, 4, 3, 5, 6, 43, 4, 3]
lent_set = set(lent)
if len(lent) == len(lent_set):
    print('Dublikatov net')
else:
    print('Dublikaty est')

set_q = {1, 4, 2, 7, 5, 9}
len_froz = [1, 5, 8, 3, 2, 9]
set_froz = frozenset(len_froz)
set_union = set_q.union(set_froz)
print(set_union)
print(set_q - set_froz)

asi = ('one', 'two', 'three')
csi = ','.join(asi)
print(csi)

xyz = {1, 2, 3}
cvz = {3, 4, 5}
print(xyz & cvz)
print(xyz - cvz)
print(cvz - xyz)

# dict.clear()  Очищает словарь.
# dict.copy() Возвращает копию словаря.
# classmethod
# dict.fromkeys(seq[,
# value])
# Создает словарь с ключами из seq и значением value
# (по умолчанию None).
# dict.get(key[, default])  Возвращает значение ключа, но если его нет, не
# бросает исключение, а возвращает default (по
# умолчанию None)
# dict.items() Возвращает пары (ключ, значение).
# dict.keys() Возвращает ключи в словаре.
# dict.pop(key[, default]) Удаляет ключ и возвращает значение. Если ключа
# нет, возвращает default (по умолчанию бросает
# исключение).
# dict.popitem() Удаляет и возвращает последнюю пару (ключ,
# значение). Если словарь пуст, бросает
# исключение KeyError. Помните, что словари не
# упорядочены.
# dict.setdefault(key[,
# default])
# Возвращает значение ключа, но если его нет, не
# бросает исключение, а создает ключ со
# значением default (по умолчанию None).
#  dict.update([other]) Обновляет словарь, добавляя пары (ключ,
# значение) из other. Существующие ключи
# перезаписываются. Возвращает None (не новый
# словарь!).
# dict.values()  Возвращает значения в словаре.
