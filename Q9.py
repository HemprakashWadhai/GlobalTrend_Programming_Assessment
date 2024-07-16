#9. Write a Python function that generates a random password. The password should contain a mix of uppercase letters, lowercase letters, digits, and special characters.
import random
import string

def generate_random_password(length=12):
    # Define the character sets to choose from
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation  # Includes punctuation and symbols
    
    # Combine all characters
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    
    # Generate a password with random characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Example usage: Generate a random password of length 16
random_password = generate_random_password(16)
print("Random Password:", random_password)
