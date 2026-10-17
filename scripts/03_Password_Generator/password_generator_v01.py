# Imports
import random

# variables

special_characters = "@#$%&*|~"
digits = "0123456789"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

def generate_letters(length, total_letters):
    if length < 0 or total_letters < 0:
        raise ValueError("Length and number of letters must be non-negative.")
    if total_letters > length:
        raise ValueError("Number of letters cannot be greater than the password length.")
    return "".join(
        random.choice(uppercase_letters + lowercase_letters)
        for _ in range(total_letters)
    )


# generate password
def generate_password(length, total_letters, begin_with_letter=False):
    if begin_with_letter:
        letters = generate_letters(length, total_letters)
        password = letters
        special_chars = "".join(random.choice(special_characters) for _ in range(1))
        nums = "".join(random.choice(digits) for _ in range(length - total_letters - 1))
        password += special_chars
        password += nums
        return password
    else:
        special_chars = "".join(random.choice(special_characters) for _ in range(length - total_letters))
        letters = generate_letters(length, total_letters)
        password = letters + special_chars
        return password

if __name__ == "__main__":
    # user input
    length = int(input("Enter the length of the password: "))
    total_letters = int(input("Enter the total number of letters: "))
    begin_with_letter = input("Should the password begin with a letter? (y/n): ").lower() == "y"
    if begin_with_letter:
        password = generate_password(length, total_letters, begin_with_letter=begin_with_letter)
        print(password)
    else:
        password = generate_password(length, total_letters)
        print(password)
