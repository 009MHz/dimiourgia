# 0 importing random, importing logo, creating global scope from cards deck
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

"""function ambil kartu"""
def deal_cards():
    draw = random.choice(cards)
    return draw


"""function CEK BLACKJACK"""
def score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # ACE REPLACEMENT
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def play_game():
    user_card = []
    bot_card = []
    """randoming 2 cards for both player"""
    for x in range(2):
        user_card.append(deal_cards())
        bot_card.append(deal_cards())

    # GAME CONTINUATION
    print(logo)
    blackjack = False
    while not blackjack:
        user_score = score(user_card)
        print(f'Your cards are {user_card} and your score is {user_score}')
        bot_score = score(bot_card)
        print(f'BOT cards are [{bot_card[0]}, X] ')
        if user_score == 0 or bot_score == 0 or user_score > 21:
            blackjack = True
        else:
            proceed = input('\nType "y" to draw next card, type "n" to pass\n')
            if proceed == "y":
                user_card.append(deal_cards())
            else:
                blackjack = True

    while bot_score != 0 and bot_score < 17:
        bot_card.append(deal_cards())
        bot_score = score(bot_card)

    def compare(last_user, last_bot):
        if user_score == bot_score:
            return "\nIt's a draw"
        elif user_score == 0 or user_score == 21:
            return "\nIt's Your BLACKJACK"
        elif bot_score == 0 or bot_score == 21:
            return "\nIt's BOT BLACKJACK"
        elif user_score > 21 and bot_score < 21:
            return "\nYou're BUSTED"
        elif user_score < 21 and bot_score > 21:
            return "\nYou WIN"
        elif user_score < 21 and bot_score < 21:
            if user_score > bot_score:
                return "\nYou WIN"
            elif user_score < bot_score:
                return "\nYOU LOSE"
        else:
            return "\nGame Over"

    """END MESSAGE"""
    print(compare(last_user=user_score, last_bot=bot_score))
    print(f'Your hands got {user_card} and your score is {user_score}')
    print(f'BOT hands got {bot_card} and AI score is {bot_score}')


while input('\nType "y" to start the game, or type "n" to end the session? ').lower() == "y":
    play_game()
else:
    print("See you next time")
    
    
# changes for cherry pick to beta
