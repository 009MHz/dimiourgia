import os
def cls():
    os.system('cls' if os.name =='nt' else 'clear')
# HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

# do 2: check the auction winner
def bid_winner(bidding_process):
    max_bid = 0
    winner = ''
    for x in bidding_process:  # mencari value lelangnya dari argument yg diberikan
        if bidding_process[x] > max_bid:  # validasi current harga lelang vs harga tertinggi
            max_bid = bidding_process[x]  # substitute max bid menjadi harga max terbaru
            winner = x.title()  # substitute previous bid winner (dict key) menjadi pemilik max bid terbaru
    print(f'The auctions is winning by "{winner}" with ${max_bid}.')


# do 1: auction process
sold = False
auctions = {}  # empty dict to store nama bidder dan harga lelang nya
while not sold:
    bidder = input("What's your name? ")
    price = int(input("How many your offer?: $"))
    auctions[bidder] = price  # storing nama dan nilai lelangnya ke dict
    prompt = input("Is there any higher bid? Type 'yes' or 'no'.\n").lower()
    if prompt == "no":
        sold = True
        bid_winner(auctions)  # calling function untuk menentukan pemenangnya dari dict yg dibuat
    else:
        cls()
        print(f'Last bid is ${price}')