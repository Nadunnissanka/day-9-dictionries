import art
from replit import clear
#HINT: You can call clear() to clear the output in the console.

print(art.logo)
print("Welcome to 4G Auction..\n")

have_bidders = True
bid_history = {}

def create_dictionary(name, bid_ammount):
    bid_history[bider_name] = bid_ammount

while have_bidders:
    #ask for bid
    bider_name = input("Enter Your Name: ")
    bid = int(input("What is your bid: $"))

    create_dictionary(name = bider_name, bid_ammount = bid)
    
    
    any_new_bidders = input("Are there any other bidders? Type 'yes or 'no'.")
    if any_new_bidders == "yes":
        clear()
    else:
        clear()
        have_bidders = False
        max = 0
        for bider in bid_history:
          bid_value = bid_history[bider]
          if bid_value > max:
              max = bid_value
              name_won = bider
              
        print(f"{name_won} won the bid by bidding ${max}")
          

    