"""Phase 4: Re-Styling and Code debugging"""
# Todo 0: Import ASCII, module and print the logo from art.py when the program starts.
from art import logo
import os
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
def caesar(texting, shifting, directioning):
    crypt_text = ""
    for letter in texting:
        # Todo 1: Handling the code when user input any letters that outside the list range
        if letter in alphabet:  # Cek user input apakah ada dalam list atau tidak
            pos = alphabet.index(letter)
            if direction == "encode":
                new_pos = pos + shifting
                while new_pos >= 26:  # Reverting position jika hasil shifting di luar range
                    new_pos -= 26
            elif direction == "decode":
                new_pos = pos - shifting
                while new_pos < 0:  # Reverting position jika hasil shifting di luar range
                    new_pos += 26
            crypt_text += alphabet[new_pos]
        # Todo 2: Debugging the code when user input is number or symbol
        else:
            crypt_text += letter  # returning user input jika bukan text (not exist in list)
    print(f'The {direction}d result: "{crypt_text}"\n')


print(logo)
# Todo 4: Looping the code based on user prompt to use or ending the programs
stop = False  # key awal untuk memulai looping command input
while not stop:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Todo 3: Checking the output
    caesar(texting=text, shifting=shift, directioning=direction)
    restart = input('Type "Yes" if you want to run again, type "No" if you decide to stop?\n').lower()
    cls()
    if restart == "no":
        stop = True  # key  untuk mengakhiri looping command input
        print("\nI'll see you next time")
