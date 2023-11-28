with open('new_file', 'r') as f:
    line = 0
    for i in f:
        line = line + 1
        print(i, len(i))
print(line)

mass = [2, 3, 4, 'hello', 'everyone']
digit = []
alpha = []
for y in mass:
    if type(y) == int:
        digit.append(y)
    else:
        alpha.append(y)
digit.sort()
alpha.sort(key=len)
with open('hello', 'w') as d:
    d.writelines(alpha)
    d.writelines('\n'+str(digit))
