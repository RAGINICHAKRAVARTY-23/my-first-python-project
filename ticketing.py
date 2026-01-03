print("welcome to the python roller coster ride!")
price = 0

height = int(input("Enter your height: "))
if (height >= 120):
  pass
else:
  print("Sorry, you are not eligible for it.")
  exit()

age = int(input("Enter your age: "))
if (age<12):
  price+=5
  print("Child tickets costs $5")
elif (age<=18):
  price+=7
  print("Youth tickets cost $7")
elif (age>=45):
  print("Enojy your ride. It is free.")
else:
  price+=12
  print("Adults tickets costs $12")

photo = input("Do you want any photos ( Y or N): ").lower()
if (photo=="y"):
  price+=2
  print("Photos will cost $2")
else:
  print(f"The total cost for your ride is ${price}")
  print("Fine,enjoy your ride.")
  exit()

print(f"The cost of your ride is ${price}")
