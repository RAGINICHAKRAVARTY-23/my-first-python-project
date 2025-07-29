print("Welcome to Quiz Competition")
score = 0

a = input("1. What is the capital of Assam?: ")
if a.lower() == "dispur":
    score += 1

b = input("2. What is the capital of India?: ")
if b.lower() == "new delhi":
    score += 1

c = input("3. Who wrote the national anthem of India?: ")
if c.lower() == "rabindranath tagore":
    score += 1

d = input("4. What is the largest 2 digit number?: ")
if d == "99":
    score += 1

e = input("5. Who was the first president of India?: ")
if e.lower() == "rajendra prasad":
    score += 1

f = input("6. Which is the smallest state in India?: ")
if f.lower() == "goa":
    score += 1

g = input("7. Which animal has a long nose called 'trunk'?: ")
if g.lower() == "elephant":
    score += 1

h = input("8. What was the first colour of Doraemon?: ")
if h.lower() == "yellow":
    score += 1

i = input("9. Which is the tallest land animal?: ")
if i.lower() == "giraffe":
    score += 1

j = input("10. Which is the national bird of India?: ")
if j.lower() == "peacock":
    score += 1

print(f"\nYOU SCORED {score} OUT OF 10")
