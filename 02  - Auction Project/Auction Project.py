import os
from art import logo
def cls():
    os.system('cls' if os.name =='nt' else 'clear')  # only work using VS code


print(logo)
# Check the auction winner
def bid_winner(bidding_process):
    """Function to check the auction winner"""
    max_bid = 0
    winner = ''
    for x in bidding_process:
        if bidding_process[x] > max_bid:
            max_bid = bidding_process[x]
            winner = x.title()
    print(f'The auctions is winning by "{winner}" with ${max_bid}.')


# Auction processes
sold = False
auctions = {}
while not sold:
    bidder = input("What's your name? ")
    price = int(input("How many your offer?: $"))
    auctions[bidder] = price
    # print(auctions)  # used for debugging
    prompt = input("Is there any higher bid? Type 'yes' or 'no'.\n").lower()
    if prompt == "no":
        sold = True
        bid_winner(auctions)
    else:
        cls()
        print(f'Last bid is ${price}')