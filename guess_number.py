#get a number from user
#generate a random number from 0 upto the 1 which user entered
#ask the user to make a guess
#will display a message if guess number is correct
#if not correct, it will go ack and ask for the number again
#finally, it keeps the count of how many times the user tried
#at the end it will display the correct number and how many guesses it took

import random
ending_value = int(input("enter ending number: "))
random = random.randint(0,ending_value)
guess = 0
while True:
    num = int(input("enter a number which is your guess: "))
    if num == random:
        print("your guess is correct.")
        guess += 1
        break
    else:
        print("your guess is not correct.")
        guess += 1
print(f"you took {guess} guesses")
