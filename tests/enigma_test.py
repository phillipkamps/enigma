from ..lib.enigma import Enigma
from datetime import date

wip = Enigma()
key = "02715"
date_string = "040895"
message = "hello world"
caps_message = "HeLLo WoRlD"


class TestEnigma():
    def test_encrypt_single_arg(self):
        encrypted = wip.encrypt("hello world")
        assert encrypted is not None
        assert type(encrypted) is dict

        assert type(encrypted['encryption']) == str

        assert type(encrypted['key']) == str
        assert len(list(encrypted['key'])) == 5
        
        assert type(encrypted['date']) == str
        assert len(list(encrypted['date'])) == 6
        assert encrypted['date'] == date.today().strftime("%d%m%y")
    
    def test_encrypt_with_args(self):
        encrypted = wip.encrypt(message, key, date_string)
        assert encrypted is not None
        assert type(encrypted) is dict
        assert encrypted == {
            "encryption": "keder ohulw",
            "key": "02715",
            "date": "040895"
        }