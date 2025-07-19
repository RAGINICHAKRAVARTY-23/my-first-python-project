words = input("Enter words: ").split()  # M
for word in words:
    for letter in word:
        if letter == "e":
            continue
        print(letter)
