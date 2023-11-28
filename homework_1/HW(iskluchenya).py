a = input('enter num1')
b = input('enter num2')
if b == 0:
    b = int(input('enter num2 again'))
try:
    res = int(a)/int(b)
except ZeroDivisionError:
    print('you are fool')
except ValueError:
    print('you are moron')
else:
    print(res)
