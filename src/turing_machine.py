from typing import List
import numpy as np

from shifts import keygen, final_shifts

# import sys
# sys.path.insert(0, '/enigma/lib/shifts.py')
# from shifts import Shifts

# ALPHABET = [
#     "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
#     "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "
# ]
ALPHABET = "abcdefghijklmnopqrstuvwxyz "


class Machine:
    def __init__(self, name) -> None:
        self.name = name


class TuringMachine(Machine):
    def __init__(
        self, name: str, key: str, date: str = None, char_list: List[str] = ALPHABET
    ) -> None:
        super().__init__(name)
        self.char_list = char_list
        self._date = date
        self.key = key
        self._final_shifts = None

    @property
    def date(self):
        if self._date is None:
            self._date = "today'sdate"
        return self._date

    @property
    def final_shifts(self):
        if self._final_shifts is None:
            self._final_shifts = final_shifts(self.key, self.date)
        return self._final_shifts

    def alphabetically_index_message(self, message):

        alphabetically_indexed_message = []
        # message_chars = list(message.lower())
        for char in message.lower():
            alphabetically_indexed_message.append(self.char_list.index(char))
        return alphabetically_indexed_message

    def char_shifts(self, message, key):
        final_shifts = self.final_shifts
        message_shifts = []
        for index, _ in enumerate(message):
            # if index % 4 == 0:
            #     message_shifts.append(final_shifts['a_shift'])
            # elif index % 4 == 1:
            #     message_shifts.append(final_shifts['b_shift'])
            # elif index % 4 == 2:
            #     message_shifts.append(final_shifts['c_shift'])
            # elif index % 4 == 3:
            #     message_shifts.append(
            #         final_shifts['d_shift']
            #     )
            message_shifts.append(final_shifts[index % 4])
        return message_shifts

    def calc_shifts(self, message, key, date):
        # rounded = []
        # calcd = [
        #     sum(x)
        #     for x in zip(
        #         self.alphabetically_index_message(message),
        #         self.char_shifts(message, key, date)
        #     )
        # ]
        # for i in calcd:
        #     rounded.append(round(i%27))
        # return rounded
        return [
            (sum(x) % len(self.char_list))
            for x in zip(
                self.alphabetically_index_message(message),
                self.char_shifts(message, key)
            )
        ]

    def decrypt_calc_shifts(self, message, key, date):
        rounded = []
        array1 = self.alphabetically_index_message(message)
        array2 = self.char_shifts(message, key)
        subtracted_array = np.subtract(array1, array2)
        subtracted = list(subtracted_array)
        for i in subtracted:
            rounded.append(round(i % 27))
        return rounded

    def scramble(self, message, key, date):
        scrambled = []
        shifts = self.calc_shifts(message, key, date)
        [scrambled.append(self.char_list[e]) for e in shifts]
        # for (e) in shifts:
        #     scrambled.append(self.char_list[e])
        return "".join(scrambled)

    def unscramble(self, message, key, date):
        unscrambled = []
        shifts = self.decrypt_calc_shifts(message, key, date)
        for (e) in shifts:
            unscrambled.append(self.char_list[e])
        return "".join(unscrambled)


# wip = TuringMachine()
# message = 'keder ohulw'
# key = "02715"
# date = "040895"
# char_shifts = wip.char_shifts(message, key, date)
# alpha = wip.alphabetically_index_message(message)
# decalcd = wip.decrypt_calc_shifts(message, key, date)
# unscrambled = wip.unscramble(message, key, date)
# import ipdb; ipdb.set_trace()

# wip = TuringMachine()
# message = 'hello world'
# key = "02715"
# date = "040895"
# char_shifts = wip.char_shifts(message, key, date)
# alpha = wip.alphabetically_index_message(message)
# calcd = wip.calc_shifts(message, key, date)
# scrambled = wip.scramble(message, key, date)
# import ipdb; ipdb.set_trace()

# original = TuringMachine(name="OG")
# german_char = list(ALPHABET)
# german_char.append("B")
# german = TuringMachine(name="German", char_list=german_char)

# german._date = "newdate"
