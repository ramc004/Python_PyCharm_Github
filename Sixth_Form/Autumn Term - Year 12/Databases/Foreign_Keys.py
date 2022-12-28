import sqlite3


with sqlite3.connect("myForeignKeyDB.db") as db:
    cur =db.cursor
    cur.execute("PRAGMA foreign_keys = ON")
    db.commit()


    sql = """CREATE TABLE IF NOT EXISTS tblStudent
            (StudentID TEXT PRIMARY KEY AUTOINCREMENT,
            FName TEXT,
            SName TEXT,
            DOB DATE,
            Course ID TEXT,
            FOREIGN KEY (Course I) REFERNCES tblCourse(Course ID)
            )"""