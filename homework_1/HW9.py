operand1 = float(input('vvedi chislo 1'))
operator = input('vvedy operacyu -+/*')
operand2 = float(input('vvedy chislo 2'))
if operator == "+":
    print(operand1+operand2)
elif operator == "-":
    print(operand1-operand2)
elif operator == "*":
    print(operand1*operand2)
elif operator == "/":
    print(operand1/operand2)
else:
    print("vvedy druguiu operaciyu")
