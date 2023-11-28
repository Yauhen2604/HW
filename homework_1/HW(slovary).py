# zadanie 4
dict_1 = {'ten': 10, 'twenty': 20, 'thirty': 30}
res = 1
for i in dict_1.values():
    res = i * res
print(res)
# zadanie 5
list_1 = ['ten', 'twenty', 'thirty']
list_2 = [10, 20, 30]
dict_2 = dict(zip(list_1, list_2))
print(dict_2)
# zadanie 6
str_1 = 'pythonist'
keys = []
values = []
for i in str_1:
    keys.append(i)
    values.append(str_1.count(i))
dict_3 = dict(zip(keys, values))
print(dict_3)
# Homework
products = {'apples': [30, 5], 'oranges': [40, 4], 'pear': [35, 8], 'pineapple': [50, 6]}
product = []
prise = []
quantity = []
for i, y in products.items():
    product.append(i)
    prise.append(y[0])
    quantity.append(y[-1])
seller = input(str('enter name product'))
if seller == 'apples':
    print(product[0], '-', prise[0], '$', '-', quantity[0], 'things')
elif seller == 'oranges':
    print(product[1], '-', prise[1], '$', '-', quantity[1], 'things')
elif seller == 'pear':
    print(product[2], '-', prise[2], '$', '-', quantity[2], 'things')
elif seller == 'pineapple':
    print(product[3], '-', prise[3], '$', '-', quantity[3], 'things')
else:
    print('entered incorrectly')
