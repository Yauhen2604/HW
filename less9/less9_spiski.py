# from less8 import less8
# from homework_1.HW_funkc import calcul
#
# print(calcul(3, 5))
import random
#
# # # elem = list()
# my_lst = [random.randint(0, 100) for _ in range(6)]
# # print(my_lst)
# # my_lst2 = [i * 100 for i in range(6)]  #0,100,200,300,400,500
# # print(my_lst2)
#
# lst_1 = ['hello', 1, True]
# lst_1.append('world')
# print(lst_1)
# lst_1.insert(1, 'True')
# print(lst_1)
# lst_1[1] = False
# print(lst_1)
# del lst_1[1]  # del index iz spiska
# print(lst_1)
# lst_1.remove(1)  # ydaliaet pervoe whozdenie v spisok
# print(lst_1)
# lst_2 = [1, 2, 3, ['11', '22'], False]
# del lst_2[3][0]
# print(lst_2)
# del lst_2[:2]
# print(lst_2)
# if 3 in lst_2:  # esli est v spiske to dobavliaet, proverka est li v spiske
#     lst_2.append('fire')
# else:
#     lst_2.append('warning')
# print(lst_2)
# # adresses = [['minsk', 'zavod', 8],
# #             ['minsk', 'libknehta', 68],
# #             ['nezavis', '117a']]
# # for adr in adresses:
# #     if 'minsk' in adr:
# #         adresses = ''.join(adr)
# #     else:
# #         adr.append('minsk')
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# res = l1 + l2
# print(res)
# l1.append(l2)  # dobavl v -1 element spiska
# print(l1)
# l3 = [7, 8, 9]
# l2.extend(range(6))  # dobavl v spisok po 1 elementu
# l2.extend(l3)
# print(l2)
#
# a = [1, 2, 3, 4]
# b = a
# print(id(a))
# print(id(b))
# a.append(5)
# b.append(6)
# print(id(a))
# print(id(b))
# print('*' * 10)
# a1 = [1, 2, 3, 4]
# b1 = a1.copy()
# print(a1, id(a1))
# print(b1, id(b1))
# import copy
#
# c3 = copy.copy(a1)
# c4 = copy.deepcopy(a1)
# c5 = list(a1)
# print('copy copy', c3, id(c3))
# print('deepcopy', c4, id(c4))
# print(c5, id(c5))
#
# elements = [['apples', 50], ['oranges', 190], ['pineapples', 100]]
# print(elements[0])
# print(elements[1][0])
# o = []
# for pos in elements:
#     o.append(pos[0])
# print(o)
#
# spisok = [1, 2, 3, 4, 5]
# print(spisok)
# spisok.reverse()
# print(spisok)
#
spis2 = [random.randint(0, 100) for _ in range(5)]
print(spis2)
if spis2.count(20) >= 1:
    ind = spis2.index(20)
    spis2[ind] = 200
print(spis2)
#
# spis3 = [5, [1, 2], 2, 'r', 4, 'ee']
# spis4 = [4, 'we', 'ee', 3, [1, 2]]
# res_spis = []
# for i in spis3:
#     if i in spis4:
#         res_spis.append(i)
# print(res_spis)

# spis5 = [4, 6, 'py', 78, 'helly']
# spis6 = [44, 'hello', 56, 'exept', 3]
# spis7 = spis5 + spis6
# print(spis7)
# spis7.insert(2, 6)
# for tex in spis7:
#     if type(tex) is str:
#         spis7.remove(tex)
# print(spis7)
# print(len(spis7))
