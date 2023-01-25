from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import emoji
import re
import random
import smtplib

# rmr tpo paste this in terminal 'python -m aiosmtpd -n -1 localhost: 8025' for server hosting


# the first line tells the program to search for the built-in library Tkinter
# and import all the modules found within Tkinter
# the next line tells the program to search for the library Pillow
# and import two modules: Image, which is used to allow us to use Images within our program
# and ImageTk to allow us to import Images within a Tkinter window
# the next import line imports our database module
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


# creates table


def sign_up():
    return


def verify():
    return


def register():
    """this function creates a new window which allows the user to register their details
     and saves them to the database"""
    conn = sqlite3.connect('User Login Page Database.db')
    # creates a database with a name of 'User Login Page Database' or connects to a database with this name
    c = conn.cursor()
    # creates a cursor
    register_screen = Tk()
    # creates a new Tkinter user interface
    register_screen.title("Register")
    # gives the new Tkinter interface a title of 'Register'
    register_screen.geometry("500x600")
    # gives the starting size for the Tkinter user interface
    register_screen.resizable(False, False)
    # limits the user from resizing the interface
    email_address_entry = Entry(register_screen)

    email_address_entry.place(x=150, y=70)

    email_address_text = Label(register_screen, text="Email address")

    email_address_text.place(x=56.2, y=72)

    verify_box_entry = Entry(register_screen)

    verify_box_entry.place(x=150, y=170)

    verify_text = Label(register_screen, text=" Enter six digit code: ")

    verify_text.place(x=13, y=173)

    code = str(random.randint(100000, 999999))

    def send_email():
        """"""
        email = email_address_entry.get()

        server = smtplib.SMTP('localhost', 8025)

        message = "Your code is: " + code

        server.sendmail("", email, message)

        server.quit()

        sent_label = Label(register_screen, text="Email sent!")

        sent_label.grid(row=2, column=0)

    email_address_verify_button = Button(register_screen, text="Verify", width=10, height=1, command=send_email)

    email_address_verify_button.place(x=350, y=74)

    def check():
        entered_code = verify_box_entry.get()
        if entered_code == code:
            print("correct code")
        else:
            print("incorrect code")

    check_button = Button(register_screen, text="Check", width=10, height=1, command=check)

    check_button.place(x=350, y=174)

    verify_button_description = Label(register_screen, text="click verify, email sent, 6 digit code")

    verify_button_description.place(x=240, y=45)

    def check_email_address():
        """"""
        email = email_address_entry.get()

        if "@" in email:

            emoji_label_clause_2_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_2_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')

        if "gmail.com" in email \
                or "yahoo.com" in email \
                or "outlook.com" in email \
                or "richardchalloner.com" in email \
                or "icloud.com" in email \
                or "mail.com" in email \
                or "email.com" in email \
                or "aol.com" in email \
                or "proton.me" in email \
                or "tutanota.com" in email \
                or "tutanota.de" in email \
                or "tutamail.com" in email \
                or "tuta.io" in email \
                or "keemail.me" in email \
                or "zohomail.eu" in email \
                or "tmmwj.com" in email \
                or "gmx.com" in email \
                or "gmx.co.uk" in email \
                or "yahoo.co.uk" in email:

            emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')

        if "caleb" in email \
                or "hannah" in email \
                or "mark" in email \
                or "niki" in email \
                or "sean" in email \
                or "katherine" in email \
                or "kat" in email \
                or "alyssa" in email \
                or "katy" in email \
                or "isaac" in email \
                or "esther" in email \
                or "ben" in email \
                or "connor" in email \
                or "daisy" in email \
                or "josh" in email \
                or "zoey" in email \
                or "valentina" in email \
                or "stacy" in email \
                or "george" in email \
                or "graham" in email \
                or "isabella" in email \
                or "bella" in email \
                or "ella" in email \
                or "grace" in email \
                or "ellis" in email \
                or "emmanuel" in email \
                or "christian" in email \
                or "finn" in email \
                or "fin" in email \
                or "rachael" in email \
                or "liv" in email \
                or "olivia" in email \
                or "elaine" in email \
                or "bert" in email \
                or "nilusha" in email \
                or "andy" in email \
                or "emma" in email \
                or "emily" in email \
                or "amelia" in email \
                or "charlotte" in email \
                or "sophia" in email \
                or "mia" in email \
                or "ava" in email \
                or "eva" in email \
                or "keira" in email \
                or "kiera" in email \
                or "harper" in email \
                or "jessie" in email \
                or "alex" in email \
                or "liam" in email \
                or "noah" in email \
                or "elijah" in email \
                or "oliver" in email \
                or "ollie" in email \
                or "lucas" in email \
                or "luke" in email \
                or "james" in email \
                or "alexia" in email \
                or "aaron" in email \
                or "william" in email \
                or "will" in email \
                or "jo" in email \
                or "joseph" in email \
                or "benjamin" in email \
                or "henry" in email \
                or "laura" in email \
                or "theo" in email \
                or "daniel" in email \
                or "marios" in email \
                or "mario" in email \
                or "benjy" in email \
                or "arthur" in email \
                or "john" in email \
                or "tim" in email \
                or "javier" in email \
                or "xavier" in email \
                or "eve" in email \
                or "niamh" in email \
                or "niam" in email \
                or "alannah" in email \
                or "reshee" in email \
                or "amelie" in email \
                or "nishtha" in email \
                or "sofia" in email \
                or "abi" in email \
                or "abigail" in email \
                or "penelope" in email \
                or "brooke" in email \
                or "brook" in email \
                or "brooklyn" in email \
                or "sophie" in email \
                or "laila" in email \
                or "jaimie" in email \
                or "claudia" in email \
                or "elena" in email \
                or "eleanor" in email \
                or "ram" in email \
                or "mat" in email \
                or "matt" in email \
                or "matthew" in email \
                or "mary" in email \
                or "martha" in email \
                or "peter" in email \
                or "tamar" in email \
                or "darius" in email \
                or "edith" in email \
                or "elise" in email:

            emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')

    check_rules_button_email_address = Button(register_screen, text="check rules", command=check_email_address)

    check_rules_button_email_address.place(x=345, y=125)

    check_clause_1_email_address = Label(register_screen, text="Contains account name")

    check_clause_1_email_address.place(x=150, y=100)

    check_clause_2_email_address = Label(register_screen, text="'@' sign")

    check_clause_2_email_address.place(x=150, y=120)

    check_clause_3_email_address = Label(register_screen, text="Domain name")

    check_clause_3_email_address.place(x=150, y=140)

    password_label = Label(register_screen, text='Password')

    password_label.place(x=80, y=250)

    password_entry = Entry(register_screen, show='*')

    password_entry.place(x=150, y=250)

    def show_password():
        """this defines a function which allows the users password to be shown where check box is ticked"""
        if password_entry.cget('show') == '*':

            password_entry.config(show='')

        else:

            password_entry.config(show='*')

    show_password_check_box = Checkbutton(register_screen, text='Show Password', command=show_password)

    show_password_check_box.place(x=85, y=277)

    def check_password():

        password_length = password_entry.get()

        if len(password_length) >= 8:

            emoji_label_clause_1_password.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_1_password.config(text=f'{emoji.emojize(":cross_mark:")}')

        password_caps = password_entry.get()

        if re.search(r'[A-Z]{1,}', password_caps):

            emoji_label_clause_2_password.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_2_password.config(text=f'{emoji.emojize(":cross_mark:")}')

        password_numbers = password_entry.get()

        if re.search(r'\d{,}', password_numbers):

            emoji_label_clause_4_password.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_4_password.config(text=f'{emoji.emojize(":cross_mark:")}')

        password_special_chars = password_entry.get()

        if re.search(r'[∑´®†¥¨~`Ω≈ç√∫µ≤≥«æ…¬˚∆˙©ƒ∂ßåπø“‘≠–ºª•¶§∞¢#€¡±œ!@$%^&*(),.;?":{+}|<-=>/]{1,}'
                , password_special_chars):

            emoji_label_clause_3_password.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_3_password.config(text=f'{emoji.emojize(":cross_mark:")}')

    check_rules_button_password = Button(register_screen, text="check rules", command=check_password)

    check_rules_button_password.place(x=345, y=325)

    check_clause_1_password = Label(register_screen, text="At least 8 characters")

    check_clause_1_password.place(x=150, y=300)

    check_clause_2_password = Label(register_screen, text="At least 2 capital letters")

    check_clause_2_password.place(x=150, y=320)

    check_clause_3_password = Label(register_screen, text="At least 1 special character")

    check_clause_3_password.place(x=150, y=340)

    check_clause_4_password = Label(register_screen, text="At least 2 numbers")

    check_clause_4_password.place(x=150, y=360)

    sign_up_button = Button(register_screen, text='Sign Up', command=sign_up)

    sign_up_button.place(x=350, y=390)

    emoji_label_clause_1_password = Label(register_screen)

    emoji_label_clause_1_password.place(x=125, y=300)

    emoji_label_clause_2_password = Label(register_screen)

    emoji_label_clause_2_password.place(x=125, y=320)

    emoji_label_clause_3_password = Label(register_screen)

    emoji_label_clause_3_password.place(x=125, y=340)

    emoji_label_clause_4_password = Label(register_screen)

    emoji_label_clause_4_password.place(x=125, y=360)

    emoji_label_clause_1_email_address = Label(register_screen)

    emoji_label_clause_1_email_address.place(x=125, y=100)

    emoji_label_clause_2_email_address = Label(register_screen)

    emoji_label_clause_2_email_address.place(x=125, y=120)

    emoji_label_clause_3_email_address = Label(register_screen)

    emoji_label_clause_3_email_address.place(x=125, y=140)

    conn.commit()
    # commits any changes the users inputs have made to the database
    conn.close()
    # closes the connection for the database


def login():
    """defines another function with the name of login
    this will allow the user to log in with credentials they used to register with"""
    conn = sqlite3.connect('User Login Page Database.db')
    # creates a database with a name of 'User Login Page Database' or connects to a database with this name
    c = conn.cursor()
    # creates a cursor
    login_screen = Tk()
    # creates another interface, this time for the login screen
    login_screen.title("Login")
    # this gives a title to this interface, of login
    login_screen.geometry("500x600")
    # gives some limits for our window
    login_screen.resizable(False, False)
    # gives the window a fixed size

    conn.commit()
    # commits any changes the users inputs have made to the database
    conn.close()
    # closes the connection for the database


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
    login_and_register_user_screen.title('Register and Login screen')
    # givers the new tkinter window a title of Login and Register screen
    login_and_register_user_screen.geometry("500x500")
    # sets some parameters for the user interface
    login_and_register_user_screen.resizable(False, False)
    # sets the login and register user window to a fixed size
    register_button = Button(login_and_register_user_screen, text="Register", height="2", width="30", command=register)
    # creates a variable that creates a button and places it inside our new tkinter interface
    # which allows the user to register
    register_button.place(x=100, y=75)
    # tells the system to place my register button along the x and y axes
    login_button = Button(login_and_register_user_screen, text="Login", height="2", width="30", command=login)
    # creates a variable that creates a button and places it inside our new tkinter interface
    # which allows the user to login
    login_button.place(x=100, y=125)
    # tells the system to place my login button along the x and y axes
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

Button(text="No", height="2", width="30", command=no).place(x=84, y=175)

proceed.resizable(False, False)
# fixes the size of the window
conn.commit()
# commits any changes the users inputs have made to the database
conn.close()
# closes the connection for the database
proceed.mainloop()
# this calls the variable proceed and displays our graphical user interface with all of its attributes defined above
