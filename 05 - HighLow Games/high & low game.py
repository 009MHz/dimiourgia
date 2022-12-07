import os
import random
from art import logo, vs
from game_data import data


def topics():
    """Generate a random account from the game data."""
    return random.choice(data)


def details(topic):
    """Function to convert randomized dictionary into printable format"""
    figure = topic['name']
    details = topic['description']
    city = topic['country']
    # print (f'{figure}, a {details}, from {city}.')  # for debugging purpose
    return f'{figure}, a {details}, from {city}'


def checker(answer, a_count, b_count):
    """User input validation"""
    if b_count > a_count:
        return answer == "b"
    else:
        return answer == "a"


def game():
    """Game Continuation"""
    game_proceed = True
    print(logo)
    score = 0
    a_topic = topics()
    b_topic = topics()
    while game_proceed:
        a_topic = b_topic
        b_topic = topics()

        while a_topic == b_topic:
            b_topic = topics()
        
        print(f'Compare A: {details(a_topic)}.')
        print(vs)
        print(f'Against B: {details(b_topic)}.')
        # prompt to answer
        answer = input('Who has more follower? Type "A" or "B": ').lower()
        
        # Comparing the data contents
        a_follower = a_topic["follower_count"]
        b_follower = b_topic["follower_count"]
        correct_answer = checker(answer, a_follower, b_follower)

        os.system('clear')
        # Scoring based on correct answer
        if correct_answer:
            score += 1
            print(f'BRAVO! Current score: "{score}".')
        else:
            game_proceed = False
            print(f'Incorrect! Your final score is: "{score}".')
            print(f'the "A" count is {a_follower} & the "B" count is {b_follower}')


while input('\nType "y" to start the game, or type "n" to end the session? ').lower() == "y":
    game()
else:
    print("See you next time")