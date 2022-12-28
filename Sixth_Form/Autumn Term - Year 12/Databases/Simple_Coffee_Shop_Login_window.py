from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Coffee_Shop')
root.geometry("400x600")

conn = sqlite3.connect('../GUIs/Coffee_Shop.db')

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
    conn = sqlite3.connect('../GUIs/Coffee_Shop.db')
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

    conn = sqlite3.connect('../GUIs/Coffee_Shop.db')

    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM Identification WHERE oid = " + record_id)
    records = c.fetchall()



    username_updater = Entry(updater, width=30)
    username_updater.grid(row=0, column=1, padx=20, pady=(10, 0))
    password_updater = Entry(updater, width=30)
    password_updater.grid(row=1, column=1)
    Coffee_updater = Entry(updater, width=30)
    Coffee_updater.grid(row=2, column=1)
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
    conn = sqlite3.connect('../GUIs/Coffee_Shop.db')
    c = conn.cursor()

    c.execute("DELETE from Identification WHERE oid = " + delete_box.get())

    conn.commit()

    conn.close()


def submit():
    conn = sqlite3.connect('../GUIs/Coffee_Shop.db')
    c = conn.cursor()

    c.execute("INSERT INTO Identification VALUES (:Username, :Password, :Coffee, :Order_Number)",
              {
                  username: username.get(),
                  password: password.get(),
                  coffee: coffee.get(),
                  Order_number: coffee.get(),
              })

    conn.commit()

    conn.close()

    username.delete(0, END)
    password.delete(0, END)
    Coffee.delete(0, END)
    Order_Number.delete(0, END)


def query():
    conn = sqlite3.connect('../GUIs/Coffee_Shop.db')

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
Coffee = Entry(root, width=30)
Coffee.grid(row=2, column=1)
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
