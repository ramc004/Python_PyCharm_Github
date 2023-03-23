from tkinter import *
# tells the program to use the built-in library Tkinter and import all the modules found within Tkinter
from PIL import ImageTk, Image
# finds the library PIL and imports two separate packages, ImageTk and Image allowing us to store images inside tkinter
import emoji
# emoji library allowing us to show emojis inside our program
import random
# uses an algorithm to generate random numbers
import smtplib
# allows to send emails from a specific email using smtp, which stands for simple mail transfer protocol
from email.message import EmailMessage
# allows me to place a specific message inside our email; I will be combining this with the above library to send emails
proceed = Tk()
# we are creating a variable called proceed, and setting it equal to our tkinter window
# so whenever we need to put something inside out Tkinter window we just have to call proceed
proceed.title('A Level Computer Science Project')
# we are calling our variable root and defining more of its attributes giving our tkinter window a title
proceed.geometry("450x300")
# gives some restrictions for our tkinter window of 400x300


def login():
    return


def register():
    """this function creates a new window which allows the user to register their details
    and saves them to the database"""
    register_screen = Tk()
    # creates a new Tkinter user interface
    register_screen.title("Register")
    # gives the new Tkinter interface a title of 'Register'
    register_screen.geometry("500x600")
    # gives the starting size for the Tkinter user interface
    register_screen.resizable(False, False)
    # limits the user from resizing the interface
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
proceed.mainloop()
# this calls the variable proceed and displays our graphical user interface with all of its attributes defined above
