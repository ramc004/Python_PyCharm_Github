print("%-20s%20s%20s%20s"
%("City", "Temperature(C)", "Temperature(F)", "Local time"))
for n in range (len(sortedTable)):
    print("%-20s%20.1f%20s"
    %(sortedTable[n][0], sortedTable[n][1], sortedTable[n][2], 
      sortedTable[n][3]))
