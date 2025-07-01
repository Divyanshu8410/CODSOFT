import random
import string
def password_generator():
    letter=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    print("------Welcome to password generator------")
    total_length = int(input("Enter total password length: "))
    n_letter=int(input("Enter number of letter you want to use in your password :"))
    n_digits=int(input("Enter number of digits you want to use in your password : "))
    n_special=int(input("Enter number of special character you want to use in your password :"))
    if n_letter + n_digits + n_special != total_length:
        print("Error: The sum of letters, digits, and special characters must equal total password length!")
        return
    password=""
    for i in range(1,n_letter+1):
        char=random.choice(letter)
        password+=char
    for i in range(1,n_digits+1):
        dig=random.choice(digits)
        password+=dig
    for i in range(1,n_special+1):
        spec=random.choice(special)
        password+=spec
    password_list=list(password)
    random.shuffle(password_list)
    generate_password = ''.join(password_list)
    print("Generated Password:", generate_password)

password_generator()
