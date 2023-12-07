import string


class Alphabet:
    def __init__(self, language, letters):
        self.lang = language
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('Eng', string.ascii_uppercase)

    def is_eng_alph(self, letter):
        if letter.upper() in self.letters:
            return True
        else:
            return False

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print('Hello World')


if __name__ == '__main__':
    eng_alpha = EngAlphabet()
    eng_alpha.print()
    print(eng_alpha.letters_num())
    print(eng_alpha.is_eng_alph('F'))
    print(eng_alpha.is_eng_alph('Ц'))
    EngAlphabet.example()
    eng_alpha.example()


class Tomato:
    states = {0: 'green', 1: 'yellow', 2: 'red'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state != 2:
            self._state += 1
            return self._state

    def is_ripe(self):
        if self._state == 2:
            return 'OK'
        return 'NO'


ex_cl_0 = Tomato(0)
print(ex_cl_0.grow())
print(ex_cl_0.grow())
print(ex_cl_0.is_ripe())


class TomatoBush:
    def __init__(self, count_tomato):
        self.tomatoes = [Tomato(index) for index in range(count_tomato)]
        # self.tomatoes = [Tomato(0), Tomato(1), Tomato(2)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if tomato.is_ripe():
                return True
            return False

    def give_away_all(self):
        self.tomatoes.clear()
        print('list is empty')


class Gardener:
    def __init__(self, name, plant: Tomato):
        self.name = name
        self._plant = plant

    def work(self):
        return self._plant.grow()

    def harvest(self):
        if self._plant.is_ripe():

            return print('Tomatoes is good')
        else:
            return print('Tomatoes is not good')

    @staticmethod
    def knowledge_base():
        print('reference')


Gardener.knowledge_base()
gardener = Gardener('Evgeniy', Tomato(1))
tom_bush = TomatoBush(1)

print(gardener.work())
gardener.harvest()
print(gardener.work())
gardener.harvest()
