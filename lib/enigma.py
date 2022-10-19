from platform import machine
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

    def decrypt(self, cyphertext, key, date = date.today().strftime("%d%m%y")):
        machine = TuringMachine()
        return dict(
            decryption = machine.scramble(cyphertext, key, date),
            key = key,
            date = date
        )
wip = Enigma()
key = '02715'
date_str = '040895'
message = 'keder ohulw'
result = wip.decrypt(message, key, date_str)
import ipdb; ipdb.set_trace()