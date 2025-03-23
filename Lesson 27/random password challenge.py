import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits  # Only letters and numbers
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password

# Ask the user
a = input("Would you like a random password? (Y/N): ")

if a.upper() == "N":
    exit()
elif a.upper() == "Y":
    length = int(input("Enter password length: "))
    print("Your password is:", generate_password(length))
else:
    print("Please enter Y or N.")
    