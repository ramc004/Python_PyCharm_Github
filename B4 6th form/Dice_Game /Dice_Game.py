import random
import time
print("Welcome to your dice game ")
name = input("Please type the letter, 'n' , if you're are new user, if you are an existing user type the letter, 'e' :")
while name not in ('e', 'n'):
    name = input("Make sure you have typed 'e' for existing user or 'n' for new user.")

if name == "n":
    print("You need to register and to do this you need to make an account")
    username = input("type in a username that you are able to remember"
                     ", for example, maybe the first few letters of your "
                     "last name and the first letter of your first name "
                     "and 2 digits to make sure it can't be easily guessed")
    first_time_to_enter_password = input("Please enter your password")
    second_time_to_enter_password = input("Please re-enter your password")
    if first_time_to_enter_password == second_time_to_enter_password:
        print("Your password is", first_time_to_enter_password)
        f = open("username + password.txt", "a+")
        f.write(f"{username}:{second_time_to_enter_password}\n")
        f.close()
        name = input("Please type the letter, 'n', if you're are new user, if you are an existing user type the "
                     "letter, 'e' :")
    else:
        print("The password you entered does not match, please try again")

if name == "e":
    check = True
    while check:
        print("1st player enter your details")
        username1 = input("Username = ")
        password1 = input("Password = ")
        with open("username + password.txt", "r") as finder_username:
            for line in finder_username:
                if(username1 + ":" + password1) == line.strip():
                    print("You have been successfully logged in, congratulations!!!")
                    while check:
                        print("incorrect password or username, please try again, check for any errors like "
                              "spelling or an unneeded space")
                        username2 = input("Username = ")
                        password2 = input("Password = ")
                        with open("username + password.txt", "r") as finder_username1:
                            for line2 in finder_username1:
                                if(username2 + ":" + password2) == line2.strip():
                                    check = False
                                    print("You have been successfully logged in, Congratulations!!!")
                                    player1 = 0
                                    player2 = 0
                                    print("Welcome to the famous, the one and only, dice game")
                                    print("Is player 1 ready ")
                                    time.sleep(1)
                                    print("Is Player 2 ready")
                                    total_score1 = 0
                                    total_score2 = 0
                                    dice1 = random.randint(1, 6)
                                    dice2 = random.randint(1, 6)
                                    round_no = 1
                                    while round_no < 5:
                                        total_score1 = total_score1+player1
                                        total_score2 = total_score2+player2
                                        player1 = dice1+dice2
                                        round_no = round_no+1
                                        print("round", round_no)
                                        time.sleep(1)
                                        print("---")
                                        asdf = input("player 1, please can you press enter to roll")
                                        print("player 1 is rolling")
                                        print("player 1's first roll was", dice1)
                                        time.sleep(1)
                                        print("player 1's second roll was", dice2)
                                        time.sleep(1)
                                        print("---")
                                        if player1 % 2 == 0:
                                            print("This is an even number, so +10 points")
                                            time.sleep(1)
                                            player1 = player1 + 10
                                            time.sleep(1)
                                            print("score is", player1)
                                            if player1 <= 0:
                                                print("Better luck next time, sadly you lost the game")
                                                print("---")
                                            else:
                                                print("This is an odd number.")
                                                time.sleep(2)
                                                player1 = player1-5
                                                print("score is", player1)
                                                time.sleep(3)
                                                print("player 1 score", player1)
                                                print("---")

                                            time.sleep(1)
                                            dice1 = random.randint(1, 6)
                                            dice2 = random.randint(1, 6)
                                            total_score1 = total_score1+player1
                                            total_score2 = total_score2+player2
                                            player2 = dice1+dice2
                                            print("---")
                                            asdf2 = input("player 2 press enter to roll")
                                            print("player 2 is rolling")
                                            time.sleep(1)
                                            dice1 = random.randint(1, 6)
                                            dice2 = random.randint(1, 6)
                                            total_score1 = total_score1 + player1
                                            total_score2 = total_score2 + player2
                                            player2 = dice1 + dice2
                                            print("---")
                                            asdf = input("player 2 press enter to roll")
                                            print("player 2 is rolling")
                                            time.sleep(1)
                                            print("player 2's first roll is", dice1)
                                            time.sleep(1)
                                            asdf1 = input("player 2 press enter to roll again")
                                            time.sleep(1)
                                            print("player 2's second roll is", dice2)
                                            time.sleep(1)
                                            print("---")
                                            if player2 % 2 == 0:
                                                print("This is an even number. so +10 points")
                                                time.sleep(1)
                                                player2 = player2 + 10
                                                print("score is", player2)
                                                time.sleep(1)
                                                if player2 <= 0:
                                                    print("you have lost the game")
                                                    print("---")
                                            else:
                                                print("This is an odd number.")
                                                time.sleep(1)
                                                player2 = player2 - 5
                                                print("score is", player2)
                                                time.sleep(3)
                                                print("player 2 score", player2)
                                                print("---")

                                        print("the total score for player 1 is ", total_score1)
                                        print("the total score for player 2 is ", total_score2)
                                        if total_score1 > total_score2:
                                            print("player 1 wins")
                                            file = open("scores.txt2", "a+")
                                            file.write("player 1 ")
                                            file.write(username1)
                                            file.write(" has won overall with ")
                                            file.write(str(total_score1))
                                            file.write(" points")
                                            file.write("\n")
                                            if total_score2 > total_score1:
                                                print("player 2 wins")
                                            file = open("scores.txt2", "a+")
                                            file.write("player 2 ")
                                            file.write(username2)
                                            file.write(" has won overall with ")
                                            file.write(str(total_score2))
                                            file.write(" points")
                                            file.write("\n")
                                    else:
                                        print("incorrect username or password")
                    else:
                        print("incorrect username or password")