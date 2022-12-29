from tkinter import *
import os
import sqlite3
from PIL import ImageTk, Image


# this is to import the python library tkinter to be able to build a graphical user interface using its framework
# I have imported os to allow my system to access how the user interacts with their device in relation to my system
# I have imported sqlite3, so I am able to connect to a database and store the users information


def register():
    """this function is the code for the 'Register' window
       whenever the user doesn't have an account yet but would like to create one"""
    global register_screen
    #
    register_screen = Toplevel(main_screen)
    #
    register_screen.title("Register")
    #
    register_screen.geometry("500x800")
    #
    register_screen.resizable(False, False)
    #
    global email_address
    #
    global password
    #
    global email_address
    #
    global password_entry
    #
    email_address = StringVar()
    #
    password = StringVar()
    #
    email_address_label_2 = Label(register_screen, text="Email Address ")
    #
    email_address_label_2.pack()
    #
    email_address = Entry(register_screen, textvariable=email_address)
    #
    email_address.pack()
    #
    password_label_2 = Label(register_screen, text="Password * ")
    #
    password_label_2.pack()
    #
    password_entry = Entry(register_screen, textvariable=password, show='*')
    #
    password_entry.pack()
    #
    Label(register_screen, text="").pack()
    #
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()
    #
    Button(register_screen, text="Authenticate", width=10, height=1, bg="blue", command=register_user).pack()
    # this function will create a button
    # that when pressed will enable an email to be sent to the email address provided


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


def register_user():
    #
    email_address_info = email_address.get()
    #
    password_info = password.get()
    #
    file = open(email_address_info, "w")
    #
    file.write(email_address_info + "\n")
    #
    file.write(password_info)
    #
    file.close()
    #
    email_address.delete(0, 0)
    #
    password_entry.delete(0, 0)
    #
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    #


def login_verify():
    #
    email_address1 = email_address_verify.get()
    #
    password1 = password_verify.get()
    #
    email_address_login_entry.delete(0, 0)
    #
    password_login_entry.delete(0, 0)
    #
    list_of_files = os.listdir()
    #
    if email_address1 in list_of_files:
        #
        file1 = open(email_address1, "r")
        #
        verify = file1.read().splitlines()
        #
        if password1 in verify:
            #
            login_success()
            #
        else:
            #
            password_not_recognised()
            #
    else:
        #
        user_not_found()
        #


def login_success():
    #
    global login_success_screen
    #
    login_success_screen = Toplevel(login_screen)
    #
    login_success_screen.title("Success")
    #
    login_success_screen.geometry("150x100")
    #
    Label(login_success_screen, text="Login Success").pack()
    #
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
    #


def password_not_recognised():
    #
    global password_not_recognised_screen
    #
    password_not_recognised_screen = Toplevel(login_screen)
    #
    password_not_recognised_screen.title("Error")
    #
    password_not_recognised_screen.geometry("150x100")
    #
    Label(password_not_recognised_screen, text="Invalid Password ").pack()
    #
    Button(password_not_recognised_screen, text="OK", command=delete_password_not_recognised).pack()
    #


def user_not_found():
    #
    global user_not_found_screen
    #
    user_not_found_screen = Toplevel(login_screen)
    #
    user_not_found_screen.title("Error")
    #
    user_not_found_screen.geometry("150x100")
    #
    Label(user_not_found_screen, text="User Not Found").pack()
    #
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
    #


def delete_login_success():
    #
    login_success_screen.destroy()
    #


def delete_password_not_recognised():
    #
    password_not_recognised_screen.destroy()
    #


def delete_user_not_found_screen():
    #
    user_not_found_screen.destroy()
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
    frame = Frame(main_screen, width=300, height=55)
    #
    frame.place(x=5, y=5)
    #
    img = ImageTk.PhotoImage(Image.open("third.png"))
    #
    label = Label(frame, image=img)
    #
    label.place(x=40, y=0)
    #
    Label(text="").pack()
    #
    Button(text="Login", height="2", width="30", command=login).place(x=100, y=75)
    #
    Label(text="").place(x=5, y=5)
    #
    Button(text="Register", height="2", width="30", command=register).place(x=100, y=125)
    #
    main_screen.resizable(False, False)
    #
    main_screen.mainloop()
    #


main_account_screen()
#
