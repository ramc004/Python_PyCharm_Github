from tkinter import *
import os
# This is to import the python library tkinter to be able to build a graphical user interface using its framework
# I have imported os to allow my system to access how the user interacts with their device in relation to my system


def register_user():
    return


def login_verify():
    return

def register():
    return


def login():
    return

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
