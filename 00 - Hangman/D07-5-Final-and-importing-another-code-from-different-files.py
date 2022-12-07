# do 0: importing the values from another files and setup the condition
import random
from hangman_words import word_list
from hangman_art import stages, logo

end_of_game = False
lives = 6

# do 1: Randomizing the hidden word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f'Pssst, the solution is {chosen_word}.')  # revealing the words for debugging

# do 2: Converting the text length into a stripes
display = []
used_attempt = []
for stripes in chosen_word:
    display.append("_")

print(logo)
print("You have 6 chances to guess")
# do 4: looping the prompt
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Todo 7: Handling duplicate input from previous guess
    # print(f"used attempts: {used_attempt}")
    if guess in used_attempt or guess in display:
        print(f'You already guessed "{guess}" before, try another')

    # do 3: Check the guess vs random word
    for x in range(word_length):
        letter = chosen_word[x]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[x] = letter
    print(display)

    # do 5a: reducing the lives
    if guess not in chosen_word:
        '''indent level code ini harus sejajar dengan line 83 agar tidak nge run berkali kali sejumlah huruf 
        pada kata yang diambil'''
        used_attempt.append(guess)
        lives -= 1
        print(f"You have {lives} attempts remaining")

        # do 5b: ending the game using second exit point
        if lives == 0:  # syarat untuk mengakhiri game
            end_of_game = True  # kondisi spesifik untuk mengakhiri looping
            print(f'"Game Over"\nThe Correct Word is "{chosen_word}"')

    if "_" not in display:
        end_of_game = True  # exit condition pertama
        print("You Win")

    # Todo 6: print out the stages that represent to user's attempt
    print(stages[lives])

# bonus part
# untuk membersihkan previous log supaya tidak menumpuk seperti yang sudah-sudah:
# untuk replit: from replit import clear, kemudian tambahkan command "clear" pada line yang diperlukan supaya tampilan bisa mereset dari awal dan tidak menumpuk, i.e: setelah line 28
# untuk VS code MAC:
# import os

# def cls():
#     os.system('cls' if os.name=='nt' else 'clear')

# # now, to clear the screen
# cls()
