import random
playGame = True
while playGame:
    codeArray = []
    for x in range(4):
        codeArray.append(random.randint(0, 9))
    latestCode = "****"
    totalGuesses = 0
    isGuessing = True
    while isGuessing:
        print(latestCode)
        userGuess = input("What is the code?: ")
        newString = ""
        userCorrect = True
        for x in range(4):
            if userGuess[x] == str(codeArray[x]):
                newString += str(codeArray[x])