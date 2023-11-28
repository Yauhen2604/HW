import random

hc = int(input('1 - Камень, 2 - Ножницы, 3 - Бамага: '))
pcc = random.randint(1,3)

one = 'Камень'
two = 'Ножницы'
three = 'Бумага'

if hc == pcc:
    print('Ничья!')
elif hc == 1 and pcc == 2 \
        or hc == 2 and pcc == 3 \
        or hc == 3 and pcc == 1:
    print('Вы победили!')
else:
    print('Компьютер победил!')

if hc == 1:
    hc = one
elif hc == 2:
    hc = two
else:
    hc = three

if pcc == 1:
    pcc = one
elif pcc == 2:
    pcc = two
else:
    pcc = three

print('Вы выбрали:', hc, '| Компьютер выбрал:', pcc)
