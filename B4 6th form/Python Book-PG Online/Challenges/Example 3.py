ucaseLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I",\
                "J", "K", "L", "M", "N", "O", "P", "Q", "R",\
                "S", "T", "U", "V", "W", "X", "Y", "Z"]
lcaseLetters = []
for letter in ucaseLetters:
    lcaseLetter = letter.low()
    lcaseLetters.append(lcaseLetter)
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
print("""Your password must contain at least 
        one uppercase letter
        one lowercase letter
        and one number. 
        It must be between 8 and 15 characters long\n""")
passwordChecks = 0
password = input("Please enter your new password: ")
while passwordChecks < 3:
    if len(password)>=8 and len(password)<=15:
        passwordChecks += 1
        for letter in password:
            if letter in lcaseLetters:
                passwordChecks += 1
            if letter in ucaseLetters:
                passwordChecks += 1
    if passwordChecks < 3:
        password = input("\nInvalid password - please re-enter: ")
        passwordChecks = 0
print("\nPassword accepted")