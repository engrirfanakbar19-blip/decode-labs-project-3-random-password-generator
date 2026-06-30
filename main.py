import string 
import random

def generate_password():
    length = int(input("enter lenght of password:"))

    if length <= 0:
        print("Please enter positive number...")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation 
    password = ""
    
    for i in range(length):
        password += random.choice(characters)
    print("\nGenerated Password:", password)

while True:
    generate_password()
    choice = input("\n Generate another password? (y/n):").lower()
    if choice == "n":
        print("Thanks for using password generator...")
        break