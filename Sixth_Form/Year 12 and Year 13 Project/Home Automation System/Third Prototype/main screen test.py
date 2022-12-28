from tkinter import *
import os
import sqlite3
from PIL import ImageTk, Image


def main_account_screen():
    main_screen = Tk()
    main_screen.geometry("500x800")
    main_screen.title("A Level Computer Science Project")
    frame = Frame(main_screen, width=450, height=400)
    frame.place(x=5, y=5)
    img = ImageTk.PhotoImage(Image.open("'home automation system' title.png"))
    label = Label(frame, image=img)
    label.place(x=40, y=0)
    Label(text="").pack()
    Button(text="Login", height="2", width="30").place(x=100, y=75)
    Label(text="").place(x=5, y=5)
    Button(text="Register", height="2", width="30").place(x=100, y=125)
    main_screen.resizable(False, False)
    main_screen.mainloop()

main_account_screen()