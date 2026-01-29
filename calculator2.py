def add(n1, n2):
    return n1 + n2

def subtract(n1, n2): 
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        # show available operations
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Please enter the operation: ")
        num2 = float(input("What is the second number?: "))

        # calling the function stored in dictionary
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: "
        )

        if choice == "y":
            num1 = answer  # continue calculation
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()  # restart calculator fresh

calculator()
