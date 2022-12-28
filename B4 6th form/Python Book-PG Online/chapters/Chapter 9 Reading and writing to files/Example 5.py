filmFile = open("films.txt", "r")
for row in filmFile:
    field = row.split(", ")
    ID = field[0]
    title = field[1]
    yearReleased = field[2]
    rating = field[3]
    duration = int(field[4])
    genre = field[5]
    lastchar = len(genre)- 1
    genre = genre[0:lastchar]
    if genre == "comedy":
        print(ID, title, yearReleased, rating, genre, duration)
    filmFile.close()