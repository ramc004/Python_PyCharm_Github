from tkinter import *
# tells the program to use the built-in library Tkinter and import all the modules found within Tkinter
from PIL import ImageTk, Image
# finds the library PIL and imports two separate packages, ImageTk and Image allowing us to store images inside tkinter
import sqlite3
# sqlite3 is the library I will be using for databases allowing us to read, query and write to and from the database
import emoji
# emoji library allowing us to show emojis inside our program
import re
# allows us to ensure the user follows rules when entering a password
import random
# uses an algorithm to generate random numbers
import smtplib
# allows to send emails from a specific email using smtp, which stands for simple mail transfer protocol
from email.message import EmailMessage

# allows me to place a specific message inside our email; I will be combining this with the above library to send emails
database_name = 'Home Automation System Database.db'
# gives a name to our database so that we can call it throughout our program
proceed = Tk()
# we are creating a variable called proceed, and setting it equal to our tkinter window
# so whenever we need to put something inside out Tkinter window we just have to call proceed
proceed.title('A Level Computer Science Project')
# we are calling our variable root and defining more of its attributes giving our tkinter window a title
proceed.geometry("450x300")
# gives some restrictions for our tkinter window of 400x300
conn = sqlite3.connect(database_name)
# connects to sqlite3 using a variable name of conn short for connection
# finds the variable database_name and calls our database file from above
c = conn.cursor()
# creates a cursor allowing us to execute sql commands
c.execute("""CREATE TABLE IF NOT EXISTS users (
        userID int PRIMARY KEY not null,
        email_address text not null, 
        password text not null, 
        accessLevel text, 
        nickname text, 
        date_of_birth DATE)""")
# using the execute command creates our table within our database giving it a name of users
# only creates the database if it hasn't already been created
# I have decided to make userID a primary key
# creates the field, userID, inside our database as an integer
# this field cannot equal null it has to be given a value more than zero
# creates another field, email_address, this time will be text allowing a user to input their email address
# creates another field, accessLevel, allowing us to later on give different access levels
# creates fields, nickname and date_of_birth
# these fields are only optional meaning they can be empty inside the database
# if they do enter a nickname it will be stored as text
# if they enter a date_of_birth then it will be stored as a DATE
findAdminQuery = "SELECT userID FROM users WHERE accessLevel == 'admin'"
c.execute(findAdminQuery)
ourAdmin = c.fetchone()
if not ourAdmin:
    selectIDQuery = "SELECT userID FROM users ORDER BY userID DESC LIMIT 1"
    c.execute(selectIDQuery)
    new_highestID = c.fetchone()
    if new_highestID is not None:
        new_highestID = new_highestID[0]
        newID2 = int(new_highestID) + 1
    else:
        newID2 = 0
    createAdminQuery = "INSERT INTO users(userID,email_address,password,accessLevel) " \
                       "VALUES ('%s','admin','root','admin')" % newID2
    c.execute(createAdminQuery)
register_verify = False


# creates a variable called register_verify and sets it to false

def check_verification(email_address, password, actual_code, user_code, register_screen):
    conn = sqlite3.connect(database_name)
    # connects to sqlite3 using a variable name of conn short for connection
    # finds the variable database_name and calls our database file from above
    c = conn.cursor()
    # creates a cursor allowing us to execute sql commands
    verified = True
    emoji_label_clause_1_password_check_verification = Label(register_screen)
    emoji_label_clause_1_password_check_verification.place(x=125, y=300)
    emoji_label_clause_4_password_check_verification = Label(register_screen)
    emoji_label_clause_4_password_check_verification.place(x=125, y=364)
    emoji_label_clause_3_password_check_verification = Label(register_screen)
    emoji_label_clause_3_password_check_verification.place(x=125, y=342)
    emoji_label_clause_2_password_check_verification = Label(register_screen)
    emoji_label_clause_2_password_check_verification.place(x=125, y=320)
    if not email_address:
        no_email_entry = Label(register_screen, text="please enter email")
        no_email_entry.place(x=150, y=160)
        no_email_entry.config(foreground="red")
        verified = False
    else:
        email_has_been_entered = Label(register_screen, text="you entered an email, you are now verified")
        email_has_been_entered.place(x=150, y=160)
        email_has_been_entered.config(foreground="green")
    if not password:
        no_password_entry = Label(register_screen, text="  please enter password")
        no_password_entry.place(x=150, y=385)
        no_password_entry.config(foreground="red")
        verified = False
    else:
        password_has_been_entered = Label(register_screen, text="you entered a password")
        password_has_been_entered.place(x=150, y=385)
        password_has_been_entered.config(foreground="green")
        successful_sign_up = Label(register_screen, text="you have been successfully signed up, you may now log in")
        successful_sign_up.place(x=75, y=500)
        successful_sign_up.config(foreground="green")
    if len(password) < 8:
        emoji_label_clause_1_password_check_verification.config(text=f'{emoji.emojize(":cross_mark:")}')
        verified = False
    else:
        emoji_label_clause_1_password_check_verification.config(text=f'{emoji.emojize(":check_mark_button:")}')
    if not re.search(r'[A-Z]{1,}', password):
        emoji_label_clause_2_password_check_verification.config(text=f'{emoji.emojize(":cross_mark:")}')
        verified = False
    else:
        emoji_label_clause_2_password_check_verification.config(text=f'{emoji.emojize(":check_mark_button:")}')
    if not re.search(r'[1234567890]{1,}', password):
        emoji_label_clause_4_password_check_verification.config(text=f'{emoji.emojize(":cross_mark:")}')
        verified = False
    else:
        emoji_label_clause_4_password_check_verification.config(text=f'{emoji.emojize(":check_mark_button:")}')
    if not re.search(r'[∑´®†¥¨~`Ω≈ç√∫µ≤≥«æ…¬˚∆˙©ƒ∂ßåπø“‘≠–ºª•¶§∞¢#€¡±œ!@$%^&*(),.;?":{+}|<-=>/]{1,}', password):
        emoji_label_clause_3_password_check_verification.config(text=f'{emoji.emojize(":cross_mark:")}')
        verified = False
    else:
        emoji_label_clause_3_password_check_verification.config(text=f'{emoji.emojize(":check_mark_button:")}')
    findEmailQuery = "SELECT userID FROM users WHERE email_address == '%s'" % email_address
    c.execute(findEmailQuery)
    emailID = c.fetchone()
    if emailID:
        email_already_exists_label = Label(register_screen, text="   this email is already linked to an account")
        email_already_exists_label.place(x=150, y=160)
        email_already_exists_label.config(foreground="orange")
        verified = False
    if actual_code != user_code:
        code_label_failure = Label(register_screen, text="code incorrect")
        code_label_failure.place(x=200, y=227)
        code_label_failure.config(foreground="red")
        verified = False
    else:
        code_label_success = Label(register_screen, text="  code correct")
        code_label_success.place(x=200, y=227)
        code_label_success.config(foreground="green")
    conn.commit()
    # commits any changes the users inputs have made to the database
    conn.close()
    return verified


def register():
    """this function creates a new window which allows the user to register their details
     and saves them to the database"""
    conn = sqlite3.connect(database_name)
    # connects to sqlite3 using a variable name of conn short for connection
    # finds the variable database_name and calls our database file from above
    c = conn.cursor()
    # creates a cursor allowing us to execute sql commands
    register_screen = Tk()
    # creates a new Tkinter user interface
    register_screen.title("Register")
    # gives the new Tkinter interface a title of 'Register'
    register_screen.geometry("500x600")
    # gives the starting size for the Tkinter user interface
    register_screen.resizable(False, False)

    # limits the user from resizing the interface

    def sign_up(email_address_db, password_db, actual_code, user_code):
        """this function is used for when the user clicks on the sign_up button
        I have passed is_verified, email_address_db, password_db as parameters through this function
        we are then able to call any of these parameters throughout our program
        """
        conn = sqlite3.connect(database_name)
        # connects to sqlite3 using a variable name of conn short for connection
        # finds the variable database_name and calls our database file from above
        c = conn.cursor()
        # creates a cursor allowing us to execute sql commands
        if check_verification(email_address_db, password_db, actual_code, user_code, register_screen):
            # creates a clause using a parameter from our function
            # the function will only get here if the user has been verified
            if email_address_db == "admin":
                accessLevel = "admin"
            else:
                accessLevel = "userAccount"

            selectQuery = "SELECT userID FROM users ORDER BY userID DESC LIMIT 1"

            c.execute(selectQuery)

            highestID = c.fetchone()
            if highestID is not None:
                highestID = highestID[0]
                newID = int(highestID) + 1
            else:
                newID = 0
            if not email_address_db:
                no_email_entry = Label(register_screen, text="   please enter email")
                no_email_entry.place(x=150, y=160)
                no_email_entry.config(foreground="red")
            else:
                email_has_been_entered = Label(register_screen, text="you entered an email")
                email_has_been_entered.place(x=150, y=160)
                email_has_been_entered.config(foreground="green")
            if not password_db:
                no_password_entry = Label(register_screen, text="  please enter password")
                no_password_entry.place(x=150, y=385)
                no_password_entry.config(foreground="red")
            else:
                password_has_been_entered = Label(register_screen, text="you entered a password")
                password_has_been_entered.place(x=150, y=385)
                password_has_been_entered.config(foreground="green")
            if email_address_db and password_db:
                insertQuery = """INSERT INTO users
                        (userID, email_address, password, accessLevel) 
                        VALUES
                        (%d,"%s","%s","%s")""" % (newID, email_address_db, password_db, accessLevel)
                c.execute(insertQuery)
        conn.commit()
        # commits any changes the users inputs have made to the database
        conn.close()

    email_address_entry_register_screen = Entry(register_screen)

    email_address_entry_register_screen.place(x=150, y=70)

    email_address_text_register_screen = Label(register_screen, text="Email address")

    email_address_text_register_screen.place(x=56.2, y=72)

    verify_box_entry = Entry(register_screen)

    verify_box_entry.place(x=150, y=200)

    verify_text = Label(register_screen, text=" Enter six digit code: ")

    verify_text.place(x=13, y=203)

    code = str(random.randint(100000, 999999))

    def send_email():
        """"""
        emailRecipient = email_address_entry_register_screen.get()

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        emailSender = "ramcaleb50@gmail.com"
        file = open("hello.txt", "r")
        emailPassword = file.read()
        file.close()
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

    check_clause_1_password = Label(register_screen, text="At least 8 characters")

    check_clause_1_password.place(x=150, y=300)

    check_clause_2_password = Label(register_screen, text="At least 2 capital letters")

    check_clause_2_password.place(x=150, y=320)

    check_clause_3_password = Label(register_screen, text="At least 1 special character")

    check_clause_3_password.place(x=150, y=340)

    check_clause_4_password = Label(register_screen, text="At least 2 numbers")

    check_clause_4_password.place(x=150, y=360)

    emoji_label_clause_1_password = Label(register_screen)

    emoji_label_clause_1_password.place(x=125, y=300)

    emoji_label_clause_2_password = Label(register_screen)

    emoji_label_clause_2_password.place(x=125, y=325)

    emoji_label_clause_3_password = Label(register_screen)

    emoji_label_clause_3_password.place(x=125, y=355)

    emoji_label_clause_4_password = Label(register_screen)

    emoji_label_clause_4_password.place(x=125, y=370)

    emoji_label_clause_1_email_address = Label(register_screen)

    emoji_label_clause_1_email_address.place(x=125, y=100)

    emoji_label_clause_2_email_address = Label(register_screen)

    emoji_label_clause_2_email_address.place(x=125, y=120)

    emoji_label_clause_3_email_address = Label(register_screen)

    emoji_label_clause_3_email_address.place(x=125, y=140)

    sign_up_button = Button(register_screen, text='Sign Up',
                            command=lambda: sign_up(email_address_entry_register_screen.get(),
                                                    password_entry.get(), code, verify_box_entry.get()))

    sign_up_button.place(x=350, y=430)

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
                or "admin" in email_login \
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

    optional_details_text_description = Label(login_screen,
                                              text="the details below are optional or just keep from before")

    optional_details_text_description.place(x=100, y=365)

    nickname_entry_label = Label(login_screen, text="Nickname")

    nickname_entry_label.place(x=80, y=390)

    nickname_entry = Entry(login_screen)

    nickname_entry.place(x=150, y=390)

    date_of_birth_entry = Entry(login_screen)

    date_of_birth_entry.place(x=150, y=480)

    date_of_birth_entry_label = Label(login_screen, text="Date of Birth")

    date_of_birth_entry_label.place(x=63, y=480)

    date_of_birth_entry_label_description = Label(login_screen, text="Enter like this: YYYY/MM/DD")

    date_of_birth_entry_label_description.place(x=65, y=455)
    login_button = Button(login_screen, text='Log in',
                          command=lambda: log_in(email_address_entry_login_screen.get()
                                                 , password_entry_login.get(), nickname_entry.get(),
                                                 date_of_birth_entry.get()))

    login_button.place(x=350, y=550)

    conn.commit()
    # commits any changes the users inputs have made to the database
    conn.close()

    # closes the connection for the database

    def log_in(email_address_log_in, password_db_log_in, nickname, date_of_birth):
        conn = sqlite3.connect(database_name)
        # creates a database with a name of 'User Login Page Database' or connects to a database with this name
        c = conn.cursor()
        # creates a cursor
        getPasswordQuery = "SELECT password FROM users WHERE email_address == '%s'" % email_address_log_in
        c.execute(getPasswordQuery)
        savedPassword = c.fetchone()
        if savedPassword is None:
            email_does_exist_label = Label(login_screen, text="email doesn't exist")
            email_does_exist_label.place(x=160, y=140)
            email_does_exist_label.config(foreground="red")
        else:
            savedPassword = savedPassword[0]
            email_does_exist_label = Label(login_screen, text="       email is correct")
            email_does_exist_label.place(x=160, y=140)
            email_does_exist_label.config(foreground="green")
            if password_db_log_in == savedPassword:
                password_correct = Label(login_screen, text="        password is correct")
                password_correct.place(x=160, y=330)
                password_correct.config(foreground="green")
                if nickname:
                    updateNicknameQuery = "UPDATE users SET nickname = '%s' WHERE email_address == '%s'" % (
                        nickname, email_address_log_in)
                    c.execute(updateNicknameQuery)
                    nickname_has_been_entered = Label(login_screen, text="nickname has been entered     ")
                    nickname_has_been_entered.place(x=150, y=420)
                    nickname_has_been_entered.config(foreground="blue")
                else:
                    nickname_has_not_been_entered = Label(login_screen, text="nickname has not been entered")
                    nickname_has_not_been_entered.place(x=150, y=420)
                    nickname_has_not_been_entered.config(foreground="orange")
                if date_of_birth:
                    updateDOBQuery = "UPDATE users SET date_of_birth = '%s' WHERE email_address == '%s'" % (
                        date_of_birth, email_address_log_in)
                    c.execute(updateDOBQuery)
                    date_of_birth_has_been_entered = Label(login_screen, text="date of birth has been entered    ")
                    date_of_birth_has_been_entered.place(x=145, y=510)
                    date_of_birth_has_been_entered.config(foreground="blue")
                else:
                    date_of_birth_not_entered = Label(login_screen, text="date of birth has not been entered")
                    date_of_birth_not_entered.place(x=140, y=510)
                    date_of_birth_not_entered.config(foreground="orange")
                getAccessLevelQuery = "SELECT accessLevel FROM users WHERE email_address == '%s'" % email_address_log_in
                c.execute(getAccessLevelQuery)
                access_Level = c.fetchone()
                access_Level = access_Level[0]

                if access_Level == "admin":
                    adminPage = Tk()
                    adminPage.title("Admin Page")
                    adminPage.geometry("500x700")
                    adminPage.resizable(False, False)
                    admin_email_previous = Label(adminPage, text="enter email with information to be changed below")
                    admin_email_previous.place(x=100, y=25)
                    admin_email_previous_entry = Entry(adminPage)
                    admin_email_previous_entry.place(x=165, y=45)
                    admin_email_change = Label(adminPage, text="enter new email")
                    admin_email_change.place(x=62, y=115)
                    admin_email_change_entry = Entry(adminPage)
                    admin_email_change_entry.place(x=175, y=115)
                    admin_password_change = Label(adminPage, text="enter new password")
                    admin_password_change.place(x=35, y=145)
                    admin_password_change_entry = Entry(adminPage)
                    admin_password_change_entry.place(x=175, y=145)
                    admin_nickname_change = Label(adminPage, text="enter new nickname")
                    admin_nickname_change.place(x=35, y=175)
                    admin_nickname_change_entry = Entry(adminPage)
                    admin_nickname_change_entry.place(x=175, y=175)
                    admin_Date_of_birth_change = Label(adminPage, text="enter new date of birth")
                    admin_Date_of_birth_change.place(x=20, y=205)
                    admin_Date_of_birth_change_entry = Entry(adminPage)
                    admin_Date_of_birth_change_entry.place(x=175, y=205)
                    change_button = Button(adminPage, text='Change information', command=lambda: change_information(
                        admin_email_previous_entry.get(), admin_email_change_entry.get(),
                        admin_password_change_entry.get(), admin_nickname_change_entry.get(),
                        admin_Date_of_birth_change_entry.get(), adminPage))
                    change_button.place(x=350, y=565)
                elif access_Level == "userAccount":
                    home_automation_system_window = Tk()
                    home_automation_system_window.title("Home Automation System")
                    home_automation_system_window.geometry("500x600")
                    home_automation_system_window.resizable(False, False)
            else:
                password_does_not_match = Label(login_screen, text="password does not match")
                password_does_not_match.place(x=160, y=330)
                password_does_not_match.config(foreground="red")
        conn.commit()
        conn.close()


def change_information(oldEmail, newEmail, newPassword, newNickname, newDOB, adminPage):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    # creates a cursor
    if oldEmail:
        getUserIDQuery = "SELECT userID FROM users where email_address = '%s'" % oldEmail
        c.execute(getUserIDQuery)
        id = c.fetchone()

        if id:
            id = id[0]
            email_is_valid = Label(adminPage, text="email is valid")
            email_is_valid.place(x=190, y=75)
            email_is_valid.config(foreground="green")

            if newEmail:
                changeEmailQuery = "UPDATE users SET email_address = '%s' WHERE userID == '%s'" % (
                    newEmail, id)
                c.execute(changeEmailQuery)
            if newPassword:
                changePasswordQuery = "UPDATE users SET password = '%s' WHERE userID == '%s'" % (
                    newPassword, id)
                c.execute(changePasswordQuery)
            if newNickname:
                changeNicknameQuery = "UPDATE users SET nickname = '%s' WHERE userID == '%s'" % (
                    newNickname, id)
                c.execute(changeNicknameQuery)
            if newDOB:
                changeDOBQuery = "UPDATE users SET date_of_birth = '%s' WHERE userID == '%s'" % (
                    newDOB, id)
                c.execute(changeDOBQuery)
            fields_updated = Label(adminPage, text="fields have been updated if edited")
            fields_updated.place(x=150, y=250)
            fields_updated.config(foreground="green")
        else:
            previous_email_not_found = Label(adminPage, text="previous email not found")
            previous_email_not_found.place(x=175, y=75)
            previous_email_not_found.config(foreground="red")
    else:
        previous_email_not_found = Label(adminPage, text=" you haven't entered an email")
        previous_email_not_found.place(x=175, y=75)
        previous_email_not_found.config(foreground="red")
    conn.commit()
    conn.close()


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
