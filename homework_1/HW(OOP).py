import string


#
#
# class Alphabet:
#     def __init__(self, language, len_str):
#         self.lang = language
#         self.letters = list(len_str)
#
#     def letters(self):
#         print(self.letters)
#
#     def letters_num(self):
#         len(self.letters)
#
#
# alpha = Alphabet('English', 'qwertyuiopasdfghjklzxcvbnm')
#
#
# class EngAlphabet(Alphabet):
#     __letters_num = 26
#     super().__init__('Eng', string.ascii_uppercase)
#
#     def is_eng_alph(self, letter):
#         if letter.upper() in self.letters:
#             return True
#         else:
#             return False
#
#     def letters_num(self):
#         return EngAlphabet.__letters_num
#
#     @staticmethod
#     def example():
#         print('Hello World')
#
#
# if __name__ == '__main__':
#     eng_alpha = EngAlphabet('English', 26)
#     print(eng_alpha)
#     print(eng_alpha.letters_num())
#     print(eng_alpha.is_eng_alph('F'))
#     print(eng_alpha.is_eng_alph('Ц'))
#     EngAlphabet.example()


class Tomato:
    states = {1: 'green', 2: 'yellow', 3: 'red'}

    def __init__(self, index, state):
        self._index = index
        self._state = self.states[1]

    def grow(self):
        if self._state != self.states[3]:
            plant_index = list(self.states.values()).index(self._state)
            self._state = self.states[plant_index + 1]
            return self._state

    def is_ripe(self):
        if self._state == self.states[3]:
            return 'OK'


class TomatoBush:
    def __init__(self, count_tomato):
        self.tomatoes = [Tomato(index) for index in range(count_tomato)]

    def grow_all(self):
        for i in self.tomatoes:
            return i.grow()

    def all_are_ripe(self):
        for tomato in self.tomatoes:
            return tomato.is_ripe()

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
