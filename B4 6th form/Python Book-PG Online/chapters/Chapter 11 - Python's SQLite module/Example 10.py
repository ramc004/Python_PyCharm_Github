import sqlite3
def amend():
    with sqlite3.connect("CityTemperatures.db") as conn:
        cursor = conn.cursor()
        for row in cursor.execute("SELECT * FROM tblTemps"):
            print(row)
        keyfield = input("Enter city name of the record to amend: ")
        keyfield = "'" + keyfield + "'"
        field = input("Change which field \
        (temperature or localTime)? ")
        newvalue = input("Enter the new value for this field: ")
        try:
            cursor.execute("UPDATE tblTemps SET " + field + "=" +
            newvalue + "WHERE city = " + keyfield)
            print("\nRecord updated")
        except:
            print("\nNo record updated - invalid data entered ")
        for row in cursor.execute("SELECT * FROM tblTemps"):
            print(row)
amend()
