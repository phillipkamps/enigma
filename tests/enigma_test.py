from ..lib.enigma import Enigma
from datetime import date

wip = Enigma()
key = "02715"
date_string = "040895"
message = "hello world"
caps_message = "HeLLo WoRlD"
cyphertext = "keder ohulw"


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

    def test_decrypt_single_arg(self):
        new = wip.encrypt('hello world')
        new_key = new['key']
        new_encryption = new['encryption']
        
        decrypted = wip.decrypt(new_encryption, new_key)
        assert decrypted is not None
        assert type(decrypted) is dict

        assert type(decrypted['decryption']) == str
        assert decrypted['decryption'] == 'hello world'

        assert type(decrypted['key']) == str
        assert len(list(decrypted['key'])) == 5
        assert decrypted['key'] == new_key
        
        assert type(decrypted['date']) == str
        assert len(list(decrypted['date'])) == 6
        assert decrypted['date'] == date.today().strftime("%d%m%y")
    
    def test_decrypt_with_args(self):
        decrypted = wip.decrypt(cyphertext, key, date_string)
        assert decrypted is not None
        assert type(decrypted) is dict
        assert decrypted == {
            "decryption": 'hello world',
            "key": "02715",
            "date": "040895"
        }