import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Set the desired password length (default is 8 characters)
password_length = 10

# Generate and print a password
password = generate_password(password_length)
print("Generated Password:", password)
