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
c.execute("""CREATE TABLE boring_users (
        email_address text,
        password text
    )""")
'''


def update():
    # Create a database or connect to one
    conn = sqlite3.connect('User Login Page Database.db')

    # create cursor
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""UPDATE boring_users SET 
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
    c.execute("SELECT * FROM boring_users WHERE oid = " + record_id)
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
    c.execute("DELETE from boring_users WHERE oid= " + delete_box.get())

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
    c.execute("INSERT INTO boring_users VALUES (:email_address, :password)",
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
    c.execute("SELECT *, oid FROM boring_users")
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
