import sqlite3
conn = sqlite3.connect("CityTemperatures.db")
cursor = conn.cursor()
print("%-15s%20s%20s" %("City","Temperature","Local time"))
for row in cursor.execute
('SELECT * FROM tblTemps ORDER BY temperature DESC LIMIT 5'):
    city, temperature, localTime = row
    print ("%-15s %15d %20s" %(city, temperature, localTime))

