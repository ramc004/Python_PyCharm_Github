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
        accessLevel text)""")
# using the execute command creates our table within our database giving it a name of users
# only creates the database if it hasn't already been created
# I have decided to make userID a primary key
# creates the field, userID, inside our database as an integer
# this field cannot equal null it has to be given a value more than zero
# creates another field, email_address, this time will be text allowing a user to input their email address
# creates another field, accessLevel, allowing us to later on give different access levels


def check_verification(email_address, password, actual_code, user_code, register_screen):
    """this function has been created to ensure the user follows all the rules when trying to register their details
    i have passed email_address, password, actual_code, user_code and register_screen as parameters
    to allows us to use them throughout this function"""
    connection_check_verification = sqlite3.connect(database_name)
    # connects to sqlite3 using a variable name of connection short for connection
    # finds the variable database_name and calls our database file from above
    cursor_check_verification = connection_check_verification.cursor()
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
        no_email_entry = Label(register_screen, text="please enter email", width=75)
        # tells the user to enter an email
        no_email_entry.place(x=0, y=170)
        # places the label using the place function, ensure it goes just below email box
        no_email_entry.config(foreground="red")
        # configures this text to the colour red to show the user there is an issue
        verified = False
        # calls the 'verified' variable and sets it to false to ensure it doesn't let them sign up
    else:
        # however if an email had been entered
        email_has_been_entered = Label(register_screen, text="you entered an email")
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
    cursor_check_verification.execute(findEmailQuery)
    # executes our command searching for email addresses
    emailID = cursor_check_verification.fetchone()
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
        code_label_failure = Label(register_screen, text="code incorrect, not verified")
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
        code_label_success = Label(register_screen, text="code correct, now verified")
        # system tells user code is correct
        code_label_success.place(x=200, y=227)
        # system places label at same place as code incorrect to ensure only one message appears at a time
        code_label_success.config(foreground="green")
        # configures the label to green showing the user the code is correct
    connection_check_verification.commit()
    # commits any changes the users inputs have made to the database
    connection_check_verification.close()
    # closes our connection for the database
    return verified
    # indicates the verified variable has been used in this function and is now finished being adapted


def register():
    """this function creates a new window which allows the user to register their details
     and saves them to the database"""
    connection_register = sqlite3.connect(database_name)
    # connects to sqlite3 using a variable name of conn short for connection
    # finds the variable database_name and calls our database file from above
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
        connection_sign_up = sqlite3.connect(database_name)
        # connects to sqlite3 using a variable name of conn short for connection
        # finds the variable database_name and calls our database file from above
        cursor_sign_up = connection_sign_up.cursor()
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
            cursor_sign_up.execute(selectQuery)
            # executes the selectQuery command
            highestID = cursor_sign_up.fetchone()
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
                cursor_sign_up.execute(insertQuery)
                # executes the query to ensure the database will be updated when committed
        connection_sign_up.commit()
        # commits any changes the users inputs have made to the database
        connection_sign_up.close()
        # closes the database connection until reopened

    def view_key_register_screen():
        """function with a button directing the user to a new window informing them on what each colour means"""
        view_key_window_register_screen = Tk()
        # creates a new variable and sets it equal to a new Tkinter window
        view_key_window_register_screen.geometry("540x150")
        # defines the original dimensions for the window using the built-in geometry function
        view_key_window_register_screen.resizable(False, False)
        # tells the program to fetch for the variable and then connect to the resizable function
        # and sets both the x and y direction to false to force the window to stay at its original size
        view_key_window_register_screen.title("View Key for Register Screen")
        # gives the window which will be displayed in the border of the window to show the user which window is open
        view_key_orange_colour_label = Label(view_key_window_register_screen, text="Orange: ")
        # creates a new variable and sets it equal to a specific function which allows me to put labels on the window
        view_key_orange_colour_label.place(x=15, y=30)
        # tells the system where to place this label in reference with the x and y axis
        view_key_red_colour_label = Label(view_key_window_register_screen, text="Red: ")
        # variable for label telling the user Red:
        view_key_red_colour_label.place(x=35, y=60)
        # places this text inside the label along the x axis and down the y axis
        view_key_green_colour_label = Label(view_key_window_register_screen, text="Green: ")
        # creates the colour label telling the user Green
        view_key_green_colour_label.place(x=22, y=90)
        # places this label using the place function and defining the x and y direction
        view_key_orange_description_label = Label(view_key_window_register_screen, text="You have entered "
                                                                                        "information but"
                                                                                        " you can not move on yet")
        # creates a label to indicate that the user has entered information, but cannot move on yet
        view_key_orange_description_label.place(x=68, y=30)
        # positions the label at x=68, y=30
        view_key_red_description_label = Label(view_key_window_register_screen, text="You have not entered the correct "
                                                                                     "information therefore cannot "
                                                                                     "move on")
        # creates a label to indicate that the user has not entered the correct information, and cannot move on
        view_key_red_description_label.place(x=68, y=60)
        # positions the label at x=68, y=60
        view_key_green_description_label = Label(view_key_window_register_screen, text="You have entered correct "
                                                                                       "information and are now able to"
                                                                                       " move on")
        # creates a label to indicate that the user has entered correct information and can move on
        view_key_green_description_label.place(x=68, y=90)
        # positions the label at x=68, y=90
        view_key_orange_colour_label.config(foreground="orange")
        # sets the color of the orange color label to orange
        view_key_orange_description_label.config(foreground="orange")
        # sets the color of the orange description label to orange
        view_key_red_colour_label.config(foreground="red")
        # sets the color of the red color label to red
        view_key_red_description_label.config(foreground="red")
        # sets the color of the red description label to red
        view_key_green_colour_label.config(foreground="green")
        # sets the color of the green color label to green
        view_key_green_description_label.config(foreground="green")
        # sets the color of the green description label to green
    view_key_button = Button(register_screen, text="View Key", command=view_key_register_screen)
    # creates a button to view the key and calls the function "view_key_register_screen" when clicked
    view_key_button.place(x=100, y=32)
    # positions the button at x=100, y=32
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
        file_code = open("hello.txt", "r")
        # creates a variable and tells it to open a file and allows the system to read from the file
        emailPassword = file_code.read()
        # sets the emailPassword, which will be called below, equal to reading the file
        file_code.close()
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
        if emailSender and emailPassword:
            # as long the emailPassword, emailSender and the emailRecipient exists
            server.login(emailSender, emailPassword)
            # using the built-in function passes through the emailSender and the emailPassword logging the user in
            if emailRecipient:
                # where the user has inputted some sort form of an email address
                if "@" in emailRecipient:
                    # as long the user's inputted email address contains an @ sign
                    emoji_label_clause_2_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
                    # connects to our label created above and configures it using text
                    # and the emoji library to a green tick
                    name_register_split_with_sign, domain_register_split_with_sign = emailRecipient.split("@")
                    # using two variable names splits the email address the user has inputted before and after @ sign
                    name_register = open("names.txt", "r").read().splitlines()
                    # creates a new variable
                    # setting it equal to opening a file and tells the system to read from the file
                    # splits the lines of each of the names
                    domain_register = open("emaildomains.txt", "r").read().splitlines()
                    # splits the lines of each of the domains found inside the email_register_domain.txt file
                    if name_register_split_with_sign in name_register:
                        # this ensure they are trying to send the email to an existing email address
                        # with a correct name
                        emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
                        # as long as the user's email address contains one of the above account name
                        # then a tick will be shown
                    else:
                        # however if they do not have any name that exists in the list above
                        emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
                        # this changes the text from a tick to a cross where there is no existing name
                    if domain_register_split_with_sign in domain_register:
                        # checks their email has some form of domain in its email
                        emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
                        # this will adapt a tick next door to the clause to do with domain name
                    else:
                        # but if the user's entered email address does not have one of the above names
                        emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
                        # the previous mark, tick, will change to a cross
                    if name_register_split_with_sign in name_register \
                            and domain_register_split_with_sign in domain_register:
                        # as long as the user's inputted email has a domain and a name which where found inside the file
                        emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
                        # adapts the cross to ticks because rules had been fulfilled
                        emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
                        # adapts the cross to a tick for the third clause
                        server.sendmail(emailSender, emailRecipient, email.as_string())
                        # using the sendmail function it fetches the emailSender, emailRecipient
                        # and the email the user has entered
                        sent_label = Label(register_screen, text="Email sent!", width=20)
                        # creates a label, placing it inside the register_screen with text of email sent
                        # fixes the width of this label
                        sent_label.place(x=320, y=121)
                        # places this label just underneath the verify button
                        sent_label.config(foreground="green")
                        # sets the colour of the label to green to show the user has successfully sent the email
                        server.quit()
                        # now the email has been sent, we can close the server
                    else:
                        # although if the user has not entered an email
                        not_sent_label = Label(register_screen, text="Email has failed to send 😭", width=20)
                        # it will make a new variable and set it equal to a label with text, Email has failed to send
                        not_sent_label.place(x=310, y=124)
                        # places label just above the verify button
                        not_sent_label.config(foreground="red")
                        # colours the label orange warning the user they haven't followed the rules
                        emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
                        emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
                else:
                    # where there wasn't an @ sign inside the user's inputted email
                    emoji_label_clause_2_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
                    # changes the @ sign label from blank or tick to a cross
                    with open("names.txt", "r") as file_register_domains:
                        # opens new file for names
                        name_register = file_register_domains.read().splitlines()
                        # opens file with file name and speech marks allows us to read from file
                        # and sets it equal to the variable name_register
                    with open("emaildomains.txt", "r") as file_register_names:
                        # opens file with file name and speech marks allows us to read from file
                        # and sets it equal to a variable
                        domain_register = file_register_names.read().splitlines()
                        # creates a new variable and sets equal to the file just opened
                        # tells the system to read from the file and split
                    if emailRecipient in name_register:
                        # checks their email has some form of name in its email
                        emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
                        # this will adapt a tick next door to the clause to do with account name
                    else:
                        # but if the user's entered email address does not have one of the above names
                        emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
                        # the previous mark, tick, will change to a cross
                    if emailRecipient in domain_register:
                        # this ensure they are trying to send the email to an existing email address
                        # with a correct domain
                        emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
                        # as long as the user's email address contains one of the above domains
                        # then a tick will be shown
                    else:
                        # however if they do not have any domain that exists in the list above
                        emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
                        # this changes the text from a tick to a cross where there is no existing domain
            else:
                emoji_label_clause_2_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
                emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
                emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
                # although if the user has not entered an email
                not_sent_label = Label(register_screen, text="Email has failed to send 😭", width=20)
                # it will make a new variable and set it equal to a label with text, Email has failed to send
                not_sent_label.place(x=310, y=124)
                # places label just above the verify button
                not_sent_label.config(foreground="red")
                # colours the label orange warning the user they haven't followed the rules
        else:
            # although if the user has not entered an email
            system_failure_email_sending = Label(register_screen, text="System is down, try later", width=20)
            # it will make a new variable and set it equal to a label with text, Email has failed to send
            system_failure_email_sending.place(x=320, y=103)
            # places label just above the verify button
            system_failure_email_sending.config(foreground="orange")
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

    def show_password_register():
        """this defines a function which allows the users password to be shown where check box is ticked"""
        if password_entry.cget('show') == '*':
            # tells the system to not show stars where the check box is not selected
            password_entry.config(show='')
            # instead show the actual password the user is entering
        else:
            # but if the user has selected the show password box
            password_entry.config(show='*')
            # the system will show stars in place of their password
    show_password_check_box = Checkbutton(register_screen, text='Show Password', command=show_password_register)
    # creates the check button box putting text next to the box
    show_password_check_box.place(x=85, y=277)
    # places the button in the tkinter window
    check_clause_1_password = Label(register_screen, text="At least 8 characters")
    # password clause telling the user they have to enter 8 characters
    check_clause_1_password.place(x=150, y=300)
    # places this label in our tkinter window
    check_clause_2_password = Label(register_screen, text="At least 1 capital letter")
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
    connection_register.commit()
    # commits any changes the users inputs have made to the database
    connection_register.close()
    # closes the connection for the database


def login():
    """defines another function with the name of login
    this will allow the user to log in with credentials they used to register with"""


def user_does_not_want_to_proceed():
    """this defines our function with the name of yes
    this takes the user to the main screen """
    proceed.destroy()
    # closes the window since the user has decided to they would not like to proceed


def yes_button_in_first_window():
    """this defines a function with a name of yes which directs the user to the new window
    which will allow the user to login and/or register"""
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
    login_button_yes_window = Button(login_and_register_user_screen, text="Login", height="2", width="30",
                                     command=login)
    # creates a variable that creates a button and places it inside our new tkinter interface
    # which allows the user to login
    login_button_yes_window.place(x=100, y=125)
    # tells the system to place my login button along the x and y axes


frame = Frame(proceed, width=420, height=55)
# creates a frame, links it to our proceed Tkinter window and limits to a size with a width of 450 and height of 400
frame.place(x=7, y=1)
# allows the program to most efficiently place the image inside our frame using the function pack
img = ImageTk.PhotoImage(Image.open("top_image_proceed_window.png"))
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
img2 = ImageTk.PhotoImage(Image.open("bottom_image_proceed_window.png"))
# creates the next image to be used below the last one
label2 = Label(frame2, image=img2)
# creates a new variable for our next image
label2.place(x=35, y=20)
# tells the system how to place our image using the pack function
Button(text="Yes", height="2", width="30", command=yes_button_in_first_window).place(x=84, y=125)
# creates a new button in our original tkinter window requesting for the users response
Button(text="No", height="2", width="30", command=user_does_not_want_to_proceed).place(x=84, y=175)
# button saying no which will point the program to thew no function
proceed.resizable(False, False)
# fixes the size of the window
conn.commit()
# commits any changes the users inputs have made to the database
conn.close()
# closes the connection for the database
proceed.mainloop()
# this calls the variable proceed and displays our graphical user interface with all of its attributes defined above
