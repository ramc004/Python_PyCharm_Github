storedPassword = "EHQAB6"
passwordOK = False
password = input("Please enter your password: ")
while not passwordOK:
    codedPassword = ""
    for num in range(len(password)):
        asciiValue = ord(password[num])
        codedValue = asciiValue + 3
        if codedValue > ord("X"):
            codedValue -= 26
        codedPassword = codedPassword + chr(codedValue)
    if storedPassword == codedPassword:
        print("Password accepted")
        passwordOK = True
    else:
        input("Password incorrect - please re-enter: ")
