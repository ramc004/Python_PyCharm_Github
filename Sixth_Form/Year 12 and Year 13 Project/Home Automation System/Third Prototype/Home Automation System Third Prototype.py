import parser
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import emoji
import re
import random
import smtplib
from email.message import EmailMessage

# the first line tells the program to search for the built-in library Tkinter
# and import all the modules found within Tkinter
# the next line tells the program to search for the library Pillow
# and import two modules: Image, which is used to allow us to use Images within our program
# and ImageTk to allow us to import Images within a Tkinter window
# the next import line imports our database module
# which allows us to provide a SQL-like interface to read, query, and write SQL databases from Python

database_name = 'Home Automation System Database.db'

proceed = Tk()
# we are creating a variable called proceed, and setting it equal to our tkinter window
# so whenever we need to put something inside out Tkinter window we just have to call proceed
proceed.title('A Level Computer Science Project')
# we are calling our variable root and defining more of its attributes giving our tkinter window a title
proceed.geometry("450x300")
# gives some restrictions for our tkinter window of 400x300

# database
conn = sqlite3.connect(database_name)
# creates a database with a name of 'User Login Page Database' or connects to a database with this name
c = conn.cursor()
# creates a cursor


c.execute("""CREATE TABLE IF NOT EXISTS users (
        userID int PRIMARY KEY,
        email_address text, 
        password text, 
        accessLevel text, 
        nickname text, 
        date_of_birth DATE)""")


# creates table


def log_in():
    conn = sqlite3.connect(database_name)
    # creates a database with a name of 'User Login Page Database' or connects to a database with this name
    c = conn.cursor()
    # creates a cursor
    home_automation_system_window = Tk()
    home_automation_system_window.title("Home Automation System")
    home_automation_system_window.geometry("500x600")
    add_new_device = Label(home_automation_system_window, text="Would you like to add a new device?")
    add_new_device.place(y=30, x=140)
    conn.commit()
    # commits any changes the users inputs have made to the database
    conn.close()

    return


def sign_up(email_address_db, password_db):
    conn = sqlite3.connect(database_name)
    # creates a database with a name of 'User Login Page Database' or connects to a database with this name
    c = conn.cursor()

    accessLevel = "userAccount"

    selectQuery = "SELECT userID FROM users ORDER BY userID DESC LIMIT 1"

    c.execute(selectQuery)

    highestID = c.fetchone()
    print(highestID)
    if highestID is not None:
        highestID = highestID[0]
        newID = int(highestID) + 1
    else:
        newID = 0

    insertQuery = """INSERT INTO users
                (userID, email_address, password, accessLevel) 
                VALUES
                (%d,"%s","%s","%s")""" % (newID, email_address_db, password_db, accessLevel)

    c.execute(insertQuery)

    conn.commit()
    # commits any changes the users inputs have made to the database
    conn.close()

    return


def verify():
    return


def register():
    """this function creates a new window which allows the user to register their details
     and saves them to the database"""
    conn = sqlite3.connect(database_name)
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
    email_address_entry_register_screen = Entry(register_screen)

    email_address_entry_register_screen.place(x=150, y=70)

    email_address_text_register_screen = Label(register_screen, text="Email address")

    email_address_text_register_screen.place(x=56.2, y=72)

    verify_box_entry = Entry(register_screen)

    verify_box_entry.place(x=150, y=170)

    verify_text = Label(register_screen, text=" Enter six digit code: ")

    verify_text.place(x=13, y=173)

    code = str(random.randint(100000, 999999))

    def send_email():
        """"""
        emailRecipient = email_address_entry_register_screen.get()

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        emailSender = "haspythontkinter1@gmail.com"

        emailPassword = "sshpectpbiegxtpz"

        subject = "Code Verification Email"

        email = EmailMessage()

        email["From"] = emailSender

        email["To"] = emailRecipient

        email["Subject"] = subject

        email.set_content("Your code is: " + code)

        server.login(emailSender, emailPassword)

        server.sendmail(emailSender, emailRecipient, email.as_string())

        server.quit()

        sent_label = Label(register_screen, text="Email sent!")

        sent_label.place(x=360, y=97)

        sent_label.config(foreground="green")

    email_address_verify_button = Button(register_screen, text="Verify", width=10, height=1, command=send_email)

    email_address_verify_button.place(x=350, y=74)

    def check():
        entered_code = verify_box_entry.get()
        if entered_code == code:
            code_label_success = Label(register_screen, text="  code correct")
            code_label_success.place(x=350, y=200)
            code_label_success.config(foreground="green")
        else:
            code_label_failure = Label(register_screen, text="code incorrect")
            code_label_failure.place(x=350, y=200)
            code_label_failure.config(foreground="red")

    check_button = Button(register_screen, text="Check", width=10, height=1, command=check)

    check_button.place(x=350, y=174)

    verify_button_description = Label(register_screen, text="sends your 6 digit code")

    verify_button_description.place(x=320, y=35)

    verify_button_arrow = Label(register_screen, text="↕️")

    verify_button_arrow.place(x=382, y=51)

    def check_email_address():
        """"""
        email_register = email_address_entry_register_screen.get()

        if "@" in email_register:

            emoji_label_clause_2_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_2_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')

        if "gmail.com" in email_register \
                or "yahoo.com" in email_register \
                or "outlook.com" in email_register \
                or "richardchalloner.com" in email_register \
                or "icloud.com" in email_register \
                or "mail.com" in email_register \
                or "email.com" in email_register \
                or "aol.com" in email_register \
                or "proton.me" in email_register \
                or "tutanota.com" in email_register \
                or "tutanota.de" in email_register \
                or "tutamail.com" in email_register \
                or "tuta.io" in email_register \
                or "keemail.me" in email_register \
                or "zohomail.eu" in email_register \
                or "tmmwj.com" in email_register \
                or "gmx.com" in email_register \
                or "gmx.co.uk" in email_register \
                or "yahoo.co.uk" in email_register:

            emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')

        if "caleb" in email_register \
                or "hannah" in email_register \
                or "mark" in email_register \
                or "niki" in email_register \
                or "sean" in email_register \
                or "katherine" in email_register \
                or "kat" in email_register \
                or "alyssa" in email_register \
                or "katy" in email_register \
                or "isaac" in email_register \
                or "esther" in email_register \
                or "ben" in email_register \
                or "connor" in email_register \
                or "daisy" in email_register \
                or "josh" in email_register \
                or "zoey" in email_register \
                or "valentina" in email_register \
                or "stacy" in email_register \
                or "george" in email_register \
                or "graham" in email_register \
                or "isabella" in email_register \
                or "bella" in email_register \
                or "ella" in email_register \
                or "grace" in email_register \
                or "ellis" in email_register \
                or "emmanuel" in email_register \
                or "christian" in email_register \
                or "finn" in email_register \
                or "fin" in email_register \
                or "rachael" in email_register \
                or "liv" in email_register \
                or "olivia" in email_register \
                or "elaine" in email_register \
                or "bert" in email_register \
                or "nilusha" in email_register \
                or "andy" in email_register \
                or "emma" in email_register \
                or "emily" in email_register \
                or "amelia" in email_register \
                or "charlotte" in email_register \
                or "sophia" in email_register \
                or "mia" in email_register \
                or "ava" in email_register \
                or "eva" in email_register \
                or "keira" in email_register \
                or "kiera" in email_register \
                or "harper" in email_register \
                or "jessie" in email_register \
                or "alex" in email_register \
                or "liam" in email_register \
                or "noah" in email_register \
                or "elijah" in email_register \
                or "oliver" in email_register \
                or "ollie" in email_register \
                or "lucas" in email_register \
                or "luke" in email_register \
                or "james" in email_register \
                or "alexia" in email_register \
                or "aaron" in email_register \
                or "william" in email_register \
                or "will" in email_register \
                or "jo" in email_register \
                or "joseph" in email_register \
                or "benjamin" in email_register \
                or "henry" in email_register \
                or "laura" in email_register \
                or "theo" in email_register \
                or "daniel" in email_register \
                or "marios" in email_register \
                or "mario" in email_register \
                or "benjy" in email_register \
                or "arthur" in email_register \
                or "john" in email_register \
                or "tim" in email_register \
                or "javier" in email_register \
                or "xavier" in email_register \
                or "eve" in email_register \
                or "niamh" in email_register \
                or "niam" in email_register \
                or "alannah" in email_register \
                or "reshee" in email_register \
                or "amelie" in email_register \
                or "nishtha" in email_register \
                or "sofia" in email_register \
                or "abi" in email_register \
                or "abigail" in email_register \
                or "penelope" in email_register \
                or "brooke" in email_register \
                or "brook" in email_register \
                or "brooklyn" in email_register \
                or "sophie" in email_register \
                or "laila" in email_register \
                or "jaimie" in email_register \
                or "claudia" in email_register \
                or "elena" in email_register \
                or "eleanor" in email_register \
                or "ram" in email_register \
                or "mat" in email_register \
                or "matt" in email_register \
                or "matthew" in email_register \
                or "mary" in email_register \
                or "martha" in email_register \
                or "peter" in email_register \
                or "tamar" in email_register \
                or "darius" in email_register \
                or "edith" in email_register \
                or "elise" in email_register \
                or "adam" in email_register:

            emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')

    check_rules_button_email_address = Button(register_screen, text="check rules", command=check_email_address)

    check_rules_button_email_address.place(x=355, y=125)

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

        if re.search(r'[1234567890]{2,}', password_numbers):

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

    check_rules_button_password.place(x=355, y=325)

    check_clause_1_password = Label(register_screen, text="At least 8 characters")

    check_clause_1_password.place(x=150, y=300)

    check_clause_2_password = Label(register_screen, text="At least 2 capital letters")

    check_clause_2_password.place(x=150, y=320)

    check_clause_3_password = Label(register_screen, text="At least 1 special character")

    check_clause_3_password.place(x=150, y=340)

    check_clause_4_password = Label(register_screen, text="At least 2 numbers")

    check_clause_4_password.place(x=150, y=360)

    sign_up_button = Button(register_screen, text='Sign Up',
                            command=lambda: sign_up(email_address_entry_register_screen.get(), password_entry.get()))

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
    conn = sqlite3.connect(database_name)
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
    email_address_entry_login_screen = Entry(login_screen)

    email_address_entry_login_screen.place(x=150, y=50)

    email_address_text_login_screen = Label(login_screen, text="Email address")

    email_address_text_login_screen.place(x=56.2, y=52)

    def check_email_address():
        """"""
        email_login = email_address_entry_login_screen.get()

        if "@" in email_login:

            emoji_label_clause_2_email_address_login.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_2_email_address_login.config(text=f'{emoji.emojize(":cross_mark:")}')

        if "gmail.com" in email_login \
                or "yahoo.com" in email_login \
                or "outlook.com" in email_login \
                or "richardchalloner.com" in email_login \
                or "icloud.com" in email_login \
                or "mail.com" in email_login \
                or "email.com" in email_login \
                or "aol.com" in email_login \
                or "proton.me" in email_login \
                or "tutanota.com" in email_login \
                or "tutanota.de" in email_login \
                or "tutamail.com" in email_login \
                or "tuta.io" in email_login \
                or "keemail.me" in email_login \
                or "zohomail.eu" in email_login \
                or "tmmwj.com" in email_login \
                or "gmx.com" in email_login \
                or "gmx.co.uk" in email_login \
                or "yahoo.co.uk" in email_login:

            emoji_label_clause_3_email_address_login.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_3_email_address_login.config(text=f'{emoji.emojize(":cross_mark:")}')

        if "caleb" in email_login \
                or "hannah" in email_login \
                or "mark" in email_login \
                or "niki" in email_login \
                or "sean" in email_login \
                or "katherine" in email_login \
                or "kat" in email_login \
                or "alyssa" in email_login \
                or "katy" in email_login \
                or "isaac" in email_login \
                or "esther" in email_login \
                or "ben" in email_login \
                or "connor" in email_login \
                or "daisy" in email_login \
                or "josh" in email_login \
                or "zoey" in email_login \
                or "valentina" in email_login \
                or "stacy" in email_login \
                or "george" in email_login \
                or "graham" in email_login \
                or "isabella" in email_login \
                or "bella" in email_login \
                or "ella" in email_login \
                or "grace" in email_login \
                or "ellis" in email_login \
                or "emmanuel" in email_login \
                or "christian" in email_login \
                or "finn" in email_login \
                or "fin" in email_login \
                or "rachael" in email_login \
                or "liv" in email_login \
                or "olivia" in email_login \
                or "elaine" in email_login \
                or "bert" in email_login \
                or "nilusha" in email_login \
                or "andy" in email_login \
                or "emma" in email_login \
                or "emily" in email_login \
                or "amelia" in email_login \
                or "charlotte" in email_login \
                or "sophia" in email_login \
                or "mia" in email_login \
                or "ava" in email_login \
                or "eva" in email_login \
                or "keira" in email_login \
                or "kiera" in email_login \
                or "harper" in email_login \
                or "jessie" in email_login \
                or "alex" in email_login \
                or "liam" in email_login \
                or "noah" in email_login \
                or "elijah" in email_login \
                or "oliver" in email_login \
                or "ollie" in email_login \
                or "lucas" in email_login \
                or "luke" in email_login \
                or "james" in email_login \
                or "alexia" in email_login \
                or "aaron" in email_login \
                or "william" in email_login \
                or "will" in email_login \
                or "jo" in email_login \
                or "joseph" in email_login \
                or "benjamin" in email_login \
                or "henry" in email_login \
                or "laura" in email_login \
                or "theo" in email_login \
                or "daniel" in email_login \
                or "marios" in email_login \
                or "mario" in email_login \
                or "benjy" in email_login \
                or "arthur" in email_login \
                or "john" in email_login \
                or "tim" in email_login \
                or "javier" in email_login \
                or "xavier" in email_login \
                or "eve" in email_login \
                or "niamh" in email_login \
                or "niam" in email_login \
                or "alannah" in email_login \
                or "reshee" in email_login \
                or "amelie" in email_login \
                or "nishtha" in email_login \
                or "sofia" in email_login \
                or "abi" in email_login \
                or "abigail" in email_login \
                or "penelope" in email_login \
                or "brooke" in email_login \
                or "brook" in email_login \
                or "brooklyn" in email_login \
                or "sophie" in email_login \
                or "laila" in email_login \
                or "jaimie" in email_login \
                or "claudia" in email_login \
                or "elena" in email_login \
                or "eleanor" in email_login \
                or "ram" in email_login \
                or "mat" in email_login \
                or "matt" in email_login \
                or "matthew" in email_login \
                or "mary" in email_login \
                or "martha" in email_login \
                or "peter" in email_login \
                or "tamar" in email_login \
                or "darius" in email_login \
                or "edith" in email_login \
                or "elise" in email_login \
                or "adam" in email_login:

            emoji_label_clause_1_email_address_login.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_1_email_address_login.config(text=f'{emoji.emojize(":cross_mark:")}')

    check_rules_button_email_address_login = Button(login_screen, text="check rules", command=check_email_address)

    check_rules_button_email_address_login.place(x=355, y=105)

    check_clause_1_email_address_login = Label(login_screen, text="Contains account name")

    check_clause_1_email_address_login.place(x=150, y=80)

    check_clause_2_email_address_login = Label(login_screen, text="'@' sign")

    check_clause_2_email_address_login.place(x=150, y=100)

    check_clause_3_email_address_login = Label(login_screen, text="Domain name")

    check_clause_3_email_address_login.place(x=150, y=120)

    password_label_login = Label(login_screen, text='Password')

    password_label_login.place(x=80, y=190)

    password_entry_login = Entry(login_screen, show='*')

    password_entry_login.place(x=150, y=190)

    def show_password():
        """this defines a function which allows the users password to be shown where check box is ticked"""
        if password_entry_login.cget('show') == '*':

            password_entry_login.config(show='')

        else:

            password_entry_login.config(show='*')

    show_password_check_box_login = Checkbutton(login_screen, text='Show Password', command=show_password)

    show_password_check_box_login.place(x=85, y=227)

    def check_password():

        password_length_login = password_entry_login.get()

        if len(password_length_login) >= 8:

            emoji_label_clause_1_password_login.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_1_password_login.config(text=f'{emoji.emojize(":cross_mark:")}')

        password_caps_login = password_entry_login.get()

        if re.search(r'[A-Z]{1,}', password_caps_login):

            emoji_label_clause_2_password_login.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_2_password_login.config(text=f'{emoji.emojize(":cross_mark:")}')

        password_numbers_login = password_entry_login.get()

        if re.search(r'[1234567890]{2,}', password_numbers_login):

            emoji_label_clause_4_password_login.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_4_password_login.config(text=f'{emoji.emojize(":cross_mark:")}')

        password_special_chars_login = password_entry_login.get()

        if re.search(r'[∑´®†¥¨~`Ω≈ç√∫µ≤≥«æ…¬˚∆˙©ƒ∂ßåπø“‘≠–ºª•¶§∞¢#€¡±œ!@$%^&*(),.;?":{+}|<-=>/]{1,}'
                , password_special_chars_login):

            emoji_label_clause_3_password_login.config(text=f'{emoji.emojize(":check_mark_button:")}')

        else:

            emoji_label_clause_3_password_login.config(text=f'{emoji.emojize(":cross_mark:")}')

    check_rules_button_password_login = Button(login_screen, text="check rules", command=check_password)

    check_rules_button_password_login.place(x=355, y=260)

    check_clause_1_password_login = Label(login_screen, text="At least 8 characters")

    check_clause_1_password_login.place(x=150, y=250)

    check_clause_2_password_login = Label(login_screen, text="At least 2 capital letters")

    check_clause_2_password_login.place(x=150, y=270)

    check_clause_3_password_login = Label(login_screen, text="At least 1 special character")

    check_clause_3_password_login.place(x=150, y=290)

    check_clause_4_password_login = Label(login_screen, text="At least 2 numbers")

    check_clause_4_password_login.place(x=150, y=310)

    login_button = Button(login_screen, text='Log in', command=log_in)

    login_button.place(x=350, y=550)

    emoji_label_clause_1_password_login = Label(login_screen)

    emoji_label_clause_1_password_login.place(x=125, y=250)

    emoji_label_clause_2_password_login = Label(login_screen)

    emoji_label_clause_2_password_login.place(x=125, y=270)

    emoji_label_clause_3_password_login = Label(login_screen)

    emoji_label_clause_3_password_login.place(x=125, y=290)

    emoji_label_clause_4_password_login = Label(login_screen)

    emoji_label_clause_4_password_login.place(x=125, y=310)

    emoji_label_clause_1_email_address_login = Label(login_screen)

    emoji_label_clause_1_email_address_login.place(x=125, y=80)

    emoji_label_clause_2_email_address_login = Label(login_screen)

    emoji_label_clause_2_email_address_login.place(x=125, y=100)

    emoji_label_clause_3_email_address_login = Label(login_screen)

    emoji_label_clause_3_email_address_login.place(x=125, y=120)

    optional_details_text_description = Label(login_screen, text="the details below are optional")

    optional_details_text_description.place(x=150, y=365)

    nickname_entry_label = Label(login_screen, text="Nickname")

    nickname_entry_label.place(x=80, y=390)

    nickname_entry = Entry(login_screen)

    nickname_entry.place(x=150, y=390)

    date_of_birth_entry = Entry(login_screen)

    date_of_birth_entry.place(x=150, y=480)

    date_of_birth_entry_label = Label(login_screen, text="Date of Birth")

    date_of_birth_entry_label.place(x=63, y=480)

    date_of_birth_entry_label_description = Label(login_screen, text="Enter like this: DD/MM/YYYY")

    date_of_birth_entry_label_description.place(x=65, y=455)

    conn.commit()
    # commits any changes the users inputs have made to the database
    conn.close()
    # closes the connection for the database


def no():
    """this defines our function with the name of yes
    this takes the user to the main screen """
    conn = sqlite3.connect(database_name)
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
    conn = sqlite3.connect(database_name)
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
