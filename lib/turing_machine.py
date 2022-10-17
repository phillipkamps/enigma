from shifts import Shifts
from operator import add

class TuringMachine():
    def alphabetically_index_message(self, message):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
        alphabetically_indexed_message = []
        message_chars = list(message.lower())
        for (char) in message_chars:
            alphabetically_indexed_message.append(alphabet.index(char))
        return alphabetically_indexed_message

    def char_shifts(self, message, key, date):
        shifts = Shifts()
        final_shifts = shifts.final_shifts(key, date)
        message_shifts = []
        for (index, char) in enumerate(message):
            if index % 4 == 0: message_shifts.append(final_shifts['a_shift'])
            elif index % 4 == 1: message_shifts.append(final_shifts['b_shift'])
            elif index % 4 == 2: message_shifts.append(final_shifts['c_shift'])
            elif index % 4 == 3: message_shifts.append(final_shifts['d_shift'])
        return message_shifts

    def calc_shifts(self, message, key, date):
        rounded = []
        calcd = [sum(x) for x in zip(self.alphabetically_index_message(message), self.char_shifts(message, key, date))]
        for (i) in calcd: rounded.append(round(i%27))
        return rounded

    def scramble(self, message, key, date):
        scrambled = []
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
        shifts = self.calc_shifts(message, key, date)
        for (e) in shifts:
            scrambled.append(alphabet[e])
        return "".join(scrambled)

# wip = TuringMachine()
# message = "hello world"
# key = "02715"
# date = "040895"
# char_shifts = wip.char_shifts(message, key, date)
# alpha = wip.alphabetically_index_message(message)
# calcd = wip.calc_shifts(message, key, date)
# scrambled = wip.scramble(message, key, date)
# import ipdb; ipdb.set_trace()