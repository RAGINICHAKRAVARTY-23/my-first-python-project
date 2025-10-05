import time
import random

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 1
MAX_OPERAND = 15
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = str(left) + " " + operator + " "  + str(right)
    answer = eval(expression)
    return expression , answer




start_quiz = input("Do you want to start the quiz? Type 'yes' to begin: ").strip().lower()
if start_quiz == "yes":
    print("Quiz started!")
    start_time = time.time()
    for i in range(TOTAL_PROBLEMS):
        expression, answer = generate_problem()
        while True:
            guess = input(f"Problem #{i+1}: {expression} = ")
            if guess == str(answer):
                print("Correct!")
                break
            else:
                print("Wrong, try again!")
    end_time = time.time()
    total_time = end_time - start_time
    print(f"You completed all {TOTAL_PROBLEMS} questions in {total_time:.2f} seconds!")
else:
    print("Quiz not started.")




