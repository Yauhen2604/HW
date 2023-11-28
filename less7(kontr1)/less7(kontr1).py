# numpy dliya tochnih vichisleniy v massivah, bolshie vichisleniya
# import numpy as np, vizivaetsya
import math

# import matplotlib.pyplot as plt
# # dliay grafikof
# x = [1, 2, 3, 4, 5]
# y = [25, 32, 34, 20, 25]
# plt.plot(x, y)
# plt.xlabel('os X')
# plt.ylabel('os Y')
# plt.title('first graf')
# plt.show()

# cat_1 = int(input('enter cat1'))
# cat_2 = int(input('enter cat2'))
# hippo = cat_1 ** 2 + cat_2 ** 2
# print(hippo ** 0.5)
#
# n1 = int(input('enter 1'))
# n2 = int(input('enter 2'))
# n3 = int(input('enter 3'))
# if n2 < n1 > n3:
#     print('first')
# elif n3 < n2 > n1:
#     print('second')
# else:
#     print('third')
#
# num1 = int(input('odd'))
# num2 = int(input('even'))
# if num1 % 2 == 0:
#     print(num2)
# else:
#     print(num1)
#
# numb = 3486
# print(str(numb)[::-1])

# figura = input('vvedi figuru')
# if figura == 'priamougolnik':
#     a = int(input('vvedi storonu 1'))
#     b = int(input('vvedi storonu 2'))
#     print(a*b)
# elif figura == 'treugolnik':
#     y = int(input('vvedi storonu'))
#     h = int(input('vvedi visotu'))
#     print(0.5*y*h)
# elif figura == 'krug':
#     r = int(input('vvedi radius'))
#     print(3.14*r**2)
# else:
#     print('vvedeno ne korrektno')
#
# stor1 = int(input('enter stor1'))
# stor2 = int(input('enter stor2'))
# stor3 = int(input('enter stor3'))
# if stor1 < stor2 + stor3 or stor2 < stor1 + stor3 or stor3 < stor2 + stor1:
#     print('sushestvuet')
# else:
#     print('ne sushestv')
#
# catt_1 = int(input('enter cat1'))
# catt_2 = int(input('enter cat2'))
# hippoo = catt_1 ** 2 + catt_2 ** 2
# rad = int(input('enter radius'))
# if math.sqrt(hippoo) < rad:
#     print('vnutri')
# else:
#     print('za predelamy')

# str_1 = input('enetr str')
# mass = str_1.split(' ')
# print(len(mass))


# str_2 = input('enter str')
# str_3 = ''
# for i in str_2:
#     if i == i.title():
#         str_3 = str_3 + i.swapcase()
#     else:
#         str_3 = str_3 + i
# print(str_3)

# numbers = []
# for i in range(0, 101):
#     if i % 7 != 0:
#         numbers.append(i)
# print(numbers)

# summa = 0
# for i in range(1, 101):
#     summa = summa + i
# print(summa)

# mass_1 = [1, 2, 3, 4, 5, 6]
# prizv = 1
# prizv2 = 1
# for i in mass_1:
#     prizv = prizv * i
# print(prizv)
# mass_2 = [1, 2, 3, 4]
# for i in mass_2:
#     prizv2 = prizv2 * i
# print(prizv2)

# n = 4
# f = 1
# for _ in range(1, 5):
#     f = f * n
#     n -= 1
# print(f)

# nums = int(input('enter num'))
# nums1 = ''
# for i in range(1, nums):
#     nums1 = str(nums1) + str(i)
#     print(str(nums1))

# mass1 = [1, 2, 3, 4, 5]
# mass2 = [5, 6, 7, 8, 9]
# mass3 = []
# for i in mass1:
#     for y in mass2:
#         if i == y:
#             mass3.append(i)
# print(mass3)

# mass1 = [1, 2, 3, 4, 5]
# mass2 = [5, 6, 7, 8, 9]
# mass3 = []
# for i in mass1:
#     if i in mass2:
#         mass3 = mass3 + [i]
# print(mass3)
