import sqlite3
conn = sqlite3.connect("CityTemperatures.db")
cursor = conn.cursor
sql = """
SELECT city, temperature
FROM tblTemps 
WHERE temperature >= 25
ORDER BY temperature DESC
"""
for row in curso.execute(sql):
    city, temperature = row
    print(row)
