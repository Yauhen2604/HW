import random

# m = int(input('enter num'))
# p = int(input('enter num'))
# while m < p-1:
#     m = m + 1
#     if m < 0:
#         print(m)
#
# operand1 = float(input('vvedi chislo 1'))
# operator = input('vvedy operacyu -+/*')
# operand2 = float(input('vvedy chislo 2'))
# if operator == "+":
#     print(operand1+operand2)
# elif operator == "-":
#     print(operand1-operand2)
# elif operator == "*":
#     print(operand1*operand2)
# elif operand2 == 0 and operator == '/':
#     print('nelzya delit na nol')
# elif operator == "/":
#     print(operand1/operand2)
# else:
#     print("vvedy druguiu operaciyu")


attempt = 1
while attempt <= 5:
    num = int(input('enter num'))
    color = input('enter color')
    cas_num = random.randint(1, 10)
    cas_col = random.randint(1, 2)
    if color == 'red':
        color = 1
    elif color == 'black':
        color = 2
    else:
        print('vvedeno ne korrektno')
    if cas_num == num and cas_col == color:
        print('you win')
    else:
        if cas_col == 1:
            cas_col = 'red'
        elif cas_col == 2:
            cas_col = 'black'
        print('you lost')
        print(cas_num, cas_col)
    attempt = attempt + 1
print('good bye')
