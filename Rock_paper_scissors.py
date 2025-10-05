import random
emojis = {"r": "🪨", "p": "📄", "s": "✂️"}
valid_choices = ("r", "p", "s")

while True:
    user_choice = input(" ENTER OUR CHOICE --Rock, Paper, Scissors- (r/p/s): ").lower()

    if user_choice not in valid_choices:
        print("Invalid choice! Please choose from (r/p/s).")
        continue

    computer_choice = random.choice(valid_choices)

    print(f"Computer chose: {emojis[computer_choice]}")
    print(f"You chose: {emojis[user_choice]}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "r" and computer_choice == "s")
        or (user_choice == "p" and computer_choice == "r")
        or (user_choice == "s" and computer_choice == "p")
    ):
        print("You win!🔥")
    else:
        print("Computer wins!")

    ask_to_continue = input("Do you want to play again? (yes/no): ").lower()
    if ask_to_continue == "no":
        print("Thanks for playing! 👋")
        break

