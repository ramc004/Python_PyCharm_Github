from tkinter import *

class LogIn(Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry('500x500')
        self.title('Log in')
        self.resizable(9,9)

        self.Frame1 = Frame(self,height=220,width=300,bg='#FF572A')
        self.Frame2 = Frame(self,height=250,width=300,bg='#0068B8')
        self.Lblheading = Label(self.Frame1,text='Hello Welcome',font ='calibri 24 bold italic',bg='#E2AEB6')

        self.Frame1.pack()
        self.Frame2.pack()

        self.Lblheading.place(x=70,y=25)

    # place holder labels
        self.LblUser = Label(self.Frame1,textvariable=self.userName)
    # entry
        self.entUser = Entry(self.Frame1)
        self.entUser.place(x=65,y=85)
        self.entPass = Entry(self.Frame1)
        self.entPass.place(x=65,y=115)
    # button
        self.btnSignIn = Button(self.Frame2,text='Please Sign In')
        self.btnSignIn.place(x=60,y=100)
        self.btnSignUp = Button(self.Frame2,text='Please Sign Up')
        self.btnSignUp.place(x=175,y=100)



if __name__ == '__main__':
    myApp = LogIn()
    myApp.mainloop()
