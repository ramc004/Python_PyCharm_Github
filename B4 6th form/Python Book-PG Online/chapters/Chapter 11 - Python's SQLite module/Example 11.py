import sqlite3
def deleteRec(dbname):
    conn = sqlite3.connect (dbname)
    with conn:
        cursor = conn.cursor()
        myCity = input("Enter name of city to delete: ")
        keyfield = "'" + myCity + "'"
        cursor.execute("DELETE FROM tblTemps WHERE CITY =" +
keyfield)
    for row in cursor.execute("SELECT * FROM tblTemps"):
        print(row)
deleteRec("cityTemperatures.db")
input ("\nPress Enter to exit")
