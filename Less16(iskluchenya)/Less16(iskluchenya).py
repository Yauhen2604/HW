# \n - perevod stroki
# \r - vozvrat koretky
# \r\n - perevod stroki + vozvrat koretky
# my_str = 'abcdercrec'
# print(my_str.split('c', maxsplit=1))  # ukaz skolko vhojdeniy
# s = 'ab c\nde fg\rkl\r\n'
# print(s.split())  # razbivaet po nepechatnim symbol and probelam
# print(s.splitlines())  # razbivaet po nepechatnim symbol
#
# try:
#     x = 100 / 0
# except ZeroDivisionError:  # ne tormozit kod
#     print('you are division by zero')
#
# print('code after...')
#
# try:
#     x = 100 / 0
# except ArithmeticError:  # ne tormozit kod
#     print('you are division by zero')
#
# print('code after...')
#
# try:
#     x = 100 / '0'
# except TypeError:  # ne tormozit kod
#     print('you are division by zero')
#
# print('code after...')
#
# d = {'name': 'yauhen'}
# print(dict['age'])
# try:
#     print(d['age'])
# except KeyError:
#     d['age'] = 1
#     d['lastname'] = 'yatsyna'
#     print(d['age'])
# print(d)
# print('code after...')
#
# l = ['hello', 'world']
# try:
#     print(l[2])
# except IndexError:
#     print('add this')
#     l.append(input('enter str'))
#
# print(l)


# d1 = {'name': 'yauhen', 'age': 30}
# try:
#     v = d1['city']
# except KeyError:
#     print('key not found')
# except IndexError:
#     print('index not found')
# except SyntaxError:
#     print('invalid syntax')
# except Exception:
#     print('Big problem')
# try:
#     v = d1['city']
# except (IndexError, KeyError):
#     print('We\'re have an error')
# try:
#     v = d1['city']
# except KeyError:
#     print('key not found')
# finally:
#     print('we\'re do smth')  # rabotaet vsegda

# try:
#     v = d1['age']
#     print(v)
# except KeyError:
#     print('key not found')
# else:
#     print('you\'re so cool')  # v tom sluchae esli ne otrabotaet oshibka
# finally:
#     print('you\'re great')

# a = int(input('enter num1'))
# b = int(input('enter num2'))
# try:
#     res = a/b
# except ZeroDivisionError:
#     print('you are fool')
# else:
#     print(res**2)
# finally:
#     print('you are great')


try:
    a = int(input('enter num1'))
    b = int(input('enter num2'))
    res = a/b
except ZeroDivisionError:
    print('you are fool')
except ValueError:
    print('you are moron')
except Exception:
    print('you are idiot')
else:
    print(res)
# asana planirovshik proekta
