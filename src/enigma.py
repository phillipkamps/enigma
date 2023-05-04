import random
from datetime import date as dtobj
from turing_machine import TuringMachine

class Enigma:
    def encrypt(self, message, key, date = dtobj.today().strftime("%d%m%y")):
        machine = TuringMachine()
        if key == '':
           key = f'{random.randint(10000, 99999)}'
        return {
            "encryption": machine.scramble(message, key, date),
            "key": key,
            "date": date
            }

    def decrypt(self, encrypted_message, key, date):
        machine = TuringMachine()
        if date == '':
            date = dtobj.today().strftime("%d%m%y")
        return {
            "decryption": machine.unscramble(encrypted_message, key, date),
            "key": key,
            "date": date
        }

# wip = Enigma()
# key = '02715'
# date_str = '040895'
# message = 'keder ohulw'
# result = wip.decrypt(message, key, date_str)
# import ipdb; ipdb.set_trace()