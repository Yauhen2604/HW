# class Car:
#     default_color = 'red'
#
#     def __init__(self, color):
#         self.color = color
#
#     def turn_on(self):
#         return 'Hello'
#
#     def ride(self):
#         return self.color
#
#
# car_1 = Car('black')
# print(car_1.ride())
#
#
# class Apple:
#     def __init__(self, amount):
#         self.amount = amount
#
#     def eat(self, n):
#         res = self.amount - n
#         return res
#
#
# apple = Apple(10)
# print(apple.amount)
# print(apple.eat(3))
#
#
# class Example:
#     n1 = 1
#     n2 = 2
#
#     def __init__(self,y,z):
#         self.y = y
#         self.z = z
#
#     def ex1(self):
#         self.n = 5
#         return self.n
#
#     def sum(self):
#         return self.n1 + self.n2
#
#     def step(self):
#         return self.y ** self.z
#
#
# example = Example(2,2)
# print(example.ex1())
# print(example.sum())
# print(example.step())


class Kalkul:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def summ(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def umonz(self):
        return self.a * self.b

    def delen(self):
        return self.a / self.b


kalkul = Kalkul(3, 4)
print(kalkul.umonz())
print(kalkul.delen())
print(kalkul.summ())
print(kalkul.minus())

while True:
    calc = Kalkul(int(input('enter num1')), int(input('enter num2')))
    znak = input('enter znak')
    if znak == '+':
        print(calc.summ())
    elif znak == '-':
        print(calc.minus())
    elif znak == '*':
        print(calc.umonz())
    elif znak == '/':
        print(calc.delen())
    else:
        print('newern znak')
