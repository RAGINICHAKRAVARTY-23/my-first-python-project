operator = input("Enter an operator(+ - * /):")
num1 =int(input("Enter the 1st number:"))
num2 = int(input("Enter the 2nd number:"))
print("")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print(f"{operator} is not valid. choose from (+ - * /)")

