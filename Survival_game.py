print("="*50 + "\n")
print("  HELLO! WELCOME TO THIS ZOMBIE SURVIVAL GAME")
print("="*50 + "\n")

a = input("Press ENTER to continue...")

while a == "":
    print("\nYou're stuck in a city full of zombies.")
    print("At each level, you'll make a CHOICE.")
    print("If it's correct, you'll earn 10 points.")
    print("Let the survival begin.\n")
    break
else:
    print("You didn't press ENTER. Exiting game...")
    exit()

score = 0

print("-------LEVEL 1--------")
while True:
    c1 = input("You see a zombie coming to you. Do you want to RUN or FIGHT? ").lower()
    if c1 == "run":
        print("---WRONG CHOICE-- You couldn’t run because many zombies were waiting to catch you.")
        break
    elif c1 == "fight":
        print("---BRAVO-- You chose to fight! Smart move.")
        score += 10
        break
    else:
        print("Invalid choice. Please type RUN or FIGHT.")

print(f"Your current score is: {score}\n")


print("-------LEVEL 2--------")
while True:
    c2 = input("You find a dark alley. Do you go THROUGH it or AVOID it? ").lower()
    if c2 == "through":
        print("---WRONG CHOICE-- The alley was full of zombies!")
        break
    elif c2 == "avoid":
        print("---BRAVO-- You wisely avoided the alley.")
        score += 10
        break
    else:
        print("Invalid choice. Please type THROUGH or AVOID.")

print(f"Your current score is: {score}\n")


print("-------LEVEL 3--------")
while True:
    c3 = input("You see a safe house. Do you ENTER or KEEP MOVING? ").lower()
    if c3 == "enter":
        print("---BRAVO-- You found shelter and supplies!")
        score += 10
        break
    elif c3 == "keep moving":
        print("---WRONG CHOICE-- Zombies ambushed you on the street.")
        break
    else:
        print("Invalid choice. Please type ENTER or KEEP MOVING.")

print(f"Your current score is: {score}\n")


print("-------LEVEL 4--------")
while True:
    c4 = input("You hear a noise. Do you INVESTIGATE or IGNORE it? ").lower()
    if c4 == "investigate":
        print("---WRONG CHOICE-- It was a zombie trap!")
        break
    elif c4 == "ignore":
        print("---BRAVO-- You avoided unnecessary danger.")
        score += 10
        break
    else:
        print("Invalid choice. Please type INVESTIGATE or IGNORE.")

print(f"Your current score is: {score}\n")

print("-------LEVEL 5--------")
while True:
    c5 = input("You see a helicopter leaving. Do you RUN to it or STAY hiding? ").lower()
    if c5 == "run":
        print("---BRAVO-- You made it to safety! Congratulations, survivor!")
        score += 10
        break
    elif c5 == "stay":
        print("---WRONG CHOICE-- Zombies eventually found you.")
        break
    else:
        print("Invalid choice. Please type RUN or STAY.")

print(f"\nGame Over! Your final score is: {score}")
if score == 50:
    print("🏆 Perfect survival! You are a true zombie hunter!")
elif score >= 30:
    print("👍 Good job! You survived most dangers.")
else:
    print("💀 You barely survived. Better luck next time!")
