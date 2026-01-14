from gavelart import logo
print(logo)

def find_highest_bidder(bids):
    highest_bid = max(bids.values())

    for name in bids:
        if bids[name] == highest_bid:
            print(f"The winner is {name} with a bid of ${highest_bid}.")

bids = {} #dictionary 
continue_bidding = True
while continue_bidding:
  name = input("What is your name:\n") #key
  price = int(input("What is your bid:\n$ ")) #value
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()
  if should_continue == "no":
    continue_bidding = False
    find_highest_bidder(bids)
  elif should_continue == "yes":
    print("\n" * 20) 