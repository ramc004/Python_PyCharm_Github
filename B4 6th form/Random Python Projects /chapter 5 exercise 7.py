markList = []
total = 0
name = input("Enter student name: ")
for test in range(10):
    testNumber = test + 1
    mark = int(input("Enter mark for test "+ str(testNumber) +": "))
    total+= mark
    markList.append(mark)

average = round(total/10,1)
sortedMarks = sorted(markList, reverse = True)

print(name)
print("\nTop 3 marks")
for n in range(3):
    print(sortedMarks[n])
print("\nBottom 3 marks")

for n in range(9,6,-1):
    print (sortedMarks[n])

print("\nAverage mark: ", average)    
input("\nPress Enter to exit ")

