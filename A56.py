# 56. Generate a random password of 8 characters.
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

# Example usage
print("Generated password:", generate_password())
