import tkinter as tk
import smtplib
import random

username = 'pythonmail069@gmail.com'
password = 'pythonmail'


def check_code(entry):
    email = entry.get()
    print(email)

    # Generate 6-digit code
    code = random.randint(100000, 999999)
    msg = "Your code is: " + str(code)

    # Send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    try:
        server.login(username, password)
    except:
        print("Error Logging In")

    try:
        server.sendmail(username, email, msg)
    except:
        print('Error Sending mail')
    server.close()


def main():
    root = tk.Tk()
    root.geometry("200x150")
    root.title("Enter Email")
    global label
    label = tk.Label(root)
    label.pack()
    # Send email

    # Create entry for code
    entry = tk.Entry(root)
    entry.pack()

    # Create button to check code
    button = tk.Button(root, text="Enter Email", command=lambda: check_code(entry))
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
