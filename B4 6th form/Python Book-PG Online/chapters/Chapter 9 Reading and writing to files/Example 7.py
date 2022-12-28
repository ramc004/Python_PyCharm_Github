tempsFile = open("temperature.txt", "a")
print("This program writes temperature data to \n"
      "temperature.txt")
print("If the file does not exist, it will be created")
city = input("Enter city name, xxx to end: ")


while city != "xxx":
    temperature = input("Enter temperature: ")
    localTime = input("Enter local time: ")
    tempsFile.write(city + "," + temperature + "," + localTime
                    + "," + "\n")
    city = input("Enter city name, xxx to end: ")
filmFile.close()
