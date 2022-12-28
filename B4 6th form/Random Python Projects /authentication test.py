print("Welcome to your dice game ")
name = input("Please type the letter, 'n' , if you're are new user, if you are an existing user type the letter, 'e' :")
while name not in ('e', 'n'):
    name = input("Make sure you have typed 'e' for existing user or 'n' for new user.")

if name == "n":
    print("You need to register and to do this you need to make an account")
    username = input("type in a username that you are able to remember, "
                     "for example, maybe the first few letters of your last name "
                     "and the first letter of your first name and 2 digits "
                     "to make sure it can't be easily guessed")
    first_time_to_enter_password = input("Please enter your password")
    second_time_to_enter_password = input("Please re-enter your password")
    if first_time_to_enter_password == second_time_to_enter_password:
        print("Your password is", first_time_to_enter_password)
        f = open("username + password.txt", "a+")
        f.write(f"{username}:{second_time_to_enter_password}\n")
        f.close()
        name = input("Please type the letter, 'n' "
                     ", if you're are new user, "
                     "if you are an existing user type the letter, 'e' :")
    else:
        print("The password you entered does not match,"
              " please try again")
        if name == "e":
            check = True
            while check:
                print("1st player enter your details")
                username1 = input("Username = ")
                password1 = input("Password = ")
                with open("username + password.txt", "r") as finder_username1:
                    for line in finder_username1:
                        if(username1 + ":" + password1) == line.strip():
                            print("You have been successfully logged in, congratulations!!!")
                            while check:
                                print("incorrect password or username, "
                                      "please try again, "
                                      "checking for any errors like spelling or an extra unneeded space")
                                username2 = input("Username = ")
                                password2 = input("Password = ")
                                with open("username + password.txt", "r") as finder_username2:
                                    for username2 in finder_username2:
                                        if(username2 + ":" + password2) == line.strip():
                                            check = False
                                            print("You have been successfully logged in, Congratulations!!!")
