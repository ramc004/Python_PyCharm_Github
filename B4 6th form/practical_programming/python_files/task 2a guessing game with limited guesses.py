import random
guessesTaken = 0
print('Hello! What is your name?')
myName = input()
number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
while guessesTaken < 6:
     print('Take a guess.') # There are four spaces in front of print.
     guess = input()
     guess = int(guess)
     guessesTaken = guessesTaken + 1
     guessesTakenAllowed = 3
     if guess < number:
         print('Your guess is too low.') # There are eight spaces in front of print.
         if guess > number:
             print('Your guess is too high.')
             if guess == number in guessesTakenAllowed:
                 guessesTaken = str(guessesTaken)
                 print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
                 if guessTaken == guessesTakenAllowed:
                     print("You have run out of guesses the number was", number)
