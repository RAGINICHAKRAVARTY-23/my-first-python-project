print(''' ****************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
******************************************************************************* ''')

print("Welcome to Treasure Island\nYour mission is to find the treasure.\nYou will get 10 points for each good choice.")

score = 0
print("----LEVEL 1----")

direction = input("In which direction do you want to go - LEFT or RIGHT? : ").lower()

if direction == "right":
    print("Bad choice!\nYou fell into a hole.\nThe game is over.")
    print(f"Your score is {score}")
    exit()
else:
    score += 10
    print(f"Good choice!\nYour score is {score}")


print("----LEVEL 2----")
second_choice = input("As you move foward , you see a river.\nDo you want to SWIM or WAIT ? : ").lower()

if (second_choice == "swim"):
    print("Bad choice!\nThere was a crocodile in the river.\nThe game is over")
    print(f"Your score is {score}")
    exit()
else:
    print(f"Good choice! Your score is {score}")
    score+=10

print("----LEVEL 3 ----")
third_choice = input("As you wait you see 3 doors - Which door do you want to choose? YELLOW BLUE or RED ? :")

if (third_choice=="red"):
    print("Bad choice!\nYou are burned by fire")
    print(f"Your score is {score}")
    exit()
    
elif (third_choice=="yellow"):
    print("Bad choice!\nYou are eaten by zombies at the yellow door.")
    print(f"Your score is {score}")
    exit()
else:
    print("Good choice!\nYou escaped out from the blue door")
    score+=10
    print(f"YOU WON\nYour score is {score}")

print('''
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
          """""""`     """"""''')
    


