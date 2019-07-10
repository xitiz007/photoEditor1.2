from tkinter import *

class Login:
    def __init__(self,root):
        root.geometry("300x400")
        root.title("Photo Editor")
        Label(text="Photo Editor 1.2", bg="grey",width="300",height="2",font=('Calibri',20)).pack()
        Label(text="").pack()
        Label(text="User Name:").pack()
        userName = Entry(width=30).pack()
        Label(text="").pack()
        Label(text="Password:").pack()
        userName = Entry(width=30 , show="*").pack()
        Label(text="").pack()
        Label(text="").pack()
        Button(text="Sign in",width=15,height=2,command=self.signIn).pack()
        Label(text="").pack()
        Label(text="").pack()
        Button(text="Sign up Account",command=self.signUp,borderwidth=0,font=('Calibri',12),fg='#009BFF').pack()

    def signIn(self):
        print("clicked")

    def signUp(self):
        screen = Toplevel(root)
        screen.title("Photo Editor")
        screen.geometry("300x400")
        Label(screen,text="Photo Editor 1.2", bg="grey", width="300", height="2", font=('Calibri', 20)).pack()
        Label(screen,text="").pack()
        Label(screen, text="Create a new Account").pack()
        Label(screen, text="It's free and always will be free").pack()
        Label(screen, text="").pack()
        Label(screen,text="User Name:").pack()
        userName = Entry(screen,width=30).pack()
        Label(screen,text="").pack()
        Label(screen,text="Password:").pack()
        userName = Entry(screen,width=30, show="*").pack()
        Label(screen,text="").pack()
        Label(screen,text="").pack()
        Button(screen,text="Sign up", width=15, height=2, command=self.signIn).pack()
        Label(screen,text="").pack()
        Button(screen,text="I already have an account", command=screen.quit, borderwidth=0, font=('Calibri', 12), fg='#009BFF').pack()



root = Tk()
obj = Login(root)
root.mainloop()
