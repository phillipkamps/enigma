from enigma import Enigma
import helpers

while True:
    enigma = Enigma()

    action = input("""\
             _____ _   _ ___ ____ __  __    _    
            | ____| \ | |_ _/ ___|  \/  |  / \   
            |  _| |  \| || | |  _| |\/| | / _ \  
            | |___| |\  || | |_| | |  | |/ ___ \ 
            |_____|_| \_|___\____|_|  |_/_/   \_\\
                                                               
Would you like to (e)ncrypt, (d)ecrypt, get (i)nfo, or (q)uit?
""")

    if action == "e":
        message = input("Enter message:\n")
        key = input("Enter 5-digit key (to generate a random key press [enter]):\n")
        output = enigma.encrypt(message, key)
        helpers.loading_text("Encrypting")
        helpers.encrypt_presenter(output)
        helpers.return_to_mm()

    elif action == "d":
        cyphertext = input("Enter encrypted message:\n")
        key = input("Enter 5-digit key:\n")
        date = input("Enter message receipt date [ddmmyy]:\nIf message was received today press [enter]\n")
        output = enigma.decrypt(cyphertext, key, date)
        helpers.loading_text("Decrypting")
        helpers.decrypt_presenter(output)
        helpers.return_to_mm()

    elif action == "i":
     print("""
     The Enigma machine is a cipher device developed and used in the 
     early- to mid-20th century to protect commercial, diplomatic, 
     and military communication. It was considered so secure that it
     was used to encipher the most top-secret messages.\n
     An Enigma operator would be given a plaintext message to 
     encrypt. After setting up his machine, he would type the 
     message on the Enigma keyboard. For each letter pressed, one 
     lamp lit indicating a different letter according to a pseudo-
     random substitution determined by the electrical pathways 
     inside the machine. The letter indicated by the lamp would be 
     recorded, as the cyphertext letter. The action of pressing a 
     key also moved rotors so that the next key press used a 
     different electrical pathway, and thus a different substitution
     would occur even if the same plaintext letter were entered 
     again. This process continued until the message was completed.
     The cyphertext recorded by the second operator would then be 
     transmitted to an operator of another Enigma machine. This
     operator would type in the cyphertext and — as long as all the 
     settings of the deciphering machine were identical to those of
     the enciphering machine — for every key press the reverse 
     substitution would occur and the plaintext message would emerge.\n
     The security of the system depends on machine settings that were
     generally changed daily, based on secret key lists distributed 
     in advance, and on other settings that were changed for each 
     message. The receiving station would have to know and use the 
     exact settings employed by the transmitting station to 
     successfully decrypt a message.""")
     helpers.return_to_mm()

    elif action == "q":
        break

    else:
        helpers.loading_text("Input not recognized, try again")
