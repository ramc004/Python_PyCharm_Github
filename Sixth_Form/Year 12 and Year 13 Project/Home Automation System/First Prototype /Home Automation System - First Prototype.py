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
    # Using the function 'global' to allow us to reuse the variable 'password_entry' throughout various functions
    global password_entry
    # Using the function 'global' to allow us to reuse the variable 'password_entry' throughout various functions
    email_address = StringVar()
    # Sets the variable 'email_address' to be a variable with the data type of string
    password = StringVar()
    # Sets the variable 'password' to be a string meaning the user can enter numbers, special characters and letters

    email_address_label_2 = Label(register_screen, text="email address ")
    # creates a second email add label dedicated to our register screen and sets the text for this label equal
    # to 'email address'
    email_address_label_2.pack()
    # sets the variable to be packed into our widget so that it co-insides within the parameters of password and title
    email_address = Entry(register_screen, textvariable=email_address)
    # allows the user to enter text into this entry box and sets it equal to the email address variable in order to
    # have it checked by the correct variable
    email_address.pack()
    # sets where the email address field is to be placed
    password_label_2 = Label(register_screen, text="Password * ")
    # creates a second password variable specific to our register screen
    # gives this variable a heading and sets it equal to 'Password *'
    password_label_2.pack()
    # sets this second variable in place with our widget to make sure that it the third label
    password_entry = Entry(register_screen, textvariable=password, show='*')
    # allows the user to enter text which it will set equal to password into the password field
    # stars the password out to avoid password sharing
    password_entry.pack()
    # packs the password entry box so that it fits on the final level of the widget
    Label(register_screen, text="").pack()
    # gives the register screen a label and allows the user to enter text throughout this window 
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()
    # 


def login():
    #
    global login_screen
    #
    login_screen = Toplevel(main_screen)
    #
    login_screen.title("Login")
    #
    login_screen.geometry("500x800")
    #
    Label(login_screen, text="Please enter details below to login").pack()
    #
    Label(login_screen, text="").pack()
    #
    login_screen.resizable(False, False)
    #

    global email_address_verify
    #
    global password_verify
    #

    email_address_verify = StringVar()
    #
    password_verify = StringVar()
    #

    global email_address_login_entry
    #
    global password_login_entry
    #

    Label(login_screen, text="email address * ").pack()
    #
    email_address_login_entry = Entry(login_screen, textvariable=email_address_verify)
    #
    email_address_login_entry.pack()
    #
    Label(login_screen, text="").pack()
    #
    Label(login_screen, text="Password * ").pack()
    #
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    #
    password_login_entry.pack()
    #
    Label(login_screen, text="").pack()
    #
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()
    #


def main_account_screen():
    #
    global main_screen
    #
    main_screen = Tk()
    #
    main_screen.geometry("500x800")
    #
    main_screen.title("A Level Computer Science Project")
    #
    Label(text="Home Automation System", bg="#10c2fe", width="300", height="2", font=("Arial", 13)).pack()
    #
    Label(text="").pack()
    #
    Button(text="Login", height="2", width="30", command=login).pack()
    #
    Label(text="").pack()
    #
    Button(text="Register", height="2", width="30", command=register).pack()
    #

    main_screen.resizable(False, False)
    #
    main_screen.mainloop()
    #


main_account_screen()
#
