from tkinter import *
import os
# This is to import the python library tkinter to be able to build a graphical user interface using its framework
# I have imported os to allow my system to access how the user interacts with their device in relation to my system


def register():
    """this function is the code for the 'Register' window
       whenever the user doesn't have an account yet but would like to create one"""
    global register_screen
    # I have created a variable called register_screen which I will use to show the user the register screen when they
    # first want to create an account,
    # this also globalises the variable allowing us to call the variable through the program in different functions
    register_screen = Toplevel(main_screen)
    # Register button to be connected to the main screen
    register_screen.title("Register")
    # Gives the register screen a title of 'Register'
    register_screen.geometry("500x800")
    # This gives the register screen a value of 500 along the 'x' axis and a value of 800 on the 'y' axis
    register_screen.resizable(False, False)
    # This makes the register screen not resizable
    global email_address
    # This creates a variable called 'email_address' and allows us to use it throughout the program
    global password
    # This creates a variable called 'password' and globalises it allowing us to use it throughout the program
    global email_address
    # using the function 'global' to allow us to reuse the variable 'password_entry' throughout various functions
    global password_entry
    # using the function 'global' to allow us to reuse the variable 'password_entry' throughout various functions
    email_address = StringVar()
    # sets the variable 'email_address' to be a variable with the data type of string
    password = StringVar()
    # Sets the variable 'password' to be a string meaning the user can enter numbers, special characters and letters
    email_address_label_2 = Label(register_screen, text="email address ", font=("Comic Sans MS", 15))
    # creating a label requesting for the users email address
    # giving the text 'email address' a font of Comic Sans and a size of 15
    email_address_label_2.pack()
    # tells the system where to place our request asking for the users email address
    email_address = Entry(register_screen, textvariable=email_address)
    # creates a box for the user to enter their email address into
    # converts whatever the user enters inside this box into a string, so it can then be stored in the text file
    email_address.pack()
    # system efficiently packs the email address box inside the register window
    password_label_2 = Label(register_screen, text="Password * ", font=("Comic Sans MS", 15))
    # creates a new variable 'password_label_2' and sets it equal to Tkinter's label function
    # places this new variable inside our register screen
    # requesting for the user's password
    password_label_2.pack()
    # places this new variable, so it fits perfectly within our window
    password_entry = Entry(register_screen, textvariable=password, show='*')
    # this ensures security
    # whenever the user is entering their password the system will show * instead of the actual password
    # creates another variable this time 'password entry'
    # using Tkinter's entry function will allow the user to input their desired password
    password_entry.pack()
    # tells system to pack our password entry box
    # in the window in an efficient way to ensure everything else fits nicely
    Label(register_screen, text="").pack()
    # gives a bit of spacing to our window and packs it inside the window
    Button(register_screen, text="Register",
           width=10,
           height=1,
           command=register_user,
           font=("Comic Sans MS", 15)).pack()
    # creates a button with text of register which when clicked will redirect the user to the register user window
    # gives a smaller font to this text compared to the title


def login():
    """this is the code for the login function
    when the user clicks their login button the below function will be performed"""
    global login_screen
    # creates a variable called login_screen and allows it to be used throughout our program
    login_screen = Toplevel(main_screen)
    # tells the system where to place the login_screen
    login_screen.title("Login")
    # uses the tkinter built-in function title to give our window a clear title on the border of the window
    login_screen.geometry("500x800")
    # sets the beginning size of the window with a 500 width and an 800 length
    Label(login_screen, text="Please enter details below to login", font=("Comic Sans MS", 15)).pack()
    # creates a new label and packs it inside the window
    # gives it some text telling the user how they must fill in their details
    Label(login_screen, text="").pack()
    # this is space label to force some space between each button to make all the buttons and labels fit neatly
    login_screen.resizable(False, False)
    # from the beginning size of 500 width and 800 length it stops the user from changing this size
    global email_address_verify
    # calls the variable 'email_address_verify' and allows it to be used throughout the program
    # this will be used to check that the email address the user is using to log in has an account linked
    global password_verify
    # calls the variable 'password_verify' and allows it to be called from anywhere in the program
    # ensures the password the user has entered exists with its corresponding email
    email_address_verify = StringVar()
    # defines 'email_address_verify' and sets it equal to a string variable
    # so when it is saved in the file it is saved as a string variable
    password_verify = StringVar()
    # defines 'password_verify' and will convert whatever is passed into this variable as a string variable
    global email_address_login_entry
    # calls 'email_address_login_entry' and allows it to be called inside and outside this function
    global password_login_entry
    # allows another variable which will be created below
    # has the ability to be called anywhere throughout the program
    Label(login_screen, text="email address * ", font=("Comic Sans MS", 15)).pack()
    # makes another label gives it a text of 'email address *' telling the user to please enter an email address
    # it has a font of Comic Sans and a text size of 15
    email_address_login_entry = Entry(login_screen, textvariable=email_address_verify)
    # making another variable 'email_address_login_entry' placing it inside the login_screen
    # tells the system to convert whatever was entered into a string
    email_address_login_entry.pack()
    # packs the entry box in our window,
    # system ensures it fits with all the rest of the buttons, labels and entry boxes
    # without overshadowing a particular one
    Label(login_screen, text="").pack()
    # blank space label to allow for adequate spacing between all the attributes
    Label(login_screen, text="Password * ", font=("Comic Sans MS", 15)).pack()
    # this makes another label and packs this label
    # requests the user to enter their password they would like to match with the email entered
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    # new variable 'password_login_entry' setting equal to the 'Entry' function built inside Tkinter
    # places it inside the login_screen
    # calls our variable from above and the system will be told to convert the text inside this entry box into a string
    # this string will then be called later and stored inside our text file
    password_login_entry.pack()
    # collects the variable that have been packed so far and reorders each one as well as this new one
    # ensures no overlaps between each one
    Label(login_screen, text="").pack()
    # forces some space between the password entry and the below login button packing it inside the window
    Button(login_screen, text="Login", width=10, height=1, command=login_verify, font=("Comic Sans MS", 15)).pack()
    # final button for this function
    # when the user clicks the 'Login' button the program will run through the login_verify function


def register_user():
    """this is the function that will be called when the user has clicked the register button
    this will select what the user has entered inside the relevant boxes and write to a text file"""
    email_address_info = email_address.get()
    # creates a new variable and sets it equal to the email address the user has entered
    password_info = password.get()
    # creates another new variable for password and sets it equal to whichever password the user decided to create
    file = open(email_address_info, "w")
    # using the built-in file function opens a new file and stores it as the name of the email entered
    file.write(email_address_info + "\n")
    # writes the email address the user entered inside the file
    file.write(password_info)
    # writes the password on a new line
    file.close()
    # closes the file to tell the system to stop writing or reading from the file
    email_address.delete(0, 0)
    # resets the email address box setting each to 0
    password_entry.delete(0, 0)
    # resets the password box after they have clicked on register
    Label(register_screen, text="Registration Success", fg="green", font=("Comic Sans MS", 15)).pack()
    # tells the user their information has been successfully added to a file in green text to symbolise success


def login_verify():
    """this function ensure the users details exist
    when they have clicked on the login button within the login screen"""
    email_address1 = email_address_verify.get()
    # creates another new variable and sets it equal to the email address the user has entered
    # this time specific to the login_verify function
    password1 = password_verify.get()
    # makes a new password and collects the data from the password_verify variable
    email_address_login_entry.delete(0, 0)
    # resets the email address the user has entered
    password_login_entry.delete(0, 0)
    # resets the password the user has entered
    list_of_files = os.listdir()
    # creates a new variable
    # sets it equal to the package os to allow the program to read through the files I have stored
    # checks if the email typed in exists
    if email_address1 in list_of_files:
        # creates our first if clause to check the email address entered exists inside one of the files
        file1 = open(email_address1, "r")
        # creates a new variable and opens the file where the email did exist
        verify = file1.read().splitlines()
        # sets a new variable equal to our file we have just opened and splits the lines up
        # they can now be interpreted separately
        if password1 in verify:
            # if the password the user has entered where equal to the password matching the email in the file
            login_success()
            # it will follow through with the login_success function
        else:
            # or if the password entered by the user is different to the one in the file with the email
            password_not_recognised()
            # then the program will follow through will the password_not_recognised function
    else:
        # this is if the email address the user entered does not exist
        user_not_found()
        # then the program will follow through with the user_not_found function


def login_success():
    """this function is called if the user has entered an email that exists and a password which matches"""
    global login_success_screen
    # calls login_success_screen and allows us to pass it into any function
    login_success_screen = Toplevel(login_screen)
    # moves this new window above the window the user was on previously
    login_success_screen.title("Success")
    # gives the window a title of success, showing the user they have successfully entered the correct details
    login_success_screen.geometry("150x100")
    # gives the window a starting size of 150 width and smaller length of 100
    Label(login_success_screen, text="Login Success", font=("Comic Sans MS", 15)).pack()
    # creates a label with text of 'login success' making it clear to the user they have entered matching credentials
    Button(login_success_screen, text="OK", command=delete_login_success, font=("Comic Sans MS", 15)).pack()
    # new button, text 'ok', font 'comic sans'
    # if pressed program will search for delete_login_success and carry out following commands
    login_success_screen.resizable(False, False)
    # forces the window to stick at the beginning size defined above


def password_not_recognised():
    """this is the function telling the user they have entered the wrong password"""
    global password_not_recognised_screen
    # calls the pass_not_recognised_screen allowing us to call it inside any command whether in or out this function
    password_not_recognised_screen = Toplevel(login_screen)
    # places this window above the login_screen
    password_not_recognised_screen.title("Failure")
    # gives the window a title of failure to show the user they have failed to log in to the system
    password_not_recognised_screen.geometry("150x100")
    # gives the window a size of 150 x 100 to start with
    Label(password_not_recognised_screen, text="Invalid Password ", font=("Comic Sans MS", 15)).pack()
    # tells the user inside a label 'invalid password' and gives this text size 15 and font comic sans
    Button(password_not_recognised_screen, text="OK",
           command=delete_password_not_recognised,
           font=("Comic Sans MS", 15)).pack()
    # creates a new button has text of 'ok'
    # if clicked program will be pointed to the delete_password_not_recognised function
    password_not_recognised_screen.resizable(False, False)
    # forces the window to be fixed at the original size defined above


def user_not_found():
    """this function will take effect
    where the email address entered on the login screen was not found in the list of files"""
    global user_not_found_screen
    # calls the user_not_found_screen variable and allows it to be used throughout all functions
    user_not_found_screen = Toplevel(login_screen)
    # tells the window manager to place this new window instead of the login screen
    user_not_found_screen.title("Failure")
    # gives this window a title of Failure telling the user they have incorrectly inputted their credentials
    user_not_found_screen.geometry("150x100")
    # gives the window an original size of 150 x 100
    Label(user_not_found_screen, text="User Not Found", font=("Comic Sans MS", 15)).pack()
    # makes another new label with text of 'User not found'
    # describing the issue to the user so they no which credential to edit
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen, font=("Comic Sans MS", 15)).pack()
    # the user is then presented with a button with text of ok
    # when this button is clicked the function delete_user_not_found_screen will be called
    user_not_found_screen.resizable(False, False)
    # sets the parameters for the window's size to non-resizable


def delete_login_success():
    """this function will affect what the user sees when they click ok when they have entered correct details"""
    login_success_screen.destroy()
    # this uses the destroy function built into tkinter to close the window
    # allowing the user to continue interacting with the graphical interface


def delete_password_not_recognised():
    """this function is created to the new window which was created when the user got their password wrong"""
    password_not_recognised_screen.destroy()
    # gets rid of the password_not_recognised_screen and allows the user to re-try entering their details


def delete_user_not_found_screen():
    """this function comes into play when the user types an email that is not recognised by the system"""
    user_not_found_screen.destroy()
    # closes the user_not_found_screen when they have clicked on the 'ok' button in the new window


def main_account_screen():
    """this function is the main code for the program to display the login and register options to the user"""
    global main_screen
    # creates a new variable main_screen and allows us to call it throughout our whole program
    main_screen = Tk()
    # creates a new variable called main_screen and sets it equal to a tkinter function
    # which creates a new window
    main_screen.geometry("500x800")
    # gives the window a starting size of 500 x 800
    main_screen.title("A Level Computer Science Project")
    # gives the graphical interface a title of A Level Computer Science Project
    Label(text="Home Automation System",
          bg="#10c2fe",
          width="300",
          height="2",
          font=("Comic Sans MS", 20, "bold")).pack()
    # creates a new label giving it text of 'Home Automation System' and gives it a background colour of blue using hex
    Label(text="").pack()
    # forces some space between the above label and the below login button
    Button(text="Login", height="2", width="30", command=login, font=("Comic Sans MS", 15)).pack()
    # creates a new button with text 'Login' and gives it a set height and width, gives it a command of login
    # when user clicks this button the login function will be executed
    Label(text="").pack()
    # packs a blank line in between the above login button and the below register button
    Button(text="Register", height="2", width="30", command=register, font=("Comic Sans MS", 15)).pack()
    # makes a new button with text register and a command of register
    # so when the user clicks on this new button the register function will be executed
    main_screen.resizable(False, False)
    # this keeps the window at the same size it was originally created with
    main_screen.mainloop()
    # tells tkinter to run the mainloop function and blocks any subsequent code


main_account_screen()
# this reopens the loop and executes the above functions and present the windows as the user interacts with each one
