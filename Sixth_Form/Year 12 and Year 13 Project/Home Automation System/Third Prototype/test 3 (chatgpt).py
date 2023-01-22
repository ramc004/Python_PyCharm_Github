import tkinter as tk
import smtplib
import random


def send_email():
    # Generate 6-digit code
    code = random.randint(100000, 999999)
    msg = "Your code is: " + str(code)

    # Send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("calebrunner75@gmail.com", "your_password")
    server.sendmail("your_email@gmail.com", "recipient_email@example.com", msg)
    server.quit()
    return code


def check_code(code, entry):
    # Compare entered code with sent code
    if int(entry.get()) == code:
        # Display tick emoji
        label.config(text="✔️")
    else:
        # Display cross emoji
        label.config(text="❌")


def main():
    root = tk.Tk()
    root.geometry("200x150")
    root.title("Code Verification")
    global label
    label = tk.Label(root)
    label.pack()
    # Send email
    code = send_email()

    # Create entry for code
    entry = tk.Entry(root)
    entry.pack()

    # Create button to check code
    button = tk.Button(root, text="Check Code", command=lambda: check_code(code, entry))
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
