from tkinter import *
from PIL import ImageTk, Image
import os
import sqlite3


# the first line tells the program to search for the built-in library Tkinter
# and import all the modules found within Tkinter
# the next line tells the program to search for the library Pillow
# and import two modules: Image, which is used to allow us to use Images within our program
# and ImageTk to allow us to import Images within a Tkinter window
# next we have told the program to import os, allowing us to interact with the operating system,
# for example to create or delete a folder
# the final import line imports our database module
# which allows us to provide a SQL-like interface to read, query, and write SQL databases from Python


def proceed_window():
    proceed = Tk()
    # we are creating a variable called proceed, and setting it equal to our tkinter window
    # so whenever we need to put something inside out Tkinter window we just have to call proceed
    proceed.title('A Level Computer Science Project')
    # we are calling our variable root and defining more of its attributes giving our tkinter window a title
    proceed.geometry("400x300")
    # gives some restrictions for our tkinter window of 400x300
    proceed.resizable(False, False)
    # fixes the size of the window
    proceed.mainloop()
    # this calls the variable proceed and displays our graphical user interface with all of its attributes defined above
    

proceed_window()
# we are calling our proceed window function which we have defined with the following attributes
# this will display our user interface


def login_and_register_user_screen():
    """defines a function to make the first user interface the user can interact with by registering or logging in"""
    return


def register():
    """defines a function and calls it register so where ever this function is called it will follow these commands
    the register function will have a button called register which will allow the user to register
    if they don't yet have any credentials"""
    return
