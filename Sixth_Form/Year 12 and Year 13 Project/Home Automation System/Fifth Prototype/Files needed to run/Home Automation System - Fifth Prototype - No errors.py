from tkinter import *
# tells the program to use the built-in library Tkinter and import each relevant module found within Tkinter
from PIL import ImageTk, Image
# finds the library PIL and imports two separate packages, ImageTk and Image allowing me to store images inside tkinter
import sqlite3
# sqlite3 is the library I will be using for databases allowing me to read, query and write to and from the database
import emoji
# emoji library allowing me to show emojis inside our program
import re
# allows me to ensure the user follows rules when entering a password
import random
# uses an algorithm to generate random numbers
import smtplib
# allows to send emails from a specific email using smtp, which stands for simple mail transfer protocol
from email.message import EmailMessage
# allows me to place a specific message inside our email; I will be combining this with the above library to send emails
import requests
# allows me to gather information from the internet using http requests
from bs4 import BeautifulSoup
# used to execute the request to the internet to find the result
import spotipy
# allows me to connect with spotify and lets me affect music in many ways
from spotipy.oauth2 import SpotifyOAuth
# signs a specific user in using a spotify authentication library to check the details given
import speech_recognition as sr
# lets me use the speech recognition library to allow me to be able to recognise the user's commands
# then execute the appropriate commands
import tinytuya
# allows me to connect to lights and adapt the status of the lights
from tkinter import colorchooser
# calls the tkinter library and pulls colorchooser which shows a range of ways to choose a colour
# the user is satisfied with to change their light(s) to

scope = "user-modify-playback-state, user-read-playback-state"
# creates a variable, 'scope', and passes in two separate parameters one for playing and pausing music,
# and one for telling the user what music is playing
clientIDFile = open("logins.txt", "r")
# creates a variable, 'clientIDFile' tells the program to open the file with the file name
# and be able to read from the file
clientID = clientIDFile.read()
# creates another new variable this time to read the file above just opened
clientIDFile.close()
# connects back to the variable with the file and closes the file
# to ensure it isn't read from throughout the rest of the problem
clientSecretFile = open("secret.txt", "r")
# makes a variable to be used for the secret code generated from spotify developers webpage
clientSecret = clientSecretFile.read()
# connects back to the variable and reads from the file
clientSecretFile.close()
# closes the file to ensure it isn't misused through the rest of the program
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id=clientID,
                                               client_secret=clientSecret,
                                               redirect_uri="http://localhost:8350/callback/"))
# creates another new variable, the name is short to keep it efficient to call it stands for spotify
# it first links to the spotipy library
# and then connects to the brand of Spotify
# and using the spotify authentication library
# setting it equal to the library defining each of the necessary parameters to be passed through
# first parameter being the scope of how spotify is allowed to access the account I am giving it
# next parameter tells the program what the client_id is calling the information read from the file opened above
# tells the program where the client secret can be found
# this link is also added to the spotify developers page when creating the api
# it is redirect website where in the case the information provided is invalid the user will be taken to an error page
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' 
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# creates another variable defining how the program must search the web referencing the architecture
# and version of each system available
# using a list calls the User-Agent which tells is a variable allowing the program
# to perform searches on the mentioned browsers in the background
scene_code_dictionary = {"Reading": '010e0d0000000000000003e801f4',
                         "Night": '000e0d0000000000000000c80000',
                         "Working": '020e0d0000000000000003e803e8',
                         "Leisure": '030e0d0000000000000001f401f4',
                         "Soft": '04464602007803e803e800000000464602007803e8000a00000000',
                         "Colourful": '05464601000003e803e800000000464601007803e803e80000000046460100f003e803e800000000'
                                      '464601003d03e803e80000000046460100ae03e803e800000000464601011303e803e800000000',
                         "Dazzling": '06464601000003e803e800000000464601007803e803e80000000046460100f003e803e800000000',
                         "Gorgeous": '07464602000003e803e800000000464602007803e803e80000000046460200f003e803e8000000004'
                                     '64602003d03e803e80000000046460200ae03e803e800000000464602011303e803e800000000'}
# creates a variable and sets it equal to a list passing through variables
# these variables links to specific scenes
# each of these codes have been found by running a python script to determine which scene the light was on at that point
roomDict = {}
# calls in the list which will be for the users rooms they have created to ensure when it is called it has been created
loggedInUserID = None
# this tells the system that user has not signed in setting its boolean operator
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
# finds the variable database_name and sets it equal to the database file from above
c = conn.cursor()
# creates a cursor allowing us to execute sql commands
c.execute("""CREATE TABLE IF NOT EXISTS users ( userID int PRIMARY KEY not null, email_address text not null, 
password text not null, accessLevel text, nickname text,  date_of_birth DATE)""")
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
c.execute("""CREATE TABLE IF NOT EXISTS UserRooms  (userID int not null, roomName text not null, 
studyLight1 BOOLEAN not null, studyLight2 BOOLEAN not null, transformer BOOLEAN not null, 
PRIMARY KEY (userID,roomName))""")
# calls the cursor connection from above
# makes a table unless table is already found, with a name of 'UserRooms' creates the field userID with an integer value
# another field, roomName with boolean operator for text
# makes fields for each of the lights so to allow a user to save which lights they wanted saved to each room created
# by giving each of the operators the default data type
# allows each field to have a value of 0 if not selected and value of 1 to be selected
# also links to the other table created above by using a primary key,
# this allows the lights to be selected to be saved to each specific user
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
        no_email_entry = Label(register_screen, text="please enter email", padx=67)
        # tells the user to enter an email
        no_email_entry.place(x=118, y=170)
        # places the label using the place function, ensure it goes just below email box
        no_email_entry.config(foreground="red")
        # configures this text to the colour red to show the user there is an issue
        verified = False
        # calls the 'verified' variable and sets it to false to ensure it doesn't let them sign up
    else:
        # however if an email had been entered
        email_has_been_entered = Label(register_screen, text="you entered an email", padx=64)
        # the program creates a new variable
        # using the label function placing text telling the user they have entered an email
        email_has_been_entered.place(x=118, y=170)
        # tells the system how to place the variable made above
        email_has_been_entered.config(foreground="orange")
        # configures the text message to pastel yellow telling the user they have followed this rule
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
        # where the user has entered 1 or more capital letters
        emoji_label_clause_2_password_check_verification.config(text=f'{emoji.emojize(":check_mark_button:")}')
        # changes the emoji to a tick to show the user they have followed this rule
    if not re.search(r'[1234567890]{1,}', password):
        # if user doesn't have 1 or more number in their password
        emoji_label_clause_4_password_check_verification.config(text=f'{emoji.emojize(":cross_mark:")}')
        # the system will find where we placed this variable from above and configure it to a cross
        verified = False
        # this sets the verified variable to false to ensure the user's details won't be saved unless follow rules
    else:
        # if they have entered 1 or more numbers
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
        email_already_exists_label = Label(register_screen, text="this email is already linked to an account")
        # tkinter will create a new label telling the user they have already signed up with this account
        email_already_exists_label.place(x=118, y=170)
        # tells the system where to put this label, this will go directly below all the email rules
        email_already_exists_label.config(foreground="orange")
        # sets the colour of the text for this label to orange
        # telling the user their is a minor issue with their details
        verified = False
        # calls the verified variable and sets it to false stopping the user from registering incorrect details
    if actual_code != user_code:
        # fetches the code sent via email and matches with the code entered by the user
        code_label_failure = Label(register_screen, text="code incorrect, email not verified")
        # tells the user they have mistyped their code
        code_label_failure.place(x=145, y=227)
        # places this label just below the code entry box
        code_label_failure.config(foreground="red")
        # tells the user this a major issue they need to fix
        verified = False
        # the verified status of the variable is set to false,
        # preventing the user from registering incorrect information
    else:
        # if the user has copied the code correctly
        code_label_success = Label(register_screen, text="     code correct, email verified    ")
        # system tells user code is correct
        code_label_success.place(x=145, y=227)
        # system places label at same place as code incorrect to ensure only one message appears at a time
        code_label_success.config(foreground="green")
        # configures the label to green showing the user the code is correct
    if verified:
        successful_sign_up = Label(register_screen, text="you have been successfully signed up, you may now log in")
        # message telling user they are free to go and log in to the system
        successful_sign_up.place(x=95, y=500)
        # places the successful message on the screen using the place function
        successful_sign_up.config(foreground="green")
        # by colouring the text green informs the user they have followed all the necessary rules
        email_has_been_entered_verified = Label(register_screen, text="you entered an email", padx=64)
        # message telling user they are free to go and log in to the system
        email_has_been_entered_verified.place(x=118, y=170)
        # places the successful message on the screen using the place function
        email_has_been_entered_verified.config(foreground="green")
        # by colouring the text green informs the user they have followed all the necessary rules
    else:
        not_successful_sign_up = Label(register_screen, text="some details have errors, please try again", padx=55)
        # message telling user they need to check their details before trying to log in
        not_successful_sign_up.place(x=95, y=500)
        # places the not successful message on the screen using the place function
        not_successful_sign_up.config(foreground="red")
        # by colouring the text red informs the user they have not followed all the necessary rules
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
        we are then able to call any of these parameters throughout our program"""
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
                no_email_entry = Label(register_screen, text="please enter email", padx=67)
                # creates a variable
                # sets it equal to Tkinter's label function with text informing the user they need to enter an email
                no_email_entry.place(x=118, y=160)
                # tells the system where to place this new label function, just below the email clauses
                no_email_entry.config(foreground="red")
                # configures the text to red telling the user they need to fix this before moving on
            else:
                # however if an email had been entered
                email_has_been_entered = Label(register_screen, text="you entered an email", padx=64)
                # the program creates a new variable
                # using the label function placing text telling the user they have entered an email
                email_has_been_entered.place(x=118, y=170)
                # tells the system how to place the variable made above
                email_has_been_entered.config(foreground="orange")
                # configures the text message to green telling the user they have followed this rule
                email_has_been_entered_verified = Label(register_screen, text="you entered an email", padx=64)
                # message telling user they are free to go and log in to the system
                email_has_been_entered_verified.place(x=118, y=170)
                # places the successful message on the screen using the place function
                email_has_been_entered_verified.config(foreground="green")
                # by colouring the text green informs the user they have followed all the necessary rules
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
                    # splits the lines of each of the domains found inside the emaildomains.txt file
                    not_sent_label = Label(register_screen, text="Email has failed to send 😭", width=20)
                    # it will make a new variable and set it equal to a label with text, Email has failed to send
                    not_sent_label.place(x=310, y=124)
                    # places label just above the verify button
                    not_sent_label.config(foreground="red")
                    # colours the label orange warning the user they haven't followed the rules
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

                    not_sent_label = Label(register_screen, text="Email has failed to send 😭", width=20)
                    # it will make a new variable and set it equal to a label with text, Email has failed to send
                    not_sent_label.place(x=310, y=124)
                    # places label just above the verify button
                    not_sent_label.config(foreground="red")
                    # colours the label orange warning the user they haven't followed the rules
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
    check_clause_4_password = Label(register_screen, text="At least 1 number")
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
    connection_login = sqlite3.connect(database_name)
    # creates a database with a name of 'User Login Page Database' or connects to a database with this name
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
        if email_login:
            # where the user has inputted some sort form of an email address
            if "@" in email_login:
                # as long the user's inputted email address contains an @ sign
                emoji_label_clause_2_email_address_login.config(text=f'{emoji.emojize(":check_mark_button:")}')
                # connects to our label created above and configures it using text
                # and the emoji library to a green tick
                name_register_split_with_sign, domain_register_split_with_sign = email_login.split("@")
                # using two variable names splits the email address the user has inputted before and after @ sign
                name_register = open("names.txt", "r").read().splitlines()
                # creates a new variable
                # setting it equal to opening a file and tells the system to read from the file
                # splits the lines of each of the names
                domain_register = open("emaildomains.txt", "r").read().splitlines()
                # splits the lines of each of the domains found inside the emaildomains.txt file
                if name_register_split_with_sign in name_register:
                    # this ensure they are trying to send the email to an existing email address
                    # with a correct name
                    emoji_label_clause_1_email_address_login.config(text=f'{emoji.emojize(":check_mark_button:")}')
                    # as long as the user's email address contains one of the above account name
                    # then a tick will be shown
                else:
                    # however if they do not have any name that exists in the list above
                    emoji_label_clause_1_email_address_login.config(text=f'{emoji.emojize(":cross_mark:")}')
                    # this changes the text from a tick to a cross where there is no existing name
                if domain_register_split_with_sign in domain_register:
                    # checks their email has some form of domain in its email
                    emoji_label_clause_3_email_address_login.config(text=f'{emoji.emojize(":check_mark_button:")}')
                    # this will adapt a tick next door to the clause to do with domain name
                else:
                    # but if the user's entered email address does not have one of the above names
                    emoji_label_clause_3_email_address_login.config(text=f'{emoji.emojize(":cross_mark:")}')
                    # the previous mark, tick, will change to a cross
                if name_register_split_with_sign in name_register \
                        and domain_register_split_with_sign in domain_register:
                    # as long as the user's inputted email has a domain and a name which where found inside the file
                    emoji_label_clause_1_email_address_login.config(text=f'{emoji.emojize(":check_mark_button:")}')
                    # adapts the cross to ticks because rules had been fulfilled
                    emoji_label_clause_3_email_address_login.config(text=f'{emoji.emojize(":check_mark_button:")}')
                    # adapts the cross to a tick for the third clause
                else:
                    # although if the user has not entered an email
                    emoji_label_clause_3_email_address_login.config(text=f'{emoji.emojize(":cross_mark:")}')
                    emoji_label_clause_1_email_address_login.config(text=f'{emoji.emojize(":cross_mark:")}')
            else:
                # where there wasn't an @ sign inside the user's inputted email
                emoji_label_clause_2_email_address_login.config(text=f'{emoji.emojize(":cross_mark:")}')
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
                if email_login in name_register:
                    # checks their email has some form of name in its email
                    emoji_label_clause_1_email_address_login.config(text=f'{emoji.emojize(":check_mark_button:")}')
                    # this will adapt a tick next door to the clause to do with account name
                else:
                    # but if the user's entered email address does not have one of the above names
                    emoji_label_clause_1_email_address_login.config(text=f'{emoji.emojize(":cross_mark:")}')
                    # the previous mark, tick, will change to a cross
                if email_login in domain_register:
                    # this ensure they are trying to send the email to an existing email address
                    # with a correct domain
                    emoji_label_clause_3_email_address_login.config(text=f'{emoji.emojize(":check_mark_button:")}')
                    # as long as the user's email address contains one of the above domains
                    # then a tick will be shown
                else:
                    # however if they do not have any domain that exists in the list above
                    emoji_label_clause_3_email_address_login.config(text=f'{emoji.emojize(":cross_mark:")}')
                    # this changes the text from a tick to a cross where there is no existing domain
        else:
            # where no email has been entered
            emoji_label_clause_2_email_address_login.config(text=f'{emoji.emojize(":cross_mark:")}')
            # 2nd clause cross adapted to red
            emoji_label_clause_3_email_address_login.config(text=f'{emoji.emojize(":cross_mark:")}')
            # using emoji library adapts 3 clause to red
            emoji_label_clause_1_email_address_login.config(text=f'{emoji.emojize(":cross_mark:")}')
            # connecting to a label made below changes the label to a cross mark

    def view_key_login_screen():
        """displays a window with color-coded labels and descriptions for colour meanings for the login window """
        view_key_window_login_screen = Tk()
        # attaches a new tkinter window to the new variable
        view_key_window_login_screen.geometry("540x180")
        # using the geometry function defines the starting size
        view_key_window_login_screen.resizable(False, False)
        # the resizable function is used to set both the across and down directions to false
        # preventing the window from being resized
        view_key_window_login_screen.title("View Key for Login Screen")
        # using the title function gives the tkinter window a title
        view_key_orange_colour_label = Label(view_key_window_login_screen, text="Orange: ")
        # using the label function creates a label with text for the orange label
        view_key_orange_colour_label.place(x=15, y=30)
        # using the place function positions the label
        view_key_red_colour_label = Label(view_key_window_login_screen, text="Red: ")
        # using the label function creates a label with text for the red label
        view_key_red_colour_label.place(x=35, y=60)
        # positions the label using the the place function and calling the x and y parameters
        view_key_green_colour_label = Label(view_key_window_login_screen, text="Green: ")
        # creates another label, this time for the green label
        view_key_green_colour_label.place(x=22, y=90)
        # positions the label below the red label and slightly before the red label to ensure it is in line with the end
        view_key_blue_colour_label = Label(view_key_window_login_screen, text="Blue: ")
        # creates a new label for the blue label and places it inside the 'view_key_window_login_screen' window
        view_key_blue_colour_label.place(x=32, y=120)
        # positions the label inside the window using the place function
        view_key_orange_description_label = Label(view_key_window_login_screen, text="You have left optional "
                                                                                     "information blank, you are able "
                                                                                     "to move on")
        # creates a new label for the orange description using the label function
        view_key_orange_description_label.place(x=68, y=30)
        # positions the orange description label inline with the orange label
        view_key_blue_description_label = Label(view_key_window_login_screen, text="You have entered information "
                                                                                   "into an optional field")
        # creates a new label for the blue description and places it inside the 'view_key_window_login_screen'
        view_key_blue_description_label.place(x=68, y=120)
        # positions the blue description label using the x and y parameters
        view_key_red_description_label = Label(view_key_window_login_screen, text="You have not entered the correct "
                                                                                  "information therefore cannot "
                                                                                  "move on")
        # makes a new label which is to be placed inside the 'view_key_window_login_screen' window
        view_key_red_description_label.place(x=68, y=60)
        # places the new label across the x axis and the y axis
        view_key_green_description_label = Label(view_key_window_login_screen, text="You have entered correct "
                                                                                    "information and are now able to"
                                                                                    " move on")
        # creates a description using the text parameter and places it inside the same window
        view_key_green_description_label.place(x=68, y=90)
        # places the label using the place function 68 along and 90 down
        view_key_orange_colour_label.config(foreground="orange")
        # using the config function sets the colour of the text of the orange label
        view_key_orange_description_label.config(foreground="orange")
        # changes the default colour of black text (foreground) and white background to orange text
        view_key_red_colour_label.config(foreground="red")
        # using the config function changes the colour of the red colour label to red
        view_key_red_description_label.config(foreground="red")
        # changes the colour of description for the red to be red
        view_key_green_colour_label.config(foreground="green")
        # makes the green label have a green colour
        view_key_green_description_label.config(foreground="green")
        # gives the description a green colour
        view_key_blue_description_label.config(foreground="blue")
        # gives the blue label a blue colour to match its text
        view_key_blue_colour_label.config(foreground="blue")
        # matching the name label gives the description the same colour
    view_key_button = Button(login_screen, text="View Key", command=view_key_login_screen)
    # creates a new button passing in parameters and pointing the program to the function above
    view_key_button.place(x=105, y=20)
    # places the button inside the window above the email address entry box
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

    def show_password_login():
        """this defines a function which allows the users password to be shown where check box is ticked"""
        if password_entry_login.cget('show') == '*':
            # this says that if check button ticked password will be shown and stars will be hidden
            password_entry_login.config(show='')
            # by configuring the stars to instead show whatever is being entered
        else:
            # if the checkbutton is not ticked then password will stay starred
            password_entry_login.config(show='*')
            # by configuring the password_entry with stars

    show_password_check_box_login = Checkbutton(login_screen, text='Show Password', command=show_password_login)
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
        if re.search(r'[1234567890]{1,}', password_numbers_login):
            # calls the re library and using the built in search function, searches through the user's entered password
            emoji_label_clause_4_password_login.config(text=f'{emoji.emojize(":check_mark_button:")}')
            # either changes the cross to a tick or shows the user a tick
        else:
            # where the user's password doesn't follow this rule
            emoji_label_clause_4_password_login.config(text=f'{emoji.emojize(":cross_mark:")}')
            # adapts the emoji to show a cross emoji
        password_special_chars_login = password_entry_login.get()
        # creates another variable and sets it equal to the users password entered
        if re.search(r'[∑´®†¥¨~`Ω≈ç√∫µ≤≥«æ…¬˚∆'
                     r'˙©ƒ∂ßåπø“‘≠–ºª•¶§∞¢#€¡±œ!@$%^&*(),.;?":{+}|<-=>/]{1,}', password_special_chars_login):
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
    check_clause_2_password_login = Label(login_screen, text="At least 1 capital letters")
    # creates another variable where it will show a label on the login screen with text
    check_clause_2_password_login.place(x=150, y=270)
    # this will place the password clause 20 below the above clause
    check_clause_3_password_login = Label(login_screen, text="At least 1 special character")
    # creates a new variable and gives it a label that will have text saying at least 1 special character
    # hopefully informing the user the information they have to input into their password
    check_clause_3_password_login.place(x=150, y=290)
    # informs the system where to place the third password clause
    check_clause_4_password_login = Label(login_screen, text="At least 1 number")
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
    login_button = Button(login_screen,
                          text='Log in',
                          command=lambda: log_in(email_address_entry_login_screen.get(),
                                                 password_entry_login.get(), nickname_entry.get(),
                                                 date_of_birth_entry.get()))
    # makes a button with text of log in and command of log_in,
    # when button pressed the system will run through the log_in function passing through all the named parameters
    login_button.place(x=350, y=550)
    # tells the system where to put the login button, near the bottom of the window
    connection_login.commit()
    # commits any changes the users inputs have made to the database
    connection_login.close()
    # closes the connection for the database

    def log_in(email_address_log_in, password_db_log_in, nickname, date_of_birth):
        """this function informs the user of the fields the user has inputted
        and whether or not they match the saved information by connecting to a and reading from the database"""
        connection_log_in = sqlite3.connect(database_name)
        # creates a database with a name of 'User Login Page Database' or connects to a database with this name
        cursor_log_in = connection_log_in.cursor()
        # creates a cursor
        getPasswordQuery = "SELECT password FROM users WHERE email_address == '%s'" % email_address_log_in
        # creates a new variable and sets it equal to a sql command checking if the users email address entered
        # can be found inside the database
        cursor_log_in.execute(getPasswordQuery)
        # execute the above command allow us to call and use it throughout
        savedPassword = cursor_log_in.fetchone()
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
                password_correct = Label(login_screen, text="           password is correct")
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
                    cursor_log_in.execute(updateNicknameQuery)
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
                    cursor_log_in.execute(updateDOBQuery)
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
                cursor_log_in.execute(getAccessLevelQuery)
                # executes the command above
                access_Level = cursor_log_in.fetchone()
                # forces program to fetch only one piece of data at a time
                access_Level = access_Level[0]
                # sets the access level search from 0 so this is where it starts
                getUserIDQuery = "SELECT userID FROM users where email_address = '%s'" % email_address_log_in
                # creates new variable and using a select statement collects the user id
                # where the email address is equal to the email address entered
                cursor_log_in.execute(getUserIDQuery)
                # executes the above sql statement
                id = cursor_log_in.fetchone()
                # creates a variable for one piece of data the system will collect
                if id:
                    # where the variable does exist
                    id = int(id[0])
                    # give the new id a new increment from the previous id
                    global loggedInUserID
                    # allows us to call the logged in account as none from the top
                    loggedInUserID = id
                    # then sets the new logged in account to the new increment
                if access_Level == "admin":
                    # the following code is where the admin account is trying update users' information
                    # where the access level has been fetched and found to be admin
                    adminPage = Tk()
                    # creates a new variable and sets it equal to a new tkinter window
                    adminPage.title("Admin Page")
                    # gives this new tkinter page a title of admin page
                    adminPage.geometry("500x400")
                    # calling the variable created for the tkinter page just created gives it a starting size
                    adminPage.resizable(False, False)
                    # stops the user from resizing the window
                    admin_email_previous = Label(adminPage, text="enter email with information to be changed below")
                    # creates a new variable for the admin user to input
                    # connects it to the adminPage and gives it some text
                    admin_email_previous.place(x=100, y=25)
                    # tells program where to place specific label
                    admin_email_previous_entry = Entry(adminPage)
                    # creates a new variable connecting to a tkinter function to make an entry box inside adminPage
                    admin_email_previous_entry.place(x=165, y=45)
                    # tells the system where to put this entry box
                    admin_email_change = Label(adminPage, text="enter new email")
                    # creates a new label with text telling the admin which details they need to put where
                    admin_email_change.place(x=62, y=115)
                    # using the built in place function tells the system where to put the label along the axis
                    admin_email_change_entry = Entry(adminPage)
                    # new entry box for the user to type information into
                    admin_email_change_entry.place(x=175, y=115)
                    # tells program where in the adminPage window to place this entry box
                    admin_password_change = Label(adminPage, text="enter new password")
                    # creates the label for the password box, telling the user to enter new password
                    admin_password_change.place(x=35, y=145)
                    # using the built in place function from tkinter puts our label along the axes
                    admin_password_change_entry = Entry(adminPage)
                    # creates a new variable, sets it equal to entry window, a function allowing input into a box
                    admin_password_change_entry.place(x=175, y=145)
                    # tells the system how and where to place the entry box in the adminPage
                    admin_nickname_change = Label(adminPage, text="enter new nickname")
                    # tells the admin user which information to put where by creating a new label
                    admin_nickname_change.place(x=35, y=175)
                    # places this label in line with the nickname entry box below
                    admin_nickname_change_entry = Entry(adminPage)
                    # creates the entry box for which the admin can put the new nickname
                    admin_nickname_change_entry.place(x=175, y=175)
                    # places the entry box slightly after the label
                    # so it doesn't overlap but is also inline with the rest
                    admin_Date_of_birth_change = Label(adminPage, text="enter new date of birth")
                    # creates a new label and places it in the adminPage with text
                    admin_Date_of_birth_change.place(x=20, y=205)
                    # places this label to be below the nickname label
                    # and at the beginning of the window because of the length of text
                    admin_Date_of_birth_change_entry = Entry(adminPage)
                    # creates the entry box for the admin to input the new date of birth
                    admin_Date_of_birth_change_entry.place(x=175, y=205)
                    # places the entry box next to the label so the admin knows which information to put where
                    change_button = Button(adminPage, text='Change information', command=lambda: change_information(
                        admin_email_previous_entry.get(), admin_email_change_entry.get(),
                        admin_password_change_entry.get(), admin_nickname_change_entry.get(),
                        admin_Date_of_birth_change_entry.get(), adminPage))
                    # creates a variable setting it equal to a button for the admin to click
                    # when button is clicked it will check if email entered at top exists
                    # and then execute the defined sql statements
                    # it also passes through the above variables as get
                    # able to receive the details the admin has input
                    change_button.place(x=330, y=300)
                    # places the button at the bottom and on the right so it is the last command the user does
                    # however can be done in any order
                elif access_Level == "userAccount":
                    # where if a non admin account has logged in
                    study_light_1 = tinytuya.BulbDevice(dev_id='bfaa556f9ac6334e9ajnec',
                                                        address='192.168.1.159',
                                                        local_key='622ab2625722d80a',
                                                        version=3.3)
                    study_light_2 = tinytuya.BulbDevice(dev_id='bf57d83388422ac905nl4q',
                                                        address='192.168.1.147',
                                                        local_key='ed75d11af9d56a62',
                                                        version=3.3)
                    Transformer = tinytuya.BulbDevice(dev_id='bf95a987949dd79c645dw7',
                                                      address='192.168.1.155',
                                                      local_key='021d37949f73862e',
                                                      version=3.3)
                    roomDict = {}
                    getRoomsQuery = """SELECT roomName, studyLight1,studyLight2,transformer FROM UserRooms WHERE userID = %d""" % id
                    cursor_log_in.execute(getRoomsQuery)
                    roomList = cursor_log_in.fetchall()
                    if roomList:
                        roomList = roomList[0:]

                        for room in roomList:
                            roomName = room[0]
                            bulbBooleans = room[1:]
                            bulbList = []
                            if bulbBooleans[0] == 1:
                                bulbList.append(study_light_1)
                            if bulbBooleans[1] == 1:
                                bulbList.append(study_light_2)
                            if bulbBooleans[3] == 1:
                                bulbList.append(Transformer)
                            roomDict[roomName] = [bulbList]

                    home_automation_system_window = Tk()
                    # a new tkinter page will be created and set equal to a new variable
                    home_automation_system_window.title("Home Automation System HomePage")
                    # gives this new tkinter window a title to inform the user what stage of my system they are at
                    home_automation_system_window.geometry("500x650")
                    # gives the user a starting size using the geometry function built into tkinter
                    home_automation_system_window.resizable(False, False)
                    # creates limits for the window at the original size
                    roomButtons = []

                    def room_more_controls(room_Name):
                        room_more_controls_window = Tk()
                        room_more_controls_window.title("Home Automation System Rooms More Controls")
                        room_more_controls_window.geometry("500x375")
                        room_more_controls_window.resizable(False, False)
                        more_controls_button_on = Button(room_more_controls_window,
                                                         text="On",
                                                         command=lambda: OnButtonRoom(room_Name))
                        more_controls_button_on.place(x=195, y=70)
                        more_controls_button_off = Button(room_more_controls_window,
                                                          text="Off",
                                                          command=lambda: OffButtonRoom(room_Name))
                        more_controls_button_off.place(x=255, y=70)
                        more_controls_colour_picker = Button(room_more_controls_window,
                                                             text="Select colour",
                                                             command=lambda: choose_colour_room(room_Name))
                        more_controls_colour_picker.place(x=195, y=140)
                        more_controls_name_of_bulb = Label(room_more_controls_window, text=room_Name)
                        more_controls_name_of_bulb.place(x=195, y=40)
                        slider_more_controls = Scale(
                            room_more_controls_window,
                            from_=10,
                            to=1000,
                            orient='horizontal',
                            command=lambda value: room_slider_control(room_Name, value))
                        slider_more_controls.place(x=200, y=97)
                        scenes_more_controls = Label(room_more_controls_window, text="Scenes")
                        scenes_more_controls.place(x=225, y=195)

                        def set_Scene(sceneBulb, scene):
                            sceneBulb.set_mode("scene")
                            scene_code = scene_code_dictionary[scene]
                            sceneBulb.set_value(25, scene_code)

                        scenes_reading = Button(room_more_controls_window,
                                                text="Reading", command=lambda: setRoomScenes(room_Name, "Reading"))
                        scenes_reading.place(x=50, y=225)
                        scenes_night = Button(room_more_controls_window,
                                              text="Night", command=lambda: setRoomScenes(room_Name, "Night"))
                        scenes_night.place(x=220, y=225)
                        scenes_leisure = Button(room_more_controls_window,
                                                text="Leisure", command=lambda: setRoomScenes(room_Name, "Leisure"))
                        scenes_leisure.place(x=380, y=225)
                        scenes_working = Button(room_more_controls_window,
                                                text="Working", command=lambda: setRoomScenes(room_Name, "Working"))
                        scenes_working.place(x=50, y=275)
                        scenes_soft = Button(room_more_controls_window,
                                             text="Soft", command=lambda: setRoomScenes(room_Name, "Soft"))
                        scenes_soft.place(x=220, y=275)
                        scenes_colourful = Button(room_more_controls_window,
                                                  text="Colourful",
                                                  command=lambda: setRoomScenes(room_Name, "Colourful"))
                        scenes_colourful.place(x=380, y=275)
                        scenes_dazzling = Button(room_more_controls_window,
                                                 text="Dazzling", command=lambda: setRoomScenes(room_Name, "Dazzling"))
                        scenes_dazzling.place(x=120, y=325)
                        scenes_gorgeous = Button(room_more_controls_window,
                                                 text="Gorgeous", command=lambda: setRoomScenes(room_Name, "Gorgeous"))
                        scenes_gorgeous.place(x=310, y=325)

                        def setRoomScenes(roomName2, scene):
                            bulbs = roomDict[roomName2]
                            for bulb in bulbs:
                                set_Scene(bulb, scene)

                    def OnButtonRoom(room_Name):
                        bulbs = roomDict[room_Name]
                        for bulb in bulbs:
                            bulb.turn_on()

                    def OffButtonRoom(room_Name):
                        bulbs = roomDict[room_Name]
                        for bulb in bulbs:
                            bulb.turn_off()

                    def room_slider_control(room_Name, value):
                        bulbs = roomDict[room_Name]
                        for bulb in bulbs:
                            bulb.set_brightness(int(value))

                    def choose_colour_room(room_Name):
                        try:
                            color_code = colorchooser.askcolor(title="Choose Colour")
                            (r, g, b) = color_code[0]
                            bulbs = roomDict[room_Name]
                            for bulb in bulbs:
                                bulb.set_colour(r, g, b)
                        except:
                            return

                    def loadRoomPage(room_Name):
                        load_room_page = Tk()
                        load_room_page.title("HAS - Rooms")
                        load_room_page.geometry("200x200")
                        load_room_page.resizable(False, False)
                        roomName_button = Button(load_room_page, text=room_Name,
                                                 command=lambda: room_more_controls(room_Name))
                        roomName_button.place(x=40, y=32)
                        on_button_rooms = Button(load_room_page, text="On", command=lambda: OnButtonRoom(room_Name))
                        on_button_rooms.place(x=40, y=60)
                        off_button_rooms = Button(load_room_page, text="Off", command=lambda: OffButtonRoom(room_Name))
                        off_button_rooms.place(x=95, y=60)
                        slider_room_page = Scale(
                            load_room_page,
                            from_=10,
                            to=1000,
                            orient='horizontal',
                            command=lambda value: room_slider_control(room_Name, value))
                        slider_room_page.place(x=45, y=90)
                        room_colour_picker = Button(load_room_page,
                                                    text="Select colour",
                                                    command=lambda: choose_colour_room(room_Name))
                        room_colour_picker.place(x=40, y=130)

                    def deleteButtons():
                        roomButtons.clear()
                        for button in roomButtons:
                            button.destroy()

                    def refreshButtons():
                        deleteButtons()
                        x = 180
                        y = 100
                        rooms = roomDict.keys()
                        for room_refresh_buttons in rooms:
                            newButton = Button(home_automation_system_window,
                                               text=room_refresh_buttons,
                                               command=lambda room=room_refresh_buttons: loadRoomPage(room))
                            newButton.place(x=x, y=y)
                            roomButtons.append(newButton)
                            x = (x + 125) % 380
                            if x < 180:
                                x = 180
                                y = y + 25
                    refreshButtons()

                    def voice_assistant_button_clicked():
                        """voice assistant function that the system points to
                        when the voice assistant button is clicked on
                        it will report the user the weather, do maths calculations
                        and be able to control spotify's playback for my account details"""
                        try:
                            # try the following commands
                            def do_spotify_command():
                                """spotify voice assistant function to allow the user to request
                                the playback in multiple ways"""
                                r_spotify = sr.Recognizer()
                                # spotify specific variable used to recognize speech
                                with sr.Microphone() as source_spotify:
                                    # using the sr function it stores the microphones
                                    # reading inside the spotify variable
                                    r_spotify.adjust_for_ambient_noise(source_spotify, duration=0.2)
                                    # using the adjust for ambient noise function ensures
                                    # that only the user's voice is interpreted and then executed
                                    question_spotify_label = Label(home_automation_system_window,
                                                                   text="What would you like to do with spotify?")
                                    # creates a spotify label for command
                                    question_spotify_label.place(x=50, y=588)
                                    # places spotify command label on screen
                                    home_automation_system_window.update()
                                    # updates the home automation system window
                                    audio_spotify = r_spotify.listen(source_spotify)
                                    # new variable used to listen to what the user's request is
                                    speech_spotify = r_spotify.recognize_google(audio_spotify)
                                    # then the user's audio is converted and recognised by google
                                    if "pause" in speech_spotify:
                                        # where the voice assistant manged to recognise
                                        # the key word pause in the user's speech
                                        sp.pause_playback()
                                        # using the sp variable to log the user in and modify playback,
                                        # playback is paused
                                    elif "play" in speech_spotify:
                                        # where the system recognises the user says play
                                        sp.start_playback()
                                        # playback begins from where the user left off
                                    elif "change volume" in speech_spotify:
                                        # if the user is recognised to say change volume
                                        r_volume = sr.Recognizer()
                                        # variable used to recognise speech
                                        with sr.Microphone() as source_volume:
                                            # using the microphone to detect the users speech
                                            # and capturing inside the variable
                                            r_volume.adjust_for_ambient_noise(source_volume, duration=0.2)
                                            # ensuring only the user's commands are interpreted
                                            percentage_playback_question = Label(home_automation_system_window,
                                                                                 text="What would you like the new "
                                                                                      "percentage of playback to be?",
                                                                                 padx=70, pady=15)
                                            # percentage question label created
                                            percentage_playback_question.place(x=5, y=530)
                                            # percentage label placed
                                            home_automation_system_window.update()
                                            # home automation system window updated
                                            volume_change = r_volume.listen(source_volume)
                                            # then again using a variable to listen to the user's response
                                            speech_volume = r_volume.recognize_google(volume_change)
                                            # their response is converted using google recognize module
                                            sp.volume(int(speech_volume))
                                            # the volume to the value used
                                            percentage_playback_response = Label(home_automation_system_window,
                                                                                 text="Your volume has been changed to"
                                                                                      " " + speech_volume + "%, if this"
                                                                                                            " is the "
                                                                                                            "wrong "
                                                                                                            "volume "
                                                                                                            "please "
                                                                                                            "retry"
                                                                                 , pady=15)
                                            # label created for new volume
                                            percentage_playback_response.place(x=5, y=530)
                                            # new volume window placed
                                            home_automation_system_window.update()
                                            # window updated with labels
                                    elif "song" in speech_spotify:
                                        # if the system recognises the user says for example song
                                        r_song = sr.Recognizer()
                                        # variable used to recognise speech
                                        with sr.Microphone() as song_user:
                                            # using the microphone its findings are reported and stored in the song_user
                                            r_song.adjust_for_ambient_noise(song_user, duration=0.2)
                                            # to be sure that any important information is reported(speech)
                                            song_question_label = Label(home_automation_system_window,
                                                                        text="Which song would you like to play?",
                                                                        pady=20, padx=200)
                                            # song request label
                                            song_question_label.place(x=8, y=525)
                                            # song request label placed
                                            home_automation_system_window.update()
                                            # home automation window updated with labels
                                            song_audio = r_spotify.listen(song_user)
                                            # using the listen module and the microphone
                                            song_user = r_spotify.recognize_google(song_audio)
                                            # the users speech is converted and interpreted
                                            song_response_label_line_1 = Label(home_automation_system_window,
                                                                               text="You said: " + song_user + ", "
                                                                               + song_user +
                                                                               " is playing, if this wasn't the song "
                                                                               "you wanted")
                                            # song interpreted and being played label
                                            song_response_label_line_1.place(x=5, y=530)
                                            # label placed on window
                                            song_response_label_line_2 = Label(home_automation_system_window,
                                                                               text="to play, please retry", padx=200)
                                            # second half of label
                                            song_response_label_line_2.place(x=5, y=550)
                                            # placed on new line of label
                                            home_automation_system_window.update()
                                            # system will update labels to user
                                            results = sp.search(q=song_user, type='track')
                                            # then to find the song the user asked for a query is run
                                            # on the converted speech only searching for specific tracks
                                            track_uri = results['tracks']['items'][0]['uri']
                                            # then fetching the actual songs data
                                            # selects the track found along with the song name and its uri
                                            sp.start_playback(uris=[track_uri])
                                            # then the sp variable will start playback
                                            # of song just interpreted and found
                                    elif "shuffle" in speech_spotify:
                                        # if the user is detected to have said shuffle
                                        sp.shuffle(True)
                                        # the system will shuffle playback
                                    elif "skip" or "next" or "skip it" in speech_spotify:
                                        # if the user says skip, next or skip it
                                        sp.next_track()
                                        # the system will move onto the next song in the queue
                                    elif "previous" or "go back" in speech_spotify:
                                        # if the user is detected to want to go back a song,
                                        # for example by saying go back
                                        sp.previous_track()
                                        # then using the previous_track function along with the sp module the
                                        # system will go back to the previous song in the queue
                                    else:
                                        # where none of these commands are in users speech
                                        general_error_spotify_label_main = Label(home_automation_system_window,
                                                                                 text="I am not sure how to help you, "
                                                                                      "click on voice assistant again "
                                                                                      "to retry")
                                        # retry label created
                                        general_error_spotify_label_main.place(x=5, y=550)
                                        # using place function label is positioned in window
                                        home_automation_system_window.update()
                                        # the window is then updated with the label just created

                            def find_weather():
                                """the weather function where the voice assistant recognises the key word to be weather"""
                                url = "https://www.google.co.uk/search?q=weather"
                                # creates a variable and passes through a website to find the current weather
                                find_weather_result = requests.get(url, headers=headers)
                                # then using a new variable the get function within the requests library
                                # used to perform the request to one of the available browser from the header
                                # defined at the top of the file
                                soup = BeautifulSoup(find_weather_result.text, "html.parser")
                                # variable connected with the beautiful soup library of how the website must be searched
                                # using the text function and the html parser for how the result must be processed
                                temperature = soup.select("#wob_tm")[0].getText().strip()
                                # another variable using the variable for how to search the website is told
                                # which part of the website to find and store using the getText and the strip functions to
                                # only collecting the information required
                                weather_description = soup.select("#wob_dc")[0].getText().strip()
                                # then performing another search using the select function
                                # going from the first index selects more information from the website
                                # this time instead of the temperature the weathers conditions
                                return temperature, weather_description
                                # both the temperature and the weather conditions are then returned to the system to be used

                            def do_maths(maths_question):
                                """maths function to execute maths question received from user"""
                                maths_question = maths_question.replace(" ", "+")
                                # using the parameter passed through the function to then allow it to be executed
                                # using the replace function splitting the question with spaces where a new word is said
                                url = "https://www.google.co.uk/search?q=%s" % maths_question
                                # using a the web search for the calculator on google
                                # replacing the maths question inside the request box
                                do_maths_result = requests.get(url, headers=headers)
                                # variable created to get the result using the requests library
                                # defining the header from the variable created at the top
                                soup = BeautifulSoup(do_maths_result.text, "html.parser")
                                # another new variable using the bs4 module to perform the variable create
                                # above getting the request using the html parser
                                answer = soup.select("#cwos")
                                # then using the soup variable created above a new variable is created to select a
                                # specific part of that web search where the result of the maths problem is displayed
                                if answer:
                                    # where answer variable was successfully created
                                    answer = answer[0].getText().strip()
                                    # new answer variable is now the text displayed from the question
                                    return answer
                                    # the answer is then stored and return as a tuple
                                else:
                                    # however if there is not answer
                                    return None
                                    # return nothing to the user

                            r = sr.Recognizer()
                            # variable used to recognise speech
                            song = sp.current_playback()
                            # using a new variable the current where a song is being played
                            currVolume = 0
                            # a variable to start where the volume is coming from
                            if song:
                                # where the variable was created
                                currVolume = song["device"]["volume_percent"]
                                # using the variable find the device that's playing the music and volume percentage
                                sp.volume(int(10))
                                # increment it back to 10
                            try:
                                # try the following commands while capturing the error
                                with sr.Microphone() as source:
                                    # this line of code initializes a new microphone object using the sr library
                                    # which is used to capture audio input from a microphone
                                    # the with statement creates a temporary context in which the source object is active
                                    # allowing any code inside the with block to access and use it
                                    # once the with block is exited, the source object is automatically released
                                    # any resources it was using are freed up
                                    r.adjust_for_ambient_noise(source, duration=0.2)
                                    # uses the adjust_for_ambient_noise method of a Recognizer object
                                    # to adjust for any background noise from the audio input
                                    # the method takes in a source object, which is the audio source that was initialized
                                    # in the previous line, the duration parameter specifies the length of time (in seconds)
                                    # that the method should listen for background noise before making adjustments
                                    speak_now_label = Label(home_automation_system_window, text="Speak now",
                                                            pady=20, padx=135)
                                    # the ready label is created with text of speak now
                                    speak_now_label.place(x=5, y=570)
                                    # the speak now label is placed
                                    home_automation_system_window.update()
                                    # labels are updated to the window
                                    audio = r.listen(source)
                                    # using a variable and connection to the recognizer made above the listen function is
                                    # used while passing in the microphones input
                                    speech = r.recognize_google(audio)
                                    # variable used to convert the audio into understandable text
                                    # using googles recognize module
                                    if "Spotify" in speech:
                                        # where spotify is recognised in speech
                                        do_spotify_command()
                                        # the conditional statement will point to the spotify command
                                    elif "weather" in speech:
                                        # where the recognizer finds that the user had weather in their speech
                                        tempValue, description = find_weather()
                                        # two variables are linked to the find weather function for the temperature
                                        # and for the conditions respectively
                                        weather_label = Label(home_automation_system_window,
                                                              text=tempValue + " °C " + description, padx=120, pady=10)
                                        # reports the temperature along with the conditions back to the user in a label
                                        weather_label.place(x=0, y=580)
                                        # places the weather label
                                        home_automation_system_window.update()
                                        # updates the window with the weather label
                                    elif "calculator" in speech:
                                        # where the user's speech contained the key word calculator
                                        r.adjust_for_ambient_noise(source, duration=0.2)
                                        # voice assistant will listen to only user's speech
                                        question_calculator_label = Label(home_automation_system_window,
                                                                          text="Ask your question")
                                        # specific question for calculator label created
                                        question_calculator_label.place(x=120, y=590)
                                        # calculator label placed
                                        home_automation_system_window.update()
                                        # home automation system window updated with new label
                                        questionAudio = r.listen(source)
                                        # where the user has something in source variable is created
                                        # that is used when listening to the users speech
                                        question = r.recognize_google(questionAudio)
                                        # then a new variable is used to convert
                                        # the user's speech into executable commands
                                        result = do_maths(question)
                                        # then a variable is used to execute the function passing in the function
                                        if not result:
                                            # where result was not found
                                            general_error_voice_assistant_maths_label_line_1 = Label(
                                                home_automation_system_window,
                                                text="I am not sure how to help you, "
                                                     "click on voice assistant")
                                            # general error label created where speech is not recognised (1st half)
                                            general_error_voice_assistant_maths_label_line_1.place(x=5, y=570)
                                            # first half of label is placed
                                            general_error_voice_assistant_maths_label_line_2 = Label(
                                                home_automation_system_window,
                                                text="again to retry", padx=100)
                                            # second half, requesting the user retry
                                            general_error_voice_assistant_maths_label_line_2.place(x=50, y=590)
                                            # label placed line below in middle
                                            home_automation_system_window.update()
                                            # window updated with new labels
                                        else:
                                            # where result  is found tp exist
                                            maths_label_answer_line_1 = Label(home_automation_system_window,
                                                                              text="The answer to " +
                                                                                   question)
                                            # creates a variable
                                            # holding a label with text of the result to the maths problem
                                            maths_label_answer_line_1.place(x=65, y=590)
                                            # places the maths label answer
                                            # where result  is found to exist
                                            maths_label_answer_line_2 = Label(home_automation_system_window,
                                                                              text=" is " + result)
                                            # creates a variable
                                            # holding a label with text of the result to the maths problem
                                            maths_label_answer_line_2.place(x=65, y=610)
                                            # places the maths label answer
                                            home_automation_system_window.update()
                                            # will update the system's window so user can see latest labels
                                    else:
                                        # however if the speech did not contain weather
                                        general_error_label_line_1 = Label(home_automation_system_window,
                                                                           text="I am not sure how to help you, "
                                                                                "click on voice assistant")
                                        # help error label is created
                                        general_error_label_line_1.place(x=5, y=570)
                                        # general error is placed
                                        general_error_label_line_2 = Label(home_automation_system_window,
                                                                           text="again to retry", padx=100)
                                        # general error is created
                                        general_error_label_line_2.place(x=50, y=590)
                                        # general error is placed
                                        home_automation_system_window.update()
                                        # updates window with labels
                            except:
                                # capture the error and where occurs hold it
                                spotify_no_speech_label_line_1 = Label(home_automation_system_window,
                                                                       text="I am not sure how to help you, "
                                                                            "click on voice assistant")
                                # specific error label created with text and placed on home automation system window
                                spotify_no_speech_label_line_1.place(x=5, y=570)
                                # specific error label placed
                                spotify_no_speech_label_line_2 = Label(home_automation_system_window,
                                                                       text="again to retry", padx=100)
                                # system is told about the creation of a label where text and a padx are passed
                                spotify_no_speech_label_line_2.place(x=50, y=590)
                                # label informs system where it will be positioned
                                home_automation_system_window.update()
                                # labels are updated to system
                                sp.volume(int(currVolume))
                                # the volume is then set to what is found to be at
                        except:
                            # if the above commands did not run successfully instead of throwing the user scary error
                            # the error is hidden and ignored
                            general_error_voice_assistant_label_line_1 = Label(home_automation_system_window,
                                                                               text="I am not sure how to help you, "
                                                                                    "click on voice assistant")
                            # creates general label for first half of error
                            general_error_voice_assistant_label_line_1.place(x=8, y=570)
                            # places label on screen
                            general_error_voice_assistant_label_line_2 = Label(home_automation_system_window,
                                                                               text="again to retry",
                                                                               padx=15)
                            # creates label for second half of general label
                            general_error_voice_assistant_label_line_2.place(x=50, y=590)
                            # places second half of general error label
                            home_automation_system_window.update()
                            # system updates current labels on window
                    voice_assistant_button = Button(home_automation_system_window,
                                                    text="Voice Assistant",
                                                    command=voice_assistant_button_clicked)
                    # button linked to voice assistant function is created
                    voice_assistant_button.place(x=350, y=580)
                    # button is placed on window

                    def more_controls(bulb, bulbName):
                        more_controls_window = Tk()
                        more_controls_window.title("Home Automation System More Controls For Devices")
                        more_controls_window.geometry("500x375")
                        more_controls_window.resizable(False, False)
                        more_controls_button_on = Button(more_controls_window,
                                                         text="On",
                                                         command=lambda: light_on(bulb))
                        more_controls_button_on.place(x=195, y=70)
                        more_controls_button_off = Button(more_controls_window,
                                                          text="Off",
                                                          command=lambda: light_off(bulb))
                        more_controls_button_off.place(x=255, y=70)
                        more_controls_colour_picker = Button(more_controls_window,
                                                             text="Select colour",
                                                             command=lambda: choose_colour(bulb))
                        more_controls_colour_picker.place(x=195, y=140)
                        more_controls_name_of_bulb = Label(more_controls_window, text=bulbName)
                        more_controls_name_of_bulb.place(x=195, y=40)
                        slider_more_controls = Scale(
                            more_controls_window,
                            from_=10,
                            to=1000,
                            orient='horizontal',
                            command=lambda value: slider_control(bulb, value))
                        slider_more_controls.place(x=200, y=97)
                        scenes_more_controls = Label(more_controls_window, text="Scenes")
                        scenes_more_controls.place(x=225, y=195)

                        def set_Scene(sceneBulb, scene):
                            sceneBulb.set_mode("scene")
                            scene_code = scene_code_dictionary[scene]
                            sceneBulb.set_value(25, scene_code)

                        scenes_reading = Button(more_controls_window,
                                                text="Reading", command=lambda: set_Scene(bulb, "Reading"))
                        scenes_reading.place(x=50, y=225)
                        scenes_night = Button(more_controls_window,
                                              text="Night", command=lambda: set_Scene(bulb, "Night"))
                        scenes_night.place(x=220, y=225)
                        scenes_leisure = Button(more_controls_window,
                                                text="Leisure", command=lambda: set_Scene(bulb, "Leisure"))
                        scenes_leisure.place(x=380, y=225)
                        scenes_working = Button(more_controls_window,
                                                text="Working", command=lambda: set_Scene(bulb, "Working"))
                        scenes_working.place(x=50, y=275)
                        scenes_soft = Button(more_controls_window,
                                             text="Soft", command=lambda: set_Scene(bulb, "Soft"))
                        scenes_soft.place(x=220, y=275)
                        scenes_colourful = Button(more_controls_window,
                                                  text="Colourful", command=lambda: set_Scene(bulb, "Colourful"))
                        scenes_colourful.place(x=380, y=275)
                        scenes_dazzling = Button(more_controls_window,
                                                 text="Dazzling", command=lambda: set_Scene(bulb, "Dazzling"))
                        scenes_dazzling.place(x=120, y=325)
                        scenes_gorgeous = Button(more_controls_window,
                                                 text="Gorgeous", command=lambda: set_Scene(bulb, "Gorgeous"))
                        scenes_gorgeous.place(x=310, y=325)

                    def light_on(bulb):
                        bulb.turn_on()

                    def light_off(bulb):
                        bulb.turn_off()

                    study_light_1_control_button = Button(home_automation_system_window,
                                                          text="Study Light 1",
                                                          command=lambda: more_controls(study_light_1, "Study Light 1"))
                    study_light_1_control_button.place(x=95, y=175)
                    study_light_1_on_button = Button(home_automation_system_window,
                                                     text="On",
                                                     command=lambda: light_on(study_light_1))
                    study_light_1_on_button.place(x=95, y=205)
                    study_light_1_off_button = Button(home_automation_system_window,
                                                      text="Off",
                                                      command=lambda: light_off(study_light_1))
                    study_light_1_off_button.place(x=155, y=205)
                    study_light_2_control_button = Button(home_automation_system_window,
                                                          text="Study Light 2",
                                                          command=lambda: more_controls(study_light_2, "Study Light 2"))
                    study_light_2_control_button.place(x=295, y=175)
                    study_light_2_on_button = Button(home_automation_system_window,
                                                     text="On",
                                                     command=lambda: light_on(study_light_2))
                    study_light_2_on_button.place(x=295, y=205)
                    study_light_2_off_button = Button(home_automation_system_window,
                                                      text="Off",
                                                      command=lambda: light_off(study_light_2))
                    study_light_2_off_button.place(x=355, y=205)
                    Transformer_control_button = Button(home_automation_system_window,
                                                        text="Transformer",
                                                        command=lambda: more_controls(Transformer, "Transformer"))
                    Transformer_control_button.place(x=95, y=375)
                    Transformer_on_button = Button(home_automation_system_window,
                                                   text="On", command=lambda: light_on(Transformer))
                    Transformer_on_button.place(x=95, y=405)
                    Transformer_off_button = Button(home_automation_system_window,
                                                    text="Off", command=lambda: light_off(Transformer))
                    Transformer_off_button.place(x=155, y=405)

                    def choose_colour(bulb):
                        try:
                            color_code = colorchooser.askcolor(title="Choose Colour")
                            (r, g, b) = color_code[0]
                            bulb.set_colour(r, g, b)
                        except:
                            return

                    study_light_1_colour_picker = Button(home_automation_system_window,
                                                         text="Select colour",
                                                         command=lambda: choose_colour(study_light_1))
                    study_light_1_colour_picker.place(x=95, y=275)
                    study_light_2_colour_picker = Button(home_automation_system_window,
                                                         text="Select colour",
                                                         command=lambda: choose_colour(study_light_2))
                    study_light_2_colour_picker.place(x=295, y=275)
                    Transformer_colour_picker = Button(home_automation_system_window,
                                                       text="Select colour",
                                                       command=lambda: choose_colour(Transformer))
                    Transformer_colour_picker.place(x=95, y=475)

                    def slider_control(bulb, value):
                        bulb.set_brightness(int(value))

                    slider_study_light_1 = Scale(
                        home_automation_system_window,
                        from_=10,
                        to=1000,
                        orient='horizontal',
                        command=lambda value: slider_control(study_light_1, value))
                    slider_study_light_1.place(x=100, y=232)
                    slider_study_light_2 = Scale(
                        home_automation_system_window,
                        from_=10,
                        to=1000,
                        orient='horizontal',
                        command=lambda value: slider_control(study_light_2, value))
                    slider_study_light_2.place(x=300, y=232)
                    slider_Transformer = Scale(
                        home_automation_system_window,
                        from_=10,
                        to=1000,
                        orient='horizontal',
                        command=lambda value: slider_control(Transformer, value))
                    slider_Transformer.place(x=100, y=432)

                    def create_rooms_for_devices():
                        create_rooms_window = Tk()
                        create_rooms_window.title("Adding Devices To A Room")
                        create_rooms_window.geometry("450x250")
                        create_rooms_window.resizable(False, False)
                        question_label = Label(create_rooms_window, text="Name of device")
                        question_label.place(x=30, y=50)
                        isTransformerChecked = IntVar(create_rooms_window)
                        transformer_rooms_yes_or_no = Checkbutton(create_rooms_window, text="transformer",
                                                                  variable=isTransformerChecked)
                        transformer_rooms_yes_or_no.place(x=30, y=125)
                        isStudyLight1Checked = IntVar(create_rooms_window)
                        study_light_1_rooms_yes_or_no = Checkbutton(create_rooms_window, text="study light 1",
                                                                    variable=isStudyLight1Checked)
                        study_light_1_rooms_yes_or_no.place(x=30, y=100)
                        isStudyLight2Checked = IntVar(create_rooms_window)
                        study_light_2_yes_or_no = Checkbutton(create_rooms_window, text="study light 2",
                                                              variable=isStudyLight2Checked)
                        study_light_2_yes_or_no.place(x=30, y=75)
                        name_of_room_created_entry = Entry(create_rooms_window)
                        name_of_room_created_entry.place(x=70, y=50)

                        def ok_button_rooms_command(room_name):
                            add_room_connection = sqlite3.connect(database_name)
                            cursor = add_room_connection.cursor()
                            bulb_List = []
                            bulbBoolean = [0, 0, 0, 0]
                            if isStudyLight1Checked.get() == 1:
                                bulb_List.append(study_light_1)
                                bulbBoolean[0] = 1
                            if isStudyLight2Checked.get():
                                bulb_List.append(study_light_2)
                                bulbBoolean[1] = 1
                            if isTransformerChecked.get():
                                bulb_List.append(Transformer)
                                bulbBoolean[2] = 1
                            insertRoomQuery = "INSERT INTO UserRooms VALUES(%d,'%s',%d,%d,%d) " % (loggedInUserID,
                                                                                                   room_name,
                                                                                                   bulbBoolean[0],
                                                                                                   bulbBoolean[1],
                                                                                                   bulbBoolean[2])
                            cursor.execute(insertRoomQuery)
                            add_room_connection.commit()
                            add_room_connection.close()
                            roomDict[room_name] = bulb_List
                            refreshButtons()
                            create_rooms_window.destroy()
                        ok_button_rooms = Button(create_rooms_window, text="Ok",
                                                 command=lambda:
                                                 ok_button_rooms_command(name_of_room_created_entry.get()))
                        ok_button_rooms.place(x=130, y=160)
                    rooms_for_lights_button = Button(home_automation_system_window, text="Create a Room",
                                                     command=create_rooms_for_devices)

                    rooms_for_lights_button.place(x=45, y=100)
            else:
                # where users entered password doesn't match the password they registered with
                password_does_not_match = Label(login_screen, text="password does not match")
                # python will create a new variable
                # connect it to a label place the label in the login screen
                # put text of password doesn't match
                password_does_not_match.place(x=160, y=330)
                # tells system where to place the above label
                password_does_not_match.config(foreground="red")
                # configures the colour of the text from the label to red
                # informing the user they have to retry this field
        connection_log_in.commit()
        # connects back to our connection and commits any changes to our database
        connection_log_in.close()
        # closes the connection to our database until reopened


def change_information(oldEmail, newEmail, newPassword, newNickname, newDOB, adminPage):
    """creates the change information function passing through the each new fields plus oldEmail
    this function will be what the created button above actually executes"""
    connection_change_information = sqlite3.connect(database_name)
    # creates a new variable and using sqlite3 connects back up to the database created at the start of program
    cursor_change_information = connection_change_information.cursor()
    # creates a cursor to be used to execute sql commands
    if oldEmail:
        # where oldEmail has been entered
        getUserIDQuery = "SELECT userID FROM users where email_address = '%s'" % oldEmail
        # new variable created set equal to a sql command
        # sql command finds the userID from our users table created
        # wherever the email address saved in db is equal to oldEmail inputted by admin
        cursor_change_information.execute(getUserIDQuery)
        # connects to our cursor created above and allows the command to be executed
        id = cursor_change_information.fetchone()
        # forces system to fetch one piece of data at a time
        if id:
            # where id has been inputted and exists inside database
            id = id[0]
            # set the id to equal to the first id to allow the program to know which record it is working with
            email_is_valid = Label(adminPage, text="email is valid", width=30)
            # creates a new label placing it inside the adminPage and puts some text with it
            email_is_valid.place(x=190, y=75)
            # places the label just below the entry box to show admin which details are correct
            email_is_valid.config(foreground="green")
            # configures labels text to green showing them this is correct
            if newEmail:
                # where new email has been entered
                changeEmailQuery = "UPDATE users SET email_address = '%s' WHERE userID == '%s'" % (
                    newEmail, id)
                # new variable made, set to a sql command
                # updates the new email entered wherever the id matches
                cursor_change_information.execute(changeEmailQuery)
                # executes our above sql statement
            if newPassword:
                # where new password entry box has been filled
                changePasswordQuery = "UPDATE users SET password = '%s' WHERE userID == '%s'" % (
                    newPassword, id)
                # sql command to update users new password as long as email entered matched
                cursor_change_information.execute(changePasswordQuery)
                # executes above sql command connecting to a cursor
            if newNickname:
                # where the admin has decided they want to adapt the nickname for the email they have inputted
                changeNicknameQuery = "UPDATE users SET nickname = '%s' WHERE userID == '%s'" % (
                    newNickname, id)
                # updates the nickname the admin has inputted where the id is equal to the email record
                cursor_change_information.execute(changeNicknameQuery)
                # executes this command using a built in execute function
            if newDOB:
                # where the admin has inputted a date of birth they would like to link with the email inputted
                changeDOBQuery = "UPDATE users SET date_of_birth = '%s' WHERE userID == '%s'" % (
                    newDOB, id)
                # updates the date of birth inputted where the userID found matches the email
                cursor_change_information.execute(changeDOBQuery)
                # executes the changeDOBquery command
            fields_updated = Label(adminPage, text="fields have been updated if edited")
            # creates a new variable equal to a built in function to make a label
            # inside adminPage tkinter window with text telling user what is going on
            fields_updated.place(x=150, y=250)
            # directs system where to put this label inside the tkinter window following the place function
            fields_updated.config(foreground="green")
            # configures the text inside the label to be green to show the user the information has been changed
        else:
            # however if inputted email in entry box exists but doesn't match any id in db
            fields_updated_email_not_valid = Label(adminPage, text="", width=30)
            # blank label created
            fields_updated_email_not_valid.place(x=150, y=250)
            # placed to block 'fields have been updated' label
            previous_email_not_found = Label(adminPage, text="previous email not found", width=30)
            # label created to be put inside adminPage with text and set width to allow for no overlap between labels
            previous_email_not_found.place(x=175, y=75)
            # places the label using built in place function
            previous_email_not_found.config(foreground="red")
            # configures this labels text to be red to show the admin they need to change details
    else:
        # where nothing was entered in previous email box
        fields_updated_email_not_valid = Label(adminPage, text="", width=30)
        # makes a blank label with a fixed width to overlap when needed
        fields_updated_email_not_valid.place(x=150, y=250)
        # places this blank label in a position to overlay when email entry box is empty
        previous_email_not_found = Label(adminPage, text="you haven't entered an email", width=30)
        # creates a tkinter label informing the admin they haven't entered an email
        previous_email_not_found.place(x=175, y=75)
        # places the new label in our tkinter window
        previous_email_not_found.config(foreground="red")
        # colours the text from the label red letting admin know that if they want anything to be saved enter email
    connection_change_information.commit()
    # connects to the connection created above and commits any changes
    connection_change_information.close()
    # closes the connection with the database


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
