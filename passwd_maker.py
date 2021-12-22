import string
from random import choice

# Creates a string of random ascii characters to use for password.
random_letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

# Variable to hold our new password.
generated_password = ""

# Ask the user to input the length of password they would like to generate.
character_count = int(input("Enter password character length needed. (Choose between 8 - 32): "))
while len(generated_password) != character_count:
    generated_password += choice(random_letters)

print(generated_password)
