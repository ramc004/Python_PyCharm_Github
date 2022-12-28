from tkinter import *


class SignedIn(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("My login screen")
        self.resizable(0, 0)
        self.config(bg="blue")
        # to create a label
        self.lblTitle = Label(self, text="You have signed in", font='arial 8 bold', bg="yellow", fg="blue")
        self.lblTitle.place(x=90, y=40)
