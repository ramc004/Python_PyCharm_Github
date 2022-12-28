def getAndPrintName(message):
    name = input("Please enter your name: ")
    print(message, name)
    return name 
playerName = getAndPrintName("Hello")
print(playerName, "is player 1")
