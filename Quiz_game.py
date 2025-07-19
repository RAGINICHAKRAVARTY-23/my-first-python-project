print("Welcome to the Quiz Competition!")
print()

score = 0

a = input("1. What is the capital of India?: ")
if a.lower() == "new delhi":
    score += 1

b = input("2. What is the capital of Assam?: ")
if b.lower() == "dispur":
    score += 1

c = input("3. How many states are there in India?: ")
if c == "28":
    score += 1

d = input("4. Who is the Prime Minister of India?: ")
if d.lower() == "narendra modi":
    score += 1

e = int(input("5. How many bones does an adult have?: "))
if e == 206:
    score += 1

print()
print("You scored", score, "out of 5.")
