nameList = []


name = input ("Enter name: ")
while name.lower() != "end":
    nameList.append(name)
    name = input("Enter next name, 'end' to finish: ")
midpoint = len(nameList)//2
newList = nameList[0:midpoint]
print(newList)
input("Press Enter to exit")
