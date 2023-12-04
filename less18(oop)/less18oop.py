class Car:
    def __str__(self):
        return 'Class Car obj'

    def start(self):
        print('engine started')


car1 = Car()
print(car1)


class Phone:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def sim_check(self, operator):
        if self.model == 'q' and operator == 'a1':
            return 'ok'


ph = Phone('black', 'q')
print(ph.sim_check('a1'))


class Cat:
    @staticmethod
    def meow():
        return 'Mey!'


print(Cat.meow())
cat_1 = Cat()
print(cat_1.meow())


class Myclass():
    @staticmethod
    def castom_static():
        print('static method called')


Myclass.castom_static()


class Person:
    @staticmethod
    def is_adult(age):
        if age > 18:
            return True
        else:
            return False


print(Person.is_adult(23))


class MyClass:
    Total_obj = 0

    def __init__(self):
        MyClass.Total_obj = MyClass.Total_obj + 1

    @classmethod
    def total_obj(cls):
        print('Total objects: ', cls.Total_obj)


my_obj1 = MyClass()
my_obj2 = MyClass()
my_obj3 = MyClass()
MyClass.total_obj()


class Childclass(MyClass):
    Total_obj = 0
    pass


Childclass.total_obj()


class Human:
    default_name = 'Evgeniy'
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 100
        self.__house = 'Apartment'

    def info(self):
        return self.name, self.age, self.__money, self.__house

    @staticmethod
    def default_info():
        return Human.default_age, Human.default_name

    def earn_money(self, amount):
        self.__money += amount
        return amount, self.__money


print(Human.default_info())
human1 = Human()
print(human1.info())
print(human1.earn_money(200))


class New(Human):
    pass


class Phone:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def call(self):
        if self.is_on:
            return 'start calling'


class Mobile(Phone):

    def __init__(self):
        super().__init__()
        self.battery = 0

    def charge(self, per):
        self.battery = per
        return 'charging', self.battery


mobile = Mobile()
print(dir(mobile))
print(mobile.is_on)
print(mobile.turn_on())
print(mobile.is_on)


class Toy_phone(Phone):
    def toy_ph(self):
        print('Child class Tou_phone')


toy_phone = Toy_phone()
print(toy_phone.is_on)
toy_phone.toy_ph()


class Camera:
    def camera(self):
        pass


class Radio:
    def radio(self):
        pass

    def camera(self):
        pass


class Phone(Camera, Radio):
    def phone(self):
        pass


print(Phone().__dir__())


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, sale):
        self._price = self._price - sale
        return self._price


house = House(50, 500)
print(house.final_price(50))


class SmallHouse(House):
    default_area = 40

    def __init__(self, _price):
        super().__init__(SmallHouse.default_area, _price)
