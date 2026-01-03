print("Welcome To python Pizza Deliveries!")

price = 0

size = input("What size pizza do you want? S , M , L:").lower()
if (size == "s"):
  price+=250
elif (size == "m"):
  price+=500
else:
  price+=700

pepperoni = input("Do you want pepperoni on your pizza? Y or N:").lower()
if (pepperoni == "y"):
  price+=100
else:
  pass

cheese = input("Do you want extra cheese? Y or N:").lower()
if (cheese == "y"):
  price+=150
else:
  pass

print( f"Total bill for your Pizza is ${price}")
