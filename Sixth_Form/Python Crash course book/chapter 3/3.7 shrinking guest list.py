invitees = ['Steve Jobs', 'my family', 'George', 'Tim Cook']
invitees.insert(0, 'Elise')
invitees.insert(1, 'Jeffrey')
invitees.append('Ben')
del invitees[0]
del invitees[1]
del invitees[2]
del invitees[3]
invitees.pop(0)
message0 = "I would like to invite you, " + invitees[0].title() + " to an astounding dinner ."
message1 = "I would like to request for you , " + invitees[1].title() + " to come to a very special dinner."
print("Hello, we have found a bigger dinner table ")
print(message0)
print(message1)
message5 = invitees
print("Hello, the following people are invited due to a larger dinner table: ", message5)
print("Oh no, really sorry for the short notice but only two people are invited")
invitees.pop(0)
sorry0 = "sorry you cannot come, " + invitees[0].title() + "."
print(sorry0)
invitees.pop(1)
sorry1 = "sorry you cannot come, " + invitees[1].title() + "."
print(sorry1)
invitees.pop(3)
sorry3 = "sorry you cannot come, " + invitees[3].title() + "."
print(sorry3)
lucky4 = "You can still come, " + invitees[4].title() + "."
print(lucky4)
lucky5 = "You can still come, " + invitees[5].title() + "."
print(lucky5)
print(invitees)
