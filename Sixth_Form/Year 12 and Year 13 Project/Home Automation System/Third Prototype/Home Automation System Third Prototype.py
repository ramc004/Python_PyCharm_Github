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

proceed = Tk()
# we are creating a variable called proceed, and setting it equal to our tkinter window
# so whenever we need to put something inside out Tkinter window we just have to call proceed
proceed.title('A Level Computer Science Project')
# we are calling our variable root and defining more of its attributes giving our tkinter window a title
proceed.geometry("450x300")
# gives some restrictions for our tkinter window of 400x300

# database
conn = sqlite3.connect('User Login Page Database.db')
# creates a database with a name of 'User Login Page Database' or connects to a database with this name
c = conn.cursor()
# creates a cursor

# creates table
'''
c.execute("""CREATE TABLE users (
        email_address text, 
        password text, 
        first_digit_for_six_digit_code integer, 
        second_digit_for_six_digit_code integer, 
        third_digit_for_six_digit_code integer, 
        fourth_digit_for_six_digit_code integer, 
        fifth_digit_for_six_digit_code integer, 
        sixth_digit_for_six_digit_code integer
    )""")
'''


def register():
    return


def login():
    return


def no():
    """this defines our function with the name of yes
    this takes the user to the main screen """
    conn = sqlite3.connect('User Login Page Database.db')
    # creates a database with a name of 'User Login Page Database' or connects to a database with this name
    c = conn.cursor()
    # creates a cursor
    conn.commit()
    # commits any changes the users inputs have made to the database
    conn.close()
    # closes the connection for the database
    proceed.destroy()
    # closes the window since the user has decided to they would not like to proceed


def yes():
    """this defines a function with a name of yes which directs the user to the new window
    which will allow the user to login and/or register"""
    conn = sqlite3.connect('User Login Page Database.db')
    # creates a database with a name of 'User Login Page Database' or connects to a database with this name
    c = conn.cursor()
    # creates a cursor
    login_and_register_user_screen = Tk()
    # creates a new tkinter window allowing the user to login or register
    login_and_register_user_screen.title('Login and Register screen')
    # givers the new tkinter window a title of Login and Register screen
    login_and_register_user_screen.geometry("500x500")
    # sets some parameters for the user interface
    login_and_register_user_screen.resizable(False, False)
    # sets the login and register user window to a fixed size
    conn.commit()
    # commits any changes the users inputs have made to the database
    conn.close()
    # closes the connection for the database


frame = Frame(proceed, width=420, height=55)
# creates a frame, links it to our proceed Tkinter window and limits to a size with a width of 450 and height of 400
frame.place(x=7, y=1)
# allows the program to most efficiently place the image inside our frame using the function pack
img = ImageTk.PhotoImage(Image.open("first.png"))
# creates a variable called img and sets it equal to our image with the first bit
label = Label(frame, image=img)
# creates a variable called label places it in a Label function
# uses our frame variable on how to place it from above, and uses the image we defined as img from above
label.place(x=7, y=1)
# packs the label in the best the system thinks will place our label
frame2 = Frame(proceed, width=400, height=60)
# this is our next bit of the frame with the next line of text
frame2.place(x=35, y=40)
# this places our next bit of the frame using the function pack
img2 = ImageTk.PhotoImage(Image.open("second.png"))
# creates the next image to be used below the last one
label2 = Label(frame2, image=img2)
# creates a new variable for our next image
label2.place(x=35, y=20)
# tells the system how to place our image using the pack function
Button(text="Yes", height="2", width="30", command=yes).place(x=84, y=125)
#
Button(text="No", height="2", width="30", command=no).place(x=84, y=175)
#
proceed.resizable(False, False)
# fixes the size of the window
conn.commit()
# commits any changes the users inputs have made to the database
conn.close()
# closes the connection for the database
proceed.mainloop()
# this calls the variable proceed and displays our graphical user interface with all of its attributes defined above
