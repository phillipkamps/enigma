from ..src.turing_machine import TuringMachine
import pytest
# import sys
# sys.path.insert(0, '/enigma/lib/turing_machine.py')
# from turing_machine import TuringMachine


key = "02715"
date = "040895"
message = "hello world"
caps_message = "HeLLo WoRlD"
test = TuringMachine()

class TestTuringMachine():
    def test_alphabetically_index_message(self):
        alphabetically_indexed_message = test.alphabetically_index_message(message)
        assert alphabetically_indexed_message is not None
        assert type(alphabetically_indexed_message) is list
        assert alphabetically_indexed_message == [7, 4, 11, 11, 14, 26, 22, 14, 17, 11, 3]
    
    def test_alphabetically_index_message_caps(self):
        alphabetically_indexed_message = test.alphabetically_index_message(caps_message)
        assert alphabetically_indexed_message is not None
        assert type(alphabetically_indexed_message) is list
        assert alphabetically_indexed_message == [7, 4, 11, 11, 14, 26, 22, 14, 17, 11, 3]

    def test_char_shifts(self):
        char_shifts = test.char_shifts(message, key, date)
        assert char_shifts is not None
        assert type(char_shifts) is list
        assert char_shifts == [3, 27, 73, 20, 3, 27, 73, 20, 3, 27, 73]
    
    def test_calc_shifts(self):
        calc_shifts = test.calc_shifts(message, key, date)
        assert calc_shifts is not None
        assert type(calc_shifts) is list
        assert calc_shifts == [10, 4, 3, 4, 17, 26, 14, 7, 20, 11, 22]
    
    def test_decrypt_calc_shifts(self):
        scrambled_message = 'keder ohulw'
        decrypt_calc_shifts = test.decrypt_calc_shifts(scrambled_message, key, date)
        assert decrypt_calc_shifts is not None
        assert type(decrypt_calc_shifts) is list
        assert decrypt_calc_shifts == [7, 4, 11, 11, 14, 26, 22, 14, 17, 11, 3]
    
    def test_scramble(self):
        scrambled = test.scramble(message, key, date)
        assert scrambled is not None
        assert type(scrambled) is str
        assert scrambled == 'keder ohulw'
    
    def test_unscramble(self):
        scrambled = test.scramble(message, key, date)
        unscrambled = test.unscramble(scrambled, key, date)
        assert unscrambled is not None
        assert type(unscrambled) is str
        assert unscrambled == 'hello world'