from tkinter import *
from PIL import ImageTk, Image


def no():
    proceed.destroy()


def yes():
    login_and_register_user_screen = Tk()
    login_and_register_user_screen.title('Register and Login screen')
    login_and_register_user_screen.geometry("500x500")
    login_and_register_user_screen.resizable(False, False)
    frame1 = Frame(login_and_register_user_screen, width=420, height=55)
    frame1.place(x=7, y=1)
    img1 = ImageTk.PhotoImage(Image.open("first.png"))
    label1 = Label(frame1, image=img1)
    label1.place(x=7, y=1)


proceed = Tk()
proceed.title('A Level Computer Science Project')
proceed.geometry("450x300")
proceed.resizable(False, False)
frame = Frame(proceed, width=420, height=55)
frame.place(x=7, y=1)
img = ImageTk.PhotoImage(Image.open("first.png"))
label = Label(frame, image=img)
label.place(x=7, y=1)
Button(text="Yes", height="2", width="30", command=yes).place(x=84, y=125)
Button(text="No", height="2", width="30", command=no).place(x=84, y=175)
proceed.mainloop()
