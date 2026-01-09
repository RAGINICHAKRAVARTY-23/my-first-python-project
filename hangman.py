import random
from hangman_words import word_list
from hangman_art import stages , logo
print(logo)

chosen_word = random.choice(word_list)
placeholder = ""
for i in range(len(chosen_word)):
  placeholder+="_"
print(placeholder)
game_over = False
lives = 7
correct_word = []
while not game_over:
  print(f"************{lives}/7 lives left************")
  user_input = input("Guess one letter :\n").lower()

  if user_input in correct_word:
    print( f"You have already guessed {user_input} ")
    continue
  display = ""
  for letter in chosen_word:
    if letter == user_input:
      display+=letter
      correct_word.append(letter)
    elif letter in correct_word:
      display+=letter
    else:
      display+="_"
  print(display)

  if user_input not in chosen_word:
    lives-=1
    print(f"You guessed {user_input} which is incorrect.You loose a life")
    if lives == 0:
      print(f"YOU LOOSE!\n*****The correct word was {chosen_word}******")
      game_over = True

  if "_" not in display:
    print(f"YOU WON!!")
    game_over = True
  
  print(stages[lives])

