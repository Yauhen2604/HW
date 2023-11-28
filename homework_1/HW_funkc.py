# Функция, вычисляющая среднее арифметическое
# элементов массива. ǿассив должен состоять из
# случайных чисел, длинной 10 элементов.
import random

a = 0
mass = []
while a < 10:
    mass.append(random.randint(1, 10))
    a = a + 1
print(mass)


def massive():
    summ = 0
    for i in mass:
        summ = summ + i
    return summ / len(mass)


print(massive())


# Homewrok
def calcul(a1, b1):
    operator = input('vvedy operacyu -+/*')
    if operator == "+":
        return a1 + b1
    elif operator == "-":
        return a1 - b1
    elif operator == "*":
        return a1 * b1
    elif operator == "/":
        return a1 / b1
    elif b1 == 0 and operator == '/':
        return 'nelzia delit na nol'
    else:
        return 'vvedy druguiu operaciyu'


print(calcul(5, 5))
