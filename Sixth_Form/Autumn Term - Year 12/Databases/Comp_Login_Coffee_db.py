from tkinter import *
import os
import sqlite3


root = Tk()
root.title('Coffee_Shop')
root.geometry("400x600")

conn = sqlite3.connect('Coffee_Shop.db')

c = conn.cursor()
'''
c.execute("""CREATE TABLE Identification (
        username text, 
        password text,
        Coffee text,
        Order_Number integer,
        )""")
'''


def update2():
    conn = sqlite3.connect('Coffee_Shop.db')
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE Identification SET 
        username = :username,
        password = :password,
        Coffee = :coffees,
        Order_Number = :Order_Number


        WHERE oid = :oid""",
              {
                  'username': username_updater.get(),
                  'password': password_updater.get(),
                  'coffees': Coffee_updater.get(),
                  'Order_Number': Order_number_updater.get(),
                  'oid': record_id
              })

    conn.commit()

    conn.close()

    updater.destroy()


def update():
    global updater, username_updater, Order_number_updater, Coffee_updater, password_updater
    updater = Tk()
    updater.title('Coffee_Shop')
    updater.geometry("400x300")

    conn = sqlite3.connect('Coffee_Shop.db')

    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM Identification WHERE oid = " + record_id)
    records = c.fetchall()

    username_updater = Entry(updater, width=30)
    username_updater.grid(row=0, column=1, padx=20, pady=(10, 0))
    password_updater = Entry(updater, width=30)
    password_updater.grid(row=1, column=1)
    coffee_updater = Entry(updater, width=30)
    coffee_updater.grid(row=2, column=1)
    Order_number_updater = Entry(updater, width=30)
    Order_number_updater.grid(row=3, column=1)

    username_label = Label(updater, text="Username")
    username_label.grid(row=0, column=0, pady=(10, 0))
    password = Label(updater, text="Password")
    password.grid(row=1, column=0)
    coffee_label = Label(updater, text="Coffee")
    coffee_label.grid(row=2, column=0)
    Order_number_label = Label(updater, text="Order number")
    Order_number_label.grid(row=3, column=0)

    for record in records:
        username_updater.insert(0, record[0])
        password_updater.insert(0, record[1])
        Coffee_updater.insert(0, record[2])
        Order_number_updater.insert(0, record[3])

    update_btn = Button(updater, text="Save Record", command=update2)
    update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=145)


def delete():
    conn = sqlite3.connect('Coffee_Shop.db')
    c = conn.cursor()

    c.execute("DELETE from Identification WHERE oid = " + delete_box.get())

    conn.commit()

    conn.close()


def submit():
    conn = sqlite3.connect('Coffee_Shop.db')
    c = conn.cursor()

    c.execute("INSERT INTO Identification VALUES (:Username, :Password, :Coffee, :Order_Number)",
              {
                  username: username.get(),
                  coffee: coffee.get(),
                  password: password.get(),
                  Order_number: coffee.get(),
              })

    conn.commit()

    conn.close()

    username.delete(0, END)
    password.delete(0, END)
    Coffee.delete(0, END)
    Order_Number.delete(0, END)


def query():
    conn = sqlite3.connect('Coffee_Shop.db')

    c = conn.cursor()

    c.execute("SELECT *, oid FROM Identification")
    records = c.fetchall()
    print(records)

    print_records = ' '
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[5]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    conn.commit()

    conn.close()


username = Entry(root, width=30)
username.grid(row=0, column=1, padx=20, pady=(10, 0))
password = Entry(root, width=30)
password.grid(row=1, column=1)
coffee = Entry(root, width=30)
coffee.grid(row=2, column=1)
Order_number = Entry(root, width=30)
Order_number.grid(row=3, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

username_label = Label(root, text="Username")
username_label.grid(row=0, column=0, pady=(10, 0))
password = Label(root, text="Password")
password.grid(row=1, column=0)
coffee_label = Label(root, text="Coffee")
coffee_label.grid(row=2, column=0)
Order_number_label = Label(root, text="Order number")
Order_number_label.grid(row=3, column=0)

delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)

submit_btn = Button(root, text="Add record to database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

update_btn = Button(root, text="Update Record", command=update)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

conn.commit()

conn.close()

root.mainloop()


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_label_2 = Label(register_screen, text="Username * ")
    username_label_2.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_label_2 = Label(register_screen, text="Password * ")
    password_label_2.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, 0)
    password_entry.delete(0, 0)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, 0)
    password_login_entry.delete(0, 0)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()

        else:
            password_not_recognised()

    else:
        user_not_found()


def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


def password_not_recognised():
    global password_not_recognised_screen
    password_not_recognised_screen = Toplevel(login_screen)
    password_not_recognised_screen.title("Success")
    password_not_recognised_screen.geometry("150x100")
    Label(password_not_recognised_screen, text="Invalid Password ").pack()
    Button(password_not_recognised_screen, text="OK", command=delete_password_not_recognised).pack()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recognised_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="teal", width="300", height="2", font=("HeleveticaNue", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()
