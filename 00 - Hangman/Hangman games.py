import random
import os
from hangman_words import word_list
from hangman_art import stages, logo

# Clearing screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


end_of_game = False
lives = 6

# Randomizing the hidden word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f'Pssst, the solution is {chosen_word}.')  # words revealing for debugging

# Converting the text length into a stripes
display = []
used_attempt = []
for stripes in chosen_word:
    display.append("_")

print(logo)
print("You have 6 chances to guess")
# looping the prompt
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    cls()  # only working on VS code

# Fixing duplicate input from previous guess
    # print(f"used attempts: {used_attempt}")
    if guess in used_attempt or guess in display:
        print(f'You already guessed "{guess}" before, try another')

# Check the guess vs random word
    for x in range(word_length):
        letter = chosen_word[x]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[x] = letter
    print(display)

# Reducing the lives
    if guess not in chosen_word:
        used_attempt.append(guess)
        lives -= 1
        print(f"You have {lives} attempts remaining")

# Ending the game using second exit point
        if lives == 0:  # game over condition
            end_of_game = True
            print(f'\n\n"Game Over"\nThe Correct Word is "{chosen_word}"')

    if "_" not in display:
        end_of_game = True  # exit condition pertama
        print("You Win")

    # Todo 6: print out the stages that represent to user's attempt
    print(stages[lives])
