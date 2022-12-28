from tkinter import *
from PIL import ImageTk, Image
import os
import sqlite3

root = Tk()
root.title('A Level Computer Science Project')
root.geometry("500x800")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('User Login Page Database.db')

# create cursor
c = conn.cursor()

# create table
'''
c.execute("""CREATE TABLE users (
        email_address text,
        password text
    )""")
'''


def register():
    # Create a database or connect to one
    conn = sqlite3.connect('User Login Page Database.db')

    # create cursor
    c = conn.cursor()
    """this function is the code for the 'Register' window
       whenever the user doesn't have an account yet but would like to create one"""
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("500x800")
    register_screen.resizable(False, False)
    global email_address
    global password
    global email_address
    global password_entry
    email_address = StringVar()
    password = StringVar()
    email_address_label_2 = Label(register_screen, text="Email Address ")
    email_address_label_2.pack()
    email_address = Entry(register_screen, textvariable=email_address)
    email_address.pack()
    password_label_2 = Label(register_screen, text="Password * ")
    password_label_2.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue").pack()
    Button(register_screen, text="Authenticate", width=10, height=1, bg="blue").pack()
    # committing changes
    conn.commit()

    # close connection
    conn.close()


def login():
    # Create a database or connect to one
    conn = sqlite3.connect('User Login Page Database.db')

    # create cursor
    c = conn.cursor()
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("500x800")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
    login_screen.resizable(False, False)
    global email_address_verify
    global password_verify
    email_address_verify = StringVar()
    password_verify = StringVar()
    global email_address_login_entry
    global password_login_entry
    Label(login_screen, text="email address * ").pack()
    email_address_login_entry = Entry(login_screen, textvariable=email_address_verify)
    email_address_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1).pack()
    # committing changes
    conn.commit()

    # close connection
    conn.close()


def main_account_screen():
    # Create a database or connect to one
    conn = sqlite3.connect('User Login Page Database.db')

    # create cursor
    c = conn.cursor()
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x800")
    main_screen.title("A Level Computer Science Project")
    frame = Frame(main_screen, width=450, height=400)
    frame.place(x=5, y=5)
    img = ImageTk.PhotoImage(Image.open("'home automation system' title.png"))
    label = Label(frame, image=img)
    label.place(x=40, y=0)
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).place(x=100, y=75)
    Label(text="").place(x=5, y=5)
    Button(text="Register", height="2", width="30", command=register).place(x=100, y=125)
    main_screen.resizable(False, False)
    main_screen.mainloop()
    # committing changes
    conn.commit()

    # close connection
    conn.close()
    main_account_screen()


def update():
    # Create a database or connect to one
    conn = sqlite3.connect('User Login Page Database.db')

    # create cursor
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""UPDATE users SET 
        email_address = :email,
        password = :password
        
        WHERE oid = :oid""",
              {'email': email_address_editor.get(),
               'password': password_editor.get(),
               'oid': record_id
               })

    # committing changes
    conn.commit()

    # close connection
    conn.close()

    editor.destroy()


# Create edit function to update record
def edit():
    global editor
    editor = Tk()
    editor.title('Update a record')
    editor.iconbitmap("3c667f868bb46623c496baeab1c9384d.jpg")
    editor.geometry("400x300")
    # Create a database or connect to one
    conn = sqlite3.connect('User Login Page Database.db')

    # create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    # Query the database
    c.execute("SELECT * FROM users WHERE oid = " + record_id)
    records = c.fetchall()
    # print(records)

    # Create global variables for text box names
    global email_address_editor
    global password_editor

    # Create text boxes
    email_address_editor = Entry(editor, width=30)
    email_address_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    password_editor = Entry(editor, width=30)
    password_editor.grid(row=1, column=1)

    # Create text box labels
    label_email_address_editor = Label(editor, text="email address")
    label_email_address_editor.grid(row=0, column=0, pady=(10, 0))
    label_password_editor = Label(editor, text="password")
    label_password_editor.grid(row=1, column=0)

    # Loop through results
    for record in records:
        email_address_editor.insert(0, record[0])
        password_editor.insert(0, record[1])

    # Create a save Button to save edited records
    edit_btn_editor = Button(editor, text="Save Record", command=update)
    edit_btn_editor.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=145)


# Create function to delete a record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('User Login Page Database.db')

    # create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from users WHERE oid= " + delete_box.get())

    # committing changes
    conn.commit()

    # close connection
    conn.close()


# Create submit function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('User Login Page Database.db')

    # create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO users VALUES (:email_address, :password)",
              {
                  'email_address': email_address.get(),
                  'password': password.get()
              })

    # committing changes
    conn.commit()

    # close connection
    conn.close()

    # Clear the text boxes
    email_address.delete(0, END)
    password.delete(0, END)


# Create query function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('User Login Page Database.db')

    # create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM users")
    records = c.fetchall()
    # print(records)

    # Loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[3]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)
    # committing changes
    conn.commit()

    # close connection
    conn.close()


# Create text boxes
email_address = Entry(root, width=30)
email_address.grid(row=0, column=1, padx=20, pady=(10, 0))
password = Entry(root, width=30)
password.grid(row=1, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=5, column=1, pady=5)

# Create text box labels
label_email_address = Label(root, text="email address")
label_email_address.grid(row=0, column=0, pady=(10, 0))
label_password = Label(root, text="password")
label_password.grid(row=1, column=0)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=5, column=0, pady=5)

# Create submit button
submit_btn = Button(root, text="Authenticate", command=submit)
submit_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Create an update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

# committing changes
conn.commit()

# close connection
conn.close()

root.mainloop()
