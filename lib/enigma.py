import random
from datetime import date
from turing_machine import TuringMachine

class Enigma:
    def encrypt(self, message, key = str(random.randint(10000, 99999)), date = date.today().strftime("%d%m%y")):
        machine = TuringMachine()
        return dict(
            encryption = machine.scramble(message, key, date),
            key = key,
            date = date)

wip = Enigma()
test = wip.encrypt("hello world", "02715", "040895")
import ipdb; ipdb.set_trace()