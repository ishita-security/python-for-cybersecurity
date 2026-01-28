# password_strength_checker.py
# Checks password strength based on common security rules

import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"[0-9]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    if length_error:
        return "Weak: Password must be at least 8 characters long"
    if uppercase_error:
        return "Weak: Password must contain an uppercase letter"
    if lowercase_error:
        return "Weak: Password must contain a lowercase letter"
    if digit_error:
        return "Weak: Password must contain a number"
    if symbol_error:
        return "Weak: Password must contain a special character"

    return "Strong password"

# Example usage
password = input("Enter a password to check: ")
result = check_password_strength(password)
print(result)
