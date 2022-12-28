import random

total guesses = []

number = random.randint(1,100)

print ("Guess the hidden number bewtween 1 and 100")
print ("Enter your guess.)

guess = int(input())
totalguesses.append(guess)

while guess != number:
    if guess < number:
       print ("Too low. Try again")
       guess  = int(input())
       totalguesses.append(guess)
    elif guess < number:
       print ("Too high. Try again")
       guess  = int(input())
       totalguesses.append(guess)

print("Correct! Well done.")
       
       
       

