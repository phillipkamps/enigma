import random
from datetime import date
from lib.turing_machine import TuringMachine
import turing_machine

class Enigma:
    def encrypt(self, message, key = str(random.randint(10000, 99999)), date = date.today().strftime("%d%m%Y")):
        machine = TuringMachine()
        return dict(
            encryption = machine.scramble(message),
            key = key,
            date = date)

# wip = Enigma()
# wip.encrypt("sup", "12345", "99999999")
