import tkinter as tk
import random
import requests


def send_email(code):
    url = "https://api.emailjs.com/api/v1.0/email/send"
    payload = {
        "user_id": "your_user_id",
        "template_1w4589i": "your_template_id",
        "template_params": {
            "code": str(code)
        },
        "to": "recipient_email@gmail.com"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        label.config(text="Code sent!")
    else:
        label.config(text="Error sending code")


def generate_code():
    code = random.randint(100000, 999999)
    send_email(code)


root = tk.Tk()
root.title("Code Generator")

label = tk.Label(root, text="Click the button to generate a code")
label.pack()

generate_button = tk.Button(root, text="Generate Code", command=generate_code)
generate_button.pack()

root.mainloop()
