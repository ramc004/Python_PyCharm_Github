print("Welcome top your dice game")
name = input("Please type the letter, 'n' , if you're are new user, if you're and existing user type the letter, 'e' :")
while name not in ('e', 'n'):
    name = input("Make sure you have typed 'e' for existing user or 'n' for new user.")

if name == "n":
    print("You need  ")