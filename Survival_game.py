print("="*50 + "\n")
print("  HELLO! WELCOME TO THIS ZOMBIE SURVIVAL GAME")
print("="*50 + "\n")

# Press enter to continue
a = input("Press ENTER to continue...")

# Start game only if ENTER is pressed
while a == "":
    print("\nYou're stuck in a city full of zombies.")
    print("At each level, you'll make a CHOICE.")
    print("If it's correct, you'll earn 10 points.")
    print("Let the survival begin.\n")
    break
else:
    print("You didn't press ENTER. Exiting game...")
    exit()
print("-------LEVEL 1--------")

# Initializing  score
score = 0

# First choice
c1 = input("You see a zombie coming to you. Do you want to RUN or FIGHT? ")lower()
while True:
    c1 = input("You see a zombie coming to you. Do you want to RUN or FIGHT? ")lower()

    if c1 == "run":
        print("---WRONG CHOICE-- You couldn’t run because many zombies were waiting to catch you.")
        # Loop continues (asks again)
        
    elif c1 == "fight":
        print("---BRAVO-- You chose to fight! Smart move.")
        score += 10
        break  # Valid input, exit loop
        
    else:
        print("Invalid choice. Please type RUN or FIGHT.")
        # Loop continues (asks again)



# Show score
print(f"Your current score is: {score}")

