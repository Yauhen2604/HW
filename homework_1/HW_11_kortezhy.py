import random

tuple_1 = tuple(random.randint(0, 100) for i in range(9))
summ_tuple = 0
print(tuple_1)
for y in tuple_1:
    summ_tuple = summ_tuple + y
print(summ_tuple)
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
print(long_word.count('и'))
print(long_word.count('т'))
print(long_word.count('а'))
week_temp = (26, 29, 34, 32, 28, 26, 23)
sum_temp = 0
for z in week_temp:
    sum_temp = sum_temp + z
days = len(week_temp)
mean_temp = sum_temp / days
print(int(mean_temp))
