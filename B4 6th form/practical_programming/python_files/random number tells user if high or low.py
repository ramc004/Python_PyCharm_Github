import random

totalguesses = 0 
number = random.randint(0,100)

print("Guess the hidden number between 0 and 100")
print("Enter your guess.")

guess = int(input())
totalguesses.append(guess)

while guess != number:
    if guess < number:
        print("Too low. Try again")
        guess == int(input())
        totalguesses.append(guess)
    elif guess < number:
        print("Too high. Try again")
        guess == int(input())
        totalguesses.append(guess)
    else:
        print("well done")

print("Correct! Well done.")
print("You guessed in", str(len(totalguesses)), "guesses")
