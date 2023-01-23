from tkinter import *
import os
# This is to import the python library tkinter to be able to build a graphical user interface using its framework
# I have imported os to allow my system to access how the user interacts with their device in relation to my system


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
    main_screen.resizable(False, False)
    # fixes the windows size to 500x800, so it cannot be altered
    main_screen.mainloop()
    # tells the system to have the window ready to be run


main_account_screen()
# this outputs the window with the user to interact with
