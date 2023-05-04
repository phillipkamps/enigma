import sys, time

def loading_text(text):
    print(f'{text}', end="")
    for i in range(5):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.5)

def return_to_mm():
    page_action = input("\nPress [enter] to return to main menu")
    if page_action == "":
        exit

def encrypt_presenter(machine_output):
    divider = "-"*64
    print("\n" + divider)
    print(f"Your key is:{machine_output['key']}")
    print(f"Encrypted message:{machine_output['encryption']}")
    print(divider)

def decrypt_presenter(machine_output):
    divider = "-"*64
    print("\n" + divider)
    print(f"Message reads: {machine_output['decryption']}")
    print(divider)