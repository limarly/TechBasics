import random
import string
import os

os.system("clear")

characters = list(string.ascii_letters + string.punctuation)

print("Welcome to the password generator :D")

password_length = int(input("How many characters do you need for your password?:"))

def password_generator(characters, password_length):

    random.shuffle(characters)

    password = characters[0:password_length]

    password_generated = "".join(password)

    return (password_generated)

final_password = password_generator(characters, password_length)

print(f"The final password is {final_password}")


#password = []

#for i in range(alphabets_count):