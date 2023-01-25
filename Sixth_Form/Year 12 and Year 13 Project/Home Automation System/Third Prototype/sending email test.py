import smtplib
import random
from tkinter import *

code = str(random.randint(100000, 999999))


def send_email():
    """"""
    email = email_entry.get()

    server = smtplib.SMTP('localhost', 8025)

    message = "Your code is: " + code

    server.sendmail("", email, message)

    server.quit()

    sent_label = Label(root, text="Email sent!")

    sent_label.grid(row=2, column=0)


root = Tk()

email_label = Label(root, text="Enter the email address:")

email_label.grid(row=0, column=0)

email_entry = Entry(root)

email_entry.grid(row=0, column=1)

send_button = Button(root, text="Send email", command=send_email)

send_button.grid(row=1, column=0)

code_label_message = Label(root, text="Enter the 6 digit code")

code_label_message.grid(row=4, column=0)

code_entry = Entry(root)

code_entry.grid(row=4, column=1)


def verify_code():
    entered_code = code_entry.get()
    if entered_code == code:
        print("Correct code")
    else:
        print("Incorrect code")


verify_code_button = Button(root, text="Verify", command=verify_code)

verify_code_button.grid(row=5, column=1)

root.mainloop()
