import sqlite3
conn = sqlite3.connect("CityTemperatures.db")
cursor = conn.cursor
for row in cursor.execute:
    ('SELECT * FROM tblTemps ODER BY TEMPERATURE DESC')
    print(row)
    