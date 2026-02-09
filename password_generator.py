import random , string
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("============================WELCOME TO PYTHON PASSWORD GENERATOR============================================")
def generate_password():
  letter_range  = int(input("How many letters would you like in your password?:\n"))
  numbers_range = int(input("How many numbers would you like in your password?:\n"))
  symbols_range = int(input("How many symbols would you like in your password?:\n"))

  password_list = []
  for char in range (0, letter_range):
    password_list.append(random.choice(letters))
  for char in range (0, numbers_range):
    password_list.append(random.choice(numbers))
  for char in range (0,symbols_range):
    password_list.append(random.choice(symbols))
  
  random.shuffle(password_list)
  password = "".join(password_list)
  print(f"Your password has been generated successfully\n{password}")
generate_password()

should_continue = False
while not should_continue:
  user_choice = input("Are you satisfied with your password? (y/n):").lower()
  if user_choice == "y":
    print("All thanks to Ragini!")
    should_continue = True
  elif user_choice == "n":
    print(f"Here you go again!!")
    generate_password()
  else:
    print ("Please type 'y' or 'n'")

