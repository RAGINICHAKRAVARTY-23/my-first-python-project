num = 23
while True:
    user_num = int(input("Guess a number between 1-25:"))
    if user_num == num:
        print("🎉 Congratulations, you guessed it correct!\n")
        break
    else:
        print("❌ Wrong guess. Try again...")

print("YOU HAVE COMPLETED THE GAME")
