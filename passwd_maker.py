import random
import string


# Creates a string of random ascii characters to use for password.
random_letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

print(random_letters
      )
# Variable to hold our new password.
generated_password = ""

# Ask the user to input the length of password they would like to generate.
character_count = int(input("Enter password character length needed. (Choose between 8 - 32): "))

# Test that the numbers are between 8 - 32.
if 8 > character_count > 32:
    print("Choose a value between 8 - 32")



