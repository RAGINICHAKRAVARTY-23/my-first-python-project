from string import punctuation as spl

def password_strength_checker(password):
    score = 0

    if any(chr.isdigit() for chr in password):
        score += 1
    else:
        print("Password must contain at least one digit")

    if any(chr.isupper() for chr in password):
        score += 1
    else:
        print("Password must contain at least one uppercase letter")

    if any(chr.islower() for chr in password):
        score += 1
    else:
        print("Password must contain at least one lowercase letter")

    if len(password) >= 8:
        score += 1
    else:
        print("Password is too short. It should contain minimum 8 characters")

    if any(chr in spl for chr in password):
        score += 1
    else:
        print("Password must contain at least one special character")

    if score == 5:
        return "STRONG"
    elif score >= 3:
        return "MEDIUM"
    else:
        return "TOO WEAK"

password_input = input("Enter your password: ")
data = password_strength_checker(password_input)
print(f" REMARKS -- Password is {data}")
