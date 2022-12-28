invitees = ['Steve Jobs', 'my family', 'George', 'Tim Cook']
invitees.insert(0, 'Elise')
invitees.insert(1, 'Jeffrey')
invitees.append('Ben')
message0 = "I would like to invite you, " + invitees[0].title() + " to an astounding dinner ."
message1 = "I would like to request for you , " + invitees[1].title() + " to come to a very special dinner."
message2 = "I would like for you, " + invitees[2].title() + " to come to dinner."
message3 = "I would like to ask you, " + invitees[3].title() + " to a delicious dinner."
print("Hello, we have found a bigger dinner table ")
print(message0)
print(message1)
print(message2)
print(message3)
message5 = invitees
print("Hello, the following people are invited due to a larger dinner table: ", message5)


