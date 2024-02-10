import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+','-','*','/']

print("welcome to the password generator: ")
user_letters = int(input("enter number of letters in your password: "))
user_numbers = int(input("enter number of digits in your password: "))
user_symbols = int(input("enter number of symbols in your password: "))

password = []

for i in range(1,user_letters+1):
    random = random.choice(letters)
    password += random
for i in range(1,user_numbers+1):
    random = random.choice(numbers)
    password += random
for i in range(1,user_symbols+1):
    random = random.choice(symbols)
    password += random

random.shuffle(password)

print(f"Your Password is: {password}")
