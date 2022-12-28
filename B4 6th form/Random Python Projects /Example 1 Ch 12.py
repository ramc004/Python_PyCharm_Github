import sqlite3
connection = sqlite3.connect("MyFilms.db")
cursor = connection.cursor()
sqlCommand = """CREATE TABLE tblFilms
                (
                filmID TEXT,
                title TEXT,
                yearReleased INTEGER
                rating TEXT,
                duration INTEGER
                genre TEXT,
                primary key (filmID)
                )"""
cursor.execute(sqlCommand)
print("tblFilms created in MyFilms.db")
connection.commit()
connection.close()
