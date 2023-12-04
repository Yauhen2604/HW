class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_prise = self._price - discount
        print(f'finale prise {final_prise}')
        return final_prise


house = House(50, 500)


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


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

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            return 'у теб нет денег !!'


human = Human()
small_house = SmallHouse(30)
print(human.buy_house(small_house, 2))
human.earn_money(10000000)
print(human.buy_house(small_house, 2))
