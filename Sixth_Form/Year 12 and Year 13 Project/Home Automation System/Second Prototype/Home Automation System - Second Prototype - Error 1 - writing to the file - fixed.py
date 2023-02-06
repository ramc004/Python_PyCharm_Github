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


def login():
    """this is the code for the login function
    when the user clicks their login button the below function will be performed"""
    return


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

