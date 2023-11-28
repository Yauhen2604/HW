# with open('new_today.txt', 'r') as f:
#     line = 0
#     for i in f:
#         line = line + 1
#         print(i, len(i))
# print(line)
# a = 1
# print('result a=', a)  # est probel
# print(f'result a={a}')  # net probela
# print('result a={}'.format(a))  # net probela
#
# a = 20
# b = 10
# res = a if a > b else b  # sokrash iteracyi
# print(res)
#
# my_str = 'awesome'
# print(my_str.replace('e', 'r', 1))        #awerome, count menyiat kolichestwo vhozhdeniy

import csv

# my_f = open('example.csv', encoding='utf-8')
# my_reader = csv.reader(my_f, delimiter=';')     #razdeliaet stroki po razdelitelu po stroke
# data = list(my_reader)
# print(data)
# print(data[0][0])
# for i in data:
#     print(i[0])

# f = open('data.csv', 'w', encoding='utf-8', newline='')     #esli ne napisat newline to budet cherez pustuiy sroku
# data_writer = csv.writer(f, delimiter=';')            #dobavlyar delitel
# my_data = [['20.11', ' python, django', ' 15'], ['21.11', ' c++, c#', ' 5'], ['22.11', ' swift', ' 10']]
# for row in my_data:
#     data_writer.writerow(row)
# f.close()

import json
import demjson3

# json.load()    chitaet file
# json.loads()   chitaet stroku
# json.dump()   zapisivaet dict
# json.dumps()

# my_str = '{"id": 1, "name": "fiodar", "age": 39}'  # kovichki tolko tak
# data = json.loads(my_str)
# print(type(data))
# print(data['age'])
# print(data['id'])
# ss = {'id': 1}
# print(demjson3.encode(ss))          # korrect nor kovichki
# with open('data.json', encoding='utf-8') as f:
#     data = json.load(f)
# print(data['id'])
# print(data['age'])

my_dict = {"id": 11, "phone": 123, "addr": "минск", "name": "fiodar"}
my_s = json.dumps(my_dict)
print(my_s, type(my_s))
my_s = json.dumps(my_dict, ensure_ascii=False)
print(my_s)
with open('data_my_dict.json', 'w', encoding='utf-8') as f:
    json.dump(my_dict, f, ensure_ascii=False)           #cchtiby read kiriilica format

