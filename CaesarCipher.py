import string
from CaesarCipherart import art
print(art)
alphabet = list(string.ascii_lowercase)

print("*************************---->WELCOME TO CAESAR CIPHER<----*****************************")

def caesar(original_text, shift_amount, encode_or_decode):
  output_text = ""
  if encode_or_decode == "decode":
        shift_amount*=-1
  for letter in original_text:
    if letter not in alphabet:
      output_text+=letter
    else:
      shift_position = alphabet.index(letter) + shift_amount
      shift_position%=len(alphabet)
      output_text+=alphabet[shift_position]
  print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True

while should_continue:
  direction = input("Do you want to 'encode' or 'decode' message:\n").lower()
  text = input("Enter your message:\n").lower()
  shift = int(input("Enter the shift number:\n"))

  caesar(original_text=text , shift_amount=shift , encode_or_decode=direction)

  restart = input("Type 'yes' if you want to go again . Oterwise type 'no' .\n").lower()
  if restart == 'no':
    should_continue = False
    print("Goodbye")


