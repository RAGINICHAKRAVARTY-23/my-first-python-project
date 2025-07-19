words = input("Enter words: ").split()  # Makes a list of words
for word in words:
    for letter in word:
        if letter == "e":
            continue
        print(letter)
