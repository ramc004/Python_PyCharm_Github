import random

from pip._vendor.distlib.compat import raw_input

n = random.randint(1, 99)
guess = int(raw_input("Enter an integer from 1 to 99: "))
while n != "guess":
    if guess < n:
        print("guess is too low")
        guess = int(raw_input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print("guess is too high")
        guess = int(raw_input("Enter an integer from 1 to 99: "))
    else:
        print("you guessed it!")
        break
