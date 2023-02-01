from tkinter import *
# This is to import the python library tkinter to be able to build a graphical user interface using its framework


def register():
    """this function will create a new window which allows the user to register their details"""
    return


def login():
    """defines another function with the name of login
    this will allow the user to log in with credentials they used to register with"""
    return


def main_account_screen():
    """create a function which makes the login and register window"""
    main_screen = Tk()
    # creates a variable and sets it equal to a Tk so whenever we need to call this tkinter window we call main_screen
    main_screen.geometry("500x800")
    # gives our window a starting size of 500 width and 800 in length
    main_screen.title("A Level Computer Science Project")
    # gives the window a title of 'A Level Computer Science Project
    Label(text="Home Automation System",
          bg="#10c2fe",
          width="300",
          height="2",
          font=("Comic Sans MS", 20, "bold")).pack()
    # gives the window a label of 'Home Automation System' with a fixed border around it and a font
    Label(text="").pack()
    # gives some space between the title and the login button
    Login_Button = Button(text="Login", height="2", width="30", command=login)
    # creates a button for the user to click on with a set size of width 30 and height 2
    Login_Button.pack()
    # packs the Login button into the window directly below
    Label(text="").pack()
    # allows for some space between the login and register button
    Register_Button = Button(text="Register", height="2", width="30", command=register)
    # sets the variable register_button equal to a button with text register ste in the middle and a command of register
    Register_Button.pack()
    # packs the register button directly below the label
    main_screen.resizable(False, False)
    # fixes the windows size to 500x800, so it cannot be altered
    main_screen.mainloop()
    # tells the system to have the window ready to be run


main_account_screen()
# this outputs the window with the user to interact with
