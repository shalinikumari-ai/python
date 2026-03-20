import re

def check_password_strength(password):
    score = 0
    suggestion = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestion.append("Use at least 8 characters")

    # Uppercase check
    if re.search("[A-Z]", password):
        score += 1
    else:
        suggestion.append("Add at least one uppercase letter")

    # Lowercase check
    if re.search("[a-z]", password):
        score += 1
    else:
        suggestion.append("Add at least one lowercase letter")

    # Digit check
    if re.search("[0-9]", password):
        score += 1
    else:
        suggestion.append("Add at least one number")

    # Special character check
    if re.search("[@#$%^&*!]", password):
        score += 1
    else:
        suggestion.append("Add at least one special character")

    # Strength decision
    if score <= 2:
        print("Weak Password")
    elif score == 3 or score == 4:
        print("Medium Password")
    else:
        print("Strong Password")

    # Suggestions
    if suggestion:
        print("Suggestions:")
        for s in suggestion:
            print("-", s)


# Taking input
password = input("Enter your password: ")
check_password_strength(password)
