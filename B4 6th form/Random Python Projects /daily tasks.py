studentMarks = {"Wesley":5, "Jo":9, "Betty":6, "Robina":5}
studentMarks.get("Betty","not found")
studentMarks.get("Bill","not found")
studentMarks.keys()
studentMarks.values()
studentMarks.items()
name = input("Enter a student's name to look up: ")
if name in studentMarks:
    print("Mark: ", studentMarks[name])
else:
    print("Name not found")
print(" Finished yay ")
print("Hello","\N{winking face}")
print("\U0001F923")
