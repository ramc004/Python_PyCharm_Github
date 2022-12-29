from tkinter import *
import os
import sqlite3
from PIL import ImageTk, Image


def main_account_screen():
    main_screen = Tk()
    main_screen.geometry("500x800")
    main_screen.title("A Level Computer Science Project")
    frame = Frame(main_screen, width=500, height=55)
    frame.pack()
    img = ImageTk.PhotoImage(Image.open("third.png"))
    label = Label(frame, image=img)
    label.pack()
    Button(text="Login", height="2", width="30").place(x=100, y=75)
    Button(text="Register", height="2", width="30").place(x=100, y=125)
    main_screen.resizable(False, False)
    main_screen.mainloop()


main_account_screen()
