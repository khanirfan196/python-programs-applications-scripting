# Imports
import random

# variables

special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
numbers = "0123456789"
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
    pass

if __name__ == "__main__":
    # user input
    length = int(input("Enter the length of the password: "))
    total_letters = int(input("Enter the total number of letters: "))
    begin_with_letter = input("Should the password begin with a letter? (y/n): ").lower() == "y"
    if not begin_with_letter:
        letters = generate_letters(length, total_letters)
        print(letters)
