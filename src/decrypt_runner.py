from enigma import Enigma

cyphertext = "put encrypted string here"
key = "12345"
# date = "110122"
wip = Enigma()
print(wip.decrypt(cyphertext, key))
