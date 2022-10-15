from silentauctionart import logo
import os
clear = lambda: os.system('cls')

still_bidding = True

auction_bids = {}

print(logo)
print("Welcome to silent auction program!")

still_bidding = True

while still_bidding:
    bidder = input("What is your name? ")
    bid = int(input("What's your bid $ "))
    auction_bids[bidder] = bid
    anymore = input("Are there anymore bidders? ")
    if anymore == "no":
        still_bidding = False
   
    clear()

highest_bidder = str(max(auction_bids, key = auction_bids.get))
high_bid = auction_bids[highest_bidder]

print(f"The winner is {highest_bidder} with a bid of ${high_bid}!")