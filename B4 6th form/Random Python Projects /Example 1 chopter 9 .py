filmFile = open("films.txt", "r")
films = filmFile.read()
print(films)
filmFile.close()
