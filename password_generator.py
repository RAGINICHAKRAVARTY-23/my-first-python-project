

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':',"'",'"',',','.','<','>','?','/']

print("Welcome to the Password generator program by python")

letters_range = int(input("How many letters would you like in your password?:\n"))
numbers_range = int(input("How many numbers would you like in your password?:\n"))
symbols_range = int(input("How many symbols would you like in your password?:\n"))

password_List = []
for chars in range(0,letters_range):
  password_List.append(random.choice(letters))
for _ in range(numbers_range):
    password_List.append(str(random.choice(numbers)))
for chars in range(0,symbols_range):
  password_List.append(random.choice(symbols))

random.shuffle(password_List)

password = ""
for chars in password_List:
  password+=chars

print(f"Your password is {password}")