import random
import string

def generate_password(length=10):
    if length < 8:
        print("Length should be at least 8")
        return None
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password
