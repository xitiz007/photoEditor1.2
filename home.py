from tkinter import *
from tkinter import messagebox
import mysql.connector
import scratch
class Login:
    def __init__(self,root):
        root.geometry("300x400")
        root.title("Photo Editor")
        Label(text="Photo Editor 1.2", bg="grey",width="300",height="2",font=('Calibri',20)).pack()
        Label(text="").pack()
        Label(text="User Name:").pack()
        self.userName = Entry(width=30)
        self.userName.pack()
        Label(text="").pack()
        Label(text="Password:").pack()
        self.password = Entry(width=30 , show="*")
        self.password.pack()
        Label(text="").pack()
        Label(text="").pack()
        Button(text="Sign in",width=15,height=2,command=self.signIn).pack()
        Label(text="").pack()
        Label(text="").pack()
        Button(text="Sign up Account",command=self.signUp,borderwidth=0,font=('Calibri',12),fg='#009BFF').pack()

    def signIn(self):
        if(not self.isAccount(self.userName.get(),self.password.get())):
            messagebox.showerror('Account not found','Invalid UserName/Password')
        else:
            root.destroy()
            scratch.call()

    def isAccount(self,userName,password):
        connection = mysql.connector.connect(host='localhost',user='root',password='aezakmi',database='photoeditor')
        cursor = connection.cursor()
        cursor.execute("select * from userinfo")
        result = cursor.fetchall()
        for uName , passwd in result:
            if(uName==userName and password==passwd):
                connection.close()
                return True
        connection.close()
        return False

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
        self.userName = Entry(screen,width=30)
        self.userName.pack()
        Label(screen,text="").pack()
        Label(screen,text="Password:").pack()
        self.password = Entry(screen,width=30, show="*")
        self.password.pack()
        Label(screen,text="").pack()
        Label(screen,text="").pack()
        Button(screen,text="Sign up", width=15, height=2, command=self.checkAccount).pack()
        Label(screen,text="").pack()
        Button(screen,text="I already have an account", command=screen.quit, borderwidth=0, font=('Calibri', 12), fg='#009BFF').pack()

    def checkAccount(self):
        if(not self.userName.get().strip() or not self.password.get().strip()):
            messagebox.showerror('Account','Cannot leave any field empty')
        else:
            if(self.exist()):
                messagebox.showerror('Duplicate Account','UserName Already exist.\n Try another')
            else:
                connection = mysql.connector.connect(host='localhost', user='root', password='aezakmi', database='photoeditor')
                cursor = connection.cursor()
                cursor.execute("insert into userinfo values ('{}','{}')".format(self.userName.get().lower(),self.password.get()))
                connection.commit()
                connection.close()
                messagebox.showinfo('Account','Successfully created your Account')


    def exist(self):
        connection = mysql.connector.connect(host='localhost',user='root',password='aezakmi',database='photoeditor')
        cursor = connection.cursor()
        cursor.execute('select userName from userinfo')
        result = cursor.fetchall()
        for i in result:
            if i[0] == self.userName.get().lower():
                connection.close()
                return True
        connection.close()
        return False

root = Tk()
obj = Login(root)
root.mainloop()
