import random
scores = [["AAA01",135],
          ["BBB01",87],
          ["CCC01",188],
          ["DDD01",109]
          ]
userID = ""
userID = input ("Please enter userID: ")

while userID !="xxx":    

    listLength = len(scores)
    found = False
    for n in range (listLength):
        if userID in scores[n][0]:
            print ("Found at position ",n)
            found = True
            position = n
    if not found:
        print("UserID not found... appending it at position ", listLength)
        position = listLength
        scores.append([userID,0])
    print(scores)
          
             
    gameScore = random.randint(50,200)
    print("\nScore for this game: ",gameScore)
    if gameScore > scores[position][1]:
        scores[position][1] = gameScore
    print (scores)          
    
    userID = input ("Please enter userID, xxx to end: ")
input("Press Enter to exit ")

