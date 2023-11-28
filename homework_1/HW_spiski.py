my_len = [15, 48, 'hello', 6, 19, 'world']
summ = 0
soglasn = 0
glasn = 0
for n, i in enumerate(my_len):
    if type(i) == int and i % 2 == 0:
        summ = summ + i
    elif type(i) == int and i % 2 != 0:
        my_len[n] = 1
    elif type(i) == str:
        for y in i:
            if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' or y == 'y':
                glasn = glasn + 1
            else:
                soglasn = soglasn + 1
print(my_len)
print('kolich glasn =', glasn)
print('kolich soglasn =', soglasn)
