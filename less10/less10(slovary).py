d = {}
d_1 = {'one': 1000}  # spisok ne mozhet but kluchom
print(type(d), d)
print(type(d_1), d_1)
d_2 = dict(short='dict1', long='dictionary1')
d_3 = dict([(1, '1'), (2, '2')])
print(type(d_2), d_2)
print(type(d_3), d_3)
d_4 = dict()
print(type(d_4), d_4)
d_5 = dict.fromkeys(['py', 'jv', 'css'])
d_6 = dict.fromkeys(['py', 'jv', 'css'], 'language')
d_7 = dict.fromkeys(['py', 'jv', 'css'], ['language', 2, 3])
d_8 = dict.fromkeys(['py', 'jv', 'css'], ['language'])
print(d_5)
print(d_6)
print(d_7)
print(d_8)
d_10 = {a: a + 1 for a in range(10)}  # prisvaivaet cluchi po poriadku i znacheniya po poriadku
print(d_10)
d_2 = dict(short='dict1', long='dictionary1')
print(d_2['short'])
d_2['long'] = 'My_dictionary'
print(d_2)
d_2_1 = d_2.copy()
print(d_2_1)
d_2_1['new'] = 'hello'
print(d_2_1)
print(d_2.get('short'))
print(d_2.get('shorttt'))  # vozvraschaet bez kvadr skobok i bez oshibki esli clucha net
print(d_2.get('shorttt', 'world'))
print(d_2.items())  # vozvr pary kluch i znachenie
print(d_2.keys())  # vozvr tolko kluch
print(d_2.values())  # vozvr tolko znachenir
# d_2.pop('short')  # delete and vozwrash znachenie
# print(d_2)
# d_2.popitem()   # delete last value and key
# print(d_2)
print(d_2)
print(d_2.setdefault('shorttt', 'world'))  # znachenie klucha esli kluch verniy, esli net to zapishet znachenie
print(d_2)
d_2.update({'longgg': 'LONG'})  # obnowl spisok i dobavl slowari
print(d_2)
print(len(d_2))
del d_2['shorttt']  # delete paru c kluchom
print(d_2)
d_11 = {'fst': {'short': 'dict1',
                'long': 'My_dictionary',
                'longgg': 'LONG'},
        'scd': {'name': 111,
                'addr': 222}}
print(len(d_11))
print(d_11)
print(d_11['scd']['name'])  # obachaemsia k elementam po kluchu
print('scd' in d_11)  # vozvr True or False sprashivaet est li takoi kluch
print('scddd' in d_11)  # vozvr True or False sprashivaet est li takoi kluch, rabotat tolko s kluchami
print('long' in d_11)  # vozvr True or False sprashivaet est li takoi kluch, rabotat tolko s kluchami
print('long' in d_11['fst'])  # vozvr True or False sprashivaet est li takoi kluch, rabotat tolko s kluchami
# zip() sozdaet slowary putem soedeniya slowarey

l_1 = ['name', 'pass', 'data']
l_2 = ['fiodar', 1234, 987]
d_12 = {l_1[0]: l_2[0], l_1[1]: l_2[1]}
print(d_12)
d_13 = dict(zip(l_1, l_2))
print(d_13)

for i in d_13:  # vivodit cluchi
    print(i)
    print('key', i, 'values:', d_13[i])
for i in d_13.keys():  # tozhe samoe
    print(i)
for i in d_13.values():  # otdaet znachenia
    print(i)
for i in d_13.items():  # vozvrashaet pari kluch znachenie
    print(i)
for k, v in d_13.items():  # vozvrash na vibor kluch ili znachen
    print(k)
    print(v)
sorted_list = list(d_13.keys())  # sortiruet po alfavit
print(sorted_list)
sorted_list.sort()
print(sorted_list)
d_13_sort = {}
for i in sorted_list:
    print('{', i, ':', d_13[i], '}')
    d_13_sort[i] = d_13[i]
print(d_13_sort)

person = {'name': 'Evgeniy', 'age': 30, 'city': 'Minsk'}
print(person['age'])
print(person.get('age'))  # dliya neizvestn slovarye

cars = {'BMW': ['E39', 'E38', 'E60'], 'Tesla': ['Model X', 'Model 3', 'Model S']}
print(cars['BMW'][0], cars['BMW'][-1])
print(cars['Tesla'][0], cars['Tesla'][-1])


