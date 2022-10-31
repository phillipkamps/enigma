from enigma import Enigma
from argparse import ArgumentParser

if __name__ == "__main__":
    key = input("enter key")
    message = "hello world"
    # key = "12345"
    # date = "110122"
    wip = Enigma()
    print(wip.encrypt(message))
