cursor.execute("INSERT INTO tblTemps VALUES (?, ?, ?)", myRec)
conn.commit()
try:
    cursor.execute("INSERT INTO tblTemps VALUES (?, ?, ?)", myRec)
    conn.commit()
except:
    print("\nA record for this city already exists")
    