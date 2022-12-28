monthName = ["January","February","March","April","May","June",\
         "July","August","September","October","November","December"]
monthlyAvg = []

for m in range(3):
    print("Enter average maximum and minimum for " + monthName[m])
    maximum = int(input("Maximum: "))
    minimum = int(input ("Minimum: "))
    row = [monthName[m], maximum, minimum]
    monthlyAvg.append(row)

print("\n")
for m in range (3):
    for index in range(3):
        print (monthlyAvg[m][index],end = " ")
    print("\n")
    
hottestTemp = -50
coldestTemp = 50
for m in range(3):
    month, maximum, minimum = monthlyAvg[m]
    if  maximum > hottestTemp:
        hottestTemp = maximum
        hottestMonth = month
    if  minimum < coldestTemp:
        coldestTemp = minimum
        coldestMonth = month
print("\nHottest month ", hottestMonth, "Maximum temperature ", hottestTemp)
print("Coldest month ",coldestMonth, "Minimum temperature ", coldestTemp)

