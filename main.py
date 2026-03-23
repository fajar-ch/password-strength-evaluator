def evaluate_password(pwd):
    strength = 0

    # Length rule
    if len(pwd) >= 8:
        strength += 2
    elif len(pwd) >= 5:
        strength += 1

    # Character checks
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in pwd:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in "!@#$%^&*":
            has_special = True

    # Add score
    strength += has_upper + has_lower + has_digit + has_special

    # Final decision
    if strength <= 2:
        return "Weak"
    elif strength <= 4:
        return "Moderate"
    else:
        return "Strong"


# Run program
password = input("Enter your password: ")
print("Password Strength:", evaluate_password(password))