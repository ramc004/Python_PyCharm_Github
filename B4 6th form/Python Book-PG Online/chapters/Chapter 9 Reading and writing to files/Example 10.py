filmFile = open("films.txt", "r")
filmRec = filmFile.readline()
while filmFile != "":
    field = filmRec.split(",")
    ID = field[0]
    title = field[1]
    rating = field[2]
    duration = int(field[4])
    genre = field[5]
    if rating == "G":
        print(ID, title, rating, duration)
        filmRec = filmFile.readline()
filmFile.close()
