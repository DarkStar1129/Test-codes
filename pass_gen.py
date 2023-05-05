# Random password generator

import random
import string

# Function to generate a random password
def generate_password(length, numbers, special_chars, capital_letters):
    # Define the set of characters to choose from based on user input
    chars = string.ascii_lowercase
    if numbers:
        chars += string.digits
    if special_chars:
        chars += string.punctuation
    if capital_letters:
        chars += string.ascii_uppercase

    # Generate a password with the desired length using the chosen characters
    password = ''.join(random.choice(chars) for i in range(length))

    return password

# Prompt user for desired password length and options
print("Random Password Generator")
print("Choose options:")
print("1. Include numbers")
print("2. Include special characters")
print("3. Include capital letters")
print("4. Include numbers and special characters")
print("5. Include numbers and capital letters")
print("6. Include special characters and capital letters")
print("7. Include all options")

# User input for options
options = input("Enter choice(1/2/3/4/5/6/7): ")
numbers = False
special_chars = False
capital_letters = False

if options == '1':
    numbers = True
elif options == '2':
    special_chars = True
elif options == '3':
    capital_letters = True
elif options == '4':
    numbers = True
    special_chars = True
elif options == '5':
    numbers = True
    capital_letters = True
elif options == '6':
    special_chars = True
    capital_letters = True
elif options == '7':
    numbers = True
    special_chars = True
    capital_letters = True
else:
    print("Invalid input")
    exit()

# User input for password length
length = int(input("Enter password length (6-20): "))
if length < 6 or length > 20:
    print("Invalid length")
    exit()

# Generate and print the password
password = generate_password(length, numbers, special_chars, capital_letters)
print("Your random password is:", password)