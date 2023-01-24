# how to email any email address provided,not just gmail,
# the user has provided containing a 6 digit randomly generated code in python tkinter
import smtplib
import random
from tkinter import *


def send_email():
    # Get the email address from the user
    email = email_entry.get()

    # Generate a 6-digit random code
    code = str(random.randint(100000, 999999))

    # Set up the SMTP server
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.starttls()
    server.login("haspythontkinter@yahoo.com", "quhwas-duwsed-secHo5")

    # Send the email
    message = "Your code is: " + code
    server.sendmail("your_email@example.com", email, message)
    server.quit()

    # Confirm that the email was sent
    sent_label = Label(root, text="Email sent!")
    sent_label.grid(row=2, column=0)


# Create the GUI
root = Tk()

email_label = Label(root, text="Enter the email address:")
email_label.grid(row=0, column=0)

email_entry = Entry(root)
email_entry.grid(row=0, column=1)

send_button = Button(root, text="Send email", command=send_email)
send_button.grid(row=1, column=0)

root.mainloop()
