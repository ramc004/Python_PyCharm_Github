# if statements


mark = int(input("Please enter your grade:"))
if mark > 81 and mark <=100:
    print ("You have gained a mastering grade well done!!!!!!!!!!!")
elif mark > 61 and mark <=80:
    print ("You have gained a deepening grade well done")
elif mark > 41 and mark <=60:
    print ("You have gained a securing grade you will need to revise a bit more to gain a better grade")
elif mark > 21 and mark <=40:
    print("You have gained a developing grade, you will need to revise a lot more to get a good enough grade")
elif mark > 0 and mark <=20:
    print("You have gained an emerging grade, this is not acceptable")
else:
    print("You have an invalid grade, pls have another look")
    
    
    
