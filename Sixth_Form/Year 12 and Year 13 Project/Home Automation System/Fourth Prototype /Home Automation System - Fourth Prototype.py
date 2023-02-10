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
import speech_recognition as sr
#
import requests
#
from bs4 import BeautifulSoup
#

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#
database_name = 'Home Automation System.db'
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
# if they enter a date_of_birth then it will be stored as a DATE which allows the user to enter their dob simply
findAdminQuery = "SELECT userID FROM users WHERE accessLevel == 'admin'"
# creates a variable called findAdminQuery
# this will select the userID from our table but only where they are not a customer
# this is if they wanted to update users inputs
c.execute(findAdminQuery)
# executes the findAdminQuery to ensure its commands are executed
MyAdmin = c.fetchone()
# creates a variable, MyAdmin, forces the program to only select one record of admin at a time
if not MyAdmin:
    # where the person is trying to log in to the system it will check if they are not admin
    # also if no admin has been created yet
    selectIDQuery = "SELECT userID FROM users ORDER BY userID DESC LIMIT 1"
    # where the person is not admin a new query variable is created, selectIDQuery
    # this will select the userID of the person which wasn't an admin
    c.execute(selectIDQuery)
    # runs the command above
    new_highestID = c.fetchone()
    # creates another variable and only allows one piece of data to be selected at a time
    if new_highestID is not None:
        # as long as there is no other users they will be placed below the admin user
        new_highestID = new_highestID[0]
        # sets our variable from above to be equal to the first piece of data stored in the database
        newID2 = int(new_highestID) + 1
        # creates a new variable which will be incremented one more than the variable above,
        # so it appears like admin, then users who have created accounts
    else:
        newID2 = 0
        # this is if the admin had been pre-created beforehand
    createAdminQuery = "INSERT INTO users(userID,email_address,password,accessLevel) " \
                       "VALUES ('%s','admin','root','admin')" % newID2
    # places the admin user in the table with an access level of admin and an email of root and password of admin
    c.execute(createAdminQuery)
    # executes the admin query to ensure the above database statement follows through
register_verify = False
# creates a variable called register_verify outside any functions allowing us to call it from anywhere
# sets the user to being register to false for now, because they haven't entered any correct credentials at this point


def check_verification(email_address, password, actual_code, user_code, register_screen):
    """this function has been created to ensure the user follows all the rules when trying to register their details
    i have passed email_address, password, actual_code, user_code and register_screen as parameters
    to allows us to use them throughout this function"""
    conn = sqlite3.connect(database_name)
    # connects to sqlite3 using a variable name of conn short for connection
    # finds the variable database_name and calls our database file from above
    c = conn.cursor()
    # creates a cursor allowing us to execute sql commands
    verified = True
    # creates a new variable and as long as each of the rules are follow it will be true
    emoji_label_clause_1_password_check_verification = Label(register_screen)
    # places a variable for the first emoji to tell the user how there password is wrong
    # this one is for at least 8 characters
    emoji_label_clause_1_password_check_verification.place(x=125, y=300)
    # places the label using the place function along the x axis and down the y axis
    emoji_label_clause_4_password_check_verification = Label(register_screen)
    # this is used to check the user has inputted at least 2 numbers
    emoji_label_clause_4_password_check_verification.place(x=125, y=364)
    # tells the system where to place the variable inside our register_screen
    emoji_label_clause_3_password_check_verification = Label(register_screen)
    # checks if the user has entered 1 special character
    emoji_label_clause_3_password_check_verification.place(x=125, y=342)
    # using a place function built in to tkinter places the variable 125 along and 342 down
    emoji_label_clause_2_password_check_verification = Label(register_screen)
    # further down this variable is called and configured depending on whether or not the user has used 2 capitals
    emoji_label_clause_2_password_check_verification.place(x=125, y=320)
    # ensures the emoji is being configured next to the appropriate clause
    if not email_address:
        # this checks if the email_address field is filled
        no_email_entry = Label(register_screen, text="                             please enter email")
        # tells the user to enter an email
        no_email_entry.place(x=150, y=170)
        # places the label using the place function, ensure it goes just below email box
        no_email_entry.config(foreground="red")
        # configures this text to the colour red to show the user there is an issue
        verified = False
        # calls the 'verified' variable and sets it to false to ensure it doesn't let them sign up
    else:
        # however if an email had been entered
        email_has_been_entered = Label(register_screen, text="you entered an email, you are now verified")
        # the program creates a new variable
        # using the label function placing text telling the user they have entered an email
        email_has_been_entered.place(x=140, y=170)
        # tells the system how to place the variable made above
        email_has_been_entered.config(foreground="green")
        # configures the text message to green telling the user they have followed this rule
    if not password:
        # if the user has not entered anything into the password entry box
        no_password_entry = Label(register_screen, text="  please enter password")
        # creates a new variable as a label and text telling user to enter a password
        no_password_entry.place(x=150, y=385)
        # this places the variable above using the x axis and the y axis
        no_password_entry.config(foreground="red")
        # sets the colour of the please enter password text to red showing the user they're doing something wrong
        verified = False
        # calls the verified variable and sets it to false where no password was entered
    else:
        # but if the user does enter a password that follows the rules and also an email and a correct code
        password_has_been_entered = Label(register_screen, text="you entered a password")
        # it will a new you entered a password label
        password_has_been_entered.place(x=150, y=385)
        # it then places this label beneath the password clauses
        password_has_been_entered.config(foreground="green")
        # sets the foreground of the variable to green to show the user they have been successful
        successful_sign_up = Label(register_screen, text="you have been successfully signed up, you may now log in")
        # message telling user they are free to go and log in to the system
        successful_sign_up.place(x=75, y=500)
        # places the successful message on the screen using the place function
        successful_sign_up.config(foreground="green")
        # by colouring the text green informs the user they have followed all the necessary rules
    if len(password) < 8:
        # where password's length is less than 8 characters
        emoji_label_clause_1_password_check_verification.config(text=f'{emoji.emojize(":cross_mark:")}')
        # sets the emoji to a cross using the emoji library
        verified = False
        # calls the verified variable and sets it false blocking the user from successfully signing up
    else:
        # if the user's inputted password is 8 or more characters then they have followed this rule
        emoji_label_clause_1_password_check_verification.config(text=f'{emoji.emojize(":check_mark_button:")}')
        # the system will then overlay a tick emoji overriding the cross emoji
    if not re.search(r'[A-Z]{1,}', password):
        # using the re library to check the user has entered 2 or more capital letters
        emoji_label_clause_2_password_check_verification.config(text=f'{emoji.emojize(":cross_mark:")}')
        # calls the variable from above and places the cross emoji
        verified = False
        # sets the verified variable to false if the user hasn't entered two capital letters
    else:
        # where the user has entered 2 or more capital letters
        emoji_label_clause_2_password_check_verification.config(text=f'{emoji.emojize(":check_mark_button:")}')
        # changes the emoji to a tick to show the user they have followed this rule
    if not re.search(r'[1234567890]{1,}', password):
        # if user doesn't have 2 or more number in their password
        emoji_label_clause_4_password_check_verification.config(text=f'{emoji.emojize(":cross_mark:")}')
        # the system will find where we placed this variable from above and configure it to a cross
        verified = False
        # this sets the verified variable to false to ensure the user's details won't be saved unless follow rules
    else:
        # if they have entered 2 or more numbers
        emoji_label_clause_4_password_check_verification.config(text=f'{emoji.emojize(":check_mark_button:")}')
        # changes the emoji next to the final clause to a tick
    if not re.search(r'[∑´®†¥¨~`Ω≈ç√∫µ≤≥«æ…¬˚∆˙©ƒ∂ßåπø“‘≠–ºª•¶§∞¢#€¡±œ!@$%^&*(),.;?":{+}|<-=>/]{1,}', password):
        # where the user hasn't entered 1 or more special characters
        emoji_label_clause_3_password_check_verification.config(text=f'{emoji.emojize(":cross_mark:")}')
        # sets the label to a cross telling the user they have not followed this rule
        verified = False
        # calls the verified variable and sets it equal to false
    else:
        # if the user does have the required amount of special characters
        emoji_label_clause_3_password_check_verification.config(text=f'{emoji.emojize(":check_mark_button:")}')
        # the system shows this by changing the cross into a tick
    findEmailQuery = "SELECT userID FROM users WHERE email_address == '%s'" % email_address
    # this selects the email addresses from the database and ensures they haven't entered an email that already links
    c.execute(findEmailQuery)
    # executes our command searching for email addresses
    emailID = c.fetchone()
    # creates a new variable and forces only one piece of data at a time to be compared
    if emailID:
        # where the emailID entered by user is already saved to database
        email_already_exists_label = Label(register_screen, text="   this email is already linked to an account")
        # tkinter will create a new label telling the user they have already signed up with this account
        email_already_exists_label.place(x=140, y=170)
        # tells the system where to put this label, this will go directly below all the email rules
        email_already_exists_label.config(foreground="orange")
        # sets the colour of the text for this label to orange
        # telling the user their is a minor issue with their details
        verified = False
        # calls the verified variable and sets it to false stopping the user from registering incorrect details
    if actual_code != user_code:
        # fetches the code sent via email and matches with the code entered by the user
        code_label_failure = Label(register_screen, text="code incorrect")
        # tells the user they have mistyped their code
        code_label_failure.place(x=200, y=227)
        # places this label just below the code entry box
        code_label_failure.config(foreground="red")
        # tells the user this a major issue they need to fix
        verified = False
        # the verified status of the variable is set to false,
        # preventing the user from registering incorrect information
    else:
        # if the user has copied the code correctly
        code_label_success = Label(register_screen, text="  code correct")
        # system tells user code is correct
        code_label_success.place(x=200, y=227)
        # system places label at same place as code incorrect to ensure only one message appears at a time
        code_label_success.config(foreground="green")
        # configures the label to green showing the user the code is correct
    conn.commit()
    # commits any changes the users inputs have made to the database
    conn.close()
    # closes our connection for the database
    return verified
    # indicates the verified variable has been used in this function and is now finished being adapted


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
                # this checks if the user is trying to sign up as a user or an admin
                accessLevel = "admin"
                # where the accessLevel is admin if the email address was admin
            else:
                # however if the email address was not admin
                accessLevel = "userAccount"
                # the system will correctly assume they are a user trying to create an account
            selectQuery = "SELECT userID FROM users ORDER BY userID DESC LIMIT 1"
            # creates a new variable and checks the database calling from the users table selecting the userID field
            # and ordering it descending to ensure the database can be read from efficiently
            c.execute(selectQuery)
            # executes the selectQuery command
            highestID = c.fetchone()
            # creates a new variable and only allows one piece of data to be fetched at a time
            if highestID is not None:
                # where there are other users already saved to the database
                highestID = highestID[0]
                # call the first one 0 so it places it in order
                newID = int(highestID) + 1
                # and places thew new id incremented 1 below the past id
            else:
                # if this is the first id to be added
                newID = 0
                # place it as the first id
            if not email_address_db:
                # where the user has not entered an email
                no_email_entry = Label(register_screen, text="   please enter email")
                # creates a variable
                # sets it equal to Tkinter's label function with text informing the user they need to enter an email
                no_email_entry.place(x=150, y=160)
                # tells the system where to place this new label function, just below the email clauses
                no_email_entry.config(foreground="red")
                # configures the text to red telling the user they need to fix this before moving on
            else:
                # where the user has entered an email
                email_has_been_entered = Label(register_screen, text="you entered an email")
                # new variable created, using text within label to tell user they entered an email
                email_has_been_entered.place(x=140, y=170)
                # tells system where to place new variable using the built in place function within tkinter
                email_has_been_entered.config(foreground="green")
                # by showing the user green text tells them they have followed this rule
            if not password_db:
                # where the user has not entered a password
                no_password_entry = Label(register_screen, text="  please enter password")
                # creates a new variable and sets it equal to a label telling user to enter a password
                no_password_entry.place(x=150, y=385)
                # this places the please enter a password text below the password clauses
                no_password_entry.config(foreground="red")
                # colours the text red telling the user they have to follow this rule before moving on
            else:
                # however if they have entered a password
                password_has_been_entered = Label(register_screen, text="you entered a password")
                # tells the user they have entered a password
                password_has_been_entered.place(x=150, y=385)
                # places this label and overrides the past label
                password_has_been_entered.config(foreground="green")
                # sets the colour of this label to green telling the user they have followed this rule
            if email_address_db and password_db:
                # only where both the email and password have been entered
                insertQuery = """INSERT INTO users
                        (userID, email_address, password, accessLevel) 
                        VALUES
                        (%d,"%s","%s","%s")""" % (newID, email_address_db, password_db, accessLevel)
                # creates a new variable and tells sql to insert the information into the database
                c.execute(insertQuery)
                # executes the query to ensure the database will be updated when committed
        conn.commit()
        # commits any changes the users inputs have made to the database
        conn.close()
        # closes the database connection until reopened
    email_address_entry_register_screen = Entry(register_screen)
    # creates a new variable and sets it equal to an entry box placing it in the register_screen
    email_address_entry_register_screen.place(x=150, y=70)
    # tells the system where to place this register screen
    email_address_text_register_screen = Label(register_screen, text="Email address")
    # creates another new variable telling the user what to write in the entry box, their email address
    email_address_text_register_screen.place(x=56.2, y=72)
    # places the text telling the user to write an email address
    verify_box_entry = Entry(register_screen)
    # creates another entry box this time for the 6 digit code
    verify_box_entry.place(x=150, y=200)
    # places this six digit code entry box below the email address clauses
    verify_text = Label(register_screen, text=" Enter six digit code: ")
    # tells the user to enter a six digit code
    verify_text.place(x=13, y=203)
    # places this label next to the verify box so the user knows where to put the information
    code = str(random.randint(100000, 999999))
    # using the random function which uses an algorithm to cycle through numbers and creates a six digit code

    def send_email():
        """this function is called when the user clicks the verify button
        it will then send the the user a short email"""
        emailRecipient = email_address_entry_register_screen.get()
        # fetches the email address the user has inputted and sets it equal to emailRecipient to be called later on
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        # opens up the mail server where email will be sent from
        emailSender = "ramcaleb50@gmail.com"
        # creates an emailSender variable to called later, and sets this to an email address,
        # this will be the email address the code is sent by
        file = open("fp.txt", "r")
        # creates a variable and tells it to open a file and allows the system to read from the file
        emailPassword = file.read()
        # sets the emailPassword, which will be called below, equal to reading the file
        file.close()
        # closes our file opened from above
        subject = "Code Verification Email"
        # sets another variable which will be called below to code verification email
        email = EmailMessage()
        # making another variable and sets it equal to the class EmailMessage
        # allowing us to set the where the email is going where its coming from and a message
        email["From"] = emailSender
        # calls the emailSender variable above and sets it equal to who is sending the email
        email["To"] = emailRecipient
        # calls the email address the user entered to tell the system where to send the email
        email["Subject"] = subject
        # adds a subject onto the email to tell the user why they are receiving this email
        email.set_content("Your code is: " + code)
        # gives the user their code by using the built in function set_content
        if emailSender and emailPassword and emailRecipient:
            # as long the emailPassword, emailSender and the emailRecipient exists
            sent_label = Label(register_screen, text="Email sent!", width=20)
            # creates a label, placing it inside the register_screen with text of email sent
            # fixes the width of this label
            sent_label.place(x=320, y=103)
            # places this label just underneath the verify button
            sent_label.config(foreground="green")
            # sets the colour of the label to green to show the user has successfully sent the email
            why_clause_email_sent = Label(register_screen, text="click button above to see why")
            # informs the user to click the button so they can see why their email wasn't set
            why_clause_email_sent.place(x=315, y=152)
            # places this clause just below the verify button
            why_clause_email_sent.config(foreground="green")
            # configures the label to green
            server.login(emailSender, emailPassword)
            # using the built-in function passes through the emailSender and the emailPassword logging the user in
            server.sendmail(emailSender, emailRecipient, email.as_string())
            # using the sendmail function it fetches the emailSender, emailRecipient and the email the user has entered
            server.quit()
            # now the email has been sent, we can close the server
        else:
            # although if the user has not entered an email
            not_sent_label = Label(register_screen, text="Email has failed to send 😭", width=20)
            # it will make a new variable and set it equal to a label with text, Email has failed to send
            why_clause_email_not_sent = Label(register_screen, text="click button above to see why")
            # creates another variable telling the user how to tell what they haven't included
            why_clause_email_not_sent.place(x=315, y=152)
            # tells the system where to place the label
            why_clause_email_not_sent.config(foreground="orange")
            # configures the text to orange showing the user they need to follow the rules
            not_sent_label.place(x=320, y=103)
            # places label just above the verify button
            not_sent_label.config(foreground="orange")
            # colours the label orange warning the user they haven't followed the rules
    email_address_verify_button = Button(register_screen, text="Verify", command=send_email)
    # creates a button in the register_screen with text of verify and puts a command of send_email
    # where this button is clicked the email will be sent
    email_address_verify_button.place(x=365, y=74)
    # tells system where to place the verify button
    verify_button_description = Label(register_screen, text="sends your 6 digit code")
    # describes to the user what the verify button does
    verify_button_description.place(x=330, y=32)
    # places the button description above the verify button
    verify_button_arrow = Label(register_screen, text="↕️")
    # creates a label inside our tkinter window with text
    verify_button_arrow.place(x=388, y=50)
    # places this label in between the description and the verify button

    def check_email_address():
        """this ensure the user's email address follows all the rules"""
        email_register = email_address_entry_register_screen.get()
        # creates a new variable and sets it equal to whatever the user entered inside the email address entry box
        # this is using the get function built in to python
        if "@" in email_register:
            # as long as the user's email has an @ sign inside of it
            emoji_label_clause_2_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
            # configures the label to be a tick showing the user they have followed this rule
        else:
            # on the other hand if the user has not inputted an @ sign in their email
            emoji_label_clause_2_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
            # then the emoji library will work with tkinter and configure the text to a cross
        if "gmail.com" in email_register \
                or "yahoo.com" in email_register or "outlook.com" in email_register \
                or "richardchalloner.com" in email_register or "icloud.com" in email_register \
                or "mail.com" in email_register or "email.com" in email_register \
                or "aol.com" in email_register or "proton.me" in email_register \
                or "tutanota.com" in email_register or "tutanota.de" in email_register \
                or "tutamail.com" in email_register or "tuta.io" in email_register \
                or "keemail.me" in email_register or "zohomail.eu" in email_register \
                or "tmmwj.com" in email_register or "gmx.com" in email_register \
                or "gmx.co.uk" in email_register or "yahoo.co.uk" in email_register:
            # this ensure they are trying to send the email to an existing email address with a correct domain
            emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
            # as long as the user's email address contains one of the above domains then a tick will be shown
        else:
            # however if they do not have any domain that exists in the list above
            emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
            # this changes the text from a tick to a cross where there is no existing domain
        if "caleb" in email_register \
                or "fish" in email_register or "hannah" in email_register or "mark" in email_register \
                or "niki" in email_register or "sean" in email_register or "katherine" in email_register \
                or "kat" in email_register or "alyssa" in email_register or "katy" in email_register \
                or "isaac" in email_register or "esther" in email_register or "ben" in email_register \
                or "connor" in email_register or "daisy" in email_register or "josh" in email_register \
                or "zoey" in email_register or "valentina" in email_register or "stacy" in email_register \
                or "george" in email_register or "graham" in email_register or "isabella" in email_register \
                or "bella" in email_register or "ella" in email_register or "grace" in email_register \
                or "ellis" in email_register or "emmanuel" in email_register or "christian" in email_register \
                or "finn" in email_register or "fin" in email_register or "rachael" in email_register \
                or "liv" in email_register or "olivia" in email_register or "elaine" in email_register \
                or "bert" in email_register or "nilusha" in email_register or "andy" in email_register \
                or "emma" in email_register or "emily" in email_register or "amelia" in email_register \
                or "charlotte" in email_register or "sophia" in email_register or "mia" in email_register \
                or "ava" in email_register or "eva" in email_register or "keira" in email_register \
                or "kiera" in email_register or "harper" in email_register or "jessie" in email_register \
                or "alex" in email_register or "liam" in email_register or "noah" in email_register \
                or "elijah" in email_register or "oliver" in email_register or "ollie" in email_register \
                or "lucas" in email_register or "luke" in email_register or "james" in email_register \
                or "alexia" in email_register or "aaron" in email_register or "william" in email_register \
                or "will" in email_register or "jo" in email_register or "joseph" in email_register \
                or "benjamin" in email_register or "henry" in email_register or "laura" in email_register \
                or "theo" in email_register or "daniel" in email_register or "marios" in email_register \
                or "mario" in email_register or "benjy" in email_register or "arthur" in email_register \
                or "john" in email_register or "tim" in email_register or "javier" in email_register \
                or "xavier" in email_register or "eve" in email_register or "niamh" in email_register \
                or "niam" in email_register or "alannah" in email_register or "reshee" in email_register \
                or "amelie" in email_register or "nishtha" in email_register or "sofia" in email_register \
                or "abi" in email_register or "abigail" in email_register or "penelope" in email_register \
                or "brooke" in email_register or "brook" in email_register or "brooklyn" in email_register \
                or "sophie" in email_register or "laila" in email_register or "jaimie" in email_register \
                or "claudia" in email_register or "elena" in email_register or "eleanor" in email_register \
                or "ram" in email_register or "mat" in email_register or "matt" in email_register \
                or "matthew" in email_register or "mary" in email_register or "martha" in email_register \
                or "peter" in email_register or "tamar" in email_register or "darius" in email_register \
                or "edith" in email_register or "elise" in email_register or "adam" in email_register:
            # checks their email has some form of name in its email
            emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
            # this will adapt a tick next door to the clause to do with account name
        else:
            # but if the user's entered email address does not have one of the above names
            emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
            # the previous mark, tick, will change to a cross
    check_rules_button_email_address = Button(register_screen, text="check rules", command=check_email_address)
    # creates a variable and sets it equal to a button placed in the register_screen with text being check rules
    # it will then run through the above rules adapting the text to a tick or a cross
    check_rules_button_email_address.place(x=355, y=125)
    # tells the system where to place the check rules button
    check_clause_1_email_address = Label(register_screen, text="Contains account name")
    # creates a variable and sets it equal to a label inside the register_screen with text
    check_clause_1_email_address.place(x=150, y=100)
    # places the first clause inside our tkinter window below the email address entry box
    check_clause_2_email_address = Label(register_screen, text="'@' sign")
    # this puts a label next to the tick or cross clause to show how the user has put an @ sign or not
    check_clause_2_email_address.place(x=150, y=120)
    # places the clause inside our tkinter window
    check_clause_3_email_address = Label(register_screen, text="Domain name")
    # makes a new variable and sets it equal to another clause telling the user how to input information
    check_clause_3_email_address.place(x=150, y=140)
    # directs the system how to place the label
    password_label = Label(register_screen, text='Password')
    # tells the user what they need to put in the entry boxes
    password_label.place(x=80, y=250)
    # places the text from our label inside our tkinter window
    password_entry = Entry(register_screen, show='*')
    # creates another variable and sets it equal to another entry box where the users password can be inputted
    # to ensure security the users password will stay safe we star out whatever they type in to the password box
    password_entry.place(x=150, y=250)
    # places these stars inside the tkinter window

    def show_password():
        """this defines a function which allows the users password to be shown where check box is ticked"""
        if password_entry.cget('show') == '*':
            # tells the system to not show stars where the check box is not selected
            password_entry.config(show='')
            # instead show the actual password the user is entering
        else:
            # but if the user has selected the show password box
            password_entry.config(show='*')
            # the system will show stars in place of their password
    show_password_check_box = Checkbutton(register_screen, text='Show Password', command=show_password)
    # creates the check button box putting text next to the box
    show_password_check_box.place(x=85, y=277)
    # places the button in the tkinter window
    check_clause_1_password = Label(register_screen, text="At least 8 characters")
    # password clause telling the user they have to enter 8 characters
    check_clause_1_password.place(x=150, y=300)
    # places this label in our tkinter window
    check_clause_2_password = Label(register_screen, text="At least 2 capital letters")
    # creates a variable for a label housed in the register_screen telling the user to enter 2 capital letters
    check_clause_2_password.place(x=150, y=320)
    # tells the program where to put the 2 clause
    check_clause_3_password = Label(register_screen, text="At least 1 special character")
    # creates a new variable for a new clause
    # sets it equal to a label which shall be put inside the register_screen with some text
    check_clause_3_password.place(x=150, y=340)
    # lets the system know where the label should be placed
    check_clause_4_password = Label(register_screen, text="At least 2 numbers")
    # creates a new variable and lets it equal to a label placed inside the register_screen with text
    check_clause_4_password.place(x=150, y=360)
    # places our variable created above using the 'x' and the 'y' axis
    emoji_label_clause_1_password = Label(register_screen)
    # creates a clause telling the user what to put in their password
    emoji_label_clause_1_password.place(x=125, y=300)
    # places the clause in the tkinter window using the place function
    emoji_label_clause_2_password = Label(register_screen)
    # creates a second password clause and places this label in our register_screen tkinter window
    emoji_label_clause_2_password.place(x=125, y=325)
    # tells the system where to place the above label created
    emoji_label_clause_3_password = Label(register_screen)
    # this will inform the user if there password conforms to the third rule
    emoji_label_clause_3_password.place(x=125, y=355)
    # places this beneath the password entry box
    emoji_label_clause_4_password = Label(register_screen)
    # informs the user they have or haven't followed a specific rule
    emoji_label_clause_4_password.place(x=125, y=370)
    # places this rule inside the tkinter window
    emoji_label_clause_1_email_address = Label(register_screen)
    # email rules are displayed on the register screen
    emoji_label_clause_1_email_address.place(x=125, y=100)
    # places these rules using a place function
    emoji_label_clause_2_email_address = Label(register_screen)
    # creates a new variable and sets it equal to a label telling the system to put in the register screen
    emoji_label_clause_2_email_address.place(x=125, y=120)
    # places this label telling the user about the email address on the screen
    emoji_label_clause_3_email_address = Label(register_screen)
    # a new variable is made and then set equal to a label which is set to be put inside the register_screen window
    emoji_label_clause_3_email_address.place(x=125, y=140)
    # places the final email clause on the screen just above the six digit code entry box
    sign_up_button = Button(register_screen, text='Sign Up',
                            command=lambda: sign_up(email_address_entry_register_screen.get(),
                                                    password_entry.get(), code, verify_box_entry.get()))
    # creates a new variable and sets it equal to a button and allows a command to be run through this button
    # this allowed me to pass parameters through this function
    # meaning they can be used throughout
    sign_up_button.place(x=350, y=430)
    # places the button using the x and y axis
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
    # creates an entry box inside the login_screen
    email_address_entry_login_screen.place(x=150, y=50)
    # places this entry box 150 across and 50 down
    email_address_text_login_screen = Label(login_screen, text="Email address")
    # tells the user which information they need to enter with text
    email_address_text_login_screen.place(x=56.2, y=52)
    # places email address text next to the email address box

    def check_email_address():
        """similar function to that from the register screen
        activated when the user clicks the check rules button adjacent to the email address rules"""
        email_login = email_address_entry_login_screen.get()
        # creates a new variable and sets it equal to the email address the user has inputted
        if "@" in email_login:
            # where the users email inputted contains an @ sign
            emoji_label_clause_2_email_address_login.config(text=f'{emoji.emojize(":check_mark_button:")}')
            # configures a tick to be placed next to the second email clause
        else:
            # but if the users email doesn't contain an @ sign
            emoji_label_clause_2_email_address_login.config(text=f'{emoji.emojize(":cross_mark:")}')
            # configures the label with text to be a cross showing the user they need to fix this rule
        if "gmail.com" in email_login \
                or "yahoo.com" in email_login or "outlook.com" in email_login or "richardchalloner.com" in email_login \
                or "icloud.com" in email_login or "mail.com" in email_login or "email.com" in email_login \
                or "aol.com" in email_login or "proton.me" in email_login or "tutanota.com" in email_login \
                or "tutanota.de" in email_login or "tutamail.com" in email_login or "tuta.io" in email_login \
                or "keemail.me" in email_login or "zohomail.eu" in email_login or "tmmwj.com" in email_login \
                or "gmx.com" in email_login or "gmx.co.uk" in email_login or "yahoo.co.uk" in email_login:
            # as long the user's email has one of the above domain names
            emoji_label_clause_3_email_address_login.config(text=f'{emoji.emojize(":check_mark_button:")}')
            # the system will put a tick next to the clause saying contains domain name
        else:
            # but if the user's email doesn't have one of the above domains
            emoji_label_clause_3_email_address_login.config(text=f'{emoji.emojize(":cross_mark:")}')
            # the system will display directing the user to add a domain name
        if "caleb" in email_login \
                or "fish" in email_login or "admin" in email_login or "hannah" in email_login \
                or "mark" in email_login or "niki" in email_login or "sean" in email_login \
                or "katherine" in email_login or "kat" in email_login or "alyssa" in email_login \
                or "katy" in email_login or "isaac" in email_login or "esther" in email_login or "ben" \
                in email_login or "connor" in email_login or "daisy" in email_login or "josh" in email_login \
                or "zoey" in email_login or "valentina" in email_login or "stacy" in email_login \
                or "george" in email_login or "graham" in email_login or "isabella" in email_login \
                or "bella" in email_login or "ella" in email_login or "grace" in email_login \
                or "emmanuel" in email_login or "christian" in email_login or "finn" in email_login \
                or "fin" in email_login or "rachael" in email_login or "liv" in email_login \
                or "olivia" in email_login or "elaine" in email_login or "bert" in email_login \
                or "nilusha" in email_login or "andy" in email_login or "emma" in email_login \
                or "emily" in email_login or "amelia" in email_login or "ellis" in email_login \
                or "charlotte" in email_login or "sophia" in email_login or "mia" in email_login \
                or "ava" in email_login or "eva" in email_login or "keira" in email_login \
                or "kiera" in email_login or "harper" in email_login or "jessie" in email_login \
                or "alex" in email_login or "liam" in email_login or "noah" in email_login \
                or "elijah" in email_login or "oliver" in email_login or "ollie" in email_login \
                or "lucas" in email_login or "luke" in email_login or "james" in email_login \
                or "alexia" in email_login or "aaron" in email_login or "william" in email_login \
                or "will" in email_login or "jo" in email_login or "joseph" in email_login \
                or "benjamin" in email_login or "henry" in email_login or "laura" in email_login \
                or "theo" in email_login or "daniel" in email_login or "marios" in email_login \
                or "mario" in email_login or "benjy" in email_login or "arthur" in email_login \
                or "john" in email_login or "tim" in email_login or "javier" in email_login \
                or "xavier" in email_login or "eve" in email_login or "niamh" in email_login \
                or "niam" in email_login or "alannah" in email_login or "reshee" in email_login \
                or "amelie" in email_login or "nishtha" in email_login or "sofia" in email_login \
                or "abi" in email_login or "abigail" in email_login or "penelope" in email_login \
                or "brooke" in email_login or "brook" in email_login or "brooklyn" in email_login \
                or "sophie" in email_login or "laila" in email_login or "jaimie" in email_login \
                or "claudia" in email_login or "elena" in email_login or "eleanor" in email_login \
                or "ram" in email_login or "mat" in email_login or "matt" in email_login \
                or "matthew" in email_login or "mary" in email_login or "martha" in email_login \
                or "peter" in email_login or "tamar" in email_login or "darius" in email_login \
                or "edith" in email_login or "elise" in email_login or "adam" in email_login:
            # if the above names or in the user's email
            emoji_label_clause_1_email_address_login.config(text=f'{emoji.emojize(":check_mark_button:")}')
            # the user will be presented with a green tick
        else:
            # where the user hasn't got an account name
            emoji_label_clause_1_email_address_login.config(text=f'{emoji.emojize(":cross_mark:")}')
            # the program will tell them by showing a red cross
    check_rules_button_email_address_login = Button(login_screen, text="check rules", command=check_email_address)
    # creates a variable connecting it to a button inside the login_screen with text and a command
    # the command wil check which rules pass or fail
    check_rules_button_email_address_login.place(x=355, y=105)
    # connects back to the variable created and places this 355 along the x axis and 105 down the y axis
    check_clause_1_email_address_login = Label(login_screen, text="Contains account name")
    # puts text on screen telling the user contains account name
    check_clause_1_email_address_login.place(x=150, y=80)
    # places the above 'contains account name' text inside our window
    check_clause_2_email_address_login = Label(login_screen, text="'@' sign")
    # creates a new variable for the email clause telling the user whether or not they have an @ sign in the email
    check_clause_2_email_address_login.place(x=150, y=100)
    # places our @ sign text in our login_screen window
    check_clause_3_email_address_login = Label(login_screen, text="Domain name")
    # makes a new label in tkinter inside our login_screen where its text will be Domain name
    check_clause_3_email_address_login.place(x=150, y=120)
    # tells the system where to place the domain name text
    password_label_login = Label(login_screen, text='Password')
    # creates a new label telling the user what information to enter into each entry box
    password_label_login.place(x=80, y=190)
    # places the password information next to the password entry box
    password_entry_login = Entry(login_screen, show='*')
    # creates a new variable and sets it equal to an entry box showing stars in place of whatever the user enters
    password_entry_login.place(x=150, y=190)
    # directs the program to where the entry box is to be placed inside the login_screen

    def show_password():
        """this defines a function which allows the users password to be shown where check box is ticked"""
        if password_entry_login.cget('show') == '*':
            # this says that if check button ticked password will be shown and stars will be hidden
            password_entry_login.config(show='')
            # by configuring the stars to instead show whatever is being entered
        else:
            # if the checkbutton is not ticked then password will stay starred
            password_entry_login.config(show='*')
            # by configuring the password_entry with stars
    show_password_check_box_login = Checkbutton(login_screen, text='Show Password', command=show_password)
    # creates a variable and sets it equal to a checkbutton which will have text of show password
    # has a command linking to the above function telling the system how to behave
    # whether or not the check box is ticked
    show_password_check_box_login.place(x=85, y=227)
    # places the checkButton along the x axis and down the y axis

    def check_password():
        """function to ensure password on login screen follows the rules to create a secure password """
        password_length_login = password_entry_login.get()
        # creates a new variable and sets it equal to whichever password the user has chosen by using the get function
        if len(password_length_login) >= 8:
            # where the password has a length of 8 or more characters
            emoji_label_clause_1_password_login.config(text=f'{emoji.emojize(":check_mark_button:")}')
            # configure the clause emoji to a tick
        else:
            # however if the user's password is 7 characters or less
            emoji_label_clause_1_password_login.config(text=f'{emoji.emojize(":cross_mark:")}')
            # sets the emoji to a cross informing the user they need to re-check their password
        password_caps_login = password_entry_login.get()
        # creates another new variable and sets it equal to the password entered by the user
        if re.search(r'[A-Z]{1,}', password_caps_login):
            # using the re library searches through the users password entered
            # ensures there is 1 or more capital letter
            emoji_label_clause_2_password_login.config(text=f'{emoji.emojize(":check_mark_button:")}')
            # places a tick emoji on the screen following the place instructions created
        else:
            # but if the user has not put capital letters in their password
            emoji_label_clause_2_password_login.config(text=f'{emoji.emojize(":cross_mark:")}')
            # emoji will reflect this by being a red cross
        password_numbers_login = password_entry_login.get()
        # new variable now equal to the information entered into the password entry box
        if re.search(r'[1234567890]{2,}', password_numbers_login):
            # calls the re library and using the built in search function, searches through the user's entered password
            emoji_label_clause_4_password_login.config(text=f'{emoji.emojize(":check_mark_button:")}')
            # either changes the cross to a tick or shows the user a tick
        else:
            # where the user's password doesn't follow this rule
            emoji_label_clause_4_password_login.config(text=f'{emoji.emojize(":cross_mark:")}')
            # adapts the emoji to show a cross emoji
        password_special_chars_login = password_entry_login.get()
        # creates another variable and sets it equal to the users password entered
        if re.search(r'[∑´®†¥¨~`Ω≈ç√∫µ≤≥«æ…¬˚∆˙©ƒ∂ßåπø“‘≠–ºª•¶§∞¢#€¡±œ!@$%^&*(),.;?":{+}|<-=>/]{1,}'
                , password_special_chars_login):
            # as long as it contains 1 or more special characters from the above special characters list
            emoji_label_clause_3_password_login.config(text=f'{emoji.emojize(":check_mark_button:")}')
            # emoji next to the special characters clause will be a tick
        else:
            # but if the user's password has no special characters
            emoji_label_clause_3_password_login.config(text=f'{emoji.emojize(":cross_mark:")}')
            # then the system will be forced to configure a cross instead
    check_rules_button_password_login = Button(login_screen, text="check rules", command=check_password)
    # creates a check rules button to allow the user to see how they may need to adapt their password
    # where they are not being logged in
    check_rules_button_password_login.place(x=355, y=260)
    # allows the system to know where i want the check rules button to go
    check_clause_1_password_login = Label(login_screen, text="At least 8 characters")
    # creates another variable telling the user the first clause they must follow for their password
    check_clause_1_password_login.place(x=150, y=250)
    # shows the user how they need to place this label inside our tkinter window using the place function
    check_clause_2_password_login = Label(login_screen, text="At least 2 capital letters")
    # creates another variable where it will show a label on the login screen with text
    check_clause_2_password_login.place(x=150, y=270)
    # this will place the password clause 20 below the above clause
    check_clause_3_password_login = Label(login_screen, text="At least 1 special character")
    # creates a new variable and gives it a label that will have text saying at least 1 special character
    # hopefully informing the user the information they have to input into their password
    check_clause_3_password_login.place(x=150, y=290)
    # informs the system where to place the third password clause
    check_clause_4_password_login = Label(login_screen, text="At least 2 numbers")
    # final clause for password made be creating a variable setting it equal label with text in login screen
    check_clause_4_password_login.place(x=150, y=310)
    # places the label inside the login screen
    emoji_label_clause_1_password_login = Label(login_screen)
    # creates another variable this time set for the emoji
    emoji_label_clause_1_password_login.place(x=125, y=250)
    # places it next to the corresponding clause
    emoji_label_clause_2_password_login = Label(login_screen)
    # creates a variable setting it equal to a label to be placed inside the login screen
    emoji_label_clause_2_password_login.place(x=125, y=270)
    # this label is to be placed using the place function following the x and y axis
    emoji_label_clause_3_password_login = Label(login_screen)
    # creates the third clause for the password label emoji
    emoji_label_clause_3_password_login.place(x=125, y=290)
    # tells the program where to put this third clause
    emoji_label_clause_4_password_login = Label(login_screen)
    # final clause emoji label for password
    emoji_label_clause_4_password_login.place(x=125, y=310)
    # lets the system know to place the label in login screen according to the x and y axis
    emoji_label_clause_1_email_address_login = Label(login_screen)
    # new emoji label, this time for the email address equal to a label placed inside the login screen
    emoji_label_clause_1_email_address_login.place(x=125, y=80)
    # places this label inside our tkinter window following the place rules set
    emoji_label_clause_2_email_address_login = Label(login_screen)
    # creates a new variable and sets it equal to a label
    # this is to be used for the second clause saying whether or not the user has fulfilled the rules
    emoji_label_clause_2_email_address_login.place(x=125, y=100)
    # allows the program to know it has to place this emoji label next to and in line with the second clause
    emoji_label_clause_3_email_address_login = Label(login_screen)
    # final email clause informing the user about the details inside their email
    emoji_label_clause_3_email_address_login.place(x=125, y=120)
    # this will be beside the clause corresponding to the text, allowing the user to know how to adapt their password
    optional_details_text_description = Label(login_screen,
                                              text="the details below are optional or just keep from before")
    # on the log in screen there are some optional data entry boxes this label is telling the user how they work
    optional_details_text_description.place(x=100, y=365)
    # places the information about optional details inside our tkinter window 100 along and 365 down
    nickname_entry_label = Label(login_screen, text="Nickname")
    # tells the user using a label what they need to enter, in this case, a nickname
    nickname_entry_label.place(x=80, y=390)
    # places this label next to the nickname entry box and below the optional details information
    nickname_entry = Entry(login_screen)
    # creates an entry box on the login screen for the user to input their desired nickname if they choose to
    nickname_entry.place(x=150, y=390)
    # informs the system where this entry box needs to be placed, next to the nickname label
    date_of_birth_entry = Entry(login_screen)
    # another one of the optional fields is date of birth
    date_of_birth_entry.place(x=150, y=480)
    # tells the user how to place the date of birth entry box
    date_of_birth_entry_label = Label(login_screen, text="Date of Birth")
    # applies a label on the login screen saying date of birth
    date_of_birth_entry_label.place(x=63, y=480)
    # places this label next to the date of birth entry box
    date_of_birth_entry_label_description = Label(login_screen, text="Enter like this: YYYY/MM/DD")
    # makes another label telling the user how to input the date, this helps the database accept their date of birth
    date_of_birth_entry_label_description.place(x=65, y=455)
    # places the description on how the user must enter their information
    login_button = Button(login_screen, text='Log in',
                          command=lambda: log_in(email_address_entry_login_screen.get()
                                                 , password_entry_login.get(), nickname_entry.get(),
                                                 date_of_birth_entry.get()))
    # makes a button with text of log in and command of log_in,
    # when button pressed the system will run through the log_in function passing through all the named parameters
    login_button.place(x=350, y=550)
    # tells the system where to put the login button, near the bottom of the window
    conn.commit()
    # commits any changes the users inputs have made to the database
    conn.close()
    # closes the connection for the database

    def log_in(email_address_log_in, password_db_log_in, nickname, date_of_birth):
        """this function informs the user of the fields the user has inputted
        and whether or not they match the saved information by connecting to a and reading from the database"""
        conn = sqlite3.connect(database_name)
        # creates a database with a name of 'User Login Page Database' or connects to a database with this name
        c = conn.cursor()
        # creates a cursor
        getPasswordQuery = "SELECT password FROM users WHERE email_address == '%s'" % email_address_log_in
        # creates a new variable and sets it equal to a sql command checking if the users email address entered
        # can be found inside the database
        c.execute(getPasswordQuery)
        # execute the above command allow us to call and use it throughout
        savedPassword = c.fetchone()
        # ensures only one password at a time is fetched
        if savedPassword is None:
            # where the user has entered an email which wasn't found in the database
            email_does_exist_label = Label(login_screen, text="email doesn't exist")
            # a label is created and placed inside the login screen saying email doesn't exist
            email_does_exist_label.place(x=160, y=140)
            # this tells the program where the text needs to go
            email_does_exist_label.config(foreground="red")
            # configures the colour of the text to be red to ensure the user knows there is an issue with details given
        else:
            # where the email does exist in the database
            savedPassword = savedPassword[0]
            # new variable is set up calling the savedPassword variable meaning when system is searching
            # its start place will be at 0 and it will only search and fetch one password at a time
            email_does_exist_label = Label(login_screen, text="       email is correct")
            # the system will then inform the user the email is correct
            email_does_exist_label.place(x=160, y=140)
            # places the 'email is correct' text inside the login screen
            email_does_exist_label.config(foreground="green")
            # configures the text to green to show the user they have followed this rule
            if password_db_log_in == savedPassword:
                # as long as the users password entered
                # when trying to log in matches the password saved linking to email typed in
                password_correct = Label(login_screen, text="        password is correct")
                password_correct.place(x=160, y=330)
                password_correct.config(foreground="green")
                # creates a new variable to be used informing the user their password is correct
                # connects this to a label function in tkinter which will go inside the login_screen
                # gives our label some text saying password is correct
                # with some space at front to ensure the password is wrong label doesn't overlay
                if nickname:
                    # where the user has decided to enter into the optional field
                    updateNicknameQuery = "UPDATE users SET nickname = '%s' WHERE email_address == '%s'" % (
                        nickname, email_address_log_in)
                    # new variable created and set equal to a sql statement
                    # adapts the users table specifically the nickname column corresponding to the email entered
                    c.execute(updateNicknameQuery)
                    # executes the command into our database
                    nickname_has_been_entered = Label(login_screen, text="nickname has been entered     ")
                    # tells the user they have entered a nickname
                    nickname_has_been_entered.place(x=150, y=420)
                    # places our label above along the x and y axis
                    nickname_has_been_entered.config(foreground="blue")
                    # configures the text of the label to blue
                    # this is to the show the user they have filled an optional piece of data
                else:
                    # however if the user hasn't entered a nickname
                    nickname_has_not_been_entered = Label(login_screen, text="nickname has not been entered")
                    # the program will create a new label connecting to a new variable
                    # with text informing the user they have not inputted a nickname
                    nickname_has_not_been_entered.place(x=150, y=420)
                    # places the label created above using the x and y axis variable
                    nickname_has_not_been_entered.config(foreground="orange")
                    # allows the system to give a specific colour of orange to the labels text
                    # orange shows the user that they are allowed to move on without filling box
                if date_of_birth:
                    # where user has entered a date of birth
                    updateDOBQuery = "UPDATE users SET date_of_birth = '%s' WHERE email_address == '%s'" % (
                        date_of_birth, email_address_log_in)
                    # another new variable is set equal to a new sql command
                    # updating users table wherever the email address is in the table for their date of birth
                    c.execute(updateDOBQuery)
                    # using our cursor uses the execute function within sql to execute the command created above
                    date_of_birth_has_been_entered = Label(login_screen, text="date of birth has been entered    ")
                    # creates a label informing the user they gave
                    date_of_birth_has_been_entered.place(x=145, y=510)
                    # tells the system where to put the label just created
                    date_of_birth_has_been_entered.config(foreground="blue")
                    # configures the text to be blue to show the user their date of birth has beren added
                else:
                    # where the user hasn't entered a date of birth
                    date_of_birth_not_entered = Label(login_screen, text="date of birth has not been entered")
                    # program will make a new variable connecting it to a new label to be put on login_screen with text
                    date_of_birth_not_entered.place(x=140, y=510)
                    # tells program where to put this new label
                    date_of_birth_not_entered.config(foreground="orange")
                    # gives the label a colour by connecting to the variable
                getAccessLevelQuery = "SELECT accessLevel FROM users WHERE email_address == '%s'" % email_address_log_in
                # only lets a user put a date of birth and nickname
                c.execute(getAccessLevelQuery)
                # executes the command above
                access_Level = c.fetchone()
                # forces program to fetch only one piece of data at a time
                access_Level = access_Level[0]
                # sets the access level search from 0 so this is where it starts

                if access_Level == "admin":
                    # the following code is where the admin account is trying update users' information
                    # where the access level has been fetched and found to be admin
                    adminPage = Tk()
                    # creates a new variable and sets it equal to a new tkinter window
                    adminPage.title("Admin Page")
                    # gives this new tkinter page a title of admin page
                    adminPage.geometry("500x700")
                    # calling the variable created for the tkinter page just created gives it a starting size
                    adminPage.resizable(False, False)
                    # stops the user from resizing the window
                    admin_email_previous = Label(adminPage, text="enter email with information to be changed below")
                    # creates a new variable for the admin user to input
                    # connects it to the adminPage and gives it some text
                    admin_email_previous.place(x=100, y=25)
                    # tells program where to place specific label
                    admin_email_previous_entry = Entry(adminPage)
                    # 
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
                    # stop commenting for now when get here and move to line 1193
                    home_automation_system_prompt_window = Tk()
                    home_automation_system_prompt_window.title("Home Automation System Adding Devices")
                    home_automation_system_prompt_window.geometry("500x600")
                    home_automation_system_prompt_window.resizable(False, False)
                    add_device_question = Label(home_automation_system_prompt_window,
                                                text="Would you like to add a device?")
                    add_device_question.place(x=45, y=45)

                    def yes_button_to_add_device_question_command():
                        device_brand_question_label = Label(home_automation_system_prompt_window,
                                                            text="What brand is the device you would like to pair?")
                        device_brand_question_label.place(x=20, y=250)
                        device_brand_entry_box = Entry(home_automation_system_prompt_window)
                        device_brand_entry_box.place(x=45, y=270)
                        enter_button_device_brand = Button(home_automation_system_prompt_window, text="Enter")
                        enter_button_device_brand.place(x=250, y=268)
                        device_adding_description_label_first_line = Label(home_automation_system_prompt_window,
                                                                           text="Download the corresponding app and "
                                                                                "follow their instructions to add the "
                                                                                "device")
                        device_adding_description_label_first_line.place(x=25, y=300)
                        device_adding_description_label_second_line = Label(home_automation_system_prompt_window,
                                                                            text="You can then click next to connect it"
                                                                                 " via this system")
                        device_adding_description_label_second_line.place(x=25, y=320)

                    yes_button_to_add_device_question = Button(home_automation_system_prompt_window,
                                                               text="Yes",
                                                               command=yes_button_to_add_device_question_command)
                    yes_button_to_add_device_question.place(x=75, y=100)

                    def voice_assistant_button_pressed_prompt_window():
                        """"""
                        def find_weather():
                            """"""
                            url = "https://www.google.co.uk/search?q=weather"
                            #
                            find_weather_result = requests.get(url, headers=headers)
                            #
                            soup = BeautifulSoup(find_weather_result.text, "html.parser")
                            #
                            temperature = soup.select("#wob_tm")[0].getText().strip()
                            #
                            weather_description = soup.select("#wob_dc")[0].getText().strip()
                            #
                            return temperature, weather_description
                            #

                        def do_maths(maths_question):
                            """"""
                            maths_question = maths_question.replace(" ", "+")
                            #
                            url = "https://www.google.co.uk/search?q=%s" % maths_question
                            #
                            do_maths_result = requests.get(url, headers=headers)
                            #
                            soup = BeautifulSoup(do_maths_result.text, "html.parser")
                            #
                            answer = soup.select("#cwos")[0].getText().strip()
                            #
                            return answer
                            #

                        r = sr.Recognizer()
                        # variable used to recognise speech

                        with sr.Microphone() as source:
                            #
                            r.adjust_for_ambient_noise(source, duration=0.2)
                            #
                            print("Speak now")
                            #
                            audio = r.listen(source)
                            #
                            speech = r.recognize_google(audio)
                            #
                            print("You said: " + speech)
                            #
                            if "weather" in speech:
                                #
                                tempValue, description = find_weather()
                                #
                                print(tempValue + " degree celsius", description)
                                #
                            else:
                                #
                                print("I am not sure how to help you, click on voice assistant again to retry")
                                #
                            if "calculator" in speech:
                                #
                                r.adjust_for_ambient_noise(source, duration=0.2)
                                #
                                print("Ask your question")
                                #
                                questionAudio = r.listen(source)
                                #
                                question = r.recognize_google(questionAudio)
                                #
                                result = do_maths(question)
                                #
                                print(result)
                                #
                            else:
                                #
                                print("I am not sure how to help you, click on voice assistant again to retry")
                                #

                    voice_assistant_prompt_window = Button(home_automation_system_prompt_window,
                                                           text="Voice Assistant",
                                                           command=voice_assistant_button_pressed_prompt_window)
                    voice_assistant_prompt_window.place(x=350, y=500)

                    def next_button():
                        adding_devices_window = Tk()
                        adding_devices_window.title("Searching for Devices")
                        adding_devices_window.geometry("500x600")
                        adding_devices_window.resizable(False, False)

                    next_button = Button(home_automation_system_prompt_window, text="Next",
                                         command=next_button)
                    next_button.place(x=230, y=550)

                    def no_button_to_add_device_question_command():
                        home_automation_system_prompt_window.destroy()
                        home_automation_system_control_devices_window = Tk()
                        home_automation_system_control_devices_window.title("Home Automation System Control Devices")
                        home_automation_system_control_devices_window.geometry("500x600")
                        home_automation_system_control_devices_window.resizable(False, False)

                        def show_rooms_for_devices():
                            return

                        rooms_for_lights_button = Button(home_automation_system_control_devices_window, text="Rooms",
                                                         command=show_rooms_for_devices)
                        rooms_for_lights_button.place(x=45, y=100)

                        def voice_assistant_control_window_button_pressed():
                            return

                        voice_assistant_control_devices = Button(home_automation_system_control_devices_window,
                                                                 text="Voice Assistant",
                                                                 command=voice_assistant_control_window_button_pressed)
                        voice_assistant_control_devices.place(x=350, y=500)

                    no_button_to_add_device_question = Button(home_automation_system_prompt_window,
                                                              text="No",
                                                              command=no_button_to_add_device_question_command)
                    no_button_to_add_device_question.place(x=155, y=100)

            else:
                password_does_not_match = Label(login_screen, text="password does not match")
                password_does_not_match.place(x=160, y=330)
                password_does_not_match.config(foreground="red")
        conn.commit()
        conn.close()


def change_information(oldEmail, newEmail, newPassword, newNickname, newDOB, adminPage):
    """"""
    conn = sqlite3.connect(database_name)
    #
    c = conn.cursor()
    # creates a cursor
    if oldEmail:
        #
        getUserIDQuery = "SELECT userID FROM users where email_address = '%s'" % oldEmail
        #
        c.execute(getUserIDQuery)
        #
        id = c.fetchone()
        #
        if id:
            #
            id = id[0]
            #
            email_is_valid = Label(adminPage, text="email is valid")
            #
            email_is_valid.place(x=190, y=75)
            #
            email_is_valid.config(foreground="green")
            #
            if newEmail:
                #
                changeEmailQuery = "UPDATE users SET email_address = '%s' WHERE userID == '%s'" % (
                    newEmail, id)
                #
                c.execute(changeEmailQuery)
                #
            if newPassword:
                #
                changePasswordQuery = "UPDATE users SET password = '%s' WHERE userID == '%s'" % (
                    newPassword, id)
                #
                c.execute(changePasswordQuery)
                #
            if newNickname:
                #
                changeNicknameQuery = "UPDATE users SET nickname = '%s' WHERE userID == '%s'" % (
                    newNickname, id)
                #
                c.execute(changeNicknameQuery)
                #
            if newDOB:
                #
                changeDOBQuery = "UPDATE users SET date_of_birth = '%s' WHERE userID == '%s'" % (
                    newDOB, id)
                #
                c.execute(changeDOBQuery)
                #
            fields_updated = Label(adminPage, text="fields have been updated if edited")
            #
            fields_updated.place(x=150, y=250)
            #
            fields_updated.config(foreground="green")
            #
        else:
            #
            previous_email_not_found = Label(adminPage, text="previous email not found")
            #
            previous_email_not_found.place(x=175, y=75)
            #
            previous_email_not_found.config(foreground="red")
            #
    else:
        #
        previous_email_not_found = Label(adminPage, text=" you haven't entered an email")
        #
        previous_email_not_found.place(x=175, y=75)
        #
        previous_email_not_found.config(foreground="red")
        #
    conn.commit()
    #
    conn.close()
    #


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
