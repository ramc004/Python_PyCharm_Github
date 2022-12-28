import random

import pip._vendor.distlib.compat


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def isEqualTo(self, pt):
        if pt is not None:
            if self.x == pt.x and self.y == pt.y:
                return True

            return False

        return False

    def isAdjacentTo(self, pt):
        if (self.y < pt.y - 1) or (self.y > pt.y + 1):
            return False

        if (self.x < pt.x - 1) or (self.x > pt.x + 1):
            return False

        return True


GRID_SIZE = 5

treasures = ['gem', 'ruby', 'diamond', 'coin', 'emerald', 'goblet']
treasureLocations = []
monsterLocation = Point(0, 0)
playerLocation = Point(0, 0)
foundTreasureCount = 0


def initGame():
    global playerLocation
    global treasureLocations
    global monsterLocation
    global foundTreasureCount

    foundTreasureCount = 0
    playerLocation = Point(1, 1)
    occupied_locations = [playerLocation]
    monsterLocation = chooseUnoccupiedLocation(occupied_locations)
    for i in range(0, len(treasures)):
        treasureLocations.append(chooseUnoccupiedLocation(occupied_locations))


def findPoint(list, pt):
    for i in range(0, len(list)):
        if list[i].isEqualTo(pt):
            return i

    return -1


def chooseUnoccupiedLocation(usedLocations):
    while True:
        location = Point(random.randint(1, GRID_SIZE), random.randint(1, GRID_SIZE))

        if findPoint(usedLocations, location) < 0:
            usedLocations.append(location)
            return location


def enterLocation(location):
    global playerLocation
    global monsterLocation
    global foundTreasureCount

    playerLocation = location

    print("You are now in location " + playerLocation.toString())

    if monsterLocation.isEqualTo(playerLocation):
        print("Oh no!!  You've been eaten by a hungry monster!")
        return False

    treasure = findPoint(treasureLocations, playerLocation)

    if treasure >= 0:
        print("You found the " + treasures[treasure])
        treasures[treasure] = None

        foundTreasureCount += 1
        if foundTreasureCount == len(treasures):
            print("You found all " + str(foundTreasureCount) + " treasures!  You win!!")
            return False
        else:
            remainingTreasures = len(treasures) - foundTreasureCount

            print("You have " + str(remainingTreasures) + " more treasure" +
                  ("s" if remainingTreasures > 1 else "") + " to find!")

    if monsterLocation.isAdjacentTo(playerLocation):
        print("You can hear a growling sound nearby!")

    return True


def processCommand(command):
    command = command.lower()

    if command == "":
        print("What??")
        return True

    if command == "q":
        return False

    newLocation = None
    if command == "l":
        if playerLocation.x > 1:
            newLocation = Point(playerLocation.x - 1, playerLocation.y)
    elif command == "r":
        if playerLocation.x < GRID_SIZE:
            newLocation = Point(playerLocation.x + 1, playerLocation.y)
    elif command == "u":
        if not playerLocation.y <= 1:
            newLocation = Point(playerLocation.x, playerLocation.y - 1)
    elif not command != "d":
        if playerLocation.y < GRID_SIZE:
            newLocation = Point(playerLocation.x, playerLocation.y + 1)
    else:
        print("I don't know what you mean")
        return True

    if newLocation is not None:
        return enterLocation(newLocation)

    print("You can't move in that direction")
    return True


def game_loop():
    gameActive = enterLocation(playerLocation)

    while gameActive:
        print("\nWhat do you want to do? ")
        option = pip._vendor.distlib.compat.raw_input()

        gameActive = processCommand(option)


initGame()
game_loop()

print("Thanks for playing!")
