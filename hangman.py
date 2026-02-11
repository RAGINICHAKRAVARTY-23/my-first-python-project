import random 
from hangman_words import word_list
from hangman_art import logo , stages
print(logo)

def hangman():
  chosen_word = random.choice(word_list)
  placeholder = ""
  for letter in chosen_word:
    placeholder+="_"
  print(placeholder)

  lives = 7
  correct_letter = []
  game_over = False
  while not game_over:
    print(f"Your score is - 7/{lives}")
    user_guess = input("Guess a letter:\n").lower()

    if user_guess in correct_letter:
      print(f"You have already guessed {user_guess}")
      continue

    display = ""
    for letter in chosen_word:
      if letter == user_guess:
        display+=letter
        correct_letter.append(letter)
      elif letter in correct_letter:
        display+=letter
      else:
        display+="_"
    print(display)

    if user_guess not in chosen_word:
      lives -= 1
      print("Wrong you loose a live!")
    print(stages[lives])
    if lives == 0:
        print("You loose!")
        print(f"The correct word was {chosen_word}.")
        game_over = True

    if not "_" in display:
     print("Yeah! you won.")
     game_over = True
hangman()
continue_game = False
while not continue_game:
  choice = input("Would you like to continue with the hangman_game? (y/n):\n").lower()

  if choice == "y":
    print("Here you go!")
    hangman()
  elif choice == "n":
    print("See you later!")
    break
  else:
    print("Please type (y/n)")
