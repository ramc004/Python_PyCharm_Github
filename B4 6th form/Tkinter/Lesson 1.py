from tkinter import *
import SignIn

class Login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title("My login screen")
        self.resizable(0,0)
        # to create a label
        self.lblTitle = Label(self, text="Welcome", font='arial 20 bold')
        self.lblTitle.place(x=80, y=40)
        # username label
        self.lblUsername = Label(self, text="Username", font='arial 8 bold')
        self.lblUsername.place(x=20, y=100)
        # add user entry widget
        self.entryName = Entry(self)
        self.entryName.place(x=90, y=97)
        # password label
        self.lblPassword = Label(self, text="Password", font='arial 8 bold')
        self.lblPassword.place(x=20, y=120)
        # add password entry widget
        self.entryPass = Entry(self, show="*")
        self.entryPass.place(x=90, y=137)
        # add button
        self.btnReg = Button(self, text="Register")
        self.btnReg.place(x=20, y=200)
        # add a sign in button
        self.btnSignIn = Button(self, text="Sign In", command=self.signIn)
        self.btnSignIn.place(x=205, y=200)

        #make button functional
    def signIn(self):
        status = SignIn.SignedIn()


if __name__ == "__main__":
    MyApp = Login()
    MyApp.mainloop()
