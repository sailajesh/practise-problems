logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

import os
import subprocess

# For both Windows and Unix/Linux/Mac
subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)

# No need to import 'clear' module, as the clear function is defined in the same script.

print(logo)
bidders = {}

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for person in bidding_record:
        bid_amount = bidders[person]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = person
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while True:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bidders[name]=price
    print(bidders)

    more_bidders = input("Are there more bidders? Type 'yes' or 'no'. ")

    if more_bidders.lower() == "no":
        highest_bidder(bidders)
        break
    else:
        # Clear the console before the next iteration
        subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)
