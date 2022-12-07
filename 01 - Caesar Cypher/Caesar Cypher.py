from art import logo
import os
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
def caesar(texting, shifting, directioning):
    crypt_text = ""
    for letter in texting:
        # Fixing the code when user input any letters that outside the list range
        if letter in alphabet:
            pos = alphabet.index(letter)
            if direction == "encode":
                new_pos = pos + shifting
                while new_pos >= 26:
                    new_pos -= 26
            elif direction == "decode":
                new_pos = pos - shifting
                while new_pos < 0:
                    new_pos += 26
            crypt_text += alphabet[new_pos]
        # Debugging the code when user input is number or symbol
        else:
            crypt_text += letter
    print(f'The {direction}d result: "{crypt_text}"\n')


print(logo)
# Looping the code based on user prompt to use or ending the programs
stop = False
while not stop:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Checking the output
    caesar(texting=text, shifting=shift, directioning=direction)
    restart = input('Type "Yes" if you want to run again, type "No" if you decide to stop?\n').lower()
    cls()
    if restart == "no":
        stop = True
        print("\nI'll see you next time")
