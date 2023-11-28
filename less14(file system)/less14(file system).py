def flattening(my_lst):
    new_lst = list()
    for i in my_lst:
        if isinstance(i, list):  # yvliaetsiy li listom
            new_lst.extend(flattening(i))  # raspakuet spisok i dobavit
        else:
            new_lst.append(i)
    return new_lst


print(flattening([2, 3, [4], [5, 6, 7, [4, 5]], [3, 6, 7, [2, 3]]]))

# f = open(file_name, access_mode)        #open file
# f = open('new_today.txt', encoding='utf-8')  # esli net takog to sozdast
# print(f)  # utf-8 razbiraet kirillicu
# print(*f)  # online-decoder     opredelit kodirowku
# f.close()  # regex101.com   formaty
# with open('new_today.txt', 'w', encoding='utf-8') as f:  # jsonformatter pravilno li virezali kod, proveriaet oshibki
# print(f.read(7))        #otkroet do indexa 7
# print(f.read())         #otkroet posle indexa
# print(f.readline())        #otkroet odnu stroku       #rabotayut tolko c failami dlia chetenia
# print(f.readlines())        # otkroet spiskom
# print(f.readline().strip())     #otkroet strochku
# f.write('hello')  # udalit i dobavit new text
# f.write('world\n')  # \n ob'edenit strochki v odnu
# f.writelines('hello my friend')  # zapishet v new line

import os

# os.rename('new_today.txt','new.txt')  # reneimit
# print(os.getcwd())  # otkrivaet put' k failu
# os.mkdir('empty_folder_lesson_14')          #sozdast papku
# os.chdir('')          #proverit v kakoi vi papke
# print(os.getcwd())
# # os.chdir('..')          #vernet na shag nazad
# # os.chdir('../..')          #vernet na dva shag nazad
# # os.makedirs('empty/empty1/empty2')      #sozdast papku v papke
# # os.remove('../name')                   #delete file
# # os.rmdir('empty/empty1/empty2')          #delete papku
# os.removedirs('empty')                  #delete vse papki i vlozhennie

# with open('new_today.txt', 'r',) as f:
#     summ = 0
#     new_txt = f.readlines()
#     data = new_txt[0].split(' ')
#     for i in data:
#         if i.isdigit():
#             i = int(i)
#             summ = summ + i
#     print(summ)

# with open('new_today.txt', 'r') as f:
#     list_num = []
#     list_alpha = []
#     new_list = f.readlines()
#     finish_list = []
#     for i in new_list:
#         i = i.strip()
#         if i.isdigit():
#             list_num.append(i)
#         else:
#             list_alpha.append(i)
#     list_num.sort()
#     list_alpha.sort(key=len)
#     finish_list = list_num + list_alpha
#     print(finish_list)

with open('../homework_1/new_file', 'w') as b:
    while True:
        user_txt = input('enter txt')
        if user_txt == '':
            break
        b.write(user_txt + '\n')




