for x in range(1, 10):
    for y in range(1, 10):
        print(x * y)
    print('*' * 10)

not_even = 1
for i in range(1, 31):
    if i % 2 != 0:
        not_even *= i
print(not_even)

mass = []
for i in range(5, 101, 5):
    mass.append(i)
print(mass)

even = ''
for i in range(1, 71):
    if i % 2 == 0:
        even += ' ' + str(i)
print(even)


mass_1 = [1, 4, 3, 2, 4, 5, 6, 7]
mass_2 = []
for i in mass_1:
    if mass_1.count(i) >= 2:
        mass_2.append(i)
print(mass_2)
