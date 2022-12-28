import sqlite3
conn = sqlite3.connect("CityTemperatures.db")
cursor = conn.execute
myRec = []
city = input("\nEnter city name: ")
while city != "xxx":
    temperature = int(input ("Enter temperature: "))
    localTime = input ("Enter local time: ")
    myRec.append(city)
    myRec.append(temperature)
    myRec.append(localTime)
    cursor.execute("INSERT INTO tblTemps VALUES (?, ?, ?)", myRec)
    conn.commit()
    myRec = []
    city = input("\nEnter city name (xxx to end): ")