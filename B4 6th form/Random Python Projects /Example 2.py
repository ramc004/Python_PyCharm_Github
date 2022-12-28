import sqlite3
def readTextFile(filmFile):
    connection = sqlite3.connect("MyFilms.db")
    cursor = connection.cursor()
    numRecs = 0
    filmDBRec = []
    filmTextRec = filmFile.readline()
    while filmTextRec != "":
        numRecs += 1
        field = filmTextRec.split(", ")
        ID = field[0]
        title = field[1]
        yearReleased = field[2]
        rating = field[3]
        duration = int(field[4])
        genre = field[5]
        lastchar = len(genre)- 1
        genre = genre[0:lastchar]
        print(ID, title, yearReleased, rating, duration, genre)
        filmDBRec.append(ID)
        filmDBRec.append(title)
        filmDBRec.append(yearReleased)
        filmDBRec.append(rating)
        filmDBRec.append(duration)
        filmDBRec.append(genre)
        cursor.execute ("INSERT INTO tblFilms VALUES (?,?,?,?,?,?)",
        filmDBRec)
        connection.commit()
        filmDBRec = []
        filmTextRec = filmFile.readline()
    connection.close()
    return numRecs
filmFile = open("films.txt", "r")
numRecs = readTextFile(filmFile)
print("\n", numRecs, "records transferred")
filmFile.close()
