name =input("Enter your name:")
while name == "":
    print("Name is mandotatory")
    name = input("Enter your name:")
else:
    print(f"hello {name}")