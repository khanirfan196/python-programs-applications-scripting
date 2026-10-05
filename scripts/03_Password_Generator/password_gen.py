# Imports
import random

# variables

special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
numbers = "0123456789"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

# generate password
def generate_password(length, total_letters):
    characters = random.choices(special_characters + numbers + uppercase_letters + lowercase_letters, k=length)
    if total_letters > length:
        raise ValueError("Total letters cannot be greater than password length")

    # Ensure the password contains at least one character from each category
    password = [
        random.choice(special_characters),
        random.choice(numbers),
        random.choice(uppercase_letters),
        random.choice(lowercase_letters)
    ]

    # Fill the rest of the password with random characters
    for _ in range(length - 4):
        password.append(random.choice(special_characters + numbers + uppercase_letters + lowercase_letters))

    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    # user input
    length = int(input("Enter the length of the password: "))
    total_letters = int(input("Enter the total number of letters: "))
    print("Generated Password:", generate_password(length, total_letters))
