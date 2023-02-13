from tkinter import *
import emoji
register_screen = Tk()
# creates a new Tkinter user interface
register_screen.title("Register")
# gives the new Tkinter interface a title of 'Register'
register_screen.geometry("500x600")
# gives the starting size for the Tkinter user interface
register_screen.resizable(False, False)
# limits the user from resizing the interface
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
email_address_entry_register_screen = Entry(register_screen)
email_address_entry_register_screen.place(x=150, y=70)


def check_email_address():
    """this ensure the user's email address follows all the rules"""
    email_register = email_address_entry_register_screen.get()
    # creates a new variable and sets it equal to whatever the user entered inside the email address entry box
    # this is using the get function built in to python
    if email_register:
        if "@" not in email_register:
            emoji_label_clause_2_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
            emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
            emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
            with open("names_register.txt", "r") as file_register_domains:
                # opens new file for names
                name_register = file_register_domains.read().splitlines()
            if email_register in name_register:
                # checks their email has some form of name in its email
                emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
                # this will adapt a tick next door to the clause to do with account name
            else:
                # but if the user's entered email address does not have one of the above names
                emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
                # the previous mark, tick, will change to a cross
            with open("email_register_domain.txt", "r") as file_register_names:
                # opens file with file name and speech marks allows us to read from file
                # and sets it equal to a variable
                domain_register = file_register_names.read().splitlines()
                # creates a new variable and sets equal to the file just opened
                # tells the system to read from the file and split
            if email_register in domain_register:
                # this ensure they are trying to send the email to an existing email address with a correct domain
                emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
                # as long as the user's email address contains one of the above domains then a tick will be shown
            else:
                # however if they do not have any domain that exists in the list above
                emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
                # this changes the text from a tick to a cross where there is no existing domain
        else:
            # on the other hand if the user has not inputted an @ sign in their email
            emoji_label_clause_2_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
            # then the emoji library will work with tkinter and configure the text to a cross
            name_register_split, domain_register_split = email_register.split("@")
            if not name_register_split:
                emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
            else:
                with open("names_register.txt", "r") as file_register_names:
                    # opens file with file name and speech marks allows us to read from file
                    # and sets it equal to a variable
                    name_register = file_register_names.read().splitlines()
                    # creates a new variable and sets equal to the file just opened
                    # tells the system to read from the file and split
                if name_register_split in name_register:
                    # this ensure they are trying to send the email to an existing email address with a correct domain
                    emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
                    # as long as the user's email address contains one of the above domains then a tick will be shown
                else:
                    # however if they do not have any domain that exists in the list above
                    emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
                    # this changes the text from a tick to a cross where there is no existing domain
            if not domain_register_split:
                emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
            else:
                with open("email_register_domain.txt", "r") as file_register_domains:
                    # opens new file for names
                    domain_register = file_register_domains.read().splitlines()
                    # creates new variable and splits the line
                if domain_register_split in domain_register:
                    # checks their email has some form of name in its email
                    emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
                    # this will adapt a tick next door to the clause to do with account name
                else:
                    # but if the user's entered email address does not have one of the above names
                    emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
                    # the previous mark, tick, will change to a cross
    else:
        emoji_label_clause_2_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
        emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
        emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
        with open("names_register.txt", "r") as file_register_domains:
            # opens new file for names
            name_register = file_register_domains.read().splitlines()
        if email_register in name_register:
            # checks their email has some form of name in its email
            emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
            # this will adapt a tick next door to the clause to do with account name
        else:
            # but if the user's entered email address does not have one of the above names
            emoji_label_clause_1_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
            # the previous mark, tick, will change to a cross
        with open("email_register_domain.txt", "r") as file_register_names:
            # opens file with file name and speech marks allows us to read from file
            # and sets it equal to a variable
            domain_register = file_register_names.read().splitlines()
            # creates a new variable and sets equal to the file just opened
            # tells the system to read from the file and split
        if email_register in domain_register:
            # this ensure they are trying to send the email to an existing email address with a correct domain
            emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":check_mark_button:")}')
            # as long as the user's email address contains one of the above domains then a tick will be shown
        else:
            # however if they do not have any domain that exists in the list above
            emoji_label_clause_3_email_address.config(text=f'{emoji.emojize(":cross_mark:")}')
            # this changes the text from a tick to a cross where there is no existing domain


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
check_rules_button_email_address = Button(register_screen, text="check rules", command=check_email_address)
# creates a variable and sets it equal to a button placed in the register_screen with text being check rules
# it will then run through the above rules adapting the text to a tick or a cross
check_rules_button_email_address.place(x=355, y=125)

register_screen.mainloop()
